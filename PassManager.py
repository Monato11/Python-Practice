import string
import random

repeat=True
while repeat:
    aktion=input("What would you like to do? Create, Read, Delete, End")
    if aktion=="End":
        break
    if aktion=="Read":
        secpass=input("Please tell me your security password.")
        passlist=[]
        with open("passlist.txt", "r") as f:
            content=f.read()
            for line in content.splitlines():
                passlist.append(line)
        if secpass==passlist[0]:
            print(passlist)
        else:
          raise TabError("Wrong security password!")

    if aktion=="Delete":
        delpass=input("Which password should be removed?")
        passlist=[]
        with open("passlist.txt", "r") as f:
            content=f.read()
            for line in content.splitlines():
                passlist.append(line)
        print(passlist)
        if delpass==passlist[0]:
            raise TypeError("You can not delete your security password!")
        passlist.remove(delpass)
        with open("passlist.txt", "w") as f:
            for i in passlist:
                f.write(i+"\n")
        print(passlist)

    if aktion=="Create":
        length=int(input("How long should your desired password be? At least 4"))
        if length<4:
            raise TypeError("The Password is too short!")

        typ=input("Should the password contain only numbers or anything? Y/N")
        if not(typ=="Y" or typ=="N"):
            raise TypeError("Wrong answer concerning the type of the password!")

        password=[]
        for i in range(length):
            password.append("0")

        for i in range(length):
            for j in range(length):
                if random.randint(0,33)%3==0:
                    password[j]=str(random.randint(0,9))
                    continue
                password[j]=str(random.choice(string.ascii_uppercase))

        for i in range(length):
            if random.randint(0,50)%2==1:
                password[i]=password[i].lower()

        passw=""
        for i in range(length):
            passw+=password[i]

        with open("passlist.txt", "a") as f:
            f.write(passw+"\n")

        print(passw)