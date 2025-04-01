import os

import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def json_saver():  # type: ignore
    return JSONSaver("test_vacancies.json")


def test_save_and_load(json_saver):  # type: ignore
    """Тестируем сохранение и загрузку вакансий."""
    vacancy = Vacancy("Python Developer", "https://hh.ru/1", 100000, "Требуется опыт от 3 лет")
    json_saver.save_to_file([vacancy])

    loaded_vacancies = json_saver.load_from_file()
    assert len(loaded_vacancies) == 1
    assert loaded_vacancies[0].title == "Python Developer"

    os.remove("test_vacancies.json")


def test_add_and_delete(json_saver):  # type: ignore
    """Тестируем добавление и удаление вакансий."""
    vacancy = Vacancy("Java Developer", "https://hh.ru/2", 120000, "Требуется Java")
    json_saver.add_vacancy(vacancy)

    loaded_vacancies = json_saver.load_from_file()
    assert len(loaded_vacancies) == 1

    json_saver.delete_vacancy(vacancy)
    assert len(json_saver.load_from_file()) == 0

    os.remove("test_vacancies.json")
