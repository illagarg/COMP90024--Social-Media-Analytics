import boto
from boto.ec2.regioninfo import RegionInfo
import time


'''
Autentification
'''


class confidential:
    group_id = '7176ba4f906c43038cb33debbd058782'
    group_key = 'b1cf0de2b19344e69bc5e984db1b183f'
    pt_id = '535a9867907b4fd089829318875ddc29'
    pt_key = '76bb6de86df044729000c8b7c4c520c7'
    vadi_id = '743c2ca61f904abfa2d712fe8804318f'
    vadi_key = '6b1b1b3178544d31bad675159ad8e9c2'


def auth(id, key):
    region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
    ec2_conn = boto.connect_ec2(aws_access_key_id=id,
                                aws_secret_access_key=key,
                                is_secure=True,
                                region=region,
                                port=8773,
                                path='/services/Cloud',
                                validate_certs=False)
    print("AUTH SUCCESS")
    return ec2_conn


# ami-8aac485a NeCTAR Ubuntu 14.04 (Trusty) amd64
# keyname is the keypair we created on nectar
# instant_type: instant size m1.small etc
# security_groups  =['default']
# 1.58.34

# image 'ami-16030760' is ubuntu 16.04

# image should be a string indicating what image we using to boot the instance

# 'm1.medium'
def create_instance(ec2_conn, image, type):

    reservation = ec2_conn.run_instances(
        image, key_name='xanatower', instance_type=type, security_groups=['default'], placement='melbourne-qh2')

    instance = reservation.instances[0]
    print("CREATED ONE INSTANCE")
    # return the created instance
    return instance
# instance is the instance that need volume to attatch to

# this method returns all the running instances details


def instance_info(ec2_conn):
    reservations = ec2_conn.get_all_instances()
    instances = []
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        print('Instance {} is {}'.format(i.id, i.state))


# this method return a list of running instances


def get_all_instances(ec2_conn):
    reservations = ec2_conn.get_all_instances()
    instances = []
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        print('Instance {} is {}'.format(i.id, i.state))

    return instances
    # if this works that means I have all the instances already

# this method attach a persistant volume to a specific instance to /dev/vdc


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


def security_groups(ec2_conn):
    gp = ec2_conn.get_all_security_groups()
    print gp


def write_host_file(IP):
    f = open("host", "w+")
    counter = 0
    for ip in IP:
        if counter == 0:
            f.write("[mainnode]\r\n")
            f.write("%s ansible_user=ubuntu\r\n" % ip)
            f.write("\r\n")
            counter = counter+1
        elif counter == 1:
            f.write("[masterdbnode]\r\n")
            f.write("%s ansible_user=ubuntu\r\n" % ip)
            f.write("\r\n")
            f.write("[dbservers]\r\n")
            f.write("%s ansible_user=ubuntu\r\n" % ip)
            counter = counter+1
        else:
            f.write("%s ansible_user=ubuntu\r\n" % ip)
    f.close()


def write_host_file_temp(IP):
    f = open("host", "w+")
    counter = 0
    for ip in IP:
        if counter == 0:
            f.write("[mainnode]\r\n")
            f.write("%s ansible_user=ubuntu\r\n" % ip)
            f.write("\r\n")
            f.write("[dbservers]\r\n")
            counter = counter+1
        f.write("%s ansible_user=ubuntu\r\n" % ip)
    f.close()
