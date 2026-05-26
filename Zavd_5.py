import sys
import io
from abc import ABC, abstractmethod

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

class Logger(ABC):
    @abstractmethod
    def log(self, msg: str) -> None: 
        pass

class FileLogger(Logger):
    def log(self, msg: str) -> None: 
        print(f"Лог у файл: {msg}")

class ServerLogger(Logger):
    def log(self, msg: str) -> None: 
        print(f"Лог на сервер: {msg}")

class NetworkMonitor:
    def __init__(self, logger: Logger):
        self.logger = logger
        
    def check(self) -> None:
        self.logger.log("Мережа працює стабільно")

if __name__ == "__main__":
    server_logger = ServerLogger()
    monitor = NetworkMonitor(server_logger)
    monitor.check()
