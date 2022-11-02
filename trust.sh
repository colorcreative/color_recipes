autopkg_repo="/Users/Shared/Repositories/autopkg_recipes/"

ls -R $autopkg_repo | grep munki | while read line
do
    echo "Creating override for: $line"
    autopkg make-override $line
done