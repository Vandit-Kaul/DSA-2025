import os
import shutil

folder_map = {
    "ARRAY": "ARRAY",
    "BST": "BST",
    "CONTAINER": "CONTAINER",
    "DP": "DP",
    "GRAPH": "GRAPH",
    "GREEDY": "GREEDY",
    "HASHMAP": "HASHMAP",
    "HASH": "HASHMAP",
    "PALINDROME": "RECURSION",
    "PARA": "RECURSION",
    "QUEUE": "QUEUE",
    "RECUR": "RECURSION",
    "REC": "RECURSION",
    "STACK": "STACK",
    "STRING": "STRING",
    "TREE": "TREE",
    "TWO": "STACK",
    "VALID": "STRING"
}

for filename in os.listdir():
    if not filename.endswith(".cpp"):
        continue
    prefix = filename.split("_")[0].upper()
    folder = folder_map.get(prefix)
    if folder:
        os.makedirs(folder, exist_ok=True)
        shutil.move(filename, os.path.join(folder, filename))
        print(f"Moved {filename} → {folder}/")
