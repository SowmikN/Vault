import os
import subprocess

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]

online_nodes = []

print("VAULT COORDINATOR")
print("=================")

for node in NODES:
    status_file = os.path.join(
        "node_status",
        node + ".status"
    )

    if not os.path.exists(status_file):
        print(f"{node} -> UNKNOWN")
        continue

    with open(status_file, "r") as file:
        status = file.read().strip()

    if status == "ONLINE":
        print(f"{node} -> ONLINE")
        online_nodes.append(node)
    else:
        print(f"{node} -> OFFLINE")

print("\nHealthy nodes:")
print(online_nodes)
print(online_nodes)
if len(online_nodes) < 6:
    print("\nNode failure detected!")
    print("Starting replica repair...")
    subprocess.run(["py", "repair.py"])
else:
    print("\nAll nodes are healthy.")