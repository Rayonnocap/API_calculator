# API Калькулятор

## Эндпоинты

POST /add       {"a": 2, "b": 3}

POST /subtract  {"a": 5, "b": 3}

POST /multiply  {"a": 4, "b": 6}

POST /divide    {"a": 10, "b": 4}

## Развернуть у себя локально:

pip install -r requirements.txt
python app.py

Затем перейти в браузере: http://localhost:5000

## Docker

docker build -t calculator .

docker run -p 5000:5000 calculator

