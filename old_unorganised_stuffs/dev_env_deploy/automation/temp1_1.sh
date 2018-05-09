sudo rm -r /home/ubuntu/test
echo "Removed folder"
sudo umount /dev/vdb /mnt
echo "umount volume"
#show owner of the created folder
sudo mkdir /home/ubuntu/test_sudo
stat -c "%U %G" /home/ubuntu/test_sudo
#-H -u is not going to work as a normal user
#can only change the owner ship of the folder later
sudo mkdir /home/ubuntu/test_without_sudo
#the first argument is the onwer and the second one is the group
sudo chown -R ubuntu:ubuntu /home/ubuntu/test_without_sudo
stat -c "%U %G" /home/ubuntu/test_without_sudo
