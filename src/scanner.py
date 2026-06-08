import os
import datetime


def scan_folder(folder_path):
    files = []

    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            full_path = os.path.join(root, filename)

            try:
                stat = os.stat(full_path)
                size = stat.st_size
                modified = datetime.datetime.fromtimestamp(stat.st_mtime)
                modified_str = modified.strftime("%Y-%m-%d %H:%M:%S")
            except OSError:
                size = -1
                modified_str = "недоступно"

            files.append({
                "path": full_path,
                "size": size,
                "modified": modified_str,
            })

    return files


def print_files(files):
    if not files:
        print("Файлы не найдены.")
        return

    print(f"\nНайдено файлов: {len(files)}\n")
    print(f"{'Путь':<60} {'Размер (байт)':>15} {'Изменён'}")
    print("-" * 90)

    for f in files:
        print(f"{f['path']:<60} {f['size']:>15} {f['modified']}")