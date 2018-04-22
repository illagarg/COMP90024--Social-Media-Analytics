from all import *

ec2_conn = auth()
instances = []
instances = get_all_instances(ec2_conn)

attach_vol(ec2_conn, instances[0])


'''
Traceback (most recent call last):
  File "create_instant.py", line 15, in <module>
    all_res[0].id, all_res[0].instances.private, all_res[0].instances.place))
AttributeError: 'ResultSet' object has no attribute 'private'

'''
