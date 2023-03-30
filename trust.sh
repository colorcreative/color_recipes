#!/bin/bash

autopkg_repo="/Users/sammank/Library/AutoPkg/RecipeRepos"
cd "$autopkg_repo" || { echo "Error: Failed to change to directory '$autopkg_repo'"; exit 1; }

# Find all recipe files in the current directory and its subdirectories
recipe_files=$(find . -type f -name "*.recipe")

# Debugging line: Print the list of recipe files found
echo "Recipe files found:"
echo "$recipe_files"

# Save the current Internal Field Separator (IFS) value
oldIFS="$IFS"

# Set IFS to a newline character to properly handle file paths
IFS=$'\n'

# Iterate over each recipe file and create an override
for recipe_file in $recipe_files; do
    # Remove leading './' and file extension to get the recipe name
    recipe_name="${recipe_file#./}"
    recipe_name="${recipe_name%.recipe}"

    echo "Creating override for: $recipe_name"
    autopkg make-override "$recipe_name" --force
done

# Restore the original IFS value
IFS="$oldIFS"