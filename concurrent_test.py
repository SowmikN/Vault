import threading
import time

def operation(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

threads = []

for i in range(3):
    thread = threading.Thread(
        target=operation,
        args=(f"Operation {i + 1}",)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nAll operations completed.")