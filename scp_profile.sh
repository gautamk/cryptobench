#!/usr/bin/env bash

dd if=/dev/urandom of=file.ignore count=5120 bs=1024

for i in "3des-cbc" "aes128-cbc" "aes192-cbc" "aes256-cbc" "aes128-ctr" "aes192-ctr" "aes256-ctr" "arcfour" "arcfour128" "arcfour256" "blowfish-cbc" "cast128-cbc"; do
	./benchmark.sh -c "scp -c $i file.ignore gautamk@uw1-320-02.uwb.edu:/net/metis/home/gautamk"
done