import boto
from boto.ec2.regioninfo import RegionInfo
import time


'''
Autentification
'''


def auth():
    region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
    ec2_conn = boto.connect_ec2(aws_access_key_id='7176ba4f906c43038cb33debbd058782',
                                aws_secret_access_key='b1cf0de2b19344e69bc5e984db1b183f',
                                is_secure=True,
                                region=region,
                                port=8773,
                                path='/services/Cloud',
                                validate_certs=False)
    return ec2_conn


# ami-8aac485a NeCTAR Ubuntu 14.04 (Trusty) amd64
# keyname is the keypair we created on nectar
# instant_type: instant size m1.small etc
# security_groups  =['default']
# 1.58.34
def create_instance(ec2_conn):

    reservation = ec2_conn.run_instances(
        'ami-16030760', key_name='xanatower', instance_type='m1.medium', security_groups=['default'], placement='melbourne-qh2')

    instance = reservation.instances[0]

    print("CREATED ONE INSTANCE")
    # return the created instance
    return instance
# instance is the instance that need volume to attatch to


def instance_info(ec2_conn):
    reservations = ec2_conn.get_all_instances()
    instances = []
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        print('Instance {} is {}'.format(i.id, i.state))
        # if this works that means I have all the instances already


def get_all_instances(ec2_conn):
    reservations = ec2_conn.get_all_instances()
    instances = []
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        print('Instance {} is {}'.format(i.id, i.state))

    return instances
    # if this works that means I have all the instances already


def attach_vol(ec2_conn, instance):

    # Request	volume:
    vol_req = ec2_conn.create_volume(60, 'melbourne-qh2')

    # Check	provisioning	status:
    curr_vols = ec2_conn.get_all_volumes([vol_req.id])
    print('Volume	status:	{},	volume	AZ:	{}'.format(curr_vols[0].status,
                                                    curr_vols[0].zone))

    while instance.state != 'running':
        print('Instance {} is {}'.format(instance.id, instance.state))
        time.sleep(5)
        instance.update

    # Attach	volume	when	instance is ready
    ec2_conn.attach_volume(vol_req.id,	instance.id, '/dev/vdc')
