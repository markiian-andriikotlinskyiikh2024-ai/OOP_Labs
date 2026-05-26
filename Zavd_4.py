# 4.1: Дробимо один великий інтерфейс на три маленькі [cite: 278]
class Callable: # [cite: 278]
    def make_call(self): pass # [cite: 279]

class MessageSendable: # [cite: 282]
    def send_sms(self): pass # [cite: 284]

class DataTransferable: # [cite: 286]
    def connect_to_network(self): pass # [cite: 287]

# 4.2: IoT пристрою тепер не треба реалізовувати дзвінки [cite: 288]
class Smartphone(Callable, MessageSendable, DataTransferable): # [cite: 289]
    def make_call(self):  # [cite: 290]
        print("Дзвоню") # [cite: 290]
        
    def connect_to_network(self):  # [cite: 291]
        print("У мережі") # [cite: 291]

class IoTDevice(DataTransferable): # [cite: 306]
    def connect_to_network(self): # [cite: 307]
        print("IoT: тільки передача даних") # [cite: 308]

if __name__ == "__main__": # [cite: 309]
    IoTDevice().connect_to_network() # [cite: 310]
