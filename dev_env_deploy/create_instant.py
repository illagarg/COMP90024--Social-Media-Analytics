import boto
from boto.ec2.regioninfo import RegionInfo


region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
ec2_conn = boto.connect_ec2(aws_access_key_id='7176ba4f906c43038cb33debbd058782',
                            aws_secret_access_key='b1cf0de2b19344e69bc5e984db1b183f',
                            is_secure=True,
                            region=region,
                            port=8773,
                            path='/services/Cloud',
                            validate_certs=False)


# ami-8aac485a NeCTAR Ubuntu 14.04 (Trusty) amd64
# keyname is the keypair we created on nectar
# instant_type: instant size m1.small etc
# security_groups  =['default']
# 1.58.34

reservation = ec2_conn.run_instances(
    'ami-8aac485a', key_name='xanatower', instance_type='m1.small', security_groups=['default'])

instance = reservation.instances[0]

print("CREATED ONE INSTANCE")


# IF we want to delete one instance
# 2.00


# get a list of instances

all_res = ec2_conn.get_all_reservations()
print('Index\tID\t\tInatance')
for idx, res in enumerate(all_res):
    print('{}\t{}\t{}'.format(idx, res.id, res.instances))


# show all instances details
print('\nID:{}\tIP{}\tPlacement:{}'.format(
    all_res[0].id, all_res[0].instance.private, all_res[0].instance.place))
