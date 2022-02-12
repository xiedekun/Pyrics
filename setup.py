from os import path as os_path
from setuptools import setup

import Pyrics.Pyrics as Pyrics 

this_directory = os_path.abspath(os_path.dirname(__file__))

# reand content
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# acquire dependencies
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name='Pyrics',  # 包名
    python_requires='>=3.6.0', # python环境
    version=Pyrics.__version__, # 包的版本
    description="A tool to scrape lyrics, get rhymes, generate relevant lyrics with rhymes.",  # 包简介，显示在PyPI上
    long_description=read_file('README.md'), # 读取的Readme文档内容
    long_description_content_type="text/markdown",  # 指定包文档格式为markdown
    author="Dekun Xie (DK)", # 作者相关信息
    author_email='xiedekun@outlook.com',
    url='https://github.com/xiedekun/Pyrics',
    # 指定包信息，还可以用find_packages()函数
    packages=[
        'Pyrics',
    ],
    install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    include_package_data=True,
    license="MIT",
    keywords=['scrape', 'lyrics', 'rhymes', 'generation'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)