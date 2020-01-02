#!/bin/bash

tokens='./tokens'
while IFS= read -r line
do
  python ./scrape.py "$line"
done < "$tokens"