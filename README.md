# Лабораторная работа №4 — Unit-тесты в Python

## Быстрый старт
```bash
python3 -m venv .venv
source .venv/bin/activate  # для macOS/Linux
pip install -U pip
python -m unittest discover -s tests -p "test_*.py" -v
```

## Структура проекта
```
ISRPO-UNITTESTS/
├─ src/
│  ├─ rectangle.py
├─ tests/
│  ├─ test_rectangle.py
├─ README.md
```

## Работа с VS Code
1) Установите расширение Python от Microsoft.
2) Откройте папку проекта в VS Code.
3) Перейдите в раздел тестирования (значок с колбочкой) и нажмите «Запустить все тесты».
   Или используйте команду Cmd+Shift+P, выберите «Python: Configure Tests», затем unittest и укажите папку tests.

В данной лабораторной работе используется модуль `unittest` для написания и запуска тестов.
