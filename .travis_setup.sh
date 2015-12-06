#!/usr/bin/env bash

apt-get update
apt-get install build-essential libssl-dev libffi-dev python-dev swig
pip install -r requirements.txt
