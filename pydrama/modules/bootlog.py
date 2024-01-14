import random
import time
import os
from .data import read_file_lines
# ANSI escape codes for colors
GREEN = '\033[92m'  # ANSI escape code for green text
RED = "\033[31m"
YELLOW = "\033[33m"  # 新增黄色
BOLD = "\033[1m"
RESET = "\033[0m"
warnings = [
    "System resource low!",
    "Unusual network activity detected",
    "Possible security breach attempt",
    "High CPU usage detected",
    "Disk space reaching capacity",
    "System time out of sync",
    "Hardware failure suspected",
    "Application crash reported",
    "Access violation error",
    "Service response time delayed",
    "Memory allocation error"
]

# def load_bootlog(file_path):
#     with open(file_path, 'r') as file:
#         return [line.strip() for line in file if line.strip()]

def simulate_bootlog():
    logs = read_file_lines('bootlog.txt')
    num_lines = random.randint(50, 200)
    burst_mode = False
    count_burst_lines = 0
    burst_lines = random.randint(10, 50)

    for _ in range(num_lines):
        choice = random.choice(logs)
        line_sleep_length = random.uniform(0.01, 1.0)
        char_sleep_length = 0.005

        if burst_mode and count_burst_lines < burst_lines:
            line_sleep_length = 0.03
        elif count_burst_lines == burst_lines:
            burst_mode = False
            count_burst_lines = 0
        elif not burst_mode:
            burst_mode = random.random() < 0.05


        output = choice
        is_error = random.random() < 0.01
        is_warning = random.random() < 0.03  # 增加 5% 的概率出现警告
        is_info = random.random() < 0.05 
        
        if is_info:  # 2% 概率显示绿色信息
            info_message = GREEN + "INFO: " + choice + RESET
            print(info_message)
            time.sleep(0.1)
        
        elif is_warning:
            warning_message = YELLOW + "WARNING: " + random.choice(warnings) + RESET
            print(warning_message)
            time.sleep(0.5)  # 给警告信息略长的展示时间
            
        elif is_error:
            output = RED + "ERROR: " + choice + RESET
        elif random.random() < 0.1:
            words = choice.split()
            words[0] = BOLD + words[0] + RESET
            output = " ".join(words)

        print(output, end='', flush=True)
        time.sleep(char_sleep_length * len(output))
        print()
        time.sleep(line_sleep_length)

        if burst_mode:
            count_burst_lines += 1

# 示例用法
# logs = load_bootlog('data/bootlog.txt')
# simulate_bootlog(logs)
