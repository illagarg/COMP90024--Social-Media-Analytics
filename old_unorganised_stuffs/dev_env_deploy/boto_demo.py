# Boto demo

# print all security group id and list all availble image
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

s_groups = ec2_conn.get_all_security_groups()

for groups in s_groups:
    print('Group id: {}, Group name: {} '.format(groups.id, groups.name))


images = ec2_conn.get_all_images()

for img in images:
    print('Image id: {}, image name : {}' .format(img.id, img.name))
