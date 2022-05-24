from device import Device, VPE

mivpe015 = VPE('mivpe015', '10.176.1.39','iosxr 7.3.1', 100, 200, 'location MILANO 20152 - Via Bensi 1/6 Liberty B')
mivpe016 = VPE('mivpe016', '10.176.1.40','iosxr 7.3.1', 100, 200,  'location MILANO 20152 - Via Bensi 1/6 Liberty B')
fivpe016 = VPE('fivpe016', '10.176.1.140','iosxr 7.3.1', 100, 200, 'location FIRENZE 50013 - via Mugellese 16 Fr. Capalle CAMPI BISENZIO')
mivce501 = Device('mivce501', '10.178.38.174','nxos 9.3(5)')
mivce502 = Device('mivce502', '10.178.38.175','nxos 9.3(5)')

import shelve

db = shelve.open('devicedb')
for obj in (mivpe015, mivpe016, fivpe016, mivce501, mivce502):
    db[obj.name] = obj
db.close


