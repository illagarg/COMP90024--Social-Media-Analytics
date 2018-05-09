from all import *

ec2_conn = auth()
instances = []
instances = get_all_instances(ec2_conn)

for i in instances:
    attach_vol(ec2_conn, i)

'''
#temp use stuffs
attach_vol(ec2_conn, instances[0])
attach_vol(ec2_conn, instances[1])
attach_vol(ec2_conn, instances[2])
'''

'''
Traceback (most recent call last):
  File "create_instant.py", line 15, in <module>
    all_res[0].id, all_res[0].instances.private, all_res[0].instances.place))
AttributeError: 'ResultSet' object has no attribute 'private'

'''
