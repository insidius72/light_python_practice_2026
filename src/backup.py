import os
from scanner import scan_folder

def compare_folders(source_path, backup_path):
    source_list = scan_folder(source_path)
    backup_list = scan_folder(backup_path)

    source_files = {}
    for f in source_list:
        relative = os.path.relpath(f["path"], source_path)
        source_files[relative] = f

    backup_files = {}
    for f in backup_list:
        relative = os.path.relpath(f["path"], backup_path)
        backup_files[relative] = f

    missing = []
    changed = []
    extra = []

    for rel_path in source_files:
        if rel_path not in backup_files:
            missing.append(rel_path)
        else:
            if source_files[rel_path]["size"] != backup_files[rel_path]["size"]:
                changed.append(rel_path)

    for rel_path in backup_files:
        if rel_path not in source_files:
            extra.append(rel_path)

    return {
        "missing": missing,
        "changed": changed,
        "extra": extra,
    }

def print_backup_report(report):
    print()
    if len(report["missing"]) == 0:
        print("Отсутствующих файлов нет.")
    else:
        print(f"Отсутствуют в бэкапе ({len(report['missing'])}):")
        for f in report["missing"]:
            print(f"  - {f}")
    print()

    if len(report["changed"]) == 0:
        print("Изменённых файлов нет.")
    else:
        print(f"Изменённые файлы ({len(report['changed'])}):")
        for f in report["changed"]:
            print(f"  ~ {f}")
    print()

    if len(report["extra"]) == 0:
        print("Лишних файлов в бэкапе нет.")
    else:
        print(f"Лишние в бэкапе ({len(report['extra'])}):")
        for f in report["extra"]:
            print(f"  + {f}")