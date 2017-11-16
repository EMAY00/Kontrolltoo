print ("Esimene ülesanne: ")
arv1 = int(input("Esimene arv: "))
arv2 = int(input("Teine arv: "))
for x in range(arv1,arv2):
    if (x %2==0):
        
        print(x)

print ("Teine ülesanne: ")

print ("Kolmas ülesanne: ")
esimene_list = [11,15,6,13,13,25,32,11,20,5,31,16,32,29,11,13,3,29,28,24]
teine_list = [5,19,16,4,12,7,2,28,34,29,29,36,6,8,24,18,31,7,1,7]
print ("Kolmanda esimene: ")
print ("Kolmanda teine: ")
kaks = (esimene_list + teine_list)
maks = max(kaks)
print(maks)

print ("Kolmanda kolmas: ")
mini = min(kaks)
print(mini)

print ("Kolmanda neljas: ")

print ("Kolmanda viies: ")
