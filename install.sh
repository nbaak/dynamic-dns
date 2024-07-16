#!/bin/bash

REMOTE_COMPUTER=mercury.lan

echo installing project on $REMOTE_COMPUTER

scp -r ./* ${REMOTE_COMPUTER}:~/repositories/ddns/
