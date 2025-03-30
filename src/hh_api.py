from typing import Dict, Union

import requests

from src.api import JobAPI


class HeadHunterAPI(JobAPI):
    """Класс для работы с API hh.ru."""

    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query: str) -> list:
        """Получает вакансии по запросу из hh.ru."""
        params: Dict[str, Union[str, int]] = {"text": query, "per_page": 20, "page": 0}
        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            return response.json().get("items", [])  # type: ignore
        else:
            print(f"Ошибка {response.status_code}: {response.text}")
            return []
