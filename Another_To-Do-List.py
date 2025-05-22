import tkinter as tk
from tkinter import font
import random

root = tk.Tk()
root.title("To-Do List(with checkboxes)")

# Custom font
custom_font = font.Font(family="Helvetica", size=12)

# Task frame
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

tasks = []

def add_task():
    task_text = entry.get()
    if task_text:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(task_frame, text=task_text, variable=var, font=custom_font, anchor='w', width=40)
        cb.var = var  # Store var in the widget for reference
        cb.pack(anchor='w')
        tasks.append((cb, task_text))
        entry.delete(0, tk.END)

def sort_tasks():
    checked_tasks = [t for t in tasks if t[0].var.get()]
    unchecked_tasks = [t for t in tasks if not t[0].var.get()]
    sorted_tasks = unchecked_tasks + checked_tasks

    for widget, _ in tasks:
        widget.pack_forget()
    for cb, _ in sorted_tasks:
        cb.pack(anchor='w')

    tasks[:] = sorted_tasks

    
def del_task():
    global tasks
    remaining_tasks = []

    for cb, text in tasks:
        if cb.var.get():
            cb.destroy()
        else:
            remaining_tasks.append((cb, text))

    tasks = remaining_tasks 


entry = tk.Entry(root, width=40, font=custom_font)
entry.pack(pady=5)

btn_add = tk.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add.pack(pady=5)

btn_sort = tk.Button(root, text="Sort Tasks", fg="green", bg="white", command=sort_tasks)
btn_sort.pack(pady=5)

btn_del_task = tk.Button(root,text="Delete task",fg="green",bg="white", command = del_task)
btn_del_task.pack()


root.mainloop()