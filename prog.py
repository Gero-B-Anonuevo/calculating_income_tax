import tkinter as tk 
from tkinter import simpledialog

income = tk.simpledialog.askinteger("Hello!", "Please input your salary: ")
if income > 20000:
    above_20k = income - 20000
    tax_a_20 = above_20k*0.2
    tot_tax = tax_a_20 + 1000
    print("10000*0% + 10000*10%  + ", above_20k, "*20% = ", tot_tax)
elif income > 10000:
    above_10k = income - 10000
    tax_a_10 = above_10k*0.1
    tot_tax = tax_a_10
    print("10000*0% + ", above_10k, "*10%", tot_tax)
else:
    print("If your salary is below or equal to PHP 10,000. You are exempted from income tax")