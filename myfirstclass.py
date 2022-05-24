import re

class ConfigurationParser:
    deviceConfig = open("mivpe035-confg", "r").read()
    def parseCustomerNames(self):
        customerNamePattern = r'vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames
    def parseInterfaceNames(self):
        PatternInterfaceName = r'interface GigabitEthernet0/0/0/([0-9]+)\n'
        InterfaceName = re.findall(PatternInterfaceName, self.deviceConfig)
        # customerInterfaceDescription = r'description'
        # customerInterface = re.findall(customerInterfaceDescription, self.deviceConfig)
        return InterfaceName
    def ParseInterfaceDescription(self):
        PatternInterfaceDescription = r'escription link to ([a-zA-Z0-9_]+)\n'
        InterfaceDescription = re.findall(PatternInterfaceDescription, self.deviceConfig)
        return InterfaceDescription

cp = ConfigurationParser()
parsed_names = cp.parseCustomerNames()
print(parsed_names)
parsed_interface_names = cp.parseInterfaceNames()
print(parsed_interface_names)
parsed_interface_descriptions = cp.ParseInterfaceDescription()
print(parsed_interface_descriptions)

