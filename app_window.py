import tkinter as tk
from tkinter import ttk, messagebox
from services.task_service import TaskService


class AppWindow(tk.Tk):

    def __init__(self, service: TaskService) -> None:
        super().__init__()

        self.service = service

        self.title("Sistema de Gestión de Tareas")
        self.geometry("700x500")

        self.create_widgets()

    def create_widgets(self):

        # Título
        title_label = tk.Label(self, text="Título de la tarea")
        title_label.pack()

        self.entry_title = tk.Entry(self, width=50)
        self.entry_title.pack()

        # Descripción
        description_label = tk.Label(self, text="Descripción")
        description_label.pack()

        self.entry_description = tk.Entry(self, width=50)
        self.entry_description.pack()

        # Botón para crear tarea
        self.create_btn = tk.Button(
            self,
            text="Crear tarea",
            command=self.create_task
        )
        self.create_btn.pack(pady=10)

        # Tabla de tareas
        self.tree = ttk.Treeview(
            self,
            columns=("id", "title", "description"),
            show="headings"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Título")
        self.tree.heading("description", text="Descripción")

        self.tree.column("id", width=180)
        self.tree.column("title", width=180)
        self.tree.column("description", width=300)

        self.tree.pack(fill="both", expand=True)

        # Cargar los datos
        self.render_data_table()

    def create_task(self):

        title = self.entry_title.get().strip()
        description = self.entry_description.get().strip()

        if not title or not description:
            messagebox.showwarning(
                "Advertencia",
                "Debes completar los dos campos."
            )
            return

        self.service.create_one(title, description)

        self.render_data_table()

        self.entry_title.delete(0, "end")
        self.entry_description.delete(0, "end")

        messagebox.showinfo(
            "Información",
            "Tarea creada correctamente."
        )

    def render_data_table(self):

        tasks = self.service.find_all()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for task in tasks:
            self.tree.insert(
                "",
                "end",
                values=(
                    str(task.uuid),
                    task.title,
                    task.description
                )
            )