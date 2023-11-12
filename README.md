# OWTime - Python
Python 库 - OWTime 的时间处理工具

> __**注意：一切由任何fork版本的修改所以带来的bug均不由原开发者所负责，并且执行fork者应对fork出的仓库负责并且及时跟进原仓库的更新。原仓库的任何bug修复与性能优化包括新功能应由fork仓库维护者自行合并，对于fork仓库所添加的功能当与原仓库的某个提交产生冲突时应由fork仓库维护者自行处理**__

# 版本号

本项目版本号命名规则如下：

X.Y.Z.A

X = 基于的 OWCT 版本

Y = 基于的 OWCL 版本

Z = 基于的 OWTS 版本

A = 版本修改次数（例如 fix、feat 等）

# 安装

```shell
pip install git+https://github.com/the-other-world/owtime-py.git
```

或指定版本（例如 4.2.2.2）

```shell
pip install git+https://github.com/the-other-world/owtime-py.git@4.2.2.2
```

# 使用
## OWTime
```python
import owtime
import datetime

"""
这些对象均可以被 str() 转换为人类可读的格式

这些对象均拥有 weekday 属性，取值范围是 1 ~ 8，对应星期一到星期八
"""

print(owtime.owtimes.OWTime(3047, 1, 1, 1, 1, 1, 1))  # 创建一个异世界时间对象
print(owtime.owtimes.OWTime.now())  # 获取当前异世界时间对象
print(owtime.owtimes.OWTime.from_datetime(datetime.datetime.now()))  # 从已知的现实时间（任意时区）反推异世界时间
```
## OWTS
```python
import owtime
import datetime

"""
这些对象均可以被 str() 或 int() 转换为数字格式的时间戳

这些对象均拥有 to_int() 方法，等效于 int()
"""

# 秒级时间戳版本，格式为 3118087
print(owtime.owts.OWTS(owtime.owtimes.OWTime.now()))  # 从一个已知的异世界时间反推出异世界时间戳
print(owtime.owts.OWTS.now())  # 获取当前异世界时间戳
print(owtime.owts.OWTS.from_datetime(datetime.datetime.now()))  # 从已知的现实时间（任意时区）反推异世界时间戳
print(owtime.owts.OWTS.from_owmts_obj(owtime.owts.OWMTS(owtime.owtimes.OWTime.now())))  # 从一个已知的异世界毫秒时间戳转为秒级时间戳
print(owtime.owts.OWTS(owtime.owtimes.OWTime.now()).to_owmts_obj())  # 与上面这条等效，更优雅的写法

# 毫秒时间戳版本，格式为 3118087508
print(owtime.owts.OWMTS(owtime.owtimes.OWTime.now()))
print(owtime.owts.OWMTS.now())
print(owtime.owts.OWMTS.from_datetime(datetime.datetime.now()))
print(owtime.owts.OWMTS.from_owts_obj(owtime.owts.OWTS(owtime.owtimes.OWTime.now())))  # 从一个已知的异世界秒级时间戳转为毫秒时间戳
print(owtime.owts.OWMTS(owtime.owtimes.OWTime.now()).to_owts_obj())  # 与上面这条等效，更优雅的写法
```

## OWCT
```python
import owtime
import datetime

"""
这些对象均可以被 str() 转换为人类可读的格式
"""

print(owtime.owct.OWCT(1, 1, 1, 1))  # 创建一个异世界协调时间对象，参数从小时到毫秒，毫秒选填，不填为 0
print(owtime.owct.OWCT.now())  # 获取当前异世界协调时间对象
print(owtime.owct.OWCT.from_datetime(datetime.datetime.now()))  # # 从已知的现实时间（任意时区）反推异世界协调时间
```

## OWCL
```python
import owtime
import datetime

"""
这些对象均可以被 str() 转换为人类可读的格式

这些对象均拥有 weekday 属性，取值范围是 1 ~ 8，对应星期一到星期八
"""

print(owtime.owcl.OWCL(3047, 1, 1))  # 创建一个异世界日期对象
print(owtime.owcl.OWCL.now())  # 获取当前异世界日期对象
print(owtime.owcl.OWCL.from_datetime(datetime.datetime.now()))  # # 从已知的现实时间（任意时区）反推异世界日期
```

---

# 异世界协调时间（OWCT）

第五版（v5）

OWCTv4的起草，意味着OWST的弃用，该标准同时定义了异世界时间戳（OWTSv1）。

一天为32小时，一小时为128分钟，一分钟为128秒。

以异世界历3047年1月1日0时0分0秒为OWTS(v1)的开始（即0秒处）。

OWTSv2 规定时间戳必须精确到毫秒

# 异世界历法（OWCL）

第二版（v2）

以地球历公元2023年3月20日为异世界历3047年1月1日。

一年为8个月，一个月为4周，一周为8天。
