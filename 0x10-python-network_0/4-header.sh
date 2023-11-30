#!/bin/bash
# send a GET request to URL using curl, with header variable and  display body of response
curl -sH "X-School-User-Id: 98" "$1"
