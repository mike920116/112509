模擬 Linux 的環境：`docker run --rm -i -t -p 8000:8000 -v .:/srv -w /srv --name django_app python:3.11-slim bash`

安裝 MySQL client 需要的工具：`apt-get update && apt-get install python3-dev default-libmysqlclient-dev build-essential`

在 Linux 環境中安裝 Poetry (Python 需要事先安裝好)：`pip install poetry`

安裝所有套件：`poetry install`

進入虛擬環境：`poetry shell`

啟動伺服器：`gunicorn --bind 0.0.0.0:8000 -w 4 core.wsgi`
`-w 4`表示有四個worker可以幫忙執行 效率會更高

安裝靜態文件工具：`poetry add whitenoise`
文件：https://whitenoise.readthedocs.io/en/latest/django.html

背景啟動伺服器：`gunicorn --bind 0.0.0.0:8000 -w 4 --pid django.pid --capture-output --log-file django.log core.wsgi --daemon`

查看 pid：`cat django.pid`

停下背景中的伺服器：`kill -9 <pid>`（`<pid>` 替換成 django.pid 中的號碼）