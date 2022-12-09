
autopkg_repo='Users/sammank/Library/Application Support/AutoPkgr/test.txt'
cd $autopkg_repo
ls -R | grep recipe | while read line
#cat $autopkg_repo | while read line
do
    echo "Creating override for: $line"
    autopkg make-override "$line" --force
    # echo "Auditing: $line"
    # autopkg audit "$line"
    # echo "Updating trust for: $line"
    # autopkg update-trust-info "$line"
done