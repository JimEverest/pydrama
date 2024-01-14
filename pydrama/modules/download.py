import random
import time

# ANSI 颜色代码
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

# 错误和警告信息
warnings = ["Connection timed out", "Checksum mismatch", "Temporary network failure", "Package not found"]
errors = ["Download failed", "Invalid file format", "Corrupted download", "Permission denied"]

# 模拟下载进度条
def simulate_download_progress(filename, filesize, download_speed):
    downloaded = 0
    while downloaded < filesize:
        downloaded += download_speed
        percent = min(100, downloaded / filesize * 100)
        bar = f"[{'=' * int(percent // 2):50s}]"
        print(f"\r{GREEN}Downloading{RESET} {WHITE}{filename} {bar} {percent:.2f}%{RESET}", end="")
        time.sleep(0.5)

        # 模拟warning和retry
        if random.randint(1, 100) <= 5:  # 5% 几率触发warning或retry
            print(f"\n{YELLOW}{random.choice(warnings)}{RESET}")
            if random.randint(1, 2) == 1:
                print(f"{YELLOW}Retrying...{RESET}")
                time.sleep(1)

        # 模拟错误
        if random.randint(1, 100) <= 2:  # 2% 几率触发错误
            print(f"\n{RED}{random.choice(errors)}{RESET}")
            return False

    return True

# 模拟解压进度
def simulate_extraction(filename):
    print(f"{CYAN}Extracting {filename}...{RESET}")
    time.sleep(random.uniform(1, 3))

# 模拟下载
def simulate_download(duration=100):
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < duration:
        # 随机选择文件名和扩展名
        filename = "file_" + str(random.randint(1, 1000))
        extension = ".zip"
        full_filename = filename + extension

        # 随机确定文件大小和下载速度
        filesize = random.randint(10000000, 100000000)  # 10MB to 100MB
        download_speed = random.randint(1000000, 5000000)  # 1MB to 5MB per second

        # 模拟下载进度
        download_successful = simulate_download_progress(full_filename, filesize, download_speed)
        if download_successful:
            simulate_extraction(full_filename)
        else:
            print(f"{RED}Skipping extraction due to download error.{RESET}")
            time.sleep(1)

        elapsed_time = time.time() - start_time

# simulate_download()