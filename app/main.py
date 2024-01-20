from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis

app = FastAPI()
redis_client = Redis(host='redis', port=6379)  # Подключение к Redis

class Data(BaseModel):
    phone: str
    address: str

@app.get("/check_data")
def check_data(phone: str):
    address = redis_client.get(phone)  # Получение адреса из Redis по ключу (номеру телефона)
    if address:
        return {"address": address.decode()}  # Возврат адреса в ответе
    else:
        return {"message": "Address not found"}  # Обработка случая, когда адрес не найден

@app.post("/write_data")
def write_data(data: Data):
    redis_client.set(data.phone, data.address)  # Запись данных в Redis (ключ: номер телефона, значение: адрес)
    return {"message": "Data written successfully"}

@app.put("/write_data")
def update_data(data: Data):
    if redis_client.exists(data.phone):
        redis_client.set(data.phone, data.address)  # Обновление данных в Redis, если номер телефона существует
        return {"message": "Data updated successfully"}
    else:
        return {"message": "Phone number not found"}  # Обработка случая, когда номер телефона не найден

