from abc import ABC, abstractmethod

class Tariff(ABC):
    @abstractmethod
    def calculate_price(self, units: float) -> float:
        pass

class BaseTariff(Tariff):
    def calculate_price(self, units: float) -> float:
        return units * 0.5

class VoiceTariff(Tariff):
    def calculate_price(self, units: float) -> float:
        return units * 0.6

class DataTariff(Tariff):
    def calculate_price(self, units: float) -> float:
        return units * 0.1

class RoamingTariff(Tariff):
    def calculate_price(self, units: float) -> float:
        return units * 5.0

if __name__ == "__main__":
    tariffs = [BaseTariff(), RoamingTariff()]
    for t in tariffs:
        print(f"Тариф {t.__class__.__name__}: {t.calculate_price(100)} грн")
