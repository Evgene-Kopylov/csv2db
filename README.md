# csv2db
 скрипты для передачи даннх их файлов формата `.csv` в БД, для удобства дальнейшего использованияя


### Запуск локально

При необходимости, создать `.env`, поместить в него переменные окружения.

Получить файл БД, либо инициализировать
```console
alembic upgrade head
```
После этого можно запускать скрипты.


### Переменные окружения

`.env` - файл с переменными окружения.

Обязательно:
- ---

Не обязательно:
- `DB_NAME`  - имя SqLite базы, по-умолчанию `tg_bot.sqlite`
- `LOG_LEVEL` - уровень отображения логов в стандартной библиотеке `logging`, 
  - `30` по-умолчанию - `WARNING`, тихий. 
  - `20` - `INFO`, будет отображать дерево решений.


### Структура проекта.

- `main.py` - файл запуска скрипта. 
- `config.py` - переменные окружения, заданные и по-умолчанию
- `conflog.py` - настройки логирования
- `models.py` - используемые модели
- `schemas.py` - схемы данных
- `requirements.txt` - подключенные библиотеки.
- `target/` - Исходники данных, временные и генерируемые файлы.

