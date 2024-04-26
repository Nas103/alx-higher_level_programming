#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

json_content=$(cat "$2")

if jq -e . >/dev/null 2>&1 <<<"$json_content"; then
    response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1")
    echo "$response"
else
    echo "Not a valid JSON"
fi
