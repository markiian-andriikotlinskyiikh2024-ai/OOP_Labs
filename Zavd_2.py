# 2.1: База для тарифів. Закрита для змін, відкрита для нових класів [cite: 154]
class Tariff: # [cite: 155]
    def calculate_price(self, units): # [cite: 165]
        raise NotImplementedError # [cite: 166]

class BaseTariff(Tariff): # [cite: 167]
    def calculate_price(self, units): # [cite: 168]
        return units * 0.5 # [cite: 169]

# 2.2: Додаємо нові тарифи просто новими класами [cite: 170]
class VoiceTariff(Tariff): # [cite: 171]
    def calculate_price(self, units): # [cite: 172]
        return units * 0.6 # [cite: 173]

class DataTariff(Tariff): # [cite: 174]
    def calculate_price(self, units): # [cite: 175]
        return units * 0.1 # [cite: 176]

class RoamingTariff(Tariff): # [cite: 177]
    def calculate_price(self, units): # [cite: 192]
        return units * 5.0 # [cite: 193]

if __name__ == "__main__": # [cite: 194]
    for t in [BaseTariff(), RoamingTariff()]: # [cite: 195]
        print(f"{t.__class__.__name__}: {t.calculate_price(100)} грн") # [cite: 196]
