import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x500")
        self.root.resizable(True, True)

        # Widgets principales
        self.titulo = tk.Label(root, text="Mis Tareas", font=("Arial", 16, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=3, pady=10)

        self.entry_tarea = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry_tarea.grid(row=1, column=0, padx=10, pady=5, sticky="we")

        self.btn_agregar = tk.Button(root, text="Agregar", width=10, command=self.agregar_tarea)
        self.btn_agregar.grid(row=1, column=1, padx=5, pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar", width=10, command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=1, column=2, padx=5, pady=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=20, selectmode=tk.SINGLE, font=("Arial", 12))
        self.listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Scrollbar
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.listbox.yview)
        self.scrollbar.grid(row=2, column=3, sticky="ns")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Configuración responsive
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=0)
        root.grid_columnconfigure(2, weight=0)
        root.grid_rowconfigure(2, weight=1)

        # Doble clic para marcar completada
        self.listbox.bind("<Double-Button-1>", self.marcar_completada)

    def agregar_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.listbox.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea antes de agregar.")

    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def marcar_completada(self, event):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            texto = self.listbox.get(index)
            if not texto.startswith("✔ "):
                self.listbox.delete(index)
                self.listbox.insert(index, "✔ " + texto)
            else:
                self.listbox.delete(index)
                self.listbox.insert(index, texto[2:])

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
