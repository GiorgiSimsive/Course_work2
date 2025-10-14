import pytest

from src.hh_api import HeadHunterAPI


@pytest.fixture
def mock_hh_response(mocker):  # type: ignore
    """Мок ответа API hh.ru"""
    mock_response = {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/123",
                "salary": {"from": 100000},
                "snippet": {"requirement": "Опыт 3 года"},
            },
            {
                "name": "Data Scientist",
                "alternate_url": "https://hh.ru/vacancy/456",
                "salary": {"from": 150000},
                "snippet": {"requirement": "Опыт 2 года"},
            },
        ]
    }
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    return mock_get


def test_hh_api_get_vacancies(mock_hh_response):  # type: ignore
    """Тестируем метод get_vacancies с моком API hh.ru."""
    api = HeadHunterAPI()
    vacancies = api.get_vacancies("Python")

    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Python Developer"
    assert vacancies[1]["salary"]["from"] == 150000
