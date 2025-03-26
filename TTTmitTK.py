import tkinter as tk



root = tk.Tk()
root.title("TicTacToe")

canvas = tk.Canvas(root, width=300, height=400, bg="white")
canvas.pack()


b1 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b1))
b2 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b2))
b3 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b3))
b4 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b4))
b5 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b5))
b6 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b6))
b7 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b7))
b8 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b8))
b9 = tk.Button(root, text="",padx=0, pady=1, width=5, height=2, command=lambda: zug(b9))


canvas.create_window(70, 70, window=b1)  
canvas.create_window(150, 70, window=b2)
canvas.create_window(230, 70, window=b3)
canvas.create_window(70, 150, window=b4)
canvas.create_window(150, 150, window=b5)
canvas.create_window(230, 150, window=b6)
canvas.create_window(70, 230, window=b7)
canvas.create_window(150, 230, window=b8)
canvas.create_window(230, 230, window=b9)
canvas.create_line(110,30,110,270)
canvas.create_line(190,30,190,270)
canvas.create_line(30,110,270,110)
canvas.create_line(30,190,270,190)


count=9
win_cases=[(b1,b2,b3), (b4,b5,b6), (b7,b8,b9), (b1,b4,b7), (b2,b5,b8), (b3,b6,b9), (b1,b5,b9), (b3,b5,b7)]
b_liste=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

def zug(btn):
    global count
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget.winfo_y() == 350:
            widget.destroy()
    if count%2==1:
        if btn.cget("text")!="":
            tk.Label(root, text="Schon besetzt!").place(y=350)
        else:
            btn["text"]="O"
            count-=1
        for i in win_cases:
            if i[0].cget("text")+i[1].cget("text")+i[2].cget("text")=="OOO":
                tk.Label(root, text=f"Spiler O hat gewonnen", bg="lightgray", fg="green").place(relx=0.5, y=350, anchor="center")
                count=0
                break
        if count== 0:
            for i in b_liste:
                i["text"]=""
            count=9
    else:
        if btn.cget("text")!="":
            tk.Label(root, text="Schon besetzt!", bg="lightgray", fg="red").place(relx=0.5, y=350, anchor="center")
        else:
            btn["text"]="X"
            count-=1
        for i in win_cases:
            if i[0].cget("text")+i[1].cget("text")+i[2].cget("text")=="XXX":
                tk.Label(root, text=f"Spieler X hat gewonnen", bg="lightgray", fg="green").place(relx=0.5, y=350, anchor="center")
                count=0
                break
        if count== 0:
            for i in b_liste:
                i["text"]=""
            count=9
    

root.mainloop()


