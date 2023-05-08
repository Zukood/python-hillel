import os
import pickle

# Указываем директорию для обхода
directory = '/Users/admin/Documents/'

# Указываем граничное значение количества папок и файлов
limit = 1000

# Создаем словарь для хранения результатов
results = {
    'directories': 0,
    'files': 0,
    'largest_file': ('', 0),
    'smallest_file': ('', float('inf')),
    'longest_name': ('', 0),
    'shortest_name': ('', float('inf')),
    'processed_paths': set(),
}

# Пытаемся загрузить ранее сохраненное состояние из файла
state_file = 'state.pickle'
if os.path.exists(state_file):
    with open(state_file, 'rb') as f:
        try:
            saved_results = pickle.load(f)
            # Обновляем результаты только если мы загрузили хотя бы одно значение из файла
            results.update(saved_results)
        except:
            pass

# Рекурсивная функция для обхода всех файлов и папок
def traverse_directory(path, results, limit):
    if len(results['processed_paths']) >= limit:
        return
    if path in results['processed_paths']:
        return
    results['processed_paths'].add(path)
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                results['directories'] += 1
                traverse_directory(item_path, results, limit)
            else:
                results['files'] += 1
                size = os.path.getsize(item_path)
                if size > results['largest_file'][1]:
                    results['largest_file'] = (item_path, size)
                if size < results['smallest_file'][1]:
                    results['smallest_file'] = (item_path, size)
                length = len(item)
                if length > results['longest_name'][1]:
                    results['longest_name'] = (item_path, length)
                if length < results['shortest_name'][1]:
                    results['shortest_name'] = (item_path, length)
    except KeyboardInterrupt:
        # Если пользователь прервал выполнение скрипта, сохраняем результаты в файл и выходим
        with open(state_file, 'wb') as f:
            pickle.dump(results, f)
        return

# Запускаем обход директории
traverse_directory(directory, results, limit)

# Выводим результаты

# Сохраняем результаты в файл
# Записываем результаты в файл
# Записываем результаты в файл
with open('results.txt', 'w') as f:
    f.write(f"Number of directories: {results['directories']}\n")
    f.write(f"Number of files: {results['files']}\n")
    f.write(f"Largest file: {results['largest_file'][0]} ({results['largest_file'][1]} bytes)\n")
    f.write(f"Smallest file: {results['smallest_file'][0]} ({results['smallest_file'][1]} bytes)\n")
    f.write(f"Longest filename: {results['longest_name'][0]} ({results['longest_name'][1]} characters)\n")
    f.write(f"Shortest filename: {results['shortest_name'][0]} ({results['shortest_name'][1]} characters)\n")


