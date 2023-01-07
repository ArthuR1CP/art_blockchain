# ART Blockchain

Blockchain is a time-stamped decentralized series of fixed records that contains data of any size is controlled by a large network of computers that are scattered around the globe and not owned by a single organization. Every block is secured and connected with each other using hashing technology which protects it from being tampered by an unauthorized person. 



## Installation

1. Run the server:
    * `$ python3 art.py` 
    * `$ python3 art.py -p 5001`
    * `$ python3 art.py --port 5002`

## Tests

1. Run UnitTests
    * `$ python3 -m unittest tests/test_blockchain.py`


## Blockchain API

- /transactions/new - to create a new transaction to a block
- /mine - to tell our server to mine a new block.
- /chain - to return the full Blockchain.
- /nodes/register - to register a new node.