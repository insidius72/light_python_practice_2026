import os
import datetime


def scan_folder(folder_path):
    files = []

    def recurse(current_path):
        try:
            entries = os.listdir(current_path)
        except OSError:
            return

        for entry in entries:
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                recurse(full_path)
            elif os.path.isfile(full_path):
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

    recurse(folder_path)
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