from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем через консоль."""

    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    while True:
        print("\nМеню:")
        print("1. Ввести поисковый запрос")
        print("2. Показать топ N вакансий по зарплате")
        print("3. Найти вакансии по ключевым словам в описании")
        print("4. Удалить вакансию")
        print("5. Показать сохраненные вакансии")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            search_query = input("Введите поисковый запрос: ")
            vacancies_data = hh_api.get_vacancies(search_query)
            vacancies_list = Vacancy.create_from_hh_data(vacancies_data)

            json_saver.save_to_file(vacancies_list)
            print(f"Найдено и сохранено {len(vacancies_list)} вакансий.")

        elif choice == "2":
            try:
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                vacancies = json_saver.load_from_file()
                sorted_vacancies = sorted(vacancies, key=lambda v: v.salary if v.salary else -1, reverse=True)
                for vac in sorted_vacancies[:top_n]:
                    print(vac)
            except ValueError:
                print("Ошибка: Введите корректное число.")

        elif choice == "3":
            keyword = input("Введите ключевое слово для фильтрации вакансий: ").lower()
            vacancies = json_saver.load_from_file()
            filtered_vacancies = [v for v in vacancies if keyword in v.description.lower()]
            for vac in filtered_vacancies:
                print(vac)

        elif choice == "4":
            url = input("Введите URL вакансии для удаления: ")
            vacancies = json_saver.load_from_file()
            vacancy_to_delete = next((v for v in vacancies if v.url == url), None)
            if vacancy_to_delete:
                json_saver.delete_vacancy(vacancy_to_delete)
                print("Вакансия удалена.")
            else:
                print("Вакансия не найдена.")

        elif choice == "5":
            vacancies = json_saver.load_from_file()
            for vac in vacancies:
                print(vac)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")
