#!/bin/bash
# send request to url and display response size in bytes
curl -s "$1" | wc -c
