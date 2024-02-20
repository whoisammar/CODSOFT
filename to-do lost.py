import tkinter as tk

todo_list = []

def add():
    task = entry.get()
    if task:
        to_do_listbox.insert(tk.END, task)
        todo_list.append(task)
        entry.delete(0, tk.END)

def rem():
    selected_index = to_do_listbox.curselection()
    if selected_index:
        todo_list.pop(selected_index[0])
        to_do_listbox.delete(selected_index)

def update():
    index = to_do_listbox.curselection()
    if index != ():
        task = entry.get()
        todo_list[index[0]] = task
        to_do_listbox.delete(index[0])
        to_do_listbox.insert(index[0], task)
        entry.delete(0, tk.END)



# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x500")
root.configure(bg="#CD853F")

# Create a frame for the to-do list
f1 = tk.Frame(root, bd=5,highlightbackground="black", highlightcolor="black", highlightthickness=4, relief=tk.SUNKEN)
f1.pack(pady=20)

# Title label
label_font = ("Segoe UI", 30)
label = tk.Label(f1, text="To-Do List", bg="light blue", font=label_font,width=23,height=1)
label.pack()

# Create a frame
frame = tk.Frame(root, bg="light blue", bd=2, relief=tk.SUNKEN)
frame.pack(pady=20)

# Entry widget for new tasks
entry = tk.Entry(frame, width=30, font=("Arial", 18))
entry.grid(row=0, column=0, padx=10)

# Add and Remove buttons
add = tk.Button(frame, text="Add Task", command=add, bg="#4CAF50", fg="white", font=("Arial", 15))
add.grid(row=0, column=1, padx=10)

rem = tk.Button(frame, text="Remove Task", command=rem, bg="#FF5733", fg="white", font=("Arial", 15))
rem.place(x=405,y=120,width=125,height=40)

update= tk.Button(frame, text='Update', command=update,bg="#FF5733",fg="white",font=('Arial',15,'bold'))
update.place(x=430,y=60,width=90,height=40)

        
# Listbox to display tasks
to_do_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, height=20, width=43, font=("Arial", 12))
to_do_listbox.grid(row=1, column=0, padx=10)

# Run the Tkinter event loop
root.mainloop()