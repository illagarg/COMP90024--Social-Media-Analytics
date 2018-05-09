# check all ip adress

# wait and get information
from all import *

ec2_conn = auth(confidential.pt_id, confidential.pt_key)


print('\n------ IP addresses ------')
instances = get_all_instances(ec2_conn)

for i in instances:
    while i.state != 'running':
        print('Instance {} is {}'.format(i.id, i.state))
        time.sleep(5)
        i.update

# at this point it should be all running already, so print all IP for me
IP = []
for i in instances:
    print(i.id + ':' + i.private_ip_address)
    IP.append(i.private_ip_address)
