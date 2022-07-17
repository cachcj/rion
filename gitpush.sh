git pull 
git add *
UUID=$(cat /proc/sys/kernel/random/uuid)
git commit -m $UUID
git push
