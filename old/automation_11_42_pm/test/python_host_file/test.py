
# IP is a list of ip address in string
# this function needs to be in the host file dire


def write_host_file(IP):
    f = open("host", "w+")
    counter = 0
    for ip in IP:
        if counter == 0:
            f.write("[mainnode]\r\n")
            f.write("%s ansible_user=ubuntu\r\n" % ip)
            f.write("\r\n")
            f.write("[dbservers]\r\n")
            counter = counter+1
        else:
            f.write("%s ansible_user=ubuntu\r\n" % ip)
    f.close()
