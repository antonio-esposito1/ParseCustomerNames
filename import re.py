import re
from netaddr import IPNetwork, IPAddress

def run():
    installation_type = context.param("INSTALLATION_TYPE")
    out.collect('INST_TYPE', installation_type)
    yield findNetReachableIps()  
    
def findNetReachableIps():
    interfaces = yield device.macro("list-interfaces")
    allIps = map(lambda it: it["ipaddress"], interfaces)
    validIps = filter(lambda it: (it is not None) & (re.match(r"\d+\.\d+\.\d+\.\d+", it) is not None), allIps)
    successfullIps = []
    unexpectedFailures = []
    successfullIps2 = []
    unexpectedFailures2 = []
    for ip in validIps:
        success, errorOutput = yield _pingNet(ip)
        if success:
            successfullIps.append(ip)
    if not success and errorOutput is not None:
            unexpectedFailures.append("%s CAUSE: %s" % (ip, errorOutput))
    if len(unexpectedFailures) > 0:
        out.collect('NET_REACHABLE_IP_NOT_FOUND', unexpectedFailures)
    yield successfullIps
    out.collect('PING 8.8.8.8 OK', successfullIps)
    #
    for ip in validIps:
        success, errorOutput2 = yield _pingNet(ip, context.param("IP_ADD_NEXTHOPBNG_DATI"))
        if success:
            successfullIps2.append(ip)
    if not success and errorOutput2 is not None:
            unexpectedFailures2.append("%s CAUSE: %s" % (ip, errorOutput2))
    if len(unexpectedFailures2) > 0:
        out.collect('NET_REACHABLE_IP_NOT_FOUND2', unexpectedFailures2)
    yield successfullIps2
    out.collect('PING GW_BNG OK', successfullIps2)

def _pingNet(ipaddress, ipdest='8.8.8.8', timeoutSeconds=1, times=20, size=54):
    output = None
    if device.info.os_family in ["VRP", "VRP3G"]:
        output = yield device.type("ping -m 10 -a %s -t %s -c %s -s %s %s" % (ipaddress, timeoutSeconds * 1000, times, size, ipdest))
    elif device.info.os_family == "IOS":
        output = yield device.type("ping %s source %s timeout %s repeat %s size %s" % (ipdest, ipaddress, timeoutSeconds, times, size))
    elif device.info.os_family == "ATOS":
        output = yield device.type("ping %s source %s timeout %s tries %s size %s" % (ipdest, ipaddress, timeoutSeconds, times, size))
    if re.search('(Invalid|Error)', output):
        yield False, output  # Error output    
    #     #Huawei                                  #Cisco                                        #Aethra
    yield " 100.00% packet loss" not in output and "Success rate is 0 percent" not in output and " 100% packet loss" not in output, None
