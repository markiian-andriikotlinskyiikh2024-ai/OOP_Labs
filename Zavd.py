import paho.mqtt.client as mqtt
import ssl
import time
import requests
import websocket
import json

# 2.1. Клас MQTTClient
class MQTTClient:
    def __init__(self, broker, port, client_id="LabClient", username=None, password=None):
        self.broker = broker
        self.port = port
        
        # Використовуємо VERSION2 для сумісності з останніми версіями paho-mqtt
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id)
        
        # Налаштування авторизації для Hive Cloud
        if username and password:
            self.client.username_pw_set(username, password)
            
        # Якщо використовується порт 8883, обов'язково вмикаємо TLS
        if self.port == 8883:
            self.client.tls_set(tls_version=ssl.PROTOCOL_TLS)

    def connect(self):
        try:
            print(f"Підключення до MQTT брокера {self.broker}...")
            self.client.connect(self.broker, self.port, keepalive=60)
            self.client.loop_start() # Запуск фонового потоку для обробки мережевих подій
            print("Успішно підключено до MQTT")
        except Exception as e:
            print(f"Помилка підключення до MQTT: {e}")

    def publish(self, topic, message):
        # Відправка повідомлення
        result = self.client.publish(topic, message)
        status = result[0]
        if status == 0:
            print(f"[MQTT] Опубліковано в топік '{topic}': {message}")
        else:
            print(f"[MQTT] Помилка публікації в топік '{topic}'")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Відключено від MQTT брокера.")

# 2.2. Інтеграція компонентів
def main():
    # Налаштування MQTT
    BROKER = "66601153745649f7afab6ca41093a042.s1.eu.hivemq.cloud"
    PORT = 8883
    TOPIC = "rtis/lab/telemetry" # Тема для публікації даних
    
    # Оновлені облікові дані (без пробілів)
    MQTT_USER = "lab_user"
    MQTT_PASSWORD = "swjmn789HHH"
    
    # Ініціалізація та підключення клієнта
    mqtt_client = MQTTClient(BROKER, PORT, username=MQTT_USER, password=MQTT_PASSWORD)
    mqtt_client.connect()
    time.sleep(2) # Даємо системі час на повноцінне встановлення TLS з'єднання
    
    # Налаштування WebSocket (публічний ехо-сервер Postman)
    WS_URL = "wss://ws.postman-echo.com/raw"
    ws = websocket.WebSocket()
    
    try:
        ws.connect(WS_URL)
        print(f"Підключено до WebSocket: {WS_URL}\n")
        print("-" * 50)
        
        # Цикл інтеграції (5 ітерацій)
        for i in range(1, 6):
            try:
                print(f"--- Ітерація {i} ---")
                # 1. Отримання даних через REST API (координати МКС з таймаутом 5 сек)
                rest_response = requests.get("http://api.open-notify.org/iss-now.json", timeout=5)
                
                if rest_response.status_code == 200:
                    raw_data = rest_response.json()
                    payload = json.dumps({
                        "source": "REST_API_ISS",
                        "latitude": raw_data['iss_position']['latitude'],
                        "longitude": raw_data['iss_position']['longitude']
                    })
                    print(f"[REST] Отримано координати: {payload}")
                    
                    # 2. Передача через WebSocket
                    ws.send(payload)
                    ws_response = ws.recv()
                    print(f"[WebSocket] Отримано відповідь: {ws_response}")
                    
                    # 3. Публікація через MQTT
                    mqtt_client.publish(TOPIC, ws_response)
                else:
                    print(f"[REST] Сервер повернув помилку: {rest_response.status_code}")
                    
            except requests.exceptions.Timeout:
                print("[REST] Перевищено час очікування від сервера API. Пропускаємо ітерацію.")
            except Exception as e:
                print(f"[Помилка ітерації] {e}")
                
            print("-" * 50)
            time.sleep(3)
            
    except Exception as e:
        print(f"Сталася критична помилка в системі: {e}")
    finally:
        ws.close()
        mqtt_client.disconnect()

if __name__ == "__main__":
    main()
