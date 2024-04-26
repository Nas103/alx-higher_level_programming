#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response_size=$(curl -s -o /dev/null -w "%{size_download}" "$1")

echo "$response_size"
