# Интеграция ClearML — Быстрый старт

1) Регистрация / ключи
- Зарегистрируйтесь на https://app.clear.ml или используйте свой ClearML сервер.
- Получите `API Key` и `API Secret` в личном кабинете (User Settings → Access Key).

2) Конфигурация
- Проще всего положить файл `clearml.conf` в домашнюю папку пользователя (`C:\Users\<YourUser>\.clearml.conf`) или задать переменные окружения.
- Пример простого `clearml.conf` (настройте хосты и ключи):

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

3) Установка зависимостей

В PowerShell в корне проекта выполните:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4) Запуск агента (Windows)

Запустите `start_clearml_agent.ps1` (см. файл в проекте). Обычная команда агента:

```powershell
clearml-agent daemon --queue default
```

5) Загрузка датасета в ClearML

Выполните в PowerShell:

```powershell
python upload_dataset_clearml.py --name image_description_dataset --paths annotations val2014
```

Это загрузит папки `annotations` и `val2014` в ClearML датасет с именем `image_description_dataset` в проекте `Image description generation`.

6) Использование в ноутбуке

Ноутбук `Stage_1_Environment_Setup.ipynb` автоматически:
- ✅ Инициализирует ClearML Task (для отслеживания)
- ✅ Загружает датасет из ClearML (с кэшированием локально)
- ✅ Обрабатывает ошибки и fallback на локальные файлы

Просто запустите ноутбук - он все сделает автоматически!

7) Пример интеграции
- Используйте `clearml_integration.py` для проверки соединения и создания задачи.

8) Примечания
- Агент требует, чтобы в конфигурации были указаны корректные креденшиалы или переменные окружения.
- Если вы используете свой ClearML сервер — укажите адреса `api`, `web` и `files` в конфиге.
- Датасет кэшируется локально в ClearML кэш-директории для быстрого доступа при повторных запусках.
- Если датасет не найден в ClearML, ноутбук попытается найти данные локально.
