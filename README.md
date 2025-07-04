# CSV Processor

Скрипт для фильтрации и агрегации данных из CSV-файла.

## Использование

Примеры запуска:

```bash
python main.py sample.csv --where brand=xiaomi
python main.py sample.csv --where price>500
python main.py sample.csv --aggregate price=avg
python main.py sample.csv --where brand=xiaomi --aggregate rating=max

Пример CSV

name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4

Установка

pip install -r requirements.txt

Тесты

pytest
