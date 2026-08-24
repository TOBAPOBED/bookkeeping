from datetime import datetime
from application.salary import *
from application.db.people import *   # ← ИЗМЕНЕНО


if __name__ == '__main__':
    current_date = datetime.now()
    print(f"=== Бухгалтерия (dirty_main) ===")
    print(f"Дата запуска: {current_date.strftime('%d.%m.%Y %H:%M:%S')}")
    print("-" * 30)

    get_employees()
    print("-" * 30)
    calculate_salary()