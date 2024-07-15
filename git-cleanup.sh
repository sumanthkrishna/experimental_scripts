#!/bin/bash

# Fetch the latest branches and commits
git fetch --all --prune

# List all merged branches and delete them
echo "Deleting merged branches..."
for branch in $(git branch --merged | grep -v '^\*' | grep -v 'master' | grep -v 'main'); do
  echo "Deleting merged branch: $branch"
  git branch -d "$branch"
  git push origin --delete "$branch"
done

# Get the current date
current_date=$(date +%s)

# List all branches older than one year and delete them
echo "Deleting branches older than one year..."
for branch in $(git for-each-ref --format '%(refname:short) %(committerdate:unix)' refs/heads/ | while read -r branch date; do
  if [ $(($current_date - $date)) -gt 31536000 ]; then
    echo "$branch"
  fi
done); do
  echo "Deleting old branch: $branch"
  git branch -d "$branch"
  git push origin --delete "$branch"
done

echo "Cleanup complete!"
