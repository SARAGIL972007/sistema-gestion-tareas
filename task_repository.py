
"""Gestiona el almacenamiento de las tareas en memoria."""

from models.task import Task


class TaskRepository:

    _tasks: list[Task] = []

    def find_all(self) -> list[Task]:
        """Retorna todas las tareas."""
        return self._tasks

    def create_one(self, task: Task):
        """Guarda una nueva tarea."""
        self._tasks.append(task)