import tkinter as tk
from tkinter import messagebox

# Aplicación GUI de gestión de tareas con atajos visibles
# Permite añadir, completar y eliminar tareas
# Incluye botones, atajos de teclado y una guía en pantalla


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("500x500")
        self.root.configure(bg="#f5f5f5")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(self.root, font=("Arial", 12), bg="#ffffff", fg="#333333")
        self.entry.pack(pady=10, padx=10, fill="x")

        # Frame de botones
        button_frame = tk.Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=5)

        self.add_button = tk.Button(button_frame, text="Añadir", command=self.add_task,
                                    bg="#4caf50", fg="white", font=("Arial", 11, "bold"), width=10)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="Completar", command=self.complete_task,
                                         bg="#2196f3", fg="white", font=("Arial", 11, "bold"), width=10)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_task,
                                       bg="#f44336", fg="white", font=("Arial", 11, "bold"), width=10)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 12),
                                       selectbackground="#ffe082",
                                       bg="#ffffff", fg="#333333", height=12)
        self.task_listbox.pack(pady=10, padx=10, fill="both", expand=True)

        # Marco con los atajos (guía visual)
        shortcuts_frame = tk.LabelFrame(self.root, text="Atajos de teclado",
                                        bg="#eeeeee", fg="#333333", font=("Arial", 10, "bold"))
        shortcuts_frame.pack(pady=10, padx=10, fill="x")

        shortcuts_text = (
            "Enter → Añadir tarea\n"
            "C → Completar tarea seleccionada\n"
            "Delete / D → Eliminar tarea seleccionada\n"
            "Escape → Cerrar aplicación"
        )

        shortcuts_label = tk.Label(shortcuts_frame, text=shortcuts_text,
                                   justify="left", bg="#eeeeee", fg="#444444", font=("Arial", 10))
        shortcuts_label.pack(anchor="w", padx=10, pady=5)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task != "":
            self.tasks.append({"text": task, "done": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea primero")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea primero")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["done"]:
                self.task_listbox.insert(tk.END, f"✔ {task['text']}")
                self.task_listbox.itemconfig(tk.END, fg="gray")
            else:
                self.task_listbox.insert(tk.END, task["text"])
                self.task_listbox.itemconfig(tk.END, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
