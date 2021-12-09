# sacred使用

[sacred文档](https://sacred.readthedocs.io/en/stable/)

## 安装

```
git clone https://github.com/IDSIA/sacred.git
cd sacred
python setup.py install
```

## 测试

```
from sacred import Experiment
from sacred.observers import MongoObserver

ex = Experiment("my_experiment")


@ex.config
def my_config():
    foo = 42
    bar = "baz"


"""
ex.capture用于确定一些函数使用ex.config配置的值
"""


@ex.capture
def some_function(a, foo, bar=10):
    print(a, foo, bar)


@ex.main
def my_main():
    some_function(1, 2, 3)  #  1  2   3
    some_function(1)  #  1  42  'baz'
    some_function(1, bar=12)  #  1  42  12
    # some_function()  #  TypeError: missing value for 'a'


ex.observers.append(MongoObserver())
if __name__ == "__main__":
    ex.run_commandline()
```

运行命令python test_config.py -m MY_DB 可以将输出写入MY_DB数据库中，omniboard可以对输出进行渲染

运行命令python test_config.py -F logs可以将输出写入到本地logs文件夹中

## mongo

### 安装

[参考地址](https://www.runoob.com/mongodb/mongodb-linux-install.html)

```
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1804-5.0.5.tgz
tar -zxvf mongodb-linux-x86_64-ubuntu1804-5.0.5.tgz
mv mongodb-linux-x86_64-ubuntu1804-5.0.5.tgz /usr/local/mongodb5
export PATH=/usr/local/mongodb5/bin:$PATH
```

## omniboard

[omniboard文档](https://vivekratnavel.github.io/omniboard/#/quick-start)

omniboard需要Node.js v12或者更高的版本

### 更新node.js版本

[参考地址](https://www.jianshu.com/p/2797b0322946)

```
sudo npm cache clean -f 
sudo npm install -g n
sudo n stable 
```

### 安装

```
sudo npm install -g omniboard
```

### 启动

```
sudo omniboard -m hostname:port:database
```

eg:sudo omniboard -m 127.0.0.1:27017:MY_DB

MY_DB为sacred记录输出的数据库

127.0.0.1:27017为omniboard数据库地址

### 网页查看

浏览器输入http://localhost:9000/

