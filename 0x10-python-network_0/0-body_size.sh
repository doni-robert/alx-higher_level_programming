#!/usr/bin/bash
# Takes a URL, sends a request to it and displays the size of the response body

size=$(curl -s "$1" | wc -c)
echo "$size"
