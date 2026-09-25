import os
import shutil

REPLICATION_FACTOR = int(input("Enter replication factor (1-6): "))

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]


def replicate_chunks():

    chunk_folder = "chunks"

    chunks = sorted(os.listdir(chunk_folder))

    if not chunks:
        print("No chunks found!")
        return

    node_index = 0

    for chunk in chunks:

        print(f"\nReplicating {chunk}")

        source = os.path.join(chunk_folder, chunk)

        for i in range(REPLICATION_FACTOR):

            node = NODES[(node_index + i) % len(NODES)]

            destination_folder = os.path.join(
                "storage",
                node
            )

            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(
                destination_folder,
                chunk
            )

            shutil.copy2(source, destination)

            print(f"  -> Stored in {node}")

        node_index += REPLICATION_FACTOR


replicate_chunks()

print("\nReplication completed!")