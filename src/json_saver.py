import json
from typing import Any, List

from src.vecancy import Vacancy


class JSONSaver:
    """Класс для сохранения вакансий в JSON-файл."""

    def __init__(self, filename: str = "vacancies.json"):
        """
        Инициализация.
        """
        self.filename = filename

    def save_to_file(self, vacancies: List) -> None:
        """Сохраняет список вакансий в JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([vac.__dict__ for vac in vacancies], file, ensure_ascii=False, indent=4)

    def load_from_file(self) -> List:
        """Загружает вакансии из JSON-файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Vacancy(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_vacancy(self, vacancy: Any) -> None:
        """Добавляет новую вакансию в JSON-файл."""
        vacancies = self.load_from_file()
        vacancies.append(vacancy)
        self.save_to_file(vacancies)

    def delete_vacancy(self, vacancy: "Vacancy") -> None:
        """Удаляет вакансию по её URL."""
        vacancies = self.load_from_file()
        vacancies = [v for v in vacancies if v.url != vacancy.url]
        self.save_to_file(vacancies)
