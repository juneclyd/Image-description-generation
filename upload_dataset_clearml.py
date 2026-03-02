import sys
import subprocess
import importlib
import os
from pathlib import Path

PROJECT_NAME = "Image description generation"
DEFAULT_FOLDERS = ["annotations", "val2014"]


def ensure_package(pkg_name: str) -> bool:
    try:
        importlib.import_module(pkg_name)
        return True
    except ModuleNotFoundError:
        print(f"Пакет '{pkg_name}' не найден. Устанавливаю через pip...")
        cmd = [sys.executable, "-m", "pip", "install", pkg_name]
        res = subprocess.run(cmd)
        return res.returncode == 0


def create_and_upload(dataset_name: str, paths: list[str]):
    from clearml import Dataset, Task

    Task.init(project_name=PROJECT_NAME, task_name=f"upload_dataset:{dataset_name}")

    ds = Dataset.create(dataset_name=dataset_name, dataset_project=PROJECT_NAME)

    added = False
    for p in paths:
        p = Path(p)
        if p.exists():
            print(f"Добавляю: {p}")
            ds.add_files(str(p))
            added = True
        else:
            print(f"Пропускаю отсутствующую папку: {p}")

    if not added:
        print("Не найдено ни одной папки для загрузки. Отменяю.")
        return None

    print("Начинаю загрузку датасета (upload)... это может занять время")
    ds.upload()
    print("Файлы загружены. Финализирую датасет...")
    ds.finalize()

    print("Датасет создан:")
    print("  id:", ds.id)
    try:
        print("  remote url:", ds.get_remote_url())
    except Exception:
        pass
    return ds


if __name__ == "__main__":
    if not ensure_package("clearml"):
        print("Не удалось установить 'clearml'. Установите вручную и повторите.")
        sys.exit(1)

    import argparse

    parser = argparse.ArgumentParser(description="Upload local folders to ClearML Dataset")
    parser.add_argument("--name", help="Dataset name in ClearML", default="image_description_dataset")
    parser.add_argument("--paths", nargs="*", help="Local folders to upload", default=DEFAULT_FOLDERS)
    args = parser.parse_args()

    cwd = Path.cwd()
    # resolve relative paths from project root
    paths = [cwd / p for p in args.paths]

    ds = create_and_upload(args.name, [str(p) for p in paths])
    if ds is None:
        sys.exit(2)
    print("Готово.")
