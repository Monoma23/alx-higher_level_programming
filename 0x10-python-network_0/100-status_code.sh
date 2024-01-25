#!/bin/bash
# script sending request to URL and displaying only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
