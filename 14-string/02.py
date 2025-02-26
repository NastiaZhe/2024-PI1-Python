retazec = input("zadaj reťazec:")

print("Dĺžka reťazca je:") 

print(len(retazec))

for znak in retazec:
    print(znak)

ret = retazec
for i in range(len(ret)-1, -1, -1):
    print(ret[i])
 
for znak in ret:
    print(3*znak)