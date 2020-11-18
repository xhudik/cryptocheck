#! /bin/bash

#a simple script that load python env and run cryptocheck.py

oldpath=${pwd}
cd ~/now/cryptocheck

source bin/activate
./cryptocheck.py

deactivate
cd $oldpath