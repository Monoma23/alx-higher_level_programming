#!/bin/bash
#This script will send a request to a URL and displays size of the body
curl -s "$1" | wc -c
