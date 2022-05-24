import unittest
import re

class ConfigurationParser:
    def parseCustomerNames(self):
        deviceConfig = open("mivpe035-confg", "r").read()
        customerNamePattern = r'vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames

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

 
