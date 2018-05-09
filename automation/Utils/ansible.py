from subprocess import call

call(["ansible-playbook", "install.yml",
      "--private-key=xanatower.pem", "-i", "host"])

print("playbook has been ran")
