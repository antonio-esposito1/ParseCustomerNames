
class Device:
    def __init__(self, name, identificativo, nos, isis_metric_to_core=None, isis_metric_to_vpe= None, location= None):
        self.name = name
        self.identificativo = identificativo
        self.nos = nos
        self.isis_metric_to_core = isis_metric_to_core
        self.isis_metric_to_vpe = isis_metric_to_vpe
        self.location = location
    def city(self):
        return self.location.split()[1]
    def calcola_net(self):
        net="49.cafe.0" + self.identificativo.split('.')[0]+ '.' + self.identificativo.split('.')[1]
        return net
    def __repr__(self):
        return '[Device: %s %s %s %s %s %s ]' % (self.name, self.identificativo, self.nos, self.isis_metric_to_core, self.isis_metric_to_vpe, self.location)

class VPE(Device):
     def RiseIsis(self, percent):
         self.isis_metric_to_core=int(self.isis_metric_to_core *(1+percent))


if __name__ == '__main__':
    mivpe015 = VPE('mivpe015', '10.176.1.39','iosxr 7.3.1', 100, 200, 'location MILANO 20152 - Via Bensi 1/6 Liberty B')
    mivpe016 = VPE('mivpe016', '10.176.1.40','iosxr 7.3.1', 100, 200,  'location MILANO 20152 - Via Bensi 1/6 Liberty B')
    fivpe016 = VPE('fivpe016', '10.176.1.140','iosxr 7.3.1', 100, 200, 'location FIRENZE 50013 - via Mugellese 16 Fr. Capalle CAMPI BISENZIO')
    mivce501 = Device('mivce501', '10.178.38.174','nxos 9.3(5)')
    mivce502 = Device('mivce502', '10.178.38.175','nxos 9.3(5)')

    print(mivpe015.name, mivpe015.identificativo, mivpe015.nos, mivpe015.location)
    print(mivpe016.name, mivpe016.identificativo, mivpe016.nos, mivpe016.location)
    print(fivpe016.name, fivpe016.identificativo, fivpe016.nos, fivpe016.location)
    print(mivce501.name, mivce501.identificativo, mivce501.nos, mivce501.location)
    print(mivce502.name, mivce502.identificativo, mivce502.nos, mivce502.location)
    print(mivpe015.city(), mivpe016.city())
    print(mivpe015.calcola_net())
    print('--All nodes--')
    for obj in (mivpe015, mivpe016, fivpe016):
        obj.RiseIsis(.10)
        print(obj)
    fivpe016.RiseIsis(.10)
    print(fivpe016.isis_metric_to_core)
    print(mivpe015)
    print(mivpe016)
    print(mivce501)
    print(mivce502)
    print(fivpe016)




