import os
import random
import time
from .data import read_data_file

# ANSI 颜色代码
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'



def generate_includes(file_list, max_count):
    include_flags = set()
    for file in file_list:
        dir_path = os.path.dirname(file)
        if dir_path:
            include_flags.add(dir_path)
    return " ".join(["-I" + dir for dir in random.sample(list(include_flags), min(max_count, len(include_flags)))])

def simulate_cc():
    compilers = ["gcc", "clang"]
    opt_flags = ["-O0", "-O1", "-O2", "-O3", "-Og", "-Os"]
    warn_flags = ["-Wall", "-Wextra", "-Wno-unused-variable", "-Wno-sign-compare", "-Wno-unknown-pragmas"]
    arch_flags = ["-march=x86-64", "-mtune=generic", "-pipe"]
    def_flags = ["-DDEBUG", "-DNDEBUG", "-D_REENTRANT", "-DMATH_LOOP"]

    c_files = read_data_file('cfiles.txt')
    packages = read_data_file('packages.txt')

    compiler = random.choice(compilers)
    opt_flag = random.choice(opt_flags)
    warn_flag = random.choice(warn_flags)
    arch_flag = random.choice(arch_flags)
    def_flag = random.choice(def_flags)

    includes = generate_includes(c_files, 20)

    linker_flags = " ".join(random.sample(packages, 5))
    output_file = random.choice(packages).strip()

    start_time = time.time()
    while time.time() - start_time < 100:  # 运行约 100 秒
        print(f"{compiler} {opt_flag} {warn_flag} {arch_flag} {includes} {def_flag} -o {output_file}.o {output_file}.c")

        msg_type = random.randint(0, 100)
        if msg_type < 2:
            print(RED + "error: critical failure detected" + RESET)
        elif msg_type < 10:
            print(BLUE + "fatal: unable to proceed" + RESET)
        elif msg_type < 20:
            print(YELLOW + "warning: potential issue found" + RESET)
        elif msg_type < 30:
            print(CYAN + "info: processing input files" + RESET)
        elif msg_type < 40:
            print(GREEN + "debug: analyzing data" + RESET)
        else:
            print("Compiling...")

        time.sleep(random.uniform(0.5, 2))  # 随机暂停时间

# simulate_cc()