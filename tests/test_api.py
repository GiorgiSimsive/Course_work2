import pytest

from src.api import JobAPI  # Импортируем абстрактный класс


def test_abstract_api() -> None:
    """Проверяем, что нельзя создать экземпляр абстрактного класса API."""
    with pytest.raises(TypeError):
        JobAPI()  # type: ignore
