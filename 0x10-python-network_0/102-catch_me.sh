#!/bin/bash
# make request and make server respond with msg
curl -X OPTIONS 0.0.0.0:5000/catch_me -w "You got me!"
