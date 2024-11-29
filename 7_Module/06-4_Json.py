import json

file_path = "7_Module/dir.json"

dir = {
    "dir_name": "example_directory",
    "files": [
        {"file_name": "file1.txt", "size": 1024},
        {"file_name": "file2.txt", "size": 2048},
        {"file_name": "file3.txt", "size": 512},
    ],
}

with open(file_path, "w+", encoding="utf-8") as f:
    json.dump(dir, f)

    f.seek(0)
    data = f.read()

print(data)
