# VAULT — Distributed Storage System

## Problem Statement

VAULT is a prototype distributed storage system designed to demonstrate how a file can be split into chunks, replicated across multiple storage nodes, checked for integrity, and repaired after node failures or data corruption.

## Objective

The project demonstrates these distributed-storage concepts:

- File chunking
- Replication across multiple nodes
- SHA-256 integrity verification
- Node health/failure detection
- Automatic replica repair
- Corruption detection and repair using replica agreement
- Metadata generation
- Network-partition simulation
- Rebalancing checks
- Concurrent-operation testing

## Architecture

```text
                    +----------------+
                    |      VAULT     |
                    |    Main Menu   |
                    +-------+--------+
                            |
       +--------------------+--------------------+
       |         |          |         |          |
    Chunking  Replication Integrity Failure   Metadata
       |         |          |       Detection
       |         |          |          |
       +---------+----------+----------+
                            |
                    +-------v-------+
                    | Storage Nodes |
                    +---------------+
                    | node1 ... node6|
                    +---------------+
                            |
                    Failure / Corruption
                            |
                    +-------v-------+
                    |    Repair     |
                    +---------------+
```

The project models six storage nodes (`node1` through `node6`). Replication copies chunks into node-specific folders under `storage/`.

## How VAULT Works

### 1. Chunking

`chunk_manager.py` splits an input file into 1 KB chunks and stores them under `chunks/`.

### 2. Replication

`replication.py` asks for a replication factor from 1–6 and copies each chunk to multiple nodes under `storage/`.

### 3. Integrity Verification

`integrity.py` calculates SHA-256 checksums for the generated chunks.

### 4. Failure Detection

`failure_detector.py` creates/reads node status files in `node_status/` and reports nodes as ONLINE or OFFLINE.

### 5. Failure Repair

`repair.py` checks how many healthy online copies of each chunk exist. When the number is below the configured replication factor, it copies an available healthy replica to another online node.

### 6. Corruption Detection and Repair

`corruption_test.py` intentionally modifies `chunk_0000` on `node1` for demonstration.

`corruption_repair.py` calculates checksums of the replicas, finds the checksum shared by the majority of replicas, and replaces a mismatching replica with the healthy copy.

### 7. Metadata

`metadata.py` creates `metadata.json` containing chunk checksums and the nodes where each chunk is stored.

### 8. Network Partition Simulation

`partition_test.py` demonstrates a simulated partition by marking selected nodes as PARTITIONED in its output.

### 9. Rebalancing Check

`rebalancer.py` reports the number of stored objects on each node.

### 10. Concurrent Operations

`concurrent_test.py` demonstrates three operations running concurrently using Python threads.

## Technologies Used

- Python 3
- Python standard library
- `os`
- `shutil`
- `hashlib`
- `json`
- `subprocess`
- `threading`
- `time`
- `collections.Counter`

No external Python packages are required by the uploaded scripts.

## Project Structure

```text
VAULT/
├── vault.py
├── coordinator.py
├── chunk_manager.py
├── replication.py
├── download.py
├── integrity.py
├── failure_detector.py
├── repair.py
├── corruption_test.py
├── corruption_repair.py
├── metadata.py
├── partition_test.py
├── rebalancer.py
├── concurrent_test.py
├── README.md
├── storage/
├── chunks/
└── node_status/
```

## How to Run

Open a terminal in the `VAULT` folder and run:

```bash
python vault.py
```

On systems where the Python launcher is configured, this can also be:

```bash
py vault.py
```

The main menu provides:

1. Chunking
2. Replication
3. Integrity Check
4. Failure Detection
5. Automatic Repair
6. Metadata
7. Rebalancing
8. Exit

## Suggested Hackathon Demo

Use this sequence:

```text
Input File
   ↓
Chunking
   ↓
Replication
   ↓
Integrity Verification
   ↓
Simulate Node Failure
   ↓
Failure Detection
   ↓
Automatic Replica Repair
   ↓
Simulate Chunk Corruption
   ↓
Checksum Comparison
   ↓
Corruption Repair
   ↓
Data Available Again
```

For the demo, capture screenshots of the main menu, chunk creation, replication, integrity checks, failure detection, repair output, corruption repair, and metadata.

## Current Scope

This is a prototype/demo implementation. Node status and failures are simulated through files, and storage nodes are represented by directories on the local filesystem rather than separate physical or network machines.

## Future Improvements

Possible future work includes:

- Real networked storage nodes
- Persistent service-based node health monitoring
- Automatic background repair
- Stronger metadata management
- Configurable chunk sizes
- Better replica placement strategies
- Real data rebalancing instead of a status/check report
- End-to-end reconstruction and validation workflows
- More comprehensive automated tests
