from src.vecancy import Vacancy


def test_vacancy_creation() -> None:
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "100000", "Требования: опыт работы от 3 лет")
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://hh.ru/vacancy/123456"
    assert vacancy.salary == 100000
    assert vacancy.description == "Требования: опыт работы от 3 лет"


def test_vacancy_comparison() -> None:
    vac1 = Vacancy("Dev1", "https://hh.ru/1", "120000", "Описание 1")  # зарплата как строка
    vac2 = Vacancy("Dev2", "https://hh.ru/2", "150000", "Описание 2")  # зарплата как строка
    vac3 = Vacancy("Dev3", "https://hh.ru/3", "120000", "Описание 3")  # зарплата как строка

    assert vac2 > vac1
    assert vac1 < vac2
    assert vac1 == vac3


def test_vacancy_salary_validation() -> None:
    vac = Vacancy("Без зарплаты", "https://hh.ru/4", "None", "Описание 4")  # Передаем строку "None"
    assert vac.salary == 0
