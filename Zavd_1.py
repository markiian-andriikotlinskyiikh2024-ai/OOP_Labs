# 1.1: Розділяємо звіт: один клас створює текст, інший пише у файл [cite: 101]
class CallReportGenerator: # [cite: 102]
    def generate(self, data): # [cite: 103]
        return f"Звіт: {data}" # [cite: 104]

class ReportSaver: # [cite: 94]
    def save_to_file(self, filename, content): # [cite: 105]
        print(f"Файл {filename} збережено") # [cite: 106]

# 1.2: Розділяємо Subscriber: дані окремо, логіка окремо [cite: 107]
class Subscriber: # [cite: 108]
    def __init__(self, name, phone, balance): # [cite: 109]
        self.name = name # [cite: 111]
        self.phone = phone # [cite: 113]
        self.balance = balance # [cite: 116]

class SMSService: # [cite: 120]
    def send_sms(self, phone, message): # [cite: 128]
        print(f"SMS на {phone}: {message}") # [cite: 129]

class BillingCalculator: # [cite: 130]
    def calculate_balance(self, sub, cost): # [cite: 131]
        sub.balance -= cost # [cite: 132]
        return sub.balance # [cite: 133]

if __name__ == "__main__": # [cite: 136, 137]
    s = Subscriber("Маркіян", "+380", 100) # [cite: 141]
    BillingCalculator().calculate_balance(s, 15) # [cite: 142]
    SMSService().send_sms(s.phone, f"Баланс: {s.balance}") # [cite: 143]
