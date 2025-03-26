import tkinter as tk

while True:
    aktion=input("Was möchtest du tun? Ansehen, Bearbeiten, Ende\n")
    if aktion=="Ende":
        break

    if aktion =="B":
        while True:
            aktion2=input("Etwas erledigt, hinzufügen oder rausnehmen? E, H, R, Ende\n")
            if aktion2 not in ["H", "E", "R", "Ende"]:
                print("Wähle bitte eine richtige Aktion aus!")
                continue
            if aktion2=="Ende":
                break
            todo=input("Unzwar was?\n")
            if todo[0]!="-":
                print("Markiere es zunächst als Unerlädigt mit - !")
                continue
            liste=[]
            if aktion2=="H":
                liste.append(todo)
            with open("ToDoList.txt", "r") as f:
                content=f.read()
                for line in content .splitlines():
                    if line!=todo:
                        liste.append(line)
            if aktion2=="E":
                liste.append("+"+todo[1:len(todo)])
            with open("ToDoList.txt", "w") as f:
                for i in liste:
                    f.write(i+"\n")

    if aktion=="A":
        root = tk.Tk()
        root.title("ToDoList")

        canvas = tk.Canvas(root, width=700, height=500, bg="white")
        canvas.pack()
        
        y=10
        with open("ToDoList.txt", "r") as f:
            content=f.read()
            for line in content.splitlines():
                if line[0]=="+":
                    label=tk.Label(root, text=line, bg="lightgray", fg="green").place(x=10, y=y)
                    y+=20
                if line[0]=="-":
                    label=tk.Label(root, text=line, bg="lightgray", fg="red").place(x=10, y=y)
                    y+=20
    
        root.mainloop()