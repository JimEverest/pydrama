import os
import random
import time

# ANSI 颜色代码
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
RESET = '\033[0m'

# 读取文件内容
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# 模拟进度条
def progress_bar(color, process, duration, total=50):
    for i in range(total):
        print(f"\r{color}{process}: [{'=' * i}{' ' * (total - i)}] {int((i/total) * 100)}%", end="")
        time.sleep(duration / total)
    print(f"{RESET}")

# 模拟安装包过程
def simulate_package_installation(package, messages, installed_packages):
    # 随机选择下载地址
    url = f"https://pypi.org/simple/{package}/"

    # 模拟下载
    download_duration = random.uniform(5, 30)
    start_time = time.time()
    downloaded = 0

    while downloaded < 1:
        elapsed = time.time() - start_time
        remaining = download_duration - elapsed
        download_speed = random.uniform(1.5, 3.7)  # 速度在1.5MB/s到3.7MB/s之间变化
        eta = max(remaining, 0)  # 避免负数
        percent = int((elapsed / download_duration) * 100)
        print(f"\r{WHITE}Downloading {package} from {url} (Speed: {download_speed:.2f} MB/s, ETA: {eta:.2f}s) [{'=' * percent:<50s}] {percent}%", end="")
        downloaded = elapsed / download_duration
        time.sleep(1)

    print(f"{RESET}")

    # 模拟解压和安装
    extract_duration = random.uniform(3, 10)
    install_duration = random.uniform(2, 10)
    progress_bar(WHITE, "Extracting", extract_duration)
    progress_bar(WHITE, "Installing", install_duration)

    # 触发随机消息
    prob = random.randint(1, 100)
    if prob <= 1:  # 1% 几率出现错误
        print(f"{RED}ERROR: Failed to install {package}.{RESET}")
    elif prob <= 4:  # 3% 几率出现警告
        warning_msg = random.choice(messages).strip()
        print(f"{YELLOW}WARNING: {warning_msg}{RESET}")
    elif prob <= 9:  # 5% 几率安装缓存
        print(f"{MAGENTA}Using cached {package}.{RESET}")
    elif prob <= 14:  # 5% 几率版本不兼容，重新安装
        incompatible_package = random.choice(installed_packages)
        print(f"{YELLOW}Found incompatible version of {incompatible_package}. Reinstalling {package}.{RESET}")
        simulate_package_installation(package, messages, installed_packages)  # 重新安装
    else:
        print(f"{GREEN}Successfully installed {package}.{RESET}")
    installed_packages.append(package)

# 主函数模拟 pip install
def simulate_pip_install(duration=100):
    packages = read_file('data/packages.txt')
    messages = read_file('data/messages.txt')
    installed_packages = []
    start_time = time.time()

    while time.time() - start_time < duration:
        package = random.choice(packages).strip()
        simulate_package_installation(package, messages, installed_packages)

    # 显示所有已安装的包
    print(f"{CYAN}Installed packages:{RESET}")
    for pkg in installed_packages:
        print(f"- {pkg}")

# 示例运行
# simulate_pip_install(100)