# Используем официальный образ Python
FROM python:3.9-slim

# Установим рабочую директорию внутри контейнера
WORKDIR /app

# Скопируем все файлы в контейнер
COPY . .

# Установим необходимые пакеты
RUN pip install -r requirements.txt

# Укажем команду для запуска приложения
CMD ["python", "main.py"]
