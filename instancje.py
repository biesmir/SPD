import random
instances = []
for a in range(300, 1000, 100):
    instances.append(a)
print(instances)


for i in range(300,1000,100):
    macierz = [i, 3]
    for k in range(i):
        for p in range(3):
            x = random.randint(1,200)
            macierz.append(x)

    f1 = open("in"+str(i)+".txt", "w")
    f1.write(str(macierz[0]))
    f1.write(" " +str(macierz[1]))
    for p in range(2, len(macierz), 3):
        f1.write("\n" + str(macierz[p]))
        f1.write(" " + str(macierz[p + 1]))
        f1.write(" " + str(macierz[p + 2]))


#
# f1 = open("in900.txt","w")
#
# f1.write("900 3")
# for i in range(2,len(macierz),3):
#     f1.write("\n" +str(macierz[i]))
#     f1.write(" " +str(macierz[i+1]))
#     f1.write(" " +str(macierz[i+2]))


