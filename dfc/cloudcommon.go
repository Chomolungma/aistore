/*
 * Copyright (c) 2017, NVIDIA CORPORATION. All rights reserved.
 *
 */
package dfc

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"os"

	"github.com/golang/glog"
)

const (
	emulateobjfailure = "/tmp/failobj"
)

// Create file and initialize object state.
func initobj(fqn string) (file *os.File, errstr string) {
	var err error
	file, err = Createfile(fqn)
	if err != nil {
		errstr = fmt.Sprintf("Unable to create file %s, err: %v", fqn, err)
		return nil, errstr
	}
	err = Setxattr(fqn, Objstateattr, []byte(XAttrInvalid))
	if err != nil {
		errstr = fmt.Sprintf("Unable to set xattr %s to file %s, err: %v", Objstateattr, fqn, err)
		file.Close()
		return nil, errstr
	}
	if glog.V(3) {
		glog.Infof("Created and initialized file %s", fqn)
	}
	return file, ""

}

// Finalize object state.
func finalizeobj(fqn string, md5sum []byte) error {
	err := Setxattr(fqn, MD5attr, md5sum)
	if err != nil {
		glog.Errorf("Unable to set md5 xattr %s to file %s, err: %v",
			MD5attr, fqn, err)
		return err
	}
	err = Setxattr(fqn, Objstateattr, []byte(XAttrValid))
	if err != nil {
		glog.Errorf("Unable to set valid xattr %s to file %s, err: %v",
			Objstateattr, fqn, err)
		return err
	}
	return nil
}

// Return True for corrupted or invalid objects.
func isinvalidobj(fqn string) bool {
	// Existence of file will make all cached object(s) invalid.
	_, err := os.Stat(emulateobjfailure)
	if err == nil {
		return true
	} else {
		data, err := Getxattr(fqn, Objstateattr)
		if err != nil {
			glog.Errorf("Unable to getxttr %s from file %s, err: %v", Objstateattr, fqn, err)
			return true
		}
		if string(data) == XAttrInvalid {
			return true
		}
		return false
	}
}

// on err closes and removes the file; othwerise returns the size (in bytes) while keeping the file open
func getobjto_Md5(file *os.File, fqn, objname, omd5 string, reader io.Reader) (size int64, errstr string) {
	hash := md5.New()
	writer := io.MultiWriter(file, hash)

	// was: size, err := io.Copy(writer, reader)
	size, err := copyBuffer(writer, reader)
	if err != nil {
		file.Close()
		return 0, fmt.Sprintf("Failed to download object %s as file %q, err: %v", objname, fqn, err)
	}
	hashInBytes := hash.Sum(nil)[:16]
	fmd5 := hex.EncodeToString(hashInBytes)
	if omd5 != fmd5 {
		file.Close()
		// and discard right away
		if err = os.Remove(fqn); err != nil {
			glog.Errorf("Failed to delete file %s, err: %v", fqn, err)
		}
		return 0, fmt.Sprintf("Object's %s MD5 %s... does not match %s (MD5 %s...)", objname, omd5[:8], fqn, fmd5[:8])
	} else if glog.V(3) {
		glog.Infof("Downloaded and validated %s as %s", objname, fqn)
	}
	if err = finalizeobj(fqn, hashInBytes); err != nil {
		file.Close()
		// FIXME: more logic TBD to maybe not discard
		if err = os.Remove(fqn); err != nil {
			glog.Errorf("Failed to delete file %s, err: %v", fqn, err)
		}
		return 0, fmt.Sprintf("Unable to finalize file %s, err: %v", fqn, err)
	}
	return size, ""
}
