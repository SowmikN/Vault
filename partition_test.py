import os

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]

PARTITIONED_NODES = ["node4", "node5"]

print("VAULT NETWORK PARTITION TEST")
print("============================")

for node in NODES:
    if node in PARTITIONED_NODES:
        print(f"{node} -> PARTITIONED")
    else:
        print(f"{node} -> CONNECTED")

print("\nNetwork partition simulated successfully.")