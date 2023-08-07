#!/bin/bash

recent_py=$(ls -t *.py | head -n 1)

if [ -z "$recent_py" ]; then
  echo "Error: No .py files found in the current directory."
  exit 1
fi

chmod +x "$recent_py"

./"$recent_py"

