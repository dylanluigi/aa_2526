#!/bin/bash

set -e  

echo "Switching to main branch..."
git checkout main

echo "Pulling latest updates from professor (upstream/main)..."
git pull upstream main

echo "Pushing updates to my fork (origin/main)..."
git push origin main

echo "Switching to my-work branch..."
git checkout my-work

echo "Merging updates from main into my-work..."
git merge main

echo "Update complete! Your 'my-work' branch now includes the professor's latest material."
