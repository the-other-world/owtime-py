from setuptools import setup, find_packages

setup(
    name="owtime",
    version="5.2.2.1",
    author="KuoHu",
    author_email="y066ydg5@duck.com",
    description="Python 库 - OWTime 的时间处理工具",
    url="https://github.com/the-other-world/owtime-py",
    requires=["datetime", "pytz"],
    packages=find_packages(),
    license="MIT License",
    long_description=open("README.md", "r", encoding="UTF-8").read(),
    python_requires=">=3.6"
)
