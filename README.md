# Simple Crawler(Python3.5)
在学习Python的过程中尝试写的一个多线程爬虫工具，希望通过爬取贴吧的数据来分析贴吧用户的好友关系。
（在tools包中的模块都可以单独拿出来用，其中包括自定义的##线程池##，MySQL数据库通用模块等）

## 使用方法
>
* 将该库放到python的Lib目录下，直接调用beginCrawler函数即可（当然也可以直接修改代码定制自己的爬虫）
* 在python程序中import MyCrawler
* 配置SysConfig.ini, DbConnect.ini, XpathConfig.ini
* 调用beginCrawler,将SysConfig.ini文件的路径作为参数传入，然后运行程序就行了

## 配置文件
* SysConfig:
> [Config]
 ** url = 爬取数据的入口url（贴吧用户的个人首页）
 ** status = start or stop（暂时还没有写暂停爬虫程序的功能）

> [Path]
** xpath = 需要爬取的数据的xpath的配置文件路径，该文件中说明爬虫需要爬取页面中的哪些数据
** db = 例如“G:\\config\\DBConnect.ini”，该文件中配置数据库的主机位置、用户密码等信息
** logpath = 例如“G:”，表示日志文件存在G盘根目录

* DBConnect.ini（例如下）
> [DB]
** host = localhost
** user = root
** password = 123456
** db = crawler
** port = 3306

* XpathCOnfig.ini （例如下）
> [forums]
** name = //a[starts-with(@locate,"like")]/span/text()

> [user]
** userid = //div[@class="userinfo_title"]/span/text()
** sex = //*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[1]/@class
** age = //*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[2]/text()
** post = //*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[4]/text()

> [follow]
** followid = //*[@id="concern_wrap_concern"]/li/a/@href

> [fans]
** fansid = //*[@id="concern_wrap_fans"]/li/a/@href

## 依赖模块
* request
* lxms
* MySQLdb


### tools
所有的工具类模块都在tools下

### service
为实现针对贴吧数据的分析和抓取，通过tools的组合形成的一些新的模块

### database
包含数据模型和调用MySqlDbHelper封装的一个工具

### config
数据库、URL、页面信息的xpath等配置文件