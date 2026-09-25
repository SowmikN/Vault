import os

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]

STATUS_FOLDER = "node_status"

os.makedirs(STATUS_FOLDER, exist_ok=True)


def create_node_status():
    for node in NODES:
        status_file = os.path.join(
            STATUS_FOLDER,
            node + ".status"
        )

        if not os.path.exists(status_file):
            with open(status_file, "w") as file:
                file.write("ONLINE")


def check_nodes():
    print("\nChecking storage nodes...\n")

    for node in NODES:
        status_file = os.path.join(
            STATUS_FOLDER,
            node + ".status"
        )

        if not os.path.exists(status_file):
            print(f"{node} → OFFLINE")
            continue

        with open(status_file, "r") as file:
            status = file.read().strip()

        if status == "ONLINE":
            print(f"{node} → ONLINE")
        else:
            print(f"{node} → OFFLINE")


create_node_status()
check_nodes()