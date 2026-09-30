"""
Головна точка входу в програму.
"""
from lib import calculate_checksum, format_report

def main():
    """
    Основна функція виконання скрипту.
    """
    message = "Версія гілки А"
    checksum = calculate_checksum(message)
    output = format_report("Контрольна сума повідомлення", checksum)
    print(output)

if __name__ == "__main__":
    main()