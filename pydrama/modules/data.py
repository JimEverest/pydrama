# data.py
import os
# 文件扩展名列表
EXTENSIONS_LIST = [
    ".gif", ".mkv", ".webm", ".mp4", ".html", ".php", ".md", ".png", ".jpg", ".opus", ".ogg", ".mp3", ".flac",
    ".iso", ".zip", ".rar", ".tar.gz", ".tar.bz2", ".tar.xz", ".tar.zstd", ".deb", ".rpm", ".exe",
]

# 压缩格式列表
COMPRESSION_FORMATS_LIST = [
    "gzip", "bzip2", "lzma", "xz", "lzop", "lz4", "zstd"
]

def read_data_file(file_name):
    # Get the directory of the current script
    module_dir = os.path.dirname(__file__)
    # Go up one directory level to the 'pydrama' directory
    pydrama_dir = os.path.dirname(module_dir)
    # Construct the full path to the file in the 'data' directory
    file_path = os.path.join(pydrama_dir, 'data', file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# 将文件内容作为列表加载到内存中
def load_data(file_path):
    return [line.strip() for line in read_data_file(file_path)]

# 定义数据文件路径
BOOTLOG_FILE = 'bootlog.txt'
CFILES_FILE = 'cfiles.txt'
PACKAGES_FILE = 'packages.txt'
COMPOSERS_FILE = 'composer.txt'
SIMCITY_FILE = 'simcity.txt'
BOOT_HOOKS_FILE = 'boot_hooks.txt'
OS_RELEASES_FILE = 'os_releases.txt'
DOCKER_PACKAGES_FILE = 'docker_packages.txt'
DOCKER_TAGS_FILE = 'docker_tags.txt'
ANSIBLE_ROLES_FILE = 'ansible_roles.txt'
ANSIBLE_TASKS_FILE = 'ansible_tasks.txt'
RKHUNTER_CHECKS_FILE = 'rkhunter_checks.txt'
RKHUNTER_ROOTKITS_FILE = 'rkhunter_rootkits.txt'
RKHUNTER_TASKS_FILE = 'rkhunter_tasks.txt'
# JULIA_PACKAGES_FILE = 'julia.csv'

# 加载数据到内存
BOOTLOG_LIST = load_data(BOOTLOG_FILE)
CFILES_LIST = load_data(CFILES_FILE)
PACKAGES_LIST = load_data(PACKAGES_FILE)
COMPOSERS_LIST = load_data(COMPOSERS_FILE)
SIMCITY_LIST = load_data(SIMCITY_FILE)
BOOT_HOOKS_LIST = load_data(BOOT_HOOKS_FILE)
OS_RELEASES_LIST = load_data(OS_RELEASES_FILE)
DOCKER_PACKAGES_LIST = load_data(DOCKER_PACKAGES_FILE)
DOCKER_TAGS_LIST = load_data(DOCKER_TAGS_FILE)
ANSIBLE_ROLES_LIST = load_data(ANSIBLE_ROLES_FILE)
ANSIBLE_TASKS_LIST = load_data(ANSIBLE_TASKS_FILE)
RKHUNTER_CHECKS_LIST = load_data(RKHUNTER_CHECKS_FILE)
RKHUNTER_ROOTKITS_LIST = load_data(RKHUNTER_ROOTKITS_FILE)
RKHUNTER_TASKS_LIST = load_data(RKHUNTER_TASKS_FILE)
# JULIA_PACKAGES_LIST = load_data(JULIA_PACKAGES_FILE) # 需要特殊处理 CSV 文件

# 特殊处理 Julia 包 CSV 文件
def load_julia_packages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip().split(',') for line in file]

# JULIA_PACKAGES_LIST = load_julia_packages(JULIA_PACKAGES_FILE)



# data.py

# 示例：从文件中读取数据并创建列表
def read_file_lines(file_path):
    # Get the directory of the current script
    module_dir = os.path.dirname(__file__)
    # Go up one directory level to the 'pydrama' directory
    pydrama_dir = os.path.dirname(module_dir)
    # Construct the full path to the file in the 'data' directory
    file_path = os.path.join(pydrama_dir, 'data', file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# 定义需要的数据列表
PACKAGES_LIST = read_file_lines('packages.txt')
EXTENSIONS_LIST = [
    "gif", "mkv", "webm", "mp4", "html", "php", "md", "png", "jpg",
    "opus", "ogg", "mp3", "flac", "iso", "zip", "rar", "tar.gz",
    "tar.bz2", "tar.xz", "tar.zstd", "deb", "rpm", "exe",
]
HTTP_CODES = [200, 201, 400, 401, 403, 404, 500, 502, 503]