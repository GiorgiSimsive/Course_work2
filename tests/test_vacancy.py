from src.vacancy import Vacancy


def test_vacancy_creation() -> None:
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "100000", "Требования: опыт работы от 3 лет")
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://hh.ru/vacancy/123456"
    assert vacancy.salary == 100000
    assert vacancy.description == "Требования: опыт работы от 3 лет"


def test_vacancy_comparison() -> None:
    vac1 = Vacancy("Dev1", "https://hh.ru/1", 120000, "Описание 1")
    vac2 = Vacancy("Dev2", "https://hh.ru/2", 150000, "Описание 2")
    vac3 = Vacancy("Dev3", "https://hh.ru/3", 120000, "Описание 3")

    assert vac2 > vac1
    assert vac1 < vac2
    assert vac1.salary == vac3.salary  # Сравниваем только зарплату


def test_vacancy_salary_validation() -> None:
    vac = Vacancy("Без зарплаты", "https://hh.ru/4", "None", "Описание 4")
    assert vac.salary == 0
