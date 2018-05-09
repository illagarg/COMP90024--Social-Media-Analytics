from all import *
from subprocess import call

IP = ["123.123.123.0", "123.123.123.1", "123.123.123.2", "123.123.123.3"]

# now replace script for setting up couchDB
string_1 = "declare REPLACE_nodes=(115.146.85.192 115.146.86.208)"

string_2 = (
    "declare nodes=(%s %s %s)" % (IP[0], IP[1], IP[2]))

string_3 = "/home/x/COMP90024--Social-Media-Analytics/automation/shell/test_1_2.sh"

call(["rpl", string_1, string_2, string_3])

print("REPLACED test_1_2.sh")

# now replace script for setting up couchDB
string_1 = "declare REPLACE_nodes=(115.146.85.192 115.146.86.208)"

string_2 = (
    "declare nodes=(%s %s %s)" % (IP[0], IP[1], IP[2]))

string_3 = "/home/x/COMP90024--Social-Media-Analytics/automation/shell/test_2.sh"

call(["rpl", string_1, string_2, string_3])

print("REPLACED test_1_2.sh")
