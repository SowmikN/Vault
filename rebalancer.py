import os

NODES = [
    "node1",
    "node2",
    "node3",
    "node4",
    "node5",
    "node6"
]

print("VAULT REBALANCER")
print("================")

for node in NODES:
    folder = os.path.join("storage", node)

    if os.path.exists(folder):
        chunks = os.listdir(folder)
        print(f"{node} -> {len(chunks)} objects")
    else:
        print(f"{node} -> unavailable")

print("\nRebalancing check completed.")