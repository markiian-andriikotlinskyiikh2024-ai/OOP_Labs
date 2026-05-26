import unittest
from unittest.mock import MagicMock
from parameterized import parameterized

# ==========================================
# ЗАВДАННЯ 1: Арифметичні операції
# ==========================================
class MathTool:
    """Клас для виконання базових арифметичних операцій."""
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        
    def divide(self, a, b):
        """Ділення з перевіркою на нуль."""
        if b == 0:
            raise ValueError("Ділення на нуль неможливе!")
        return a / b

# ==========================================
# ЗАВДАННЯ 2: Клас LibraryItem
# ==========================================
class LibraryItem:
    """Клас для опису об'єкта бібліотеки."""
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def details(self):
        """Повертає рядок із повною інформацією про книгу."""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# ==========================================
# ЗАВДАННЯ 3: Взаємодія класів (Mock)
# ==========================================
class NotificationService:
    """Сервіс для надсилання повідомлень."""
    def send(self, message):
        # В реальності тут міг бути код відправки Email/SMS
        pass

class UserManager:
    """Клас для керування користувачами."""
    def __init__(self, notification_service):
        self.notification_service = notification_service
        
    def notify_user(self, message):
        """Метод, що використовує зовнішній сервіс для сповіщення."""
        self.notification_service.send(message)

# ==========================================
# ЗАВДАННЯ 4: Функція парності
# ==========================================
def check_even(number):
    """Повертає True, якщо число парне, False якщо ні."""
    return number % 2 == 0


# ==========================================
# БЛОК ТЕСТУВАННЯ (UNIT TESTS)
# ==========================================
class TestAllLabs(unittest.TestCase):
    
    # --- Тести для MathTool ---
    def setUp(self):
        self.math = MathTool()

    def test_math_operations(self):
        """Перевірка базової арифметики."""
        self.assertEqual(self.math.add(10, 5), 15)
        self.assertEqual(self.math.subtract(10, 5), 5)
        self.assertEqual(self.math.multiply(10, 5), 50)
        self.assertEqual(self.math.divide(10, 2), 5)

    def test_math_divide_by_zero(self):
        """Перевірка виключення при діленні на нуль."""
        with self.assertRaises(ValueError):
            self.math.divide(10, 0)

    # --- Тести для LibraryItem ---
    def test_library_item_details(self):
        """Перевірка коректності формування рядка details()."""
        item = LibraryItem("Kobzar", "Shevchenko", 1840)
        expected = "Title: Kobzar, Author: Shevchenko, Year: 1840"
        self.assertEqual(item.details(), expected)

    # --- Тести для UserManager (Mock) ---
    def test_user_manager_notification(self):
        """Перевірка взаємодії класів через Моск-об'єкт."""
        mock_service = MagicMock(spec=NotificationService)
        manager = UserManager(mock_service)
        test_msg = "Test Alert"
        
        manager.notify_user(test_msg)
        
        # Перевіряємо, чи був викликаний метод send з правильним параметром
        mock_service.send.assert_called_once_with(test_msg)

    # --- Параметризовані тести для парності ---
    @parameterized.expand([
        ("even_positive", 2, True),
        ("odd_positive", 3, False),
        ("zero", 0, True),
        ("even_negative", -4, True),
        ("odd_negative", -5, False),
    ])
    def test_even_logic(self, name, num, expected):
        """Тестування парності на різних вхідних даних."""
        self.assertEqual(check_even(num), expected)


# Запуск усіх тестів
if __name__ == '__main__':
    unittest.main()
