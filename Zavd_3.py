class NetworkConnection:
    def connect(self) -> str:
        return "З'єднання..."

class WiFiConnection(NetworkConnection):
    def connect(self) -> str:
        return "WiFi OK"

class LTEConnection(NetworkConnection):
    def connect(self) -> str:
        return "LTE OK"

class AdvancedConnection(NetworkConnection):
    def prepare(self) -> str:
        pass

class SatelliteConnection(AdvancedConnection):
    def prepare(self) -> str:
        return "Шукаю супутник..."
    
    def connect(self) -> str:
        return "Супутник підключено"

if __name__ == "__main__":
    connections = [WiFiConnection(), SatelliteConnection()]
    for conn in connections:
        if isinstance(conn, AdvancedConnection):
            print(conn.prepare())
        print(conn.connect())
