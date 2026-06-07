import sys
import os


def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <путь к папке>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Ошибка: '{folder_path}' не является папкой или не существует.")
        sys.exit(1)

    print(f"Индексатор запущен. Папка: {folder_path}")


if __name__ == "__main__":
    main()
