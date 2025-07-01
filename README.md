# Git 项目同步工具

## 项目介绍

这是一个用 Python 编写的 Git 项目同步工具，支持通过配置文件配置多个 Git 仓库，并自动克隆或更新（`git pull`）到指定的本地存储目录。支持使用 HTTP 和 SSH 协议的 Git 仓库。

## 特性

- 支持配置多个 Git 仓库地址，并指定每个仓库的本地存储目录。
- 如果目标目录已存在对应的项目，自动执行 `git pull` 拉取最新代码。
- 如果目标目录不存在对应的项目，自动执行 `git clone` 克隆仓库。
- 通过 JSON 格式的配置文件进行项目配置，灵活可扩展。

## 快速开始

1. 克隆本项目或下载源码。
2. 安装依赖：
   - Python 3.x（建议 3.6 及以上）
   - Git
3. 配置项目仓库列表（见下方配置说明）。
4. 运行：

```bash
python main.py
```

## 配置文件说明

项目通过 `projects_config.json` 文件进行配置，示例：

```json
{
  "projects": [
    {
      "repo_url": "ssh://git@192.168.1.24:222/topbpm/asp.git",
      "local_directory": "./git/topbpm"
    },
    {
      "repo_url": "ssh://git@192.168.1.24:222/topbpm/examples/cloud-middleware-docker.git",
      "local_directory": "./git/topbpm/examples"
    }
  ]
}
```

- `repo_url`：Git 仓库地址，支持 HTTP/HTTPS/SSH。
- `local_directory`：本地存储目录，支持相对路径和绝对路径。

## 使用

### 源代码运行

```bash
python main.py
```

### 打包成exe

```bash
pyinstaller --onefile --name git_sync_tool main.py
```

## 常见问题

- **Q:** 运行时报错找不到 `git` 命令？
  **A:** 请确保已正确安装 Git，并将其加入系统环境变量。
- **Q:** 如何添加新仓库？
  **A:** 在 `projects_config.json` 的 `projects` 数组中添加新的仓库配置即可。

## 贡献

欢迎提交 issue 和 PR 参与改进！

## 许可证

MIT License