import sys
import os
from scanner import scan_folder, print_files
from duplicates import find_duplicates, print_duplicates
from backup import compare_folders, print_backup_report

def main():
    if len(sys.argv) < 2:
        print("Использование: python src/main.py <путь к папке> [путь к бэкапу]")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Ошибка: '{folder_path}' не является папкой или не существует.")
        sys.exit(1)

    print(f"Индексатор запущен. Папка: {folder_path}")

    files = scan_folder(folder_path)
    print_files(files)

    print("\n--- Поиск дубликатов ---")
    duplicates = find_duplicates(files)
    print_duplicates(duplicates)

    if len(sys.argv) >= 3:
        backup_path = sys.argv[2]
        if not os.path.isdir(backup_path):
            print(f"Ошибка: '{backup_path}' не является папкой или не существует.")
            sys.exit(1)
        print("\n--- Сравнение с резервной копией ---")
        report = compare_folders(folder_path, backup_path)
        print_backup_report(report)

if __name__ == "__main__":
    main()