import random
import time

# ANSI 颜色代码
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def generate_ipv4_address():
    return '.'.join([str(random.randint(0, 255)) for _ in range(4)])

def generate_ipv6_address():
    return ':'.join([''.join([random.choice('0123456789abcdef') for _ in range(4)]) for _ in range(8)])

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def do_for_all_hosts(hosts, is_gather):
    for host in hosts:
        host_outcome = random.randint(1, 100)  # 使用1到100的范围来增加多样性

        # 为 "gather" 阶段设置不同的逻辑
        if is_gather:
            if host_outcome <= 60:  # 60% 的几率输出白色 "ok"
                text = f"ok: [{host}]"
            elif host_outcome <= 70:  # 10% 的几率输出 "skipping"
                text = CYAN + f"skipping: [{host}]" + RESET
            elif host_outcome <= 80:  # 10% 的几率输出 "failed"
                text = RED + f"failed: [{host}]" + RESET
            elif host_outcome <= 90:  # 10% 的几率输出 "changed"
                text = YELLOW + f"changed: [{host}]" + RESET
            else:  # 剩下的10% 输出绿色 "ok"
                text = GREEN + f"ok: [{host}]" + RESET
        else:
            # 对于非 "gather" 阶段
            if host_outcome <= 60:  # 60% 的几率输出白色 "ok"
                text = f"ok: [{host}]"
            elif host_outcome <= 70:  # 10% 的几率输出 "changed"
                text = YELLOW + f"changed: [{host}]" + RESET
            elif host_outcome <= 80:  # 10% 的几率输出 "failed"
                text = RED + f"failed: [{host}]" + RESET
            elif host_outcome <= 90:  # 10% 的几率输出 "skipping"
                text = CYAN + f"skipping: [{host}]" + RESET
            else:  # 剩下的10% 输出绿色 "ok"
                text = GREEN + f"ok: [{host}]" + RESET

        print(text)
        time.sleep(random.uniform(0.1, 0.5))

def simulate_ansible():
    roles = read_file('data/ansible_roles.txt')
    tasks = read_file('data/ansible_tasks.txt')
    ipv4_hosts = [generate_ipv4_address() for _ in range(5)]
    ipv6_hosts = [generate_ipv6_address() for _ in range(5)]
    hosts = ipv4_hosts + ipv6_hosts

    print("PLAY [setup server]")
    do_for_all_hosts(hosts, is_gather=True)

    num_roles = random.randint(3, 7)
    for _ in range(num_roles):
        role = random.choice(roles).strip()
        print(f"TASK [setup {role}]")
        num_tasks = random.randint(1, 5)
        for _ in range(num_tasks):
            task = random.choice(tasks).strip()
            print(f"RUNNING TASK: {task}")
            do_for_all_hosts(hosts, is_gather=False)

# simulate_ansible()