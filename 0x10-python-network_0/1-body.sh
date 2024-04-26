#!/bin/usr/bash

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

curl_output=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$curl_output" -eq 200 ]; then
	curl -s "$1"
fi
