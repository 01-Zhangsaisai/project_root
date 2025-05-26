# 📂 Project Root

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/01-Zhangsaisai/project_root/ci.yml?branch=main)](https://github.com/01-Zhangsaisai/project_root/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/01zhangsaisai/project_root)](https://hub.docker.com/r/01zhangsaisai/project_root)

**Мультиформатный парсер документов**. Поддерживаются: PDF, DOCX, HTML, DOC и DJVU.

---

## 📑 Содержание

- [📋 Особенности](#-особенности)
- [💻 Совместимость с ОС](#-совместимость-с-ос)
- [🚀 Установка и запуск](#-установка-и-запуск)
- [🐳 Docker](#-docker)
- [🤝 Участие в развитии](#-участие-в-развитии)
- [📄 Лицензия](#-лицензия)

---

## 📋 Особенности

- 🗂️ Обработка документов различных форматов
- ⌨️ Лёгкий CLI-интерфейс
- 🧩 Гибкая архитектура для расширения форматов

---

## 💻 Совместимость с ОС

Проект протестирован на следующих платформах:

| Платформа       | Зависимости                              | Команды установки                          |
|-----------------|------------------------------------------|--------------------------------------------|
| **Windows 10/11** | Python 3.8+, Ghostscript, LibreOffice CLI | 1. Установите Python с [python.org](https://python.org)<br>2. Установите Ghostscript и LibreOffice |
| **Ubuntu (Linux)** | python3, python3-pip, ghostscript, libreoffice | ```bash<br>sudo apt update<br>sudo apt install -y python3 python3-pip ghostscript libreoffice<br>``` |
| **macOS**       | Python 3.8+, Ghostscript, LibreOffice    | ```bash<br>brew install python ghostscript libreoffice<br>``` |

> ⚠️ Убедитесь, что команды `gs` и `libreoffice` доступны в PATH.

---

## 🚀 Установка и запуск

1. Клонируйте репозиторий и установите зависимости:
   ```bash
   git clone https://github.com/01-Zhangsaisai/project_root.git
   cd project_root
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
Запустите парсер:

```bash
python main.py <путь_к_файлу> -t <тип_документа>
```
Пример:

```bash
python main.py ./examples/sample.pdf -t pdf
```
🐳 Docker
Сборка и запуск через Docker:
1.Сборка образа:
```bash
docker build -t project_root:latest .
```
2.Запуск контейнера:
```bash
docker run --rm -v $(pwd)/data:/data project_root:latest /data/sample.docx -t docx
```
Dockerfile:
```dockerfile
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y ghostscript libreoffice && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
```
🤝 Участие в развитии
Форкните репозиторий

Создайте ветку: git checkout -b feature/new-feature

Зафиксируйте изменения: git commit -m 'Add new feature'

Отправьте изменения: git push origin feature/new-feature

Создайте Pull Request

📄 Лицензия
Этот проект лицензирован под лицензией MIT. Смотрите LICENSE для подробностей.
