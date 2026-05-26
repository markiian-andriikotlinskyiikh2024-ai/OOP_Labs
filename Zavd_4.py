from abc import ABC, abstractmethod

class Callable(ABC):
    @abstractmethod
    def make_call(self) -> None: 
        pass

class MessageSendable(ABC):
    @abstractmethod
    def send_sms(self) -> None: 
        pass

class DataTransferable(ABC):
    @abstractmethod
    def connect_to_network(self) -> None: 
        pass

class Smartphone(Callable, MessageSendable, DataTransferable):
    def make_call(self) -> None: 
        print("Дзвоню...")
        
    def send_sms(self) -> None:
        print("Відправляю SMS...")
        
    def connect_to_network(self) -> None: 
        print("Підключено до мережі")

class IoTDevice(DataTransferable):
    def connect_to_network(self) -> None:
        print("IoT: доступна тільки передача даних")

if __name__ == "__main__":
    iot = IoTDevice()
    iot.connect_to_network()
