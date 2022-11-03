autopkg_repo="~/Library/Application Support/AutoPkgr/recipe_list.txt"

# ls -R $autopkg_repo | grep recipe | while read line
cat $autopkg_repo | while read line
do
    echo "Creating override for: $line"
    autopkg make-override $line
    # echo "Auditing: $line"
    # autopkg audit "$line"
    # echo "Updating trust for: $line"
    # autopkg update-trust-info "$line"
done