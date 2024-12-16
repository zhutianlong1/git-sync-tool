import os
import subprocess
import json

# 函数：如果目录不存在则创建
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# 函数：执行 git clone 或 git pull
def sync_git_project(repo_url, target_directory):
    # 在目标目录下检查是否已经克隆了项目
    project_name = repo_url.split('/')[-1].replace('.git', '')  # 获取项目名
    project_path = os.path.join(target_directory, project_name)

    # 判断项目目录是否存在
    if os.path.exists(project_path):
        print(f"项目 {project_name} 已存在，正在拉取最新的代码...")
        # 如果项目目录存在，执行 git pull 拉取最新代码
        subprocess.run(['git', '-C', project_path, 'pull'])
    else:
        print(f"项目 {project_name} 不存在，正在克隆仓库: {repo_url} 到 {project_path}")
        # 如果项目目录不存在，执行 git clone 克隆项目
        subprocess.run(['git', 'clone', repo_url, project_path])

# 函数：处理项目同步
def sync_projects(config_file):
    # 读取配置文件
    with open(config_file, 'r') as file:
        config = json.load(file)

    for project in config['projects']:
        repo_url = project['repo_url']
        local_directory = project['local_directory']  # 从配置文件中获取本地存储目录
        
        # 创建必要的目录
        create_directory(local_directory)
        
        # 同步项目（克隆或拉取）
        sync_git_project(repo_url, local_directory)

# 主函数：运行脚本
if __name__ == "__main__":
    # 配置文件路径
    config_file = 'projects_config.json'
    sync_projects(config_file)
