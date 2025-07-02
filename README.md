# Git 项目同步工具

## 项目介绍

这是一个用 Python 编写的 Git 项目批量同步工具，支持通过配置文件配置多个 Git 仓库，并自动克隆或更新（`git pull`）到指定的本地存储目录。支持 HTTP/HTTPS/SSH 协议的 Git 仓库。

## 目录结构

```
├── LICENSE
├── main.py                # 主程序，读取配置并同步所有仓库
├── projects_config.json   # 仓库配置文件，定义要同步的所有项目
├── README.md              # 项目说明文档
```

## 特性

- 支持配置多个 Git 仓库地址，并指定每个仓库的本地存储目录。
- 已存在项目自动执行 `git pull` 拉取最新代码。
- 不存在项目自动执行 `git clone` 克隆仓库。
- 通过 JSON 格式的配置文件进行项目配置，灵活可扩展。
- 支持相对路径和绝对路径。

## 依赖环境

- Python 3.x（建议 3.6 及以上）
- Git（需配置到系统环境变量）

## 快速开始

1. 克隆本项目或下载源码：
   ```bash
   git clone https://github.com/zhutianlong1/git-sync-tool.git
   cd git-sync-tool
   ```
2. 配置项目仓库列表（见下方配置说明）。
3. 运行：
   ```bash
   python main.py
   ```

## 配置文件说明

项目通过 `projects_config.json` 文件进行配置，示例：

```json
{
  "projects": [
    {
      "repo_url": "https://github.com/example-org/example-repo1.git",
      "local_directory": "./git/example-repo1"
    },
    {
      "repo_url": "https://github.com/example-org/example-repo2.git",
      "local_directory": "./git/example-repo2"
    },
    {
      "repo_url": "https://github.com/example-org/example-repo3.git",
      "local_directory": "./git/example-repo3"
    },
    {
      "repo_url": "https://github.com/zhutianlong1/git-sync-tool.git",
      "local_directory": "./git/git-sync-tool"
    }
  ]
}
```

- `repo_url`：Git 仓库地址，支持 HTTP/HTTPS/SSH。
- `local_directory`：本地存储目录，支持相对路径和绝对路径。

## 使用说明

### 源代码运行

```bash
python main.py
```

### 打包成可执行文件（可选）

需先安装 pyinstaller：

```bash
pip install pyinstaller
pyinstaller --onefile --name git_sync_tool main.py
```

## 常见问题

- 请确保本地已安装 Git 并配置到环境变量。
- 若使用 SSH 协议，请确保已配置好 SSH key。
- 若遇到权限问题，请检查本地目录权限。

## 许可证

本项目基于 [MIT License](./LICENSE) 开源。