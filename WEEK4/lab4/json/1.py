import json

with open('sample-data.json') as f:
    data = json.load(f)

print('Interface Status')
print('=' * 80)
print('{:<50}{:<25}{:<8}{}'.format('DN', 'Description', 'Speed', 'MTU'))
print('-' * 80)

for row in data['imdata']:
    dn = row['l1PhysIf']['attributes']['dn']
    desc = row['l1PhysIf']['attributes'].get('descr', 'N/A') 
    speed = row['l1PhysIf']['attributes']['speed']
    mtu = row['l1PhysIf']['attributes']['mtu']
    print('{:<50}{:<25}{:<8}{}'.format(dn, desc, speed, mtu))