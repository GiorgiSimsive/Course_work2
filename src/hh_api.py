import requests

from src.api import JobAPI


class HeadHunterAPI(JobAPI):
    """Класс для работы с API hh.ru."""

    __slots__ = ("base_url",)

    def __init__(self) -> None:
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword: str) -> list:
        """Получает список вакансий с hh.ru по ключевому слову."""
        params = {"text": keyword, "per_page": 20, "page": 0}

        try:
            response = requests.get(self.base_url, params=params)  # type: ignore
            response.raise_for_status()
            return response.json().get("items", [])  # type: ignore
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API hh.ru: {e}")
            return []
