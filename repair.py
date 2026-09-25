import os
import shutil

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]

REPLICATION_FACTOR = 3


def get_online_nodes():
    online_nodes = []

    for node in NODES:
        status_file = os.path.join(
            "node_status",
            node + ".status"
        )

        if os.path.exists(status_file):
            with open(status_file, "r") as file:
                status = file.read().strip()

            if status == "ONLINE":
                online_nodes.append(node)

    return online_nodes


def repair():

    online_nodes = get_online_nodes()

    print("Online nodes:", online_nodes)

    all_chunks = set()

    for node in NODES:

        node_folder = os.path.join(
            "storage",
            node
        )

        if os.path.exists(node_folder):

            for chunk in os.listdir(node_folder):
                all_chunks.add(chunk)

    if not all_chunks:
        print("No chunks found!")
        return

    for chunk in sorted(all_chunks):

        healthy_copies = []

        for node in online_nodes:

            chunk_path = os.path.join(
                "storage",
                node,
                chunk
            )

            if os.path.isfile(chunk_path):
                healthy_copies.append(node)

        print("\nChunk:", chunk)
        print("Healthy copies:", healthy_copies)

        if len(healthy_copies) >= REPLICATION_FACTOR:
            print("No repair needed.")
            continue

        if len(healthy_copies) == 0:
            print("No healthy copy available!")
            continue

        source_node = healthy_copies[0]

        source = os.path.join(
            "storage",
            source_node,
            chunk
        )

        for target_node in online_nodes:

            if len(healthy_copies) >= REPLICATION_FACTOR:
                break

            if target_node in healthy_copies:
                continue

            destination = os.path.join(
                "storage",
                target_node,
                chunk
            )

            shutil.copy2(source, destination)

            healthy_copies.append(target_node)

            print(
                "REPAIRED:",
                chunk,
                source_node,
                "->",
                target_node
            )

        print("Final copies:", healthy_copies)


repair()