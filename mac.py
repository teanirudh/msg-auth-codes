import random
keys=[]

#Key-Generation Algorithm to generate key
def Gen(klen):                                  #Takes in key length as input
    global keys                                 #If key length=k, 2**k keys are possible
    for i in range(0,2**klen):                  #For every number from 0 to (2**klen)-1
        key=str(bin(i).replace("0b",""))        #Binary equivalent is calculated
        key='0'*(klen-len(key))+key             #Zeroes added to maintain key length
        keys.append(key)                        #Appended to the key list
    k=random.choice(keys)                       #Random key selected from the key list
    return k                                    #Selected key is returned

#MAC Algorithm to generate valid tag
def Mac(k,m,tlen):                              #Takes in k, m & tag length as input
    mk=m+k                                      #message and key concatenated
    mk=int(mk,2)                                #Decimal equivalent is calculated
    t=mk%(2**tlen)                              #Calculation of tag 
    t=str(bin(t).replace("0b",""))              #Binary equivalent is calculated
    t='0'*(tlen-len(t))+t                       #Zeroes added to maintain tag length
    return t                                    #Generated tag is returned

#Verify algorithm to check validity of tag
def Vrfy(key,msg,tag):                          #Takes in key, message and tag as input
    global t
    if Mac(key,msg,len(tag))==t:                #Checks if (k,m) generate valid tag 
        b=1                                     #Sets b bit as 1 if satisfied
    else:
        b=0                                     #Sets b bit as 0 otherwise
    return b                                    #Returns the value of bit 'b'

#Brute-force attack algorithm
def Attack(m,t):
    global keys
    attempts=0                                  #attempts counter set to 0
    for key in keys:                            #For each key in key list
        attempts+=1                             #attempts incremented for each iteration
        print("Attempt:",attempts,end="")       #Displaying the attempt number
        print("\t     Key:",key,end="")         #Displaying the current key
        if (Vrfy(key,m,t)==1):                  #Performing verification
            k=key                               #k set as key if verified
            print("\t\tSuccess")                #Printing success message
            break
        print("\t\tFailed")                     #Printing failure message
    print("\n")                             
    print("Total attempts:",attempts,end="")    #Displaying the total number of attempts
    print("\t|    \tKey found:",k)              #Displaying the cracked key

#Sender's end
def Sender():
    global m,k,t,klen,tlen,keys
    keys=[]
    f="-"*50
    s=" "*18
    print()
    print(f,"\n")
    print(s,"Sender's side",s)
    m=input("\nEnter the message:\t")           #Getting input message from the sender 
    klen=int(input("Enter length of key:\t"))   #Getting the key length
    k=Gen(klen)                                 #Passing klen to the Gen() function
    tlen=int(input("Enter length of tag:\t"))   #Getting the tag length
    t=Mac(k,m,tlen)                             #Passing tlen to the Mac() function
    print()
    print("Key:",k,"\t\t|\t\tTag:",t)           #Displaying the key and tag 

#Attacker's end
def Attacker():
    global m,t                                  #Attacker knows the message and the tag
    f="-"*50
    s=" "*17
    print()
    print(f,"\n")
    print(s,"Attacker's side",s)
    print()
    Attack(m,t)                                 #Attacker's brute-force algorithm
    print()
    print(f)

Sender()
Attacker()