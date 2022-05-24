# eq?(TYPE,"BNG") && str:contains?(SOFTWARE_VERSION,"VRP")
import re

def run():
  yield device.type('screen-length 0 temporary')

  #CPU USAGE
  output = yield device.type("display health")
  match = re.search("MPU\(Master\)\s+(?P<cpu>(\d)+%)\s+(?P<memory>(\d)+%)",output)
  if match:
      out.collect("CPU USAGE", match.group("cpu"))
      out.collect("MEMORY USAGE", match.group("memory"))
      
      
  #CARD REGISTERED
  output = yield device.type("display device")
  match = re.findall("Registered", output)
  if match: out.collect("CARD REGISTERED", len(match))


  #ALLARMI    
  output = yield device.type("dis alarm all")
  if not re.search("NO alarm",output):
    match = re.findall("^\d+\s+\w+",output,re.MULTILINE)
    out.collect("ALLARMI", len(match))
  else: out.collect("ALLARMI", 0)
    
  
  #ISIS
  output = yield device.type("dis isis peer")
  match = re.search("Total\s+Peer\(s\):\s+(?P<peer_isis>\d+)",output)
  if match: out.collect("PEER ISIS", match.group("peer_isis"))
  else : out.collect("PEER ISIS", 0)
  
  #CIRCUITI TOTALE
  output = yield device.type("display access-user online-total-number")
  match = re.search("Total users  :(\s)(?P<tot_user>(\d)+)",output)
  if match:
      out.collect("CIRCUITI_TOT", match.group("tot_user"))
  
  #CIRCUITI TELETU
  output = yield device.type("dis access-user online-total-number domain teletu_direct_data")
  match = re.search("Total users  :(\s)(?P<tot_user>(\d)+)",output)
  if match: direct = int(match.group("tot_user"))    
  else: direct = 0
    
  output = yield device.type("dis access-user online-total-number domain teletu_1net_data")
  match = re.search("Total users  :(\s)(?P<tot_user>(\d)+)",output)
  if match: onenet_data = int(match.group("tot_user"))    
  else: onenet_data = 0  
  
  output = yield device.type("dis access-user online-total-number domain teletu_1net_voice")
  match = re.search("Total users  :(\s)(?P<tot_user>(\d)+)",output)
  if match: onenet_voice = int(match.group("tot_user"))    
  else: onenet_voice = 0

  output = yield device.type("dis access-user online-total-number domain teletu_easyip_data")
  match = re.search("Total users  :(\s)(?P<tot_user>(\d)+)",output)
  if match: easyip_data = int(match.group("tot_user"))    
  else: easyip_data = 0 

  out.collect("CLIENTI_TELETU", direct + onenet_data + onenet_voice + easyip_data )

  
  #CIRCUITI NATTATI
  output = yield device.type("display access-user ip-pool pool_data_consumer_private_1 summary")
  match = re.search(" Normal users(\s)+:(\s)+(?P<clt_nat>(\d)+)",output)
  if match:
    out.collect("CLIENTI_NATTATI", match.group("clt_nat"))
  else:
    out.collect("CLIENTI_NATTATI", 0)
    
    
  #N_PEER_LDP
  output = yield device.type("display mpls ldp peer | i TOTAL")
  match = re.search("(\s)+TOTAL:(\s)+(?P<peer_ldp>(\d)+)",output)
  if match:
    out.collect("PEER LDP", match.group("peer_ldp"))
  else:
    out.collect("PEER LDP", 0)
    
    
  #ROTTE ANNUNCIATE  10.176.2.21
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.21 advertised-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_adv>(\d)+)",output)
  if match: out.collect("ROTTE ADV. 10.176.2.21", match.group("routes_adv"))
  else: out.collect("ROTTE ADV. 10.176.2.21", 0)  
    
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.21 received-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_rcv>(\d)+)",output)
  if match: out.collect("ROTTE RCV. 10.176.2.21", match.group("routes_rcv"))
  else: out.collect("ROTTE RCV. 10.176.2.21", 0)   
  """    
  #ROTTE ANNUNCIATE  10.176.2.78
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.78 advertised-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_adv>(\d)+)",output)
  if match: out.collect("ROTTE ADV. 10.176.2.78", match.group("routes_adv"))
  else: out.collect("ROTTE ADV. 10.176.2.78", 0)  
    
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.78 received-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_rcv>(\d)+)",output)
  if match: out.collect("ROTTE RCV. 10.176.2.78", match.group("routes_rcv"))
  else: out.collect("ROTTE RCV. 10.176.2.78", 0)
    
  
  #ROTTE ANNUNCIATE  10.176.2.142
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.142 advertised-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_adv>(\d)+)",output)
  if match: out.collect("ROTTE ADV. 10.176.2.142", match.group("routes_adv"))
  else: out.collect("ROTTE ADV. 10.176.2.142", 0)  
    
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.142 received-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_rcv>(\d)+)",output)
  if match: out.collect("ROTTE RCV. 10.176.2.142", match.group("routes_rcv"))
  else: out.collect("ROTTE RCV. 10.176.2.142", 0) 
    
    
  #ROTTE ANNUNCIATE  10.176.2.143
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.143 advertised-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_adv>(\d)+)",output)
  if match: out.collect("ROTTE ADV. 10.176.2.143", match.group("routes_adv"))
  else: out.collect("ROTTE ADV. 10.176.2.143", 0)  
    
  output = yield device.type("display bgp vpnv4 all routing-table peer 10.176.2.143 received-routes statistics")
  match = re.search("(\s)+total:(\s)+(?P<routes_rcv>(\d)+)",output)
  if match: out.collect("ROTTE RCV. 10.176.2.143", match.group("routes_rcv"))
  else: out.collect("ROTTE RCV. 10.176.2.143", 0) 
  """ 

  #ROTTE DSL_DATA
  output = yield device.type("display bgp vpnv4 vpn-instance DSL_DATA brief")
  match = re.search("(\s)+DSL_DATA(\s)+\d+\s+(?P<routes_dsl_data>\d+)",output)
  if match: out.collect("ROTTE DSL_DATA", match.group("routes_dsl_data"))
  else: out.collect("ROTTE DSL_DATA", 0)
    
  output = yield device.type("display bgp vpnv4 vpn-instance DSL_DATA peer")
  match_peer = re.search("(?P<peer>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d\s+30722[\s\w:]+Established",output)
  if match_peer: 
    output = yield device.type("display bgp vpnv4 vpn-instance DSL_DATA routing-table peer " + match_peer.group("peer") + " advertised-routes  statistics")
    match = re.search("(\s)+total:\s+(?P<routes_dsl_data_adv>\d+)",output) 
    if match: out.collect("ROTTE DSL_DATA_ADV", match.group("routes_dsl_data_adv"))
    else: out.collect("ROTTE DSL_DATA_ADV", "ERROR")
    output = yield device.type("display bgp vpnv4 vpn-instance DSL_DATA routing-table peer " + match_peer.group("peer") + " received-routes  statistics")
    match = re.search("(\s)+total:\s+(?P<routes_dsl_data_rcv>\d+)",output) 
    if match: out.collect("ROTTE DSL_DATA_RCV", match.group("routes_dsl_data_rcv"))
    else: out.collect("ROTTE DSL_DATA_RCV", "ERROR")    
  else: 
    out.collect("ROTTE DSL_DATA_ADV", "ERROR")
    out.collect("ROTTE DSL_DATA_RCV", "ERROR")
  
    
    
  #ROTTE IP-PBX_ACCESS
  output = yield device.type("display bgp vpnv4 vpn-instance IP-PBX_ACCESS brief")
  match = re.search("(\s)+IP-PBX_ACCESS(\s)+\d+\s+(?P<routes_ip_pbx>\d+)",output)
  if match: out.collect("ROTTE IP-PBX_ACCESS", match.group("routes_ip_pbx"))
  else: out.collect("ROTTE IP-PBX_ACCESS", 0)  
    
  #ROTTE SPC
  output = yield device.type("display bgp vpnv4 vpn-instance SPC_INFRANET brief")
  match = re.search("(\s)+SPC_INFRANET(\s)+\d+\s+(?P<routes_spc>\d+)",output)
  if match: out.collect("ROTTE SPC_INFRANET", match.group("routes_spc"))
  else: out.collect("ROTTE SPC_INFRANET", 0)
  
  #PING DSL_AUTH
  output = yield device.type("ping -vpn-instance DSL_AUTH 10.177.16.49")
  match = re.search("\s+(?P<packet_loss>\d+)\.\d+%\s+packet\s+loss",output)
  if match: out.collect("PING DSL_AUTH (%PackeLoss)", match.group("packet_loss"))

  #PING POOL DATA CONSUMER
  output = yield device.type("dis curr configuration ip-pool-group pool_data_consumer")
  match =  re.search("ip-pool\s+(?P<pool_name>pool_data_consumer_\d+)",output)
  if match: 
    output = yield device.type("dis curr configuration ip-pool " + match.group("pool_name"))
    match_gateway = re.search("\s+gateway\s+(?P<gateway>[\d\.]+)",output)
    output = yield device.type("ping -vpn-instance DSL_DATA -a " + match_gateway.group("gateway") + " 8.8.8.8")
    match = re.search("\s+(?P<packet_loss>\d+)\.\d+%\s+packet\s+loss",output)
    if match: out.collect("PING DNS GOOGLE (%PackeLoss)", match.group("packet_loss"))
    else: out.collect("PING DNS GOOGLE (%PackeLoss)", "ERROR")
  else: out.collect("PING DNS GOOGLE (%PackeLoss)", "ERROR")
  
  #PING POOL VOICE CONSUMER
  output = yield device.type("dis curr configuration ip-pool-group pool_voice_consumer")
  match =  re.search("ip-pool\s+(?P<pool_name>pool_voice_consumer_\d+)",output)
  if match: 
    output = yield device.type("dis curr configuration ip-pool " + match.group("pool_name"))
    match_gateway = re.search("\s+gateway\s+(?P<gateway>[\d\.]+)",output)
    match_dns = re.search("\s+dns-server\s+(?P<dns>[\d\.]+)",output)
    output = yield device.type("ping -vpn-instance IP-PBX_ACCESS -a " + match_gateway.group("gateway") + " " + match_dns.group("dns"))
    match = re.search("\s+(?P<packet_loss>\d+)\.\d+%\s+packet\s+loss",output)
    if match: out.collect("PING DNS VOICE (%PackeLoss)", match.group("packet_loss"))
    else: out.collect("PING DNS VOICE (%PackeLoss)", "ERROR")
  else: out.collect("PING DNS VOICE (%PackeLoss)", "ERROR")
    
  #TRAFFICO INPUT/OUTPUT ETH62
  output = yield device.type("dis interface Eth-Trunk 62 | i  rate")
  match =  re.search("Last\s+\d+\s+seconds\s+input\s+rate\s+(?P<input_eth_62>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO INPUT ETH62", format(float(match.group("input_eth_62"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO INPUT ETH62", "ERROR")
  match =  re.search("Last\s+\d+\s+seconds\s+output\s+rate\s+(?P<output_eth_62>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO OUTPUT ETH62", format(float(match.group("output_eth_62"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO OUTPUT ETH62", "ERROR")
    
  #TRAFFICO INPUT/ ETH62.10
  output = yield device.type("dis interface Eth-Trunk 62.10 | i rate")
  match =  re.search("Last\s+\d+\s+seconds\s+input\s+rate\s+(?P<input_eth_62_10>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO INPUT ETH62.10", format(float(match.group("input_eth_62_10"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO INPUT ETH62.10", "ERROR")
  match =  re.search("Last\s+\d+\s+seconds\s+output\s+rate\s+(?P<output_eth_62_10>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO OUTPUT ETH62.10", format(float(match.group("output_eth_62_10"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO OUTPUT ETH62.10", "ERROR")

  #TRAFFICO INPUT ETH63
  output = yield device.type("dis interface Eth-Trunk 63 | i   rate")
  match =  re.search("Last\s+\d+\s+seconds\s+input\s+rate\s+(?P<input_eth_63>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO INPUT ETH63", format(float(match.group("input_eth_63"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO INPUT ETH63", "ERROR")
  match =  re.search("Last\s+\d+\s+seconds\s+output\s+rate\s+(?P<output_eth_63>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO OUTPUT ETH63", format(float(match.group("output_eth_63"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO OUTPUT ETH63", "ERROR")
    
  #TRAFFICO INPUT ETH63.10
  output = yield device.type("dis interface Eth-Trunk 63.10 | i rate")
  match =  re.search("Last\s+\d+\s+seconds\s+input\s+rate\s+(?P<input_eth_63_10>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO INPUT ETH63.10", format(float(match.group("input_eth_63_10"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO INPUT ETH63.10", "ERROR")
  match =  re.search("Last\s+\d+\s+seconds\s+output\s+rate\s+(?P<output_eth_63_10>\d+)\s+bits\/sec", output)
  if match: out.collect("TRAFFICO OUTPUT ETH63.10", format(float(match.group("output_eth_63_10"))/1024**3,'.3f') + "Gb/s")
  else : out.collect("TRAFFICO OUTPUT ETH63.10", "ERROR")
