from subprocess import call


# ansible-playbook install.yml --private-key=xanatower.pem -i host
# https: // stackoverflow.com/questions/37099632/running-ansible-playbook-using-the-python-api

call(["ansible-playbook", "install.yml",
      "--private-key=xanatower.pem", "-i", "host"])
