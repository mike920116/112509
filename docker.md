<!-- 2023/5/6 -->
建立資料從放空間：`docker volume create mysql_data`

啟動 MySQL 資料庫：`docker run -d -p 3306:3306 -v mysql_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=pwd --name mysql mysql:8`
- docker run 啟動容器（MySQL）
- `-d` 代表啟動後放置背景執行
- `-p` 意思綁定 port 號
- `-v` 代表綁定資料存放空間
- `-e` 設定環境變數
- `--name` 設定容器名稱