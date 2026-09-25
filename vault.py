import subprocess

while True:
    print("\n================================")
    print("        VAULT STORAGE SYSTEM")
    print("================================")
    print("1. Chunking")
    print("2. Replication")
    print("3. Integrity Check")
    print("4. Failure Detection")
    print("5. Automatic Repair")
    print("6. Metadata")
    print("7. Rebalancing")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        subprocess.run(["py", "chunk_manager.py"])

    elif choice == "2":
        subprocess.run(["py", "replication.py"])

    elif choice == "3":
        subprocess.run(["py", "integrity.py"])

    elif choice == "4":
        subprocess.run(["py", "failure_detector.py"])

    elif choice == "5":
        subprocess.run(["py", "repair.py"])

    elif choice == "6":
        subprocess.run(["py", "metadata.py"])

    elif choice == "7":
        subprocess.run(["py", "rebalancer.py"])

    elif choice == "8":
        print("\nVault shutting down...")
        break

    else:
        print("\nInvalid choice. Please try again.")