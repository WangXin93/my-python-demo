# Blog demo built by flask

Usage:
```
$ pipenv install
$ pipenv shell # 安装虚拟环境
$ export PYTHONPATH=.
$ ./bin/mdserve
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
...
$ exit # 退出虚拟环境
```
然后在浏览器输入网址比如`localhost:5000/test.html`即可显示blog。

不同route的功能：
```
'/' # Hello, World!
'/<doc>.html' # Transfer markdown file to html and show on browser
'/edit/<doc>.html' # Edit markdown file, save and show again
```
