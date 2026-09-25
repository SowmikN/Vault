import os
import hashlib
import shutil
from collections import Counter

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]

CHUNK = "chunk_0000"


def checksum(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        sha256.update(file.read())

    return sha256.hexdigest()


def repair_corrupted_chunk():
    replicas = {}

    for node in NODES:
        path = os.path.join("storage", node, CHUNK)

        if os.path.isfile(path):
            replicas[node] = checksum(path)

    if not replicas:
        print("No replicas found!")
        return

    print("\nReplica checksums:")

    for node, value in replicas.items():
        print(node, "->", value)

    counts = Counter(replicas.values())
    healthy_checksum, count = counts.most_common(1)[0]

    if count < 2:
        print("\nNot enough matching replicas!")
        return

    healthy_node = next(
        node for node, value in replicas.items()
        if value == healthy_checksum
    )

    print("\nHealthy source:", healthy_node)

    for node, value in replicas.items():
        if value != healthy_checksum:
            source = os.path.join(
                "storage",
                healthy_node,
                CHUNK
            )

            destination = os.path.join(
                "storage",
                node,
                CHUNK
            )

            shutil.copy2(source, destination)

            print(
                "CORRUPTION REPAIRED:",
                node,
                "<-",
                healthy_node
            )

    print("\nRepair completed!")


repair_corrupted_chunk()