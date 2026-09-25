import os

CHUNK_FOLDER = "chunks"
OUTPUT_FILE = "reconstructed_file"

def reconstruct_file():
    chunks = sorted(os.listdir(CHUNK_FOLDER))

    if not chunks:
        print("No chunks found!")
        return

    with open(OUTPUT_FILE, "wb") as output:
        for chunk in chunks:
            chunk_path = os.path.join(CHUNK_FOLDER, chunk)

            with open(chunk_path, "rb") as chunk_file:
                data = chunk_file.read()

            output.write(data)
            print(f"Added {chunk}")

    print("\nFile reconstructed successfully!")
    print(f"Output file: {OUTPUT_FILE}")

reconstruct_file()