#!/bin/bash
# send a post request with params to URL given as argument 
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
