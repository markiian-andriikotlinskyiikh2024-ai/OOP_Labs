class CallReportGenerator:
    def generate(self, data: str) -> str:
        return f"Звіт: {data}"

class ReportSaver:
    def save_to_file(self, filename: str, content: str) -> None:
        print(f"Файл {filename} збережено з текстом: {content}")

class Subscriber:
    def __init__(self, name: str, phone: str, balance: float):
        self.name = name
        self.phone = phone
        self.balance = balance

class SMSService:
    def send_sms(self, phone: str, message: str) -> None:
        print(f"SMS на {phone}: {message}")

class BillingCalculator:
    def calculate_balance(self, sub: Subscriber, cost: float) -> float:
        sub.balance -= cost
        return sub.balance

if __name__ == "__main__":
    subscriber = Subscriber("Маркіян", "+380", 100.0)
    
    BillingCalculator().calculate_balance(subscriber, 15.0)
    SMSService().send_sms(subscriber.phone, f"Ваш баланс: {subscriber.balance}")
