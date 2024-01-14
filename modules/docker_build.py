import random
import time

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def gen_hex_string(length):
    return ''.join(random.choices('0123456789abcdef', k=length))

def simulate_docker_build():
    packages = read_file('data/docker_packages.txt')
    tags = read_file('data/docker_tags.txt')

    # 发送构建上下文到 Docker 守护进程
    target_size = random.uniform(100.0, 1000.0)
    current_size = 0.0

    while current_size <= target_size:
        print(f"\rSending build context to Docker daemon  {current_size:>4.2f}MB", end="")
        current_size += random.uniform(5.0, min(30.0, target_size - current_size))
        time.sleep(0.2)

    # 模拟构建步骤
    total_steps = random.randint(30, 100)
    for current_step in range(1, total_steps + 1):
        # 随机选择一个模块
        module = random.choice(packages).strip()
        tag = random.choice(tags).strip()

        # 输出当前步骤
        print(f"\rStep {current_step}/{total_steps} : RUN {module}:{tag}")
        time.sleep(random.uniform(0.3, 1.0))

        # 使用缓存或运行步骤
        if random.random() < 0.5:
            print(" ---> Using cache")
        else:
            step_hash = gen_hex_string(12)
            print(f" ---> Running in {step_hash}")

        final_hash = gen_hex_string(12)
        print(f" ---> {final_hash}")

    # 输出最终行
    hash = gen_hex_string(12)
    image = random.choice(packages).strip()
    image_tag = random.choice(tags).strip()

    print(f"Successfully built {hash}")
    print(f"Successfully tagged {image}:{image_tag}")

# simulate_docker_build()