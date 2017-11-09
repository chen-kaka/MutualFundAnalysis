#### 目标

- 获取基金成立基本数据 (相对静态)

- 获取基金净值数据 (动态)

- 获取黄金数据 (动态)

- 获取基金星级数据 (相对静态)

- 获取基金公司资历数据 (静态)

- 获取基金经理数据 (相对静态)

天天基金网:
- 获取基金排名数据(动态)

http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2016-02-17&ed=2017-02-17&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.490634018971817

- 为Django框架添加管理员密码校验

http://www.runoob.com/django/django-admin-manage-tool.html

python manage.py createsuperuser

username: kakachan
password: chen********

- 使用功能帮助:

http://www.oschina.net/translate/why-you-should-use-the-django-admin-9-tips

可以在展示的时候进行数据过滤

添加动作(action)

搜索

- 为基金经理添加过滤排序

- 为基金经理详情添加过滤排序

- 添加基金筛选公式


待办事项:

1、把各个拉取数据任务定时化,能够每天跑脚本计算出来。

2、前端展示页面优化,更清晰地展示推荐基金。

3、公众号推送下发推荐基金。

4、加入基金规模变化监控,基金近期收益因素的考虑等。

5、录入购买的基金以及购买价格,每日更新基金信息并推送或展示。

6、根据基金期望收益, 能承担的风险水平进行基金推荐。


基金涨幅情况：

https://fundmobapitest.eastmoney.com/FundMApi/FundPeriodIncrease.ashx?FCODE=001938&deviceid=Wap&plat=Wap&product=EFund&version=2.0.0


创建数据库：

CREATE DATABASE mutualfund DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;