#!/usr/bin/bash
# display size of body of URL response in byte
curl -s "$1" | wc -c
