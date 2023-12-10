import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=200)

label = tkinter.Label(text= "Enter Your Weight(kg)")
label.pack()



window.mainloop()
