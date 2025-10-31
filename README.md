# Lab 4 - Unit tests (unittest, Python, VS Code)

## Quick start
```bash
python3 -m venv .venv
source ./.venv/bin/activate  # macOS/Linux
pip install -U pip
python -m unittest discover -s tests -p "test_*.py" -v
```

## Structure
```
lab4_unittest_vscode/
├─ .vscode/
│  ├─ settings.json
├─ src/
│  ├─ rectangle.py
├─ tests/
│  ├─ test_rectangle.py
├─ README.md
├─ REPORT.md
├─ .gitignore
```

## VS Code
1) Install the Python extension (Microsoft).
2) Open the folder in VS Code -> Testing (beaker icon) -> Run All Tests.
   Or: Cmd+Shift+P -> "Python: Configure Tests" -> unittest -> tests
