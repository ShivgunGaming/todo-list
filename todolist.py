import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

# Function to add a task to the to-do list
def add_task():
    task_name = task_name_entry.get()
    task_description = task_description_entry.get()
    if task_name.strip() == "":
        messagebox.showwarning("Warning", "Please enter a task name.")
        return
    with open('todo_list.txt', 'a') as f:
        f.write(f"[ ] {task_name} - {task_description}\n")
    messagebox.showinfo("Success", "Task added successfully!")
    task_name_entry.delete(0, tk.END)
    task_description_entry.delete(0, tk.END)
    update_task_display()

# Function to display all tasks
def view_tasks():
    tasks_window = tk.Toplevel(root)
    tasks_window.title("To-Do List")
    tasks_window.geometry("400x300")

    tasks_label = tk.Label(tasks_window, text="To-Do List", font=("Arial", 14, "bold"))
    tasks_label.pack(pady=10)

    tasks_text = ScrolledText(tasks_window, wrap=tk.WORD, width=40, height=12)
    tasks_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

    with open('todo_list.txt', 'r') as f:
        tasks = f.readlines()
        for task in tasks:
            tasks_text.insert(tk.END, task.strip() + '\n')

# Function to mark a task as completed
def complete_task(task_index):
    with open('todo_list.txt', 'r') as f:
        tasks = f.readlines()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = tasks[task_index - 1].replace("[ ]", "[x]", 1)
        with open('todo_list.txt', 'w') as f:
            f.writelines(tasks)
        messagebox.showinfo("Success", "Task marked as completed!")
    else:
        messagebox.showerror("Error", "Invalid task number. Please enter a valid task number.")
    update_task_display()

# Function to remove a task from the to-do list
def remove_task(task_index):
    tasks = []
    with open('todo_list.txt', 'r') as f:
        tasks = f.readlines()
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        with open('todo_list.txt', 'w') as f:
            f.writelines(tasks)
        messagebox.showinfo("Success", "Task removed successfully!")
    else:
        messagebox.showerror("Error", "Invalid task number. Please enter a valid task number.")
    update_task_display()

# Function to update the task display
def update_task_display():
    task_display.delete(1.0, tk.END)
    with open('todo_list.txt', 'r') as f:
        tasks = f.readlines()
        for index, task in enumerate(tasks, start=1):
            task_display.insert(tk.END, f"{index}. {task.strip()}\n")

# Function to search for tasks
def search_tasks():
    search_term = search_entry.get().lower()
    task_display.delete(1.0, tk.END)
    with open('todo_list.txt', 'r') as f:
        tasks = f.readlines()
        for index, task in enumerate(tasks, start=1):
            if search_term in task.lower():
                task_display.insert(tk.END, f"{index}. {task.strip()}\n")

# Main function
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Title Frame
title_frame = tk.Frame(root, bg="#f0f0f0")
title_frame.pack(pady=10)

title_label = tk.Label(title_frame, text="To-Do List Manager", font=("Arial", 20, "bold"), bg="#f0f0f0")
title_label.pack()

# Task Entry Frame
task_entry_frame = tk.Frame(root, bg="#f0f0f0")
task_entry_frame.pack(pady=10)

task_name_label = tk.Label(task_entry_frame, text="Task Name:", bg="#f0f0f0")
task_name_label.grid(row=0, column=0, padx=5, pady=5)
task_name_entry = tk.Entry(task_entry_frame, width=30)
task_name_entry.grid(row=0, column=1, padx=5, pady=5)

task_description_label = tk.Label(task_entry_frame, text="Task Description:", bg="#f0f0f0")
task_description_label.grid(row=1, column=0, padx=5, pady=5)
task_description_entry = tk.Entry(task_entry_frame, width=30)
task_description_entry.grid(row=1, column=1, padx=5, pady=5)

add_button_img = Image.open("add_icon.png").resize((25, 25), Image.LANCZOS)
add_button_img = ImageTk.PhotoImage(add_button_img)
add_button = tk.Button(task_entry_frame, image=add_button_img, command=add_task, bg="#f0f0f0", bd=0)
add_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

# Task Display Frame
task_display_frame = tk.Frame(root, bg="#f0f0f0")
task_display_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

task_display_label = tk.Label(task_display_frame, text="Tasks:", font=("Arial", 14, "bold"), bg="#f0f0f0")
task_display_label.pack(side=tk.TOP, padx=5, pady=5)

task_display = ScrolledText(task_display_frame, wrap=tk.WORD, width=40, height=10)
task_display.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=5, pady=5)

# Search Frame
search_frame = tk.Frame(root, bg="#f0f0f0")
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=0, padx=5, pady=5)

search_button_img = Image.open("search_icon.png").resize((25, 25), Image.LANCZOS)
search_button_img = ImageTk.PhotoImage(search_button_img)
search_button = tk.Button(search_frame, image=search_button_img, command=search_tasks, bg="#f0f0f0", bd=0)
search_button.grid(row=0, column=1, padx=5)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(pady=10)

complete_button_img = Image.open("complete_icon.png").resize((25, 25), Image.LANCZOS)
complete_button_img = ImageTk.PhotoImage(complete_button_img)
complete_button = tk.Button(buttons_frame, image=complete_button_img, command=lambda: complete_task(int(search_entry.get())), bg="#f0f0f0", bd=0)
complete_button.grid(row=0, column=0, padx=5)

remove_button_img = Image.open("remove_icon.png").resize((25, 25), Image.LANCZOS)
remove_button_img = ImageTk.PhotoImage(remove_button_img)
remove_button = tk.Button(buttons_frame, image=remove_button_img, command=lambda: remove_task(int(search_entry.get())), bg="#f0f0f0", bd=0)
remove_button.grid(row=0, column=1, padx=5)

update_task_display()

root.mainloop()
