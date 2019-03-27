import matplotlib.pyplot as plt
"""
n=2.01
r=1000
hitcount = 0
for a in range(r):
    for b in range(r):
        if(round((a**n+b**n)**(1/n)) == (a**n+b**n)**(1/n) and a!=0 and b!=0):
            print("power",n)
            print("a",a)
            print("b",b)
            print("c",int((a**n+b**n)**(1/n)))
            print("")
            hitcount += 1
        elif(abs(round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n)) <= 10**-5 and a!=0 and b!=0):
            print("power",n)
            print("a",a)
            print("b",b)
            print("c",int((a**n+b**n)**(1/n)))
            print("error",abs(round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n)))
            print("")
            hitcount += 1
print("hitcount",hitcount)
input("finished")
"""
"""
n = 1
s = float(input("step size: "))
sn = float(input("step number: "))
r = int(input("range"))
upperbound = n+s*sn
while(n<=upperbound):
    n = n+s
    for a in range(r):
        for b in range(r):
            if(round((a**n+b**n)**(1/n)) == (a**n+b**n)**(1/n) and a!=0 and b!=0):
                print("power",n)
                print("a",a)
                print("b",b)
                print("c",int((a**n+b**n)**(1/n)))
                print("")
            elif(abs(round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n)) <= .1 and a!=0 and b!=0):
                print("power",n)
                print("a",a)
                print("b",b)
                print("c",int((a**n+b**n)**(1/n)))
                print("error",abs(round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n)))
                print("")
input("finished")
"""
#"""
n = float(input("power: "))
if(input("single or range? ") == "single"):
    s = 0
    sn = 0
else:
    s = float(input("step size: "))
    sn = float(input("step number: "))
r = int(input("range: "))
acc = int(input("accuracy: "))
printlimit = 10**(-5)
upperbound = n+s*sn
finds = [[0,0,0,0]]
truefinds = [[0,0,0,0]]
while(n<=upperbound):
    n = n+s
    for a in range(r):
        for b in range(r):
            if(a!=0 and b!=0 and a!=(a**n+b**n)**(1/n) and b!=(a**n+b**n)**(1/n)):
                if(round((a**n+b**n)**(1/n)) == (a**n+b**n)**(1/n)):
                    #print("power",n)
                    #print("a",a)
                    #print("b",b)
                    #print("c",int((a**n+b**n)**(1/n)))
                    truefinds.append([n,a,b,int((a**n+b**n)**(1/n))])
                    #print("")
                    #input("one has been found")
                elif(abs(round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n)) <= .1):
                    if(round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n) < 0):
                        np = n
                        while(round((a**np+b**np)**(1/np))-(a**np+b**np)**(1/np) < 0):
                            np = np + (round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n))**2/acc
                    else:
                        np = n
                        while(round((a**np+b**np)**(1/np))-(a**np+b**np)**(1/np) > 0):
                            np = np - (round((a**n+b**n)**(1/n))-(a**n+b**n)**(1/n))**2/acc
                    for x in range(15):
                        npr = round(np, x+1)
                        if(abs(round((a**npr+b**npr)**(1/npr))-(a**npr+b**npr)**(1/npr)) < 10**-5 and (npr!=1 and npr!=2) and a!=round((a**npr+b**npr)**(1/npr)) and b!=round((a**npr+b**npr)**(1/npr))):
                            finds.append([npr,a,b,int((a**npr+b**npr)**(1/npr))])
                            #print("power",npr)
                            #print("a",a)
                            #print("b",b)
                            #print("c",int((a**npr+b**npr)**(1/npr)))
                            #print("error",abs(round((a**npr+b**npr)**(1/npr))-(a**npr+b**npr)**(1/npr)))
                            #print("")
                            break
                    #if(abs(round((a**np+b**np)**(1/np))-(a**np+b**np)**(1/np))<printlimit):
                        #print("power",np)
                        #print("a",a)
                        #print("b",b)
                        #print("c",int((a**n+b**n)**(1/np)))
                        #print("error",abs(round((a**np+b**np)**(1/np))-(a**np+b**np)**(1/np)))
                        #print("")
    if(s==0):
        break
for x in range(len(finds)):
    if(finds[x][0]!=1 and finds[x][0]!=2):
        print("power",finds[x][0])
        print("a",finds[x][1])
        print("b",finds[x][2])
        print("c",finds[x][3])
for x in range(len(truefinds)):
    if(truefinds[x][0]!=1 and truefinds[x][0]!=2):
        print("power",truefinds[x][0])
        print("a",truefinds[x][1])
        print("b",truefinds[x][2])
        print("c",truefinds[x][3])
for x in range(len(finds)):
    plt.plot([finds[x][1]],[finds[x][2]], 'ro')
for x in range(len(truefinds)):
    plt.plot([truefinds[x][1]],[truefinds[x][2]], 'bo')
plt.axis([0,r,0,r])
plt.show()
input("finished")
#"""