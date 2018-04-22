from all import auth
from all import create_instance

ec2_conn = auth()
new_instance = create_instance(ec2_conn)

all_res = ec2_conn.get_all_reservations()
print('Index\tID\t\tInatance')
for idx, res in enumerate(all_res):
    print('{}\t{}\t{}'.format(idx, res.id, res.instances))


# show all instances details
print('\nID:{}\tIP{}\tPlacement:{}'.format(
    all_res[0].id, all_res[0].instances.private, all_res[0].instances.place))
