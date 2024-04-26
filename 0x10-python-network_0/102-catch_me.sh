#!/bin/bash

curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me -L -D - -o /dev/null
