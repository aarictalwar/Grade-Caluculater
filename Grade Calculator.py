import tkinter as tk


screen = tk.Tk()
screen.title("Grade Calculator")
screen.geometry("500x600")
screen.config(bg="lightgray")


def calculate():
    try:
        
        eng = int(english_entry.get())
        math = int(math_entry.get())
        phys = int(physics_entry.get())
        chem = int(chemistry_entry.get())
        comp = int(computer_entry.get())

        
        total = eng + math + phys + chem + comp
        tk.Label(screen, text=f"{total: <10}", font="arial 15 bold", bg="lightgray").place(x=250, y=400)

        
        average = total / 5
        tk.Label(screen, text=f"{average}%", font="arial 15 bold", bg="lightgray").place(x=250, y=450)

        
        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "Fail"

        tk.Label(screen, text=f"{grade: <5}", font="arial 15 bold", bg="lightgray").place(x=250, y=500)
    
    except ValueError:
       
        tk.Label(screen, text="Invalid Input", font="arial 12 bold", fg="red", bg="lightgray").place(x=250, y=350)


tk.Label(screen, text="Grade Calculator", font="arial 25 bold", bg="lightgray").pack(pady=20)



tk.Label(screen, text="English:", font="arial 15", bg="lightgray").place(x=50, y=100)
english_entry = tk.Entry(screen, font="arial 15", width=15)
english_entry.place(x=250, y=100)

tk.Label(screen, text="Math:", font="arial 15", bg="lightgray").place(x=50, y=150)
math_entry = tk.Entry(screen, font="arial 15", width=15)
math_entry.place(x=250, y=150)

tk.Label(screen, text="Physics:", font="arial 15", bg="lightgray").place(x=50, y=200)
physics_entry = tk.Entry(screen, font="arial 15", width=15)
physics_entry.place(x=250, y=200)

tk.Label(screen, text="Chemistry:", font="arial 15", bg="lightgray").place(x=50, y=250)
chemistry_entry = tk.Entry(screen, font="arial 15", width=15)
chemistry_entry.place(x=250, y=250)

tk.Label(screen, text="Computer:", font="arial 15", bg="lightgray").place(x=50, y=300)
computer_entry = tk.Entry(screen, font="arial 15", width=15)
computer_entry.place(x=250, y=300)


tk.Button(screen, text="Calculate", font="arial 15 bold", bg="white", command=calculate).place(x=180, y=350)




tk.Label(screen, text="Total Marks:", font="arial 15 bold", bg="lightgray").place(x=50, y=400)
tk.Label(screen, text="Percentage:", font="arial 15 bold", bg="lightgray").place(x=50, y=450)
tk.Label(screen, text="Grade:", font="arial 15 bold", bg="lightgray").place(x=50, y=500)

screen.mainloop()