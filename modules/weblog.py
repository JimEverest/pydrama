import random
import time
from datetime import datetime
from .data import PACKAGES_LIST, EXTENSIONS_LIST, HTTP_CODES

# ANSI 颜色代码
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def generate_ip():
    """生成随机的IP地址"""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_datetime():
    """生成当前的日期时间字符串"""
    return datetime.now().strftime('%d/%b/%Y:%H:%M:%S %z')

def generate_path():
    """生成一个随机的URL路径"""
    package = random.choice(PACKAGES_LIST)
    extension = random.choice(EXTENSIONS_LIST)
    return f"/{package}/{extension}"

def simulate_weblog(duration_seconds=100):
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        ip = generate_ip()
        date = generate_datetime()
        method = random.choice(["GET", "POST", "PUT", "DELETE"])
        path = generate_path()
        status = random.choice(HTTP_CODES)
        size = random.randint(200, 5000)
        user_agent = f"UserAgent/{random.randint(1, 9)}.{random.randint(0, 9)}"
        
        # 1%的概率生成错误信息
        if random.random() < 0.01:
            status = random.choice([404, 500])
            log_line = f"{RED}{ip} - - [{date}] \"{method} {path} HTTP/1.1\" {status} {size} \"-\" \"{user_agent}\"{RESET}"
        else:
            log_line = f"{GREEN}{ip} - - [{date}] \"{method} {path} HTTP/1.1\" {status} {size} \"-\" \"{user_agent}\"{RESET}"

        print(log_line)
        time.sleep(random.uniform(0.3, 3.0))

# 运行模拟
# simulate_weblog(100)
