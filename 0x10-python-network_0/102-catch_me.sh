#!/bin/bash
# Makes a request via curl
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "User_id=98" 0.0.0:5000/catch_me
