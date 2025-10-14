import json
from abc import ABC, abstractmethod
from typing import List

from src.vacancy import Vacancy


class VacancyStorage(ABC):
    """Абстрактный класс для работы с хранилищем вакансий."""

    @abstractmethod
    def save_to_file(self, vacancies: List[Vacancy]) -> None:
        pass

    @abstractmethod
    def load_from_file(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass


class JSONSaver(VacancyStorage):
    """Класс для сохранения вакансий в JSON-файл."""

    __slots__ = ("filename",)

    def __init__(self, filename: str = "vacancies.json"):
        self.filename = filename

    def save_to_file(self, vacancies: List) -> None:
        """Сохраняет список вакансий в JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [vac.to_dict() for vac in vacancies], file, ensure_ascii=False, indent=4
            )

    def load_from_file(self) -> List[Vacancy]:
        """Загружает вакансии из JSON-файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Vacancy(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет новую вакансию, исключая дубли по URL."""
        vacancies = self.load_from_file()
        if vacancy.url not in {v.url for v in vacancies}:
            vacancies.append(vacancy)
            self.save_to_file(vacancies)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию по её URL."""
        vacancies = self.load_from_file()
        vacancies = [v for v in vacancies if v.url != vacancy.url]
        self.save_to_file(vacancies)
