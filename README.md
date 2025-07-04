# CSV Processor

Скрипт для обработки CSV-файла с поддержкой фильтрации и агрегации по одной колонке.

## 📦 Установка зависимостей

```bash
pip install -r requirements.txt
```

## 🚀 Примеры запуска

Файл `sample.csv`:
```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4
```

### 🔍 Фильтрация

```bash
python -m csv_processor.main csv_processor/sample.csv --where brand=xiaomi
```

Вывод:
```
| name          | brand  | price | rating |
|---------------|--------|-------|--------|
| redmi note 12 | xiaomi |   199 |    4.6 |
| poco x5 pro   | xiaomi |   299 |    4.4 |
```

### 📊 Агрегация

```bash
python -m csv_processor.main csv_processor/sample.csv --aggregate price=avg
```

Вывод:
```
| name              | brand   | price | rating |
|-------------------|---------|-------|--------|
| iphone 15 pro     | apple   |   999 |    4.9 |
| galaxy s23 ultra  | samsung |  1199 |    4.8 |
| redmi note 12     | xiaomi  |   199 |    4.6 |
| poco x5 pro       | xiaomi  |   299 |    4.4 |

avg по колонке price: 674.0
```

### 🔀 Фильтрация + агрегация

```bash
python -m csv_processor.main csv_processor/sample.csv --where brand=xiaomi --aggregate rating=max
```

Вывод:
```
| name          | brand  | price | rating |
|---------------|--------|-------|--------|
| redmi note 12 | xiaomi |   199 |    4.6 |
| poco x5 pro   | xiaomi |   299 |    4.4 |

max по колонке rating: 4.6
```

## ✅ Тестирование

```bash
pytest --cov=csv_processor
```
