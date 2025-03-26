feld=[["","",""],
      ["","",""],
      ["","",""]]

count=9
while True:
    if count<1:
        weiter=input("Wollt ihr nochmal? Ja/*\n")
        if weiter=="Ja":
            count=9
            feld=[["","",""],
              ["","",""],
              ["","",""]]
        else:
            break
    if count%2==1:
        try:
            pos=int(input("Spieler o ist dran!\n"))
            if not(pos in range(1,10)):
                print(f"Feld {pos} gibt es nicht")
                continue
        except ValueError:
            print("Dieses Feld existiert nicht!")
            continue
        if feld[(pos-1)//3][(pos-1)%3]!="":
            print(f"Feld {pos} ist bereits besetzt!")
            continue
        feld[(pos-1)//3][(pos-1)%3]="o"
        print(feld[0])
        print(feld[1])
        print(feld[2])
        count-=1
    else:
        try:
            pos=int(input("Spieler x ist dran!\n"))
            if not(pos in range(1,10)):
                print(f"Feld {pos} gibt es nicht")
                continue
        except ValueError:
            print("Dieses Feld existiert nicht!")
            continue
        if feld[(pos-1)//3][(pos-1)%3]!="":
            print(f"Feld {pos} ist bereits besetzt!")
            continue
        feld[(pos-1)//3][(pos-1)%3]="x"
        print(feld[0])
        print(feld[1])
        print(feld[2])
        count-=1
    for i in feld:
        if i[0]+i[1]+i[2]=="xxx" or i[0]+i[1]+i[2]=="ooo":
            print(f"Spieler {i[0]} hat gewonnen!")
            count=0
            break
    for i in range(3):
        if feld[0][i]+feld[1][i]+feld[2][i]=="xxx" or feld[0][i]+feld[1][i]+feld[2][i]=="ooo":
            print(f"Spieler {feld[0][i]} hat gewonnen!")
            count=0
            break
    if feld[0][0]+feld[1][1]+feld[2][2]=="xxx" or feld[0][0]+feld[1][1]+feld[2][2]=="ooo":
        print(f"Spieler {feld[1][1]} hat gewonnen!")
        count=0
    if feld[0][2]+feld[1][1]+feld[2][0]=="xxx" or feld[0][2]+feld[1][1]+feld[2][0]=="ooo":
        print(f"Spieler {feld[1][1]} hat gewonnen!")
        count=0

