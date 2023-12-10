import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=200)


label1 = tkinter.Label(text= "Enter Your Weight(kg)")
label1.pack()

text1 = tkinter.Text(width=15,height=2)
text1.pack()

window.mainloop()
