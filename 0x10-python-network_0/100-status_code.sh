#!/bin/bash
# task 100
curl -s -w '%{http_code}' -o /dev/null "$1"
