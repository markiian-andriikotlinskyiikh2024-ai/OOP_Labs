import asyncio
import random
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

# Конфігурація бази даних
Base = declarative_base()
DATABASE_URL = "sqlite+aiosqlite:///network_monitor.db"

# === ЗАВДАННЯ №1: Створити модель таблиці nodes ===
class Node(Base):
    __tablename__ = 'nodes'
    
    id = Column(Integer, primary_key=True)
    ip_address = Column(String, unique=True, nullable=False)
    status = Column(String, default="unknown")

# Налаштування асинхронного двигуна
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Створення бази та таблиці в ній
async def init_db():
    async with engine.begin() as conn:
        # Видаляємо старе, щоб бачити чистий результат при кожному запуску
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print(">>> Завдання 1: Базу даних та таблицю 'nodes' створено.")

# Допоміжна функція: заповнення початковими даними (12 вузлів)
async def seed_data():
    async with AsyncSessionLocal() as session:
        nodes = [Node(ip_address=f"192.168.1.{i}") for i in range(1, 13)]
        session.add_all(nodes)
        await session.commit()
    print(">>> Демонстрація: Додано 12 вузлів у таблицю.")

# === ЗАВДАННЯ №2: Асинхронна функція для отримання списку вузлів ===
async def get_nodes_list(label="Список"):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Node))
        nodes = result.scalars().all()
        print(f"\n--- {label} ---")
        for n in nodes:
            print(f"ID: {n.id:2} | IP: {n.ip_address:12} | Статус: {n.status}")
        return nodes

# === ЗАВДАННЯ №3: Імітація мережевих запитів (збір статусів) ===
async def fetch_status(ip):
    # Імітуємо затримку мережі від 0.5 до 1.5 секунди
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return "active" if random.random() > 0.3 else "offline"

# === ЗАВДАННЯ №4: Збереження отриманих даних у базі через SQLAlchemy ===
async def run_monitoring():
    print("\n>>> Завдання 3 та 4: Початок асинхронного моніторингу...")
    async with AsyncSessionLocal() as session:
        # Отримуємо всі вузли для перевірки
        result = await session.execute(select(Node))
        nodes = result.scalars().all()
        
        # Створюємо список завдань для одночасного виконання
        tasks = [fetch_status(node.ip_address) for node in nodes]
        
        # Чекаємо на завершення всіх "запитів" паралельно
        new_statuses = await asyncio.gather(*tasks)
        
        # Оновлюємо статуси в об'єктах та зберігаємо в БД
        for node, status in zip(nodes, new_statuses):
            node.status = status
        await session.commit()
        
    print(">>> Завдання 4: Нові статуси успішно збережені в БД.")

# === ЗАВДАННЯ №5: Демонстрація виконання ===
async def main():
    await init_db()
    await seed_data()
    await get_nodes_list("СТАН ДО МОНІТОРИНГУ (Завдання 2)")
    await run_monitoring()
    await get_nodes_list("СТАН ПІСЛЯ МОНІТОРИНГУ (Завдання 5)")

if __name__ == "__main__":
    asyncio.run(main())
