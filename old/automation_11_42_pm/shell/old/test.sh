rm -r /home/ubuntu/test
rm -r /home/ubuntu/test_1

ls 


stat -c "%U %G" /home/ubuntu/

echo "two folders have been removed, GOOD TO GO"
#this command does change the ownership recursively
#sudo chown -R ubuntu:ubuntu /home/ubuntu/test
