from datetime import datetime
from application.salary import calculate_salary
from application.people import get_employees


if __name__ == '__main__':
    # Выводим текущую дату и время при запуске
    current_date = datetime.now()
    print(f"=== Бухгалтерия ===")
    print(f"Дата запуска: {current_date.strftime('%d.%m.%Y %H:%M:%S')}")
    print("-" * 30)

    # Вызываем импортированные функции
    get_employees()
    print("-" * 30)
    calculate_salary()