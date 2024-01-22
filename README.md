Для запуска контейнера выполнить:

docker build -t fastapi-redis .

docker run --name redis -d -p 6379:6379 redis:latest

docker run -d --name fastapi-container -p 8000:8000 --link redis fastapi-redis



2 задание:


UPDATE public.full_names fn
SET status = sn.status
FROM public.short_names sn
WHERE sn.name = substring(fn.name from 1 for position('.' in fn.name)-1); 

UPDATE public.full_names fn
SET status = sn.status
FROM public.short_names sn
WHERE regexp_like(fn.name,sn.name||'.\w+$');
