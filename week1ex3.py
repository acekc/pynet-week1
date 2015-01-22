__author__ = 'acekc'

from snmp_helper import snmp_get_oid, snmp_extract
import creds

COMMUNITY_STRING = creds.COMMUNITY_STRING
SNMP_PORT = creds.SNMP_PORT
IP = creds.IP

def extract_config_data(type, ip, port, community):

    device = (ip, community, port)

    types = dict()
    types["RLC"] = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    types["RLS"] = '1.3.6.1.4.1.9.9.43.1.1.2.0'
    types["SLC"] = '1.3.6.1.4.1.9.9.43.1.1.3.0'

    if type in types:
        return snmp_extract(snmp_get_oid(device, oid=types[type]))
    else:
        print "Invalid type"
        return None

run_last_change = extract_config_data("RLC", IP, SNMP_PORT, COMMUNITY_STRING)
run_last_save = extract_config_data("RLS", IP, SNMP_PORT, COMMUNITY_STRING)
start_last_change = extract_config_data("SLC", IP, SNMP_PORT, COMMUNITY_STRING)

if int(start_last_change) == 0:
    print "Startup configuration has not been saved since last reboot."

if int(run_last_change) > int(run_last_save):
    print "Running configuration changed but not saved."
else:
    print "Running configuration saved since last change."
