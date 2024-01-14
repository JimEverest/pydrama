from .ansible import simulate_ansible
from .bootlog import simulate_bootlog
from .docker_build import simulate_docker_build
from .weblog import simulate_weblog
from .ocr_train import simulate_ocr_training
from .download import simulate_download
from .pip_install import simulate_pip_install
from .cc import simulate_cc
# ... 其他模块导入


MODULES = {
    "ansible": simulate_ansible,
    "bootlog": simulate_bootlog,
    "docker_build": simulate_docker_build,
    "weblog": simulate_weblog,
    "ocr_train": simulate_ocr_training,
    "download": simulate_download,
    "pip_install": simulate_pip_install,
    "cc": simulate_cc
    # ... 其他模块
}