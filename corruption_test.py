import os

file_path = os.path.join(
    "storage",
    "node1",
    "chunk_0000"
)

if os.path.exists(file_path):
    with open(file_path, "ab") as file:
        file.write(b"CORRUPTED")

    print("chunk_0000 has been corrupted!")
else:
    print("chunk_0000 not found!")