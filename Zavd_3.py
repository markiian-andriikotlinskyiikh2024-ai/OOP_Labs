# 3.1: WiFi та LTE працюють однаково через базовий клас [cite: 218]
class NetworkConnection: # [cite: 220]
    def connect(self): # [cite: 221]
        return "З'єднання..." # [cite: 222]

class WiFiConnection(NetworkConnection): # [cite: 223]
    def connect(self): # [cite: 224]
        return "WiFi OK" # [cite: 225]

class LTEConnection(NetworkConnection): # [cite: 226]
    def connect(self): # [cite: 227]
        return "LTE OK" # [cite: 229]

# 3.2: Супутник специфічний, тому виносимо підготовку в окремий інтерфейс [cite: 233]
class AdvancedConnection(NetworkConnection): # [cite: 233]
    def prepare(self): pass # [cite: 238]

class SatelliteConnection(AdvancedConnection): # [cite: 239]
    def prepare(self): # [cite: 240]
        return "Шукаю супутник..." # [cite: 242]
    
    def connect(self): # [cite: 244]
        return "Супутник підключено" # [cite: 246]

if __name__ == "__main__": # [cite: 249]
    conns = [WiFiConnection(), SatelliteConnection()] # [cite: 251, 252]
    for c in conns: # [cite: 253]
        if isinstance(c, AdvancedConnection):  # [cite: 255]
            print(c.prepare()) # [cite: 255]
        print(c.connect()) # [cite: 256]
