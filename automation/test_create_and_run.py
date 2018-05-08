from all import *
from subprocess import call


ec2_conn_my = auth(confidential.pt_id, confidential.pt_key)
# ec2_conn_vad = auth(confidential.vadi_id, confidential.vadi_key)

'''
# terminate all instances before we start
# TESTING PURPOSE ONLY!!!!
instances = get_all_instances(ec2_conn)
for i in instances:
    ec2_conn.terminate_instances(instance_ids=[i.id])
    print("terminated one insstance")

for i in instances:
    print(i.state)


print("terminated all instances\n")
'''

print("now start creating instances")
# for testing purpose, I only create 3 other instances
# size is the number of instance I want to create
size = 2
for i in range(0, size):
    new_instance = create_instance(ec2_conn_my, 'ami-16030760', 'm1.small')
    # new_instance = create_instance(ec2_conn_vad, 'ami-16030760', 'm1.small')

print()

all_res = ec2_conn_my.get_all_reservations()
print('Index\tID\t\tInatance')
for idx, res in enumerate(all_res):
    print('{}\t{}\t{}'.format(idx, res.id, res.instances))
'''
all_res = ec2_conn_vad.get_all_reservations()
print('Index\tID\t\tInatance')
for idx, res in enumerate(all_res):
    print('{}\t{}\t{}'.format(idx, res.id, res.instances))

'''
instances = get_all_instances(ec2_conn_my)
#instances_2 = get_all_instances(ec2_conn_vad)

#instances = [instances_1[0], instances_1[1], instances_2[0], instances_2[1]]

# check new instance running status, if not running, keep checking and dont do anything
for i in instances:
    count = 0
    i.update()
    if(i.state == 'running'):
        continue
    while (i.state != 'running' and count <= 30):
        i.update()
        print('Instance {} is {}'.format(i.id, i.state))
        time.sleep(5)
        count = count+1


print("ALL instances are ready, print their IP address\n")
print('\n------ IP addresses ------')
# if all instances are availble already, get their public IP address
IP = []
for i in instances:
    print(i.id + ':' + i.private_ip_address)
    IP.append(i.private_ip_address)


write_host_file_temp(IP)
print("write IP file success")

# attach persiitance volume to all the VMs
# for i in instances:
#    attach_vol(ec2_conn, i)

# Now we have some running instances, try to use ansible to deploy useful packages and


# ansible-playbook install.yml --private-key=xanatower.pem -i host
# https: // stackoverflow.com/questions/37099632/running-ansible-playbook-using-the-python-api

# NOW run the ansible playbook


time.sleep(30)

call(["ansible-playbook", "install.yml",
      "--private-key=xanatower.pem", "-i", "host"])

print("playbook has been ran")
