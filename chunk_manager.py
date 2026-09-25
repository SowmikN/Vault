import os

CHUNK_SIZE = 1024  # 1 KB


def split_file(file_path):

    os.makedirs("chunks", exist_ok=True)

    with open(file_path, "rb") as file:

        index = 0

        while True:

            data = file.read(CHUNK_SIZE)

            if not data:
                break

            chunk_name = f"chunk_{index:04d}"
            chunk_path = os.path.join("chunks", chunk_name)

            with open(chunk_path, "wb") as chunk_file:
                chunk_file.write(data)

            print(f"Created: {chunk_path}")

            index += 1

    print(f"\nFile split into {index} chunks.")


file_path = input("Enter the file path: ")

if os.path.exists(file_path):
    split_file(file_path)
else:
    print("File not found!")