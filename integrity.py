import hashlib
import os

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def check_chunks():
    chunk_folder = "chunks"
    chunks = sorted(os.listdir(chunk_folder))

    if not chunks:
        print("No chunks found!")
        return

    for chunk in chunks:
        chunk_path = os.path.join(chunk_folder, chunk)

        checksum = calculate_checksum(chunk_path)

        print(f"\n{chunk}")
        print(f"Checksum: {checksum}")


check_chunks()