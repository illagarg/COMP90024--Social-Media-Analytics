from all import *
# terminate all instances before we start
# TESTING PURPOSE ONLY!!!!

ec2_conn_my = auth(confidential.pt_id, confidential.pt_key)
ec2_conn_vad = auth(confidential.vadi_id, confidential.vadi_key)


def terminate(ec2_conn):
    instances = get_all_instances(ec2_conn)
    for i in instances:
        ec2_conn.terminate_instances(instance_ids=[i.id])
        print("terminated one insstance")

    for i in instances:
        print(i.state)

    print("terminated all instances\n")


terminate(ec2_conn_my)
# terminate(ec2_conn_vad)
