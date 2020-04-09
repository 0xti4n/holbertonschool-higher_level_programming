#!/bin/bash
# task 101
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
