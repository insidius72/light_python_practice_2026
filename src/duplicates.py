import hashlib


def get_file_hash(file_path):
    hasher = hashlib.md5()

    try:
        f = open(file_path, "rb")
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hasher.update(chunk)
        f.close()
        return hasher.hexdigest()
    except OSError:
        return None


def find_duplicates(files):
    hash_map = {}

    for f in files:
        path = f["path"]
        file_hash = get_file_hash(path)

        if file_hash is None:
            continue

        if file_hash not in hash_map:
            hash_map[file_hash] = []

        hash_map[file_hash].append(path)

    duplicates = {}
    for h in hash_map:
        if len(hash_map[h]) > 1:
            duplicates[h] = hash_map[h]

    return duplicates


def print_duplicates(duplicates):
    if len(duplicates) == 0:
        print("\nДубликаты не найдены.")
        return

    print(f"\nНайдено групп дубликатов: {len(duplicates)}\n")

    i = 1
    for file_hash in duplicates:
        print(f"Группа {i} (хэш: {file_hash}):")
        for path in duplicates[file_hash]:
            print(f"  {path}")
        print()
        i = i + 1