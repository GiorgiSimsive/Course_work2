class Vacancy:
    """Класс для представления вакансии."""

    def __init__(self, title: str, url: str, salary: str, description: str):
        """
        Инициализация вакансии.
        """
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    @staticmethod
    def validate_salary(salary: str) -> int:
        """Проверяет и форматирует зарплату."""
        if not salary or (isinstance(salary, str) and salary.lower() in ["не указана", "none"]):
            return 0
        return int(salary)

    def __str__(self) -> str:
        """Форматированный вывод вакансии."""
        return f"{self.title} ({self.salary})\n{self.url}\n{self.description[:100]}..."

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (если возможно)."""
        return self.get_numeric_salary() < other.get_numeric_salary()

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (если возможно)."""
        return self.get_numeric_salary() > other.get_numeric_salary()

    def get_numeric_salary(self) -> int:
        """Возвращает числовое значение зарплаты."""
        return self.salary

    def __eq__(self, other):  # type: ignore
        """Сравнение вакансий по зарплате."""
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False
