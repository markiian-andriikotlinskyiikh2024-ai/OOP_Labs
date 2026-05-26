import asyncio
import websockets
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class WebSocketClient:
    def __init__(self):
        self.connection = None

    async def connect(self, url):
        """Встановлює WebSocket-з'єднання за вказаною адресою."""
        try:
            self.connection = await websockets.connect(url)
            logging.info(f"Підключено до {url}")
        except websockets.exceptions.InvalidURI:
            logging.error(f"Недійсний URI: {url}")
        except OSError as e:
            logging.error(f"Помилка мережі при підключенні до {url}: {e}")
        except Exception as e:
            logging.error(f"Непередбачена помилка при підключенні: {e}")

    async def send_message(self, message):
        """Надсилає повідомлення серверу."""
        if self.connection:
            try:
                await self.connection.send(message)
                logging.info(f"Надіслано: {message}")
            except websockets.exceptions.ConnectionClosed:
                logging.error("З'єднання було закрито. Неможливо надіслати повідомлення.")
            except Exception as e:
                logging.error(f"Помилка при надсиланні повідомлення: {e}")
        else:
            logging.error("Немає активного з'єднання для відправки повідомлення.")

    async def receive_message(self):
        """Отримує повідомлення від сервера."""
        if self.connection:
            try:
                message = await self.connection.recv()
                logging.info(f"Отримано: {message}")
                return message
            except websockets.exceptions.ConnectionClosed:
                logging.error("З'єднання було закрито сервером.")
                return None
        else:
            logging.error("З'єднання не було встановлено.")
            return None

    async def close_connection(self):
        """Закриває WebSocket-з'єднання."""
        if self.connection:
            try:
                await self.connection.close()
                logging.info("З'єднання закрито.")
            except Exception as e:
                logging.error(f"Помилка при закритті з'єднання: {e}")
        else:
            logging.info("З'єднання не було встановлено.")


# Приклад використання
async def main():
    test_url = "wss://ws.postman-echo.com/raw"
    client = WebSocketClient()

    # 1. Встановлюємо з'єднання
    await client.connect(test_url)

    # Перевіряємо, чи об'єкт з'єднання існує (замість перевірки .closed)
    if client.connection:
        # 2. Надсилаємо перше повідомлення та чекаємо відповідь
        await client.send_message("Привіт, сервере!")
        await client.receive_message()

        # 3. Надсилаємо друге повідомлення та чекаємо відповідь
        await client.send_message("Тестуємо асинхронний клієнт.")
        await client.receive_message()

        # 4. Закриваємо з'єднання
        await client.close_connection()

        # 5. Тестування обробки помилок: спроба взаємодії після закриття
        logging.info("Спроба відправити повідомлення після закриття")
        await client.send_message("Це повідомлення не повинно бути відправлене.")

if __name__ == "__main__":
    asyncio.run(main())
