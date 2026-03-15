import os

path = input("Введіть шлях до папки: ")

files = os.listdir(path)

print("Файли у папці:")
for f in files:
    print(f)

print("Кількість файлів:", len(files))

search = input("Введіть назву файлу для пошуку: ")

if search in files:
    print("Файл знайдено")
else:
print("File not found")