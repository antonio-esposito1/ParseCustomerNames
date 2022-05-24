import unittest
import re

class ConfigurationParser:
    deviceConfig = open("mivpe035-confg", "r").read()
    def parseCustomerNames(self):
        customerNamePattern = r'vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames
    def parseCustomerVlan(self,CustomerName):
        intPattern = (r"interface Bundle-Ether731. ([0-9]+)\n description")
        allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
        return int(all.group(1))

class TestParse(unittest.TestCase):
 def test_parse_cust_name(self):
  cp = ConfigurationParser()
  expected_names = ['OPNET', 'MANAGEMENT']
  parsed_names = cp.parseCustomerNames()
  self.assertEqual(list, type(parsed_names))
  self.assertEqual(expected_names, parsed_names)

 def test_parse_cust_vlan(self):
    cp = ConfigurationParser()
    customer_name = "OPNET"
    expected_vlan = 1051
    parsed_vlan = cp.parseCustemerVlan(customer_name)
    self.assertEqual(expected_vlan, parsed_vlan)

 
