#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s -i -X OPTIONS "$1" | grep -i "^Allow:" | awk '{print substr($0, index($0, ":") + 2)}' | tr -d '[:space:]'
