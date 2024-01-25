#!/bin/bash
# Script sending JSON POST request to a specified URL and displaying bdy of response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
