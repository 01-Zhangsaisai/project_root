# 📂 Project Root

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/01-Zhangsaisai/project_root/ci.yml?branch=main)](https://github.com/01-Zhangsaisai/project_root/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/01zhangsaisai/project_root.svg)](https://hub.docker.com/r/01-zhangsaisai/project_root)

**Мультiformатный парсер документов**. Поддерживаются: PDF, DOCX, HTML, DOC и DJVU.

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

- Обработка документов различных форматов
- Лёгкий CLI-интерфейс
- Гибкая архитектура для расширения форматов

---

## 💻 Совместимость с ОС

Проект протестирован на следующих платформах:

| Платформа         | Зависимости                              | Команды установки                          |
|:-----------------:|:----------------------------------------:|:------------------------------------------:|
| **Windows 10/11** | Python 3.8+, Ghostscript, LibreOffice CLI | См. ниже инструкции по установке           |
| **Ubuntu (Linux)**| python3, python3-pip, ghostscript, libreoffice | См. ниже команды                            |
| **macOS**         | Python 3.8+, Ghostscript, LibreOffice    | См. ниже команды                            |

Windows 10/11:
```bash
# 1. Установите Python с https://python.org
# 2. Установите Ghostscript и LibreOffice
```

Ubuntu (Linux):
```bash
sudo apt update
sudo apt install -y python3 python3-pip ghostscript libreoffice
```

**macOS:**
```bash
brew install python ghostscript libreoffice
```

> ⚠️ Убедитесь, что команды `gs` и `libreoffice` доступны в PATH.

-----------------:|:----------------------------------------:|:------------------------------------------:|
| **Windows 10/11** | Python 3.8+, Ghostscript, LibreOffice CLI | 1. Установите Python с https://python.org  
 2. Установите Ghostscript и LibreOffice.  |
| **Ubuntu (Linux)**| python3, python3-pip, ghostscript, libreoffice | ```bash  
sudo apt update  
sudo apt install -y python3 python3-pip ghostscript libreoffice  
``` |
| **macOS**         | Python 3.8+, Ghostscript, LibreOffice    | ```bash  
brew install python ghostscript libreoffice  
``` |

> Убедитесь, что команды `gs` и `libreoffice` доступны в PATH.

---

## 🚀 Установка и запуск

# 1. Клонируйте репозиторий
```bash
git clone https://github.com/01-Zhangsaisai/project_root.git
cd project_root
```

# 2. Установите зависимости
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

# 3. Запустите парсер
```bash
python main.py <путь_к_файлу> -t <тип_документа>
```

# Пример
```bash
python main.py ./examples/sample.pdf -t pdf
``` 

---

## 🐳 Docker

🔨 Сборка образа
```dockerfile
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libreoffice \
      djvulibre-bin \
      ghostscript && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
``` 

▶️ Запуск контейнера
```bash
docker build -t project_root:latest .
docker run --rm -v $(pwd)/data:/data project_root:latest /data/sample.docx -t docx
``` 

---

## 🤝 Участие в развитии

Мы рады вашему вкладу! Пожалуйста, следуйте инструкции:

1. Форкните репозиторий на GitHub.  
2. Создайте новую ветку: `git checkout -b feature/название-фичи`.  
3. Внесите изменения и напишите тесты при необходимости.  
4. Запушьте ветку на удалённый репозиторий: `git push origin feature/название-фичи`.  
5. Откройте Pull Request с описанием изменений.  

---

## 📄 Лицензия

Этот проект лицензирован по MIT. Смотрите [LICENSE](./LICENSE) для подробностей.
