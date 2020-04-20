import re


texto="Ivan Osuna Ayuste 42"
particion1=re.split(" ",texto,1)
particion2=re.split("[ ](?=[0-9])",particion1[1],1)

print(particion1)
print(particion2)