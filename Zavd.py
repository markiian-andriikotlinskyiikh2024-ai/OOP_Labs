import asyncio
import random
import time
import networkx as nx
import matplotlib.pyplot as plt

# 2. Створення класів вузлів мережі
class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, node):
        """Метод для встановлення з'єднань між вузлами"""
        if node not in self.connections:
            self.connections.append(node)
            node.connections.append(self)

    async def send(self, packet, network):
        await asyncio.sleep(random.uniform(0.01, 0.05))
        # 3. Симуляція випадкової втрати пакетів 10-15%
        if random.random() < network.loss_rate:
            network.lost_p += 1
            return
        await self.forward(packet, network)

    async def forward(self, packet, network):
        """Асинхронне просування пакету по мережі"""
        if self.name == packet.dest or self in packet.visited: 
            return
        
        packet.visited.append(self)
        
        for node in self.connections:
            if node not in packet.visited:
                await node.send(packet, network)

class Router(Node):
    """Спеціалізований вузол Router для топологій"""
    pass

# 3. Реалізація передавання пакетів (клас Packet)
class Packet:
    def __init__(self, src, dest, size, protocol):
        self.src = src
        self.dest = dest
        self.size = size
        self.protocol = protocol
        self.visited = []

# 4. Розробка моделей для TCP та UDP
class TCPProtocol:
    name = "TCP"
    
    @staticmethod
    async def transmit(src, dest, net):
        # TCP моделює надійну передачу з більшим пакетом
        packet = Packet(src.name, dest.name, random.randint(200, 500), "TCP")
        print(f"[{packet.protocol}] Sending from {src.name} to {dest.name}...")
        await src.send(packet, net)

class UDPProtocol:
    name = "UDP"
    
    @staticmethod
    async def transmit(src, dest, net):
        # UDP моделює швидку передачу без гарантій доставки
        packet = Packet(src.name, dest.name, random.randint(50, 200), "UDP")
        print(f"[{packet.protocol}] Sending from {src.name} to {dest.name}...")
        await src.send(packet, net)

# 5. Створення асинхронного механізму моделювання
class Network:
    def __init__(self, top_name):
        self.nodes = []
        self.top_name = top_name
        self.loss_rate = random.uniform(0.10, 0.15)
        self.sent_p = 0
        self.lost_p = 0
        self.total_t = 0

    async def simulate(self, protocol, tasks):
        for s, d in tasks:
            start = time.perf_counter()
            self.sent_p += 1
            await protocol.transmit(s, d, self)
            self.total_t += (time.perf_counter() - start)

    def analyze(self):
        """Аналіз продуктивності: час та втрати"""
        res = {
            'total_packets': self.sent_p,
            'lost_packets': self.lost_p,
            'average_time': self.total_t / self.sent_p if self.sent_p > 0 else 0
        }
        print(f"\nPerformance Metrics for {self.top_name} topology:")
        print(f"{res}\n")

    def get_graph(self):
        """Побудова структури для networkx"""
        G = nx.Graph()
        for n in self.nodes:
            for c in n.connections:
                G.add_edge(n.name, c.name)
        return G

async def main():
    # --- Моделювання зіркової топології (UDP) ---
    star_net = Network("star")
    r1 = Router("R1")
    pcs_s = [Node("A"), Node("B"), Node("C")]
    
    star_net.nodes = [r1] + pcs_s
    for n in pcs_s: 
        r1.connect(n)

    await star_net.simulate(UDPProtocol, [(pcs_s[0], pcs_s[1]), (pcs_s[1], pcs_s[2]), (pcs_s[2], pcs_s[0])])
    star_net.analyze()

    # --- Моделювання деревоподібної топології (TCP) ---
    tree_net = Network("tree")
    root_t = Router("R1")
    a, b, c, d = Node("A"), Node("B"), Node("C"), Node("D")
    
    root_t.connect(a)
    root_t.connect(b)
    b.connect(c)
    c.connect(d)
    tree_net.nodes = [root_t, a, b, c, d]

    await tree_net.simulate(TCPProtocol, [(a, b), (b, c), (c, d)])
    tree_net.analyze()

    # --- Візуалізація двох схем одночасно ---
    plt.figure(figsize=(12, 6))
    plt.suptitle("Аналіз топологій та протоколів телекомунікаційної мережі", fontsize=16)

    # Зірка (UDP)
    plt.subplot(121)
    nx.draw(star_net.get_graph(), with_labels=True, node_color='skyblue', node_size=1500, font_weight='bold')
    plt.title("Зірка (UDP)")

    # Дерево (TCP)
    plt.subplot(122)
    nx.draw(tree_net.get_graph(), with_labels=True, node_color='lightgreen', node_size=1500, font_weight='bold')
    plt.title("Дерево (TCP)")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
