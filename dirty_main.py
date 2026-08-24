from datetime import datetime
from application.salary import *
from application.people import *


if __name__ == '__main__':
    current_date = datetime.now()
    print(f"=== Бухгалтерия (dirty_main) ===")
    print(f"Дата запуска: {current_date.strftime('%d.%m.%Y %H:%M:%S')}")
    print("-" * 30)

    # Вызываем функции, импортированные через *
    get_employees()
    print("-" * 30)
    calculate_salary()