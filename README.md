docker build -t fastapi-redis .

docker run --name redis -d -p 6379:6379 redis:latest

docker run -d --name fastapi-container -p 8000:8000 --link redis fastapi-redis