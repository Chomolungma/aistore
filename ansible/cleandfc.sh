#!/bin/bash
set -o
./stopandcleandfc.sh
echo "Cleaning up targets"
parallel-ssh -h inventory/targets.txt -i './cleandfcstate.sh'
if [[ -s inventory/new_targets.txt ]]; then parallel-ssh -h inventory/new_targets.txt -i './cleandfcstate.sh'; fi
echo "Cleaning up proxy"
parallel-ssh -h inventory/proxy.txt -i './cleandfcstate.sh'
