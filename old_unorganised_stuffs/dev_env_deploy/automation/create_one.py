from all import *


ec2_conn = auth(confidential.vadi_id, confidential.vadi_key)


gp = ec2_conn.get_all_security_groups()
print gp[0]

'''
default = gp[0]
default.authorize('tcp', 22, 22, '0.0.0.0/0')
default.authorize('tcp', 5984, 5984, '0.0.0.0/0')
'''
print("now start creating instances")
# for testing purpose, I only create 3 other instances
# size is the number of instance I want to create
size = 1
for i in range(0, size):
    new_instance = create_instance(ec2_conn, 'ami-16030760', 'm1.small')

print()
all_res = ec2_conn.get_all_reservations()
print('Index\tID\t\tInatance')
for idx, res in enumerate(all_res):
    print('{}\t{}\t{}'.format(idx, res.id, res.instances))


instances = get_all_instances(ec2_conn)

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


# attach persiitance volume to all the VMs
# for i in instances:
#    attach_vol(ec2_conn, i)

# Now we have some running instances, try to use ansible to deploy useful packages and
