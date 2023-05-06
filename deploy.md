模擬 Linux 的環境：`docker run --rm -i -t -p 8000:8000 -v .:/srv -w /srv --name django_app python:3.11-slim bash`

安裝 MySQL client 需要的工具：`apt-get update && apt-get install python3-dev default-libmysqlclient-dev build-essential`

在 Linux 環境中安裝 Poetry (Python 需要事先安裝好)：`pip install poetry`

安裝所有套件：`poetry install`

進入虛擬環境：`poetry shell`

啟動伺服器：`gunicorn --bind 0.0.0.0:8000 core.wsgi`

安裝靜態文件工具：`poetry add whitenoise`
文件：https://whitenoise.readthedocs.io/en/latest/django.html