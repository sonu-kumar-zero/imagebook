# Command
```bash
watchfiles \
  --ignore-paths .git \
  --ignore-paths __pycache__ \
  --ignore-paths venv \
  "python main.py"

pyinstaller --windowed --name ImageBook --add-data "app/ui/assets:app/ui/assets" main.py

```
