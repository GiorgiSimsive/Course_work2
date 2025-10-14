class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title: str, url: str, salary: int | str, description: str):
        """
        Инициализация вакансии.
        """
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    def to_dict(self):  # type: ignore
        """Возвращает словарь с атрибутами вакансии."""
        return {"title": self.title, "url": self.url, "salary": self.salary, "description": self.description}

    @staticmethod
    def validate_salary(salary: int | str) -> int:
        """Преобразует зарплату в число или возвращает 0, если данных нет."""
        if isinstance(salary, int):
            return salary
        if isinstance(salary, str):
            if salary.lower() == "none":
                return 0
            if salary.isdigit():
                return int(salary)
        return 0

    @classmethod
    def create_from_hh_data(cls, vacancies_data: list) -> list:
        """Создает список объектов Vacancy из данных API hh.ru."""
        vacancies = []
        for item in vacancies_data:
            title = item.get("name", "Без названия")
            url = item.get("alternate_url", "")
            salary_info = item.get("salary")
            if salary_info and salary_info.get("from"):
                salary = salary_info["from"]
            else:
                salary = 0
            description = item.get("snippet", {}).get("responsibility", "Описание отсутствует")
            vacancies.append(cls(title, url, salary, description))
        return vacancies

    def __str__(self) -> str:
        """Форматированный вывод вакансии."""
        return f"{self.title} ({self.salary})\n{self.url}\n{self.description[:100]}..."

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (если возможно)."""
        return self.salary < other.salary

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (если возможно)."""
        return self.salary > other.salary

    def __eq__(self, other: object) -> bool:
        """Сравнение вакансий по всем параметрам."""
        if not isinstance(other, Vacancy):
            return False
        return (self.title, self.url, self.salary, self.description) == (
            other.title,
            other.url,
            other.salary,
            other.description,
        )
