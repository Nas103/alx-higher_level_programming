#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -X DELETE -s "$1"
