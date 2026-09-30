"""
Головна точка входу в програму.
"""
from lib import calculate_checksum, format_report

def main():
    """
    Основна функція виконання скрипту.
    """
    message = "Фінальна узгоджена версія"
    checksum = calculate_checksum(message)
    output = format_report("Контрольна сума повідомлення", checksum)
    print(output)

if __name__ == "__main__":
    main()
"""Головна точка входу."""
from lab1_project.lib import calculate_checksum, format_report, multiply

def main():
    """Основна логіка скрипту."""
    message = "DevSecOps Pipeline 2026"
    checksum = calculate_checksum(message)
    output = format_report("Контрольна сума повідомлення", checksum)
    print(output)
    
    product = multiply(7, 8)
    print(f"[ЗВІТ] Результат множення: {product}")

if __name__ == "__main__":
    main()