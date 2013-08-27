import qualysapi, sys
from lxml import objectify
# Connect to QualysGuard.
qgc = qualysapi.connect()
# Capture number of days from command parameter.
number_of_days = sys.argv[1]
# Request assets older than number_of_days.
assets = qgc.request('asset_search.php', {'last_scan': 'not_within:164', 'target_asset_groups': 'All'})
# Parse assets XML for list of IPs.
ips = ''
for host in root.HOST_LIST.HOST:
    for ip in host.IP:
        ips += ip + ','
ips = ips[:-1]
