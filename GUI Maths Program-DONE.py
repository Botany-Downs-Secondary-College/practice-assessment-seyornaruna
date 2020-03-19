from tkinter import *
from random import*
import tkinter as tk
root = tk.Tk()
score = 0
total = 0

def next_problem():
    global x
    global y
    global problem_label
    global answer_entry
    global problem_text
    x = randrange(10)
    y = randrange(10)
    
    problem_text = str(x) + " + " +str(y) + " ="
    problem_label.configure(text = problem_text, bg = "lightblue", font = "10")
    answer_entry.focus()

def check_answer(event):
    global answer_entry
    global next_problem
    global total
    global score
    global x
    global y
    answer = x + y   
    try:
        user_answer = int(answer_entry.get())
        if user_answer == answer:
            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")
            answer_entry.delete(0, END)
            score = score + 1
            total = total + 1
            next_problem()
        else:
            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
            answer_entry.delete(0, END)
            total = total + 1
            next_problem()
    except ValueError:
        feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
        answer_entry.delete(0, END)
        answer_entry.focus()
    if total == 20:
        Screen5()

def check_answer_btn():
    global answer_entry
    global next_problem
    global total
    global score    
    global x
    global y
    answer = x + y   
    try:
        user_answer = int(answer_entry.get())
        if user_answer == answer:
            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")
            answer_entry.delete(0, END)
            score = score + 1
            total = total + 1            
            next_problem()
        else:
            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
            answer_entry.delete(0, END)
            total = total + 1            
            next_problem()
    except ValueError:
        feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
        answer_entry.delete(0, END)
        answer_entry.focus()
    if total == 20:
        Screen5()
        
def next_problem_subtraction():
    global x
    global y
    global problem_label
    global answer_entry
    global problem_text
    x = randrange(10)
    y = randrange(10)
    
    problem_text = str(x) + " - " +str(y) + " ="
    problem_label.configure(text = problem_text, bg = "lightblue", font = "10")
    answer_entry.focus()
    
def check_answer_subtraction(event):
    global answer_entry
    global next_problem
    global total
    global score   
    global x
    global y
    answer = x - y
    try:
        user_answer = int(answer_entry.get())
        if user_answer == answer:
            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")
            answer_entry.delete(0, END)
            score = score + 1
            total = total + 1            
            next_problem_subtraction()
        else:
            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
            answer_entry.delete(0, END)
            total = total + 1            
            next_problem_subtraction()
    except ValueError:
        feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
        answer_entry.delete(0, END)
        answer_entry.focus()   
    if total == 20:
        Screen5()    
        
def check_answer_subtraction_btn():
    global answer_entry
    global next_problem
    global total
    global score   
    global x
    global y
    answer = x - y
    try:
        user_answer = int(answer_entry.get())
        if user_answer == answer:
            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue", font = "10")
            answer_entry.delete(0, END)
            score = score + 1
            total = total + 1            
            next_problem_subtraction()
        else:
            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
            answer_entry.delete(0, END)
            total = total + 1            
            next_problem_subtraction()
    except ValueError:
        feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
        answer_entry.delete(0, END)
        answer_entry.focus()
    if total == 20:
        Screen5()    
        
def next_problem_multiplication():
    global x
    global y    
    global problem_label
    global answer_entry
    global problem_text
    x = randrange(10)
    y = randrange(10)
    
    problem_text = str(x) + " x " +str(y) + " ="
    problem_label.configure(text = problem_text, bg = "lightblue", font = "10" )
    answer_entry.focus()
        
def check_answer_multiplication(event):
    global answer_entry
    global next_problem
    global total
    global score   
    global x
    global y
    answer = x * y 
    try:
        user_answer = int(answer_entry.get())
        if user_answer == answer:
            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")
            answer_entry.delete(0, END)
            score = score + 1
            total = total + 1            
            next_problem_multiplication()
        else:
            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
            answer_entry.delete(0, END)
            total = total + 1            
            next_problem_multiplication()
    except ValueError:
        feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
        answer_entry.delete(0, END)
        answer_entry.focus()
    if total == 20:
        Screen5()    
        
def check_answer_multiplication_btn():
    global answer_entry
    global next_problem
    global total
    global score   
    global x
    global y
    answer = x * y 
    try:
        user_answer = int(answer_entry.get())
        if user_answer == answer:
            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")
            answer_entry.delete(0, END)
            score = score + 1
            total = total + 1            
            next_problem_multiplication()
        else:
            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
            answer_entry.delete(0, END)
            total = total + 1            
            next_problem_multiplication()
    except ValueError:
        feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
        answer_entry.delete(0, END)
        answer_entry.focus()
    if total == 20:
        Screen5()    

def Screen1 ():
    #Creates a frame for the first 2 widgets
    global frame1
    global frame2
    global frame3
    global frame4
    global frame5
    global frame6
    global score
    global total
    frame2.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()    
    frame5.grid_remove()
    frame6.grid_remove()
    frame1 = LabelFrame(root, bg = "light blue", height = 300)
    frame1.grid(row=0, column = 0)
    
    TitleLabel = Label (frame1, bg = "light blue", fg = "black", width = 20, padx = 30, pady = 10, text = "Welcome to Maths Mania", font= ("Times", "14", "bold"))
    TitleLabel.grid(columnspan = 5)
    
    total = total - total
    score = score - score    
    
    button1 = Button(frame1, text = "     Addition     ", font =("bold", "10"), bg = "white", pady= 10, anchor = W, command = Screen2)
    button1.grid(row = 8, column = 2)
    
    button2 = Button(frame1, text = "  Subtraction   ", font =("bold", "10"), bg = "white", pady= 10, anchor = W, command = Screen3)
    button2.grid(row = 9, column = 2)

    button3 = Button(frame1, text = " Multiplication  ", font =("bold", "10"), bg = "white", pady= 10, anchor = W, command = Screen4)
    button3.grid(row = 10, column = 2)    

    
def Screen2():   
    global frame1
    global frame2
    global frame3
    global frame4
    global frame5
    global frame6   
    global next_problem  
    global problem_label
    global answer_entry
    global feedback
    global x
    global y
    
    frame1.grid_remove()
    frame2 = LabelFrame(root, height = "600", width = "300",  bg = "lightblue")
    frame2.grid(row=0, column = 0)
    
    problem_label = Label(frame2, text = "", width = 18, height = 3)
    problem_label.grid(row = 0, column = 0, sticky = W)
    
    answer_entry = Entry(frame2, width = 7, font = "10")
    answer_entry.grid(row = 0, column = 1, sticky = W)
    
    check_btn = Button(frame2, text = "Check Answer", bg = "white", command = check_answer_btn, relief = RIDGE)
    check_btn.grid(row = 1, column = 1)
    
    home_btn = Button(frame2, text = "Home", bg = "white", command = Screen1, relief = RIDGE)
    home_btn.grid(row = 1, column = 0)    
    
    feedback = Label(frame2, text = "", height = 3, bg = "lightblue")
    feedback.grid(row = 2, column = 0)
    
    root.bind('<Return>', check_answer) 
    
    next_problem()
    
def Screen3():
    global frame1
    global frame2
    global frame3
    global frame4
    global frame5
    global frame6
    global next_problem
    global problem_label
    global answer_entry
    global feedback
    global x
    global y

    frame1.grid_remove()
    frame3 = LabelFrame(root, height = "600", width = "300", bg = "lightblue")
    frame3.grid(row=0, column = 0)
    
    problem_label = Label(frame3, text = "", width = 18, height = 3)
    problem_label.grid(row = 0, column = 0, sticky = W)
    
    answer_entry = Entry(frame3, width = 7)
    answer_entry.grid(row = 0, column = 1, sticky = W)
    
    check_btn = Button(frame3, text = "Check Answer", bg = "white", command = check_answer_subtraction_btn, relief = RIDGE)
    check_btn.grid(row = 1, column = 1)
    
    home_btn = Button(frame3, text = "Home", bg = "white", command = Screen1, relief = RIDGE)
    home_btn.grid(row = 1, column = 0)     
    
    feedback = Label(frame3, text = "", height = 3, bg = "lightblue")
    feedback.grid(row = 2, column = 0)
    
    root.bind('<Return>', check_answer_subtraction)

    next_problem_subtraction()
    
def Screen4():   
    global frame1
    global frame2
    global frame3
    global frame4
    global frame5
    global frame6    
    global next_problem_multiplication 
    global problem_label
    global answer_entry
    global feedback
    global x
    global y
    
    frame1.grid_remove()
    frame4 = LabelFrame(root, height = "600", width = "300",  bg = "lightblue")
    frame4.grid(row=0, column = 0)
    
    problem_label = Label(frame4, text = "", width = 18, height = 3)
    problem_label.grid(row = 0, column = 0, sticky = W)
    
    answer_entry = Entry(frame4, width = 7, font = "10")
    answer_entry.grid(row = 0, column = 1, sticky = W)
    
    check_btn = Button(frame4, text = "Check Answer", bg = "white", command = check_answer_multiplication_btn, relief = RIDGE)
    check_btn.grid(row = 1, column = 1)
    
    home_btn = Button(frame4, text = "Home", bg = "white", command = Screen1, relief = RIDGE)
    home_btn.grid(row = 1, column = 0)     
    
    feedback = Label(frame4, text = "", height = 3, bg = "lightblue")
    feedback.grid(row = 2, column = 0)
    
    root.bind('<Return>', check_answer_multiplication)    
    
    next_problem_multiplication()
    
def Screen5():
    global frame1
    global frame2
    global frame3
    global frame4
    global frame5
    global frame6  
    global total
    global score  
    frame2.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()
    frame5 = LabelFrame(root, height = "600", width = "300",  bg = "lightblue")
    frame5.grid(row=0, column = 0)

    

    label = Label(frame5, text = "You answered {} question(s) correct out of 20".format(score),font = 20, padx = 10, fg = "black",bg = "lightblue", width = 35, height = 9)
    label.grid(row = 0, column = 0, sticky = W)

    home_btn = Button(frame5, text = "Home",font=20, bg = "white", command = Screen1, relief = RIDGE)
    home_btn.grid(row = 1, column = 0)

    end_btn = Button(frame5, text = "End",font=20, bg = "white", command = Screen6, relief = RIDGE)
    end_btn.grid(row = 2, column = 0)

def Screen6():
    global frame1
    global frame2
    global frame3
    global frame4
    global frame5
    global frame6    
    frame5.grid_remove()
    frame6 = LabelFrame(root, height = "600", width = "300",  bg = "lightblue")
    frame6.grid(row=0, column = 0)

    label = Label(frame6, text = "Thank You! ",font=20,fg = "black",bg = "lightblue", width = 40, height = 9)
    label.grid(row = 0, column = 0, sticky = W)

  


root.title("Maths Mania!")
#root.geometry("600x300+700+10")
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)

Screen1()

root.mainloop()