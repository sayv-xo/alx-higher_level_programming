#!/bin/bash
# display status code
curl -s -o okay -w "%{http_code}" "$1"
