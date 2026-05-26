import requests
import logging

# Налаштування логування для зручного відстеження помилок
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class RestClient:
    def __init__(self, base_url, headers=None):
        # Ініціалізує клієнт базовою URL-адресою та опціональними заголовками
        self.base_url = base_url.rstrip('/')
        # За замовчуванням встановлюємо заголовок для роботи з JSON
        self.headers = headers if headers else {'Content-Type': 'application/json'}

    def get(self, endpoint):
        # Виконує HTTP GET-запит.
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            logging.info(f"Виконання GET-запиту до: {url}")
            response = requests.get(url, headers=self.headers)
            # Перевірка статус-коду. Якщо код помилки (4xx, 5xx), генерується виняток
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP помилка: {http_err} Статус код: {response.status_code}")
        except requests.exceptions.ConnectionError as conn_err:
            logging.error(f"Помилка з'єднання: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            logging.error(f"Перевищено час очікування (Timeout): {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Непередбачена помилка запиту: {req_err}")
        return None

    def post(self, endpoint, data):
        # Виконує HTTP POST-запит з переданими даними (payload).
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            logging.info(f"Виконання POST-запиту до: {url}")
            # requests автоматично серіалізує словник "data" у JSON за допомогою параметра json
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            # JSONPlaceholder повертає 201 (Created) при успішному POST
            if response.status_code == 201:
                logging.info("Ресурс успішно створено!")
                return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP помилка: {http_err} Статус код: {response.status_code}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Помилка запиту: {req_err}")
        return None

# ДЕМОНСТРАЦІЯ ВИКОРИСТАННЯ
if __name__ == "__main__":
    # 1. Ініціалізація клієнта
    BASE_URL = "https://jsonplaceholder.typicode.com"
    client = RestClient(base_url=BASE_URL)

    print("-" * 50)
    print("ТЕСТ 1: Успішний GET-запит (отримання поста з ID=1)")
    print("-" * 50)
    post_data = client.get("posts/1")
    if post_data:
        print(f"Заголовок: {post_data.get('title')}")
        print(f"Тіло: {post_data.get('body')}")

    print("\n" + "-" * 50)
    print("ТЕСТ 2: Успішний POST-запит (створення нового ресурсу)")
    print("-" * 50)
    new_post = {
        "title": "Мій новий пост",
        "body": "Це тестове тіло повідомлення для перевірки методу POST.",
        "userId": 101
    }
    created_post = client.post("posts", data=new_post)
    if created_post:
        print(f"Відповідь сервера (створений об'єкт): {created_post}")

    print("\n" + "-" * 50)
    print("ТЕСТ 3: Обробка помилки (GET-запит до неіснуючого ресурсу)")
    print("-" * 50)
    # Звертаємося до ресурсу, якого не існує (ID=9999)
    error_data = client.get("posts/9999")
    if error_data is None:
        print("Запит завершився невдало (отримано None), помилку оброблено коректно.")
