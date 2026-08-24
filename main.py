from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees   # ← ИЗМЕНЕНО


if __name__ == '__main__':
    current_date = datetime.now()
    print(f"=== Бухгалтерия ===")
    print(f"Дата запуска: {current_date.strftime('%d.%m.%Y %H:%M:%S')}")
    print("-" * 30)

    get_employees()
    print("-" * 30)
    calculate_salary()