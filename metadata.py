import json
import os
import hashlib

METADATA_FILE = "metadata.json"

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]


def calculate_checksum(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def create_metadata():
    chunk_folder = "chunks"

    if not os.path.exists(chunk_folder):
        print("No chunks found!")
        return

    chunks = sorted(os.listdir(chunk_folder))

    metadata = {
        "file": "calvin.txt",
        "chunks": {}
    }

    for chunk in chunks:
        chunk_path = os.path.join(chunk_folder, chunk)

        replicas = []

        for node in NODES:
            node_path = os.path.join(
                "storage",
                node,
                chunk
            )

            if os.path.isfile(node_path):
                replicas.append(node)

        metadata["chunks"][chunk] = {
            "checksum": calculate_checksum(chunk_path),
            "replicas": replicas
        }

    with open(METADATA_FILE, "w") as file:
        json.dump(metadata, file, indent=4)

    print("Metadata updated successfully!")
    print("File:", METADATA_FILE)


create_metadata()