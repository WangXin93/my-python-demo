# Python sqlite3 demo

- `python3 db.py` 创建名为mytest.db的数据库。
- `python3 insert.py` 对mytest.db数据库插入学生数据。
- `python3 query.py` 从mytest.db中查询数据。

# sqlite3 使用笔记
```
$ sqlite3 mytest.db # open database
$ .tables # list all tables
$ .help # list all possible commands in sqlite3

$ SELECT * FROM students; # query all items from table called students
$ SElECT * FROM students WHERE id=1; # 用相等性进行过滤
$ UPDATE students SET username="default" WHERE id=3; # 用UPDATE修改记录
$ DELETE FROM students WHERE id=1; # 用DELETE删除记录
$ SELECT name FROM students ORDER BY id; # 用ORDER BY排序
$ SELECT DISTINCT username FROM students; # 用DISTINCT获取唯一的项
$ SELECT * FROM students WHERE name LIKE "W%"; # 用LIKE或者NOT LIKE查找相似项目
```
