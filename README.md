# OpenSearch + FastAPI Тестовое задание

Этот проект демонстрирует интеграцию OpenSearch с FastAPI для выполнения полнотекстового поиска с фильтрацией по типу контента.

## 🚀 Быстрый старт

1. Клонируйте репозиторий и перейдите в директорию проекта:
```bash
git clone https://github.com/IKLIF/opensearch-test.git
cd opensearch-test
```

2. Запустите систему с помощью Docker Compose:
```bash
docker-compose up --build
```

3. После запуска система будет доступна:
- OpenSearch: http://localhost:9200
- FastAPI API: http://localhost:8000

## 🧪 Тестирование

### Вариант 1: Использование curl

Выполните поисковые запросы:
```bash
# Поиск по слову "Python" в обучающих материалах
curl "http://localhost:8000/search?q=Python&content_type=tutorial"

# Поиск по слову "AI" в новостях
curl "http://localhost:8000/search?q=AI&content_type=news"

# Поиск по слову "programming" в статьях (не найдёт)
curl "http://localhost:8000/search?q=programming&content_type=article"
```

### Вариант 2: Запуск тестового скрипта

1. Установите зависимости для тестового скрипта:
```bash
pip install aiohttp
```

2. Запустите тестовый скрипт:
```bash
python test/t.py
```

## 📚 Использование API

### Поиск документов
```
GET /search
```

**Параметры:**
- `title`
- `content`
- `content_type`

**Пример ответа:**
```json
[
  {
    "title": "Python Tutorial",
    "snippet": "Learn Python programming from scratch..."
  }
]
```

## 🧩 Тестовые данные

При запуске автоматически добавляются документы:

```json
[
  {
     "title": "Python Tutorial",
     "content": "Learn Python programming from scratch...",
     "content_type": "tutorial"
  },
  {
     "title": "News about AI",
     "content": "Recent breakthroughs in artificial intelligence...",
     "content_type": "news"
  },
  {
     "title": "Linux Tutorial",
     "content": "Learn Linux from scratch...",
     "content_type": "tutorial"
  },
  {
     "title": "News about Linux",
     "content": "Recent breakthroughs in artificial Linux...",
     "content_type": "news"
  }
]
```

## 📂 Структура проекта

```
opensearch-test/
├── app/                   
│   ├── api.py             
│   ├── dependencies.py    
│   ├── main.py           
│   ├── opensearch_client.py 
│   ├── schemas.py         
│   └── requirements.txt   
├── test/                  
│   └── t.py               
├── docker-compose.yml    
├── Dockerfile            
└── README.md            
```
