# 🚀 Быстрый старт - Image Captioning с ClearML

## Что изменилось?

Проект теперь использует **ClearML** для управления датасетом вместо локальных файлов:

✅ **Датасет загружается из ClearML**  
✅ **Автоматическое кэширование** (не нужно загружать каждый раз)  
✅ **Версионирование датасета** (отслеживание изменений)  
✅ **Централизованное хранилище** (для командной работы)  

---

## 📋 Шаги для запуска

### 1️⃣ Установите зависимости

```powershell
pip install -r requirements.txt
```

### 2️⃣ Загрузите датасет в ClearML

Если это первый запуск и датасет еще не загружен:

```powershell
python upload_dataset_clearml.py --name image_description_dataset --paths annotations val2014
```

**Что происходит:**
- Скрипт ищет папки `annotations` и `val2014` в текущей директории
- Загружает их в ClearML проект `Image description generation`
- Создает датасет с именем `image_description_dataset`

⏱️ **Операция может занять несколько минут** (зависит от размера данных)

### 3️⃣ Запустите ноутбук

Откройте `Stage_1_Environment_Setup.ipynb` и выполните все ячейки по порядку:

```powershell
jupyter notebook Stage_1_Environment_Setup.ipynb
```

**Ноутбук автоматически:**
- ✅ Инициализирует ClearML
- ✅ Загружает датасет из ClearML
- ✅ Кэширует его локально
- ✅ Загружает данные в PyTorch DataLoader

**При первом запуске:** датасет будет загружен (~5-10 минут)  
**При повторных запусках:** используется локальный кэш (через ~30 сек)

---

## 🔧 Конфигурация ClearML

Убедитесь, что у вас есть файл конфигурации ClearML:

```
C:\Users\<YourUser>\.clearml.conf
```

Содержимое (пример):

```
[sdk]
api {
    host: "https://app.clear.ml"
}
web {
    host: "https://app.clear.ml"
}
[credentials]
api {
    key: "<YOUR_API_KEY>"
    secret: "<YOUR_API_SECRET>"
}
```

Получить ключи: https://app.clear.ml → User Settings → Access Key

---

## 📊 Структура проекта ClearML

```
Project: Image description generation
└── Dataset: image_description_dataset
    ├── annotations/
    │   └── captions_val2014.json
    └── val2014/
        ├── COCO_val2014_000000000042.jpg
        ├── COCO_val2014_000000000073.jpg
        └── ... (остальные изображения)
```

---

## ⚠️ Troubleshooting

### Проблема: "Dataset not found"

**Решение:**
1. Проверьте, что датасет загружен:
   ```powershell
   python upload_dataset_clearml.py --name image_description_dataset --paths annotations val2014
   ```
2. Проверьте ClearML конфигурацию и учетные данные
3. Убедитесь, что в ClearML Web UI видна папка задач

### Проблема: "Connection refused"

**Решение:**
1. Проверьте интернет соединение
2. Убедитесь, что хост в `clearml.conf` доступен
3. Перезагрузите Python Kernel в ноутбуке

### Проблема: "Долго загружается"

**Решение:**
- При первом запуске это нормально (зависит от размера датасета)
- Последующие запуски будут быстрее (используется кэш)

---

## 📁 Файлы проекта

- `Stage_1_Environment_Setup.ipynb` - Основной ноутбук (модифицирован для ClearML)
- `upload_dataset_clearml.py` - Скрипт загрузки датасета в ClearML
- `clearml_integration.py` - Пример интеграции (для проверки соединения)
- `requirements.txt` - Зависимости (обновлены)
- `CLEARML_SETUP.md` - Детальная инструкция по настройке
- `QUICKSTART_CLEARML.md` - Этот файл

---

## 🎯 Готово!

Теперь ваш проект работает с ClearML! 🎉

При следующих запусках просто откройте ноутбук и запустите ячейки. Все остальное произойдет автоматически.
