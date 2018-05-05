from all import *

ec2_conn = auth()

# for testing purpose, I only create 3 other instances

for i in [1, 2, 3]:
    new_instance = create_instance(ec2_conn, 'ami-16030760')


all_res = ec2_conn.get_all_reservations()
print('Index\tID\t\tInatance')
for idx, res in enumerate(all_res):
    print('{}\t{}\t{}'.format(idx, res.id, res.instances))


print('\n------ IP addresses ------')
instances = get_all_instances(ec2_conn)

IP = []
for i in instances:
    print(i.id + ':' + i.private_ip_address)
    IP.append(i.private_ip_address)
