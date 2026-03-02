import sys
import subprocess
import importlib


def ensure_package(pkg_name: str) -> bool:
    try:
        importlib.import_module(pkg_name)
        return True
    except ModuleNotFoundError:
        print(f"Пакет '{pkg_name}' не найден. Устанавливаю через pip...")
        cmd = [sys.executable, "-m", "pip", "install", pkg_name]
        res = subprocess.run(cmd)
        return res.returncode == 0


def main():
    if not ensure_package("clearml"):
        print("Не удалось установить 'clearml'. Установите вручную и повторите.")
        sys.exit(1)

    from clearml import Task

    task = Task.init(project_name="Image description generation", task_name="example_integration")
    print("ClearML Task created:", task.id)


if __name__ == "__main__":
    main()
