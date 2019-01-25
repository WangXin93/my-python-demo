# My_python_demo

Here will store my python scripts written while daily work.

[basic](basic) Python语言与程序结构基础。

[copy_file.py](copy_file.py) is a demo to copy files between directories.

[multiplot.py](multiplot.py) is a demo to use threads to close figure window automatically.

[slider.py](slider.py) is a demo use slider to control parameter in plt.

[douban.ipynb](douban.ipynb) is a demo show how to crawl comments of movies online and generate a wordcloud.

[crop_and_save.py](crop_and_save.py) use os.walk recursively find images in a directory and crop two piece of 180x180 from them.

[college_ranking.ipynb](college_ranking.ipynb)展示了一个网页定向爬虫爬取“中国最好大学”排名

[geojson.py](geojson.py)是一个利用google map的api获取位置的完整地理信息，并用json进行提取的示例

[credit_card.py](credit_card.py) is a demo to show vertification algorithm of American Express credit card number.

[Luhn.py](Luhn.py) is recursion version demo to verify MasterCard credit card number.

[zero_init.py](zero_init.py)用一个两层神经网络说明了，多层神经网络初始化权重全部为零会使得隐藏层每个神经元的计算结果相同，导致隐藏层多个神经元的作用和一个神经元一样。可以发现w1的每一行为相同数字。

[chart.py](chart.py) can draw a simple bar plot using "ascii art", Very funny:)

[wiki_link.py](wiki_link.py)是一递归访问维基百科链接的demo。

[wiki_start.py](wiki_start.py)是一个从维基百科首页递归访问全部链接的demo。

[graph_and_BFS.py](graph_and_BFS.py)是一个图模型和广度优先搜索的实现。

[tree.py](tree.py)是一个自己写的利用树模型列出所有走完树中节点的路径的方法。

[crawl_external_links.py](crawl_external_links.py)是一个从一个站点开始递归获取所有外部链接的demo。

[merge_sort.py](merge_sort.py) is a demo of merge sort.

[Dijkstra.py](Dijkstra.py) 是一个狄克斯特拉算法的demo。

[skeleton](skeleton) 是一个自动创建python skeleton的工具，使用方法为`./mkskl.py dir1/proj1`。

[sqlite_student](sqlite_student)是一个使用sqlite3对数据库进行操作的demo。

[flask_lucky_number](flask_lucky_number)是使用flask在浏览器上向用户随机显示一个lucky number。

[flask_blog](flask_blog)是一个基于flask的个人博客服务器demo，参考《Learn More Python the Hard Way》。

[sixteen](sixteen) is a puzzle game called sixteen.

[scrape_allitebooks](scrape_allitebooks) 使用Scrapy爬去网站www.allitebooks.com的所有书籍的url。

[mypytorch](mypytorch) 使用PyTorch展示了Numpy风格反向传播和Pytorch风格反向传播的区别，展示了自动计算梯度降的用处。

[BFS](BFS) 是一个使用广度优先搜索自动求解迷宫的方法，同时展示了pytest单元测试的基本用法。

[genwave.py](genwave.py) 用python来制作电子音乐，这里将mario音乐写入一个wav文件。

[PSO.py](PSO.py)是一个粒子群优化算法（Particle Swarm Optimization）的示例文件。

[downloader.py](downloader.py)是一个通过URLs的多进程下载程序。

[ten_steps_to_keras.py](ten_steps_to_keras.py)是一个Keras的MNIST训练示例，同时展示了用TSNE显示中间层特征的分布。

[tkBasic.py](tkBasic.py)是一个tkinter的gui基础页面，包含canvas，entry，label，button这几个基本widget。

[youdao.py](youdao.py)是一个利用爬虫原理，使用requests，lxml，xpath写的字典翻译命令行工具。

[flask_RESTful_APIs/](flask_RESTful_APIs/)是一个使用flask写的RESTful api，使用了docker和docker-compose来自动部署。

[python_expert](python_expert/)记录[PyData 2017的讲座](https://www.youtube.com/watch?v=7lmCu8wz8ro)关于Python中Data model，decorator，metaclass，generator的使用的笔记。

[CGAN-fashion-mnist.py](CGAN-fashion-mnist.py)是一个CGAN的demo根据fashoin种类条件生成服饰图像。

[My Generating Names with a Character-Level RNN.ipynb](My%20Generating%20Names%20with%20a%20Character-Level%20RNN.ipynb)是一个使用rnn生成名字的demo，可以以名字的国家作为条件生成名字。

[adversarial_autoencoder](adversarial_autoencoder)是一个用pytorch写的autoencoder, adversarial autoencoder, conditional adversarial autoencoder的demo，参考了博客<https://towardsdatascience.com/a-wizards-guide-to-adversarial-autoencoders-part-1-autoencoder-d9a5f8795af4>。

[naive_bayes](naive_bayes)是一个naive bayes模型的demo，包括Gaussian NB，和Beta NB两个demo。

[grad_cam](grad_cam)是一个使用grad_cam（Gradient Class Activation Map）进行CNN可视化的demo。

[BPR](BPR)是一个贝叶斯个性化排序（Bayesian Personalized Ranking）的demo。

[tsne_visu.py](tsne_visu.py)是一个使用TSNE可视化高维特征分布的demo。

# Resources
* 趣学Python，假定读者是个孩子一样从头学习Python，跟随本书可以写出一个火柴人游戏以及掌握Python语法和基本编程思想
* Learn Python the Hard Way， 非常好同时学习计算机思维和Python语法的书，跟随本书可以从学习命令行操作到学习web下显示一个显示一个hello，world
* Mastering Python， 适合想学习中高级Python的读者，在Python3.5环境下深入教学了每个Python指令的用法甚至给出了基本的实现，跟随本书可以全面了解Python中的常见包，并规范开发流程
* [Python最佳实践指南！](http://pythonguidecn.readthedocs.io/zh/latest/index.html): Requests作者讲述Python的优秀时间和介绍Python资源
* Python网络数据采集：讲述爬虫技术，第一章爬虫基础的教学非常优秀，理论结合实践学习爬虫，第二章高级技术需跟随目前技术发展自行拓展学习
* Flask Web 开发：基于Python的Web应用开发实战
* [Python 3 Module of the Week](https://pymotw.com/3/)用一些列文章展示了如何使用Python3标准库的各个模块
* 图解算法， 用最直观的方式讲述基本算法和数据结构比如数组，链表，散列表，图结构，树结构，贪婪算法等，书中的实现方法均基于Python。
* [Python3 Standard Library by Example](https://pymotw.com/3/)是展示Python3各个标准库用法的系列博客。
* Udacity Git tutorial
* Udemy Machine Learning
