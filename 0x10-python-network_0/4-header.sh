#!/bin/usr/bash

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

curl -s -H "X-School-User-Id: 98" "$1"
