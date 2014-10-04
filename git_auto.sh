#!/bin/sh

python converter.py

git add --all
read -p "Git commit message: " message
git commit -m $message
git push