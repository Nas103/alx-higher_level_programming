#!/bin/usr/bash

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
