import tkinter as tk

root = tk.Tk()

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=0, column=0, columnspan=3, sticky="n", pady = 10)

buttons_frame_2 = tk.Frame(root)
buttons_frame_2.grid(row = 2, column=0, columnspan=3, sticky="n", pady = 10)

boxes_frame = tk.Frame(root)
boxes_frame.grid(row = 1, column=0, columnspan=3, sticky="n", pady = 10)

entry = tk.Entry(buttons_frame, width = 80)
tasklist = tk.Listbox(boxes_frame, width = 100, border = 1)
done_tasks = tk.Listbox(boxes_frame, width = 100)



with open('undone_tasks.txt', 'r') as save_file:
    save_list = save_file.readlines()
    for line in save_list:
        tasklist.insert(tk.END, line)

with open('done_tasks.txt', 'r') as done_file:
    done_list = done_file.readlines()
    for line in done_list:
        done_tasks.insert(tk.END, line)


def save_tasks():
    """Saves the tasks on the save file"""
    with (open('undone_tasks.txt', 'w')) as save_file:
        for line in save_list:
            save_file.write(line)
    with (open('done_tasks.txt', 'w')) as done_file:
        for line in done_list:
            done_file.write(line)

def clear_task_done():
    """Clear Done Tasks field"""
    with open('done_tasks.txt', 'w') as clearing_file:
        done_tasks.delete(0, tk.END)
        clearing_file.close()


def setup_ui():
    """ Graphical UI setup"""

    root.title("Todo List")

    label = tk.Label(buttons_frame, text = "To Do list")
    done_title = tk.Label(boxes_frame, text = "Tasks Done")

    new_task = tk.Button(buttons_frame, border = 2, width = 5, text = "Add", command = add_task,
        background = 'green')
    rmv_task = tk.Button(buttons_frame, border = 2, width = 5, text = "Remove", command = remove_task,
        background = 'red', )
    task_done = tk.Button(buttons_frame, border = 1, width = 15, text = "Task Done", command = mark_as_done)
    clear_done = tk.Button(buttons_frame_2, border = 1, width = 15, text = "Clear Tasks done", command = clear_task_done)
    task_undone = tk.Button(buttons_frame_2, border = 1, width = 15, text = "Task Undone", command = mark_as_undone)

    label.grid(row = 0, column = 0, pady = 5, padx = 5)
    entry.grid(row = 1, column = 0, pady = 5, padx = 5)
    new_task.grid(row = 1, column = 1, pady = 5, padx = 5)
    rmv_task.grid(row = 1, column = 2, pady = 5, padx = 5)
    task_done.grid(row = 2, column = 0, pady = 5, padx = 5)

    tasklist.grid(row = 0, column = 0, pady = 5, padx = 5)
    done_title.grid(row = 1, column = 0, pady = 5, padx = 5)
    done_tasks.grid(row = 2, column = 0, pady = 5, padx = 5)

    task_undone.grid(row = 0, column = 0, pady = 5, padx = 5)
    clear_done.grid(row = 0, column = 1, pady = 5, padx = 5)

    root.mainloop()

def mark_as_undone():
    """Mark a task as undone and put it into the undone tasks"""
    selection = done_tasks.curselection()
    if selection:
        task_content = done_list.pop(selection[0])
        save_list.append(task_content + '\n')
        tasklist.insert(tk.END, task_content)
        save_tasks()
        done_tasks.delete(selection[0])



def mark_as_done():
    """Mark a task as done and transfert it into Done Task list"""
    selection = tasklist.curselection()
    if selection:
        task_content = save_list.pop(selection[0])
        done_list.append(task_content + '\n')
        done_tasks.insert(tk.END, task_content)
        save_tasks()
        tasklist.delete(selection[0])


def add_task():
    """Add a task to the list"""
    tache = entry.get()
    if tache:
        tasklist.insert(tk.END, tache)
        save_list.append(tache + '\n')
        save_tasks()
        entry.delete(0, tk.END)

def remove_task():
    """Remove a task"""
    selection = tasklist.curselection()
    if selection:
        save_list.pop(selection[0])
        save_tasks()
        tasklist.delete(selection[0])

def main():
    """Main Program Function"""
    setup_ui()


main()

