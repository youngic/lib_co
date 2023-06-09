"""
some useful function code
"""


def confirm(pMess):
    while (1):
        print(pMess)
        print("please input 'y' to confirm......waiting......")
        try:
            a = str(input())
            if a == 'y':
                print("...confirm done...")
                break
        except ValueError:
            print("please input y to confirm")

def auto_find():
    rm = pyvisa.ResourceManager()
    devices = rm.list_resources()
    print(devices)
    ins_dict = {'p1': None, 'p2': None, 'm1': None, 'm2': None}
    counts = {'p1': 0, 'p2': 0, 'm1': 0, 'm2': 0}
    for dev in devices:
        if dev in dev_dict['power']:
            if counts['p1'] == 0:
                ins_dict['p1'] = rm.open_resource(dev)
                counts['p1'] += 1
            elif counts['p2'] == 0:
                ins_dict['p2'] = rm.open_resource(dev)
                counts['p2'] += 1
        elif dev in dev_dict['dmm']:
            if counts['m1'] == 0:
                ins_dict['m1'] = rm.open_resource(dev)
                counts['m1'] += 1
            elif counts['m2'] == 0:
                ins_dict['m2'] = rm.open_resource(dev)
                counts['m2'] += 1
    return ins_dict