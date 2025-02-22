import json

print("Inherit status")
print("="*84)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 84)

def print_table1(data):
    data2 = json.loads(data)
    for key,val in data2.items():
        if key == "imdata":
            for item in val:
                for x,y in item.items():
                    print(y["attributes"]["dn"])

def print_table2(data):
    data2 = json.loads(data)
    for x in data2["imdata"]:
        print(x["l1PhysIf"]["attributes"]["dn"])


def print_table3(data):
    data2 = json.loads(data)
    for x in data2["imdata"]:
        print(x["l1PhysIf"]["attributes"]["speed"])        

def print_table(data):
    data2 = json.loads(data)
    for item in data2["imdata"]:
     dn = item["l1PhysIf"]["attributes"]["dn"]
     description = item["l1PhysIf"]["attributes"].get("descr", "N/A")  
     speed = item["l1PhysIf"]["attributes"]["speed"]
     mtu = item["l1PhysIf"]["attributes"]["mtu"]
        
       
     print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))

with open('sample-data.json', 'r') as file:
    data = file.read()
    print_table(data)
    


