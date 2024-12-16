# Git 项目同步工具

## 项目介绍

这是一个用 Python 编写的 Git 项目同步工具，支持通过配置文件配置多个 Git 仓库，并自动克隆或更新（`git pull`）到指定的本地存储目录。支持使用 HTTP 和 SSH 协议的 Git 仓库。

## 特性

- 支持配置多个 Git 仓库地址，并指定每个仓库的本地存储目录。
- 如果目标目录已存在对应的项目，自动执行 `git pull` 拉取最新代码。
- 如果目标目录不存在对应的项目，自动执行 `git clone` 克隆仓库。
- 通过 JSON 格式的配置文件进行项目配置，灵活可扩展。

## 安装

### 依赖

- Python 3.x
- Git

可以使用以下命令安装所需依赖（假设已经安装了 Python 和 Git）：

```bash
pip install subprocess
```

## 使用

### 源代码运行

```bash
python main.py
```

### 打包成exe

```bash
pyinstaller --onefile --name git_sync_tool main.py
```