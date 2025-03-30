from abc import ABC, abstractmethod


class JobAPI(ABC):
    """Абстрактный класс для работы с API сервиса вакансий."""

    @abstractmethod
    def get_vacancies(self, query: str) -> list:
        """Метод для получения вакансий по запросу."""
        pass
