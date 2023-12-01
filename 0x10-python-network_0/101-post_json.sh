#!/bin/bash
# sends a POST request with JSON data, displays response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
