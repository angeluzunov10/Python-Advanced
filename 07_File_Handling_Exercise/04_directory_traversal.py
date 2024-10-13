import os


def safe_extensions(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]
            extensions[extension] = extensions.get(extension, []) + [file_name]

        elif os.path.isdir(file) and not first_level:
            safe_extensions(file, first_level=True)


directory = input()
extensions = {}
result = []

try:
    safe_extensions(directory)
except FileNotFoundError:
    print("Directory not found")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("files/report.txt", "w") as report_file:
    report_file.write("\n".join(result))
