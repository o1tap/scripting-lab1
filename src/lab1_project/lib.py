"""
Модуль математичних та допоміжних утиліт.
"""

def calculate_checksum(data: str) -> int:
    """
    Обчислює просту контрольну суму для переданого рядка.
    """
    return sum(ord(char) for char in data)

def format_report(title: str, value: int) -> str:
    """
    Форматує результат для виводу в консоль.
    """
    return f"[ЗВІТ] {title}: {value}"