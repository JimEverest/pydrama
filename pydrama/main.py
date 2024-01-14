import argparse
import time
from .modules import MODULES

# 解析命令行参数
def parse_args():
    parser = argparse.ArgumentParser(description="A busy-box for various simulations.")
    parser.add_argument("-l", "--list-modules", action="store_true", help="List available modules")
    parser.add_argument("-m", "--modules", nargs="*", help="Run only these modules")
    parser.add_argument("-s", "--speed-factor", type=float, default=1, help="Global speed factor [default: 100]")
    parser.add_argument("--exit-after-time", help="Exit after running for this long (format: 2h10min)")
    parser.add_argument("--exit-after-modules", type=int, help="Exit after running this many modules")
    return parser.parse_args()

# 运行模块
def run_modules(modules, speed_factor, exit_after_modules):
    module_count = 0
    for module_name in modules:
        if module_name in MODULES:
            # MODULES[module_name](speed_factor)  # 假设每个模块都接受速度因子作为参数
            MODULES[module_name]()  # 假设每个模块都接受速度因子作为参数

            module_count += 1
            if exit_after_modules and module_count >= exit_after_modules:
                break
        else:
            print(f"Module {module_name} not found.")

# 主函数
def pydrama():
    args = parse_args()

    # 列出模块
    if args.list_modules:
        print("Available modules:")
        for module in MODULES.keys():
            print(module)
        return

    # 确定要运行的模块
    modules_to_run = args.modules if args.modules else MODULES.keys()
    print("modules_to_run:", modules_to_run)

    # 处理退出时间
    end_time = None
    if args.exit_after_time:
        try:
            hours, minutes = map(int, args.exit_after_time.split("h"))
            end_time = time.time() + hours * 3600 + minutes * 60
        except ValueError:
            print("Invalid time format for --exit-after-time. Use format like '2h10min'.")
            return
    print("end_time:", end_time)

    # 运行模块
    while True:
        run_modules(modules_to_run, args.speed_factor, args.exit_after_modules)
        if args.exit_after_modules or (end_time and time.time() > end_time):
            break

if __name__ == "__main__":
    pydrama()
