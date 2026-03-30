import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

print("=" * 60)
print("=== ЭКСПОРТ NOTEBOOK В HTML ===")
print("=" * 60)

# Читаем ноутбук
with open('main.ipynb', 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# Выполняем все ячейки
print("🔄 Выполнение ячеек ноутбука...")
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(notebook, {'metadata': {'path': '.'}})
print("✅ Ноутбук выполнен")

# Экспортируем в HTML
print("🔄 Экспорт в HTML...")
html_exporter = HTMLExporter()
html_exporter.template_name = 'classic'
(body, resources) = html_exporter.from_notebook_node(notebook)

# Сохраняем
with open('main_full.html', 'w', encoding='utf-8') as f:
    f.write(body)

print("=" * 60)
print("✅ ГОТОВО: main_full.html")
print("=" * 60)