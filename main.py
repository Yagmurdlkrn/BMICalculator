from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=250)

label1 = Label(text= "Enter Your Weight(kg)")
label1.pack()

text1 = Text(width=15,height=2)
text1.pack()

label2 = Label(text= "Enter Your Height(cm)")
label2.pack()

text2 = Text(width=15,height=2)
text2.pack()

def button_clicked():

    weight = float(text1.get("1.0", END).strip())
    height = float(text2.get("1.0", END).strip())

    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        label3.config(text=f"Your BMI is {bmi: .2f}.You are under weight")
    elif bmi >= 18.5 and bmi <25:
        label3.config(text=f"Your BMI is {bmi: .2f}.You are normal weight")
    elif bmi >= 25 and bmi <30:
        label3.config(text=f"Your BMI is {bmi: .2f}.You are over weight")
    elif bmi >= 30 and bmi <35:
        label3.config(text=f"Your BMI is {bmi: .2f}.You are Obesity (Class I)")
    elif bmi >= 35 and bmi < 40:
        label3.config(text=f"Your BMI is {bmi: .2f}.You are Obesity (Class II)")
    else:
        label3.config(f"Your BMI is {bmi: .2f}.You are Extreme Obesity")

button = Button(text="Calculate",command=button_clicked)
button.pack()

label3 = Label()
label3.pack()

window.mainloop()
