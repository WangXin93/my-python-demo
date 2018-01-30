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
$ SElECT * FROM students WHERE id=1;
```
