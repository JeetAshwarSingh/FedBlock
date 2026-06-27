import  hashlib 
from time import time
import json
import numpy as np
import os

BLOCKCHAIN_FILE = "blockchain_data.json"

class Blockchain:

    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        genesis_block = self.create_block("This is the genesis block", "0")
        self.chain.append(genesis_block)

    def create_block(self, data, previous_HASH):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': data,
            'previous_HASH': previous_HASH,
            'nonce': 0,
            'HASH': None
        }
        block['HASH'] = self.mine_block(block)
        return block
    
    def compute_HASH(self, block):
        block_copy = block.copy()
        block_copy['HASH'] = None
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, block):
        while True:
            HASH_value = self.compute_HASH(block)
            if HASH_value.startswith('0' * self.difficulty):
                return HASH_value
            else:
                block['nonce'] += 1

    def add_block(self, data):
        previous_HASH = self.chain[-1]['HASH']
        new_block = self.create_block(data, previous_HASH)
        self.chain.append(new_block)

    def print_chain(self):
        print("\n Blockchain ")
        for block in self.chain:
            print(f"\nBlock {block['index']}")
            print(f"Timestamp: {block['timestamp']}")
            print(f"Data: {block['data']}")
            print(f"Previous HASH: {block['previous_HASH']}")
            print(f"Nonce: {block['nonce']}")
            print(f"HASH: {block['HASH']}")

    def save_chain(self, chain=None):
        if chain is None:
            chain = self.chain
        with open(BLOCKCHAIN_FILE, 'w') as f:
            json.dump(chain, f, indent=4)

    def load_chain(self):
        if os.path.exists(BLOCKCHAIN_FILE):
            with open(BLOCKCHAIN_FILE, 'r') as f:
                return json.load(f)
        else:
            genesis_block = self.create_block("Genesis Block", "0")
            chain = [genesis_block]
            self.save_chain(chain)
            return chain
    
    def get_last_block(self):
            return self.chain[-1]


class hospital_data :
    def __init__(self,hospital_name = None,hospital_id = None,hospital_weight = None):
        self.hospital_name = hospital_name
        self.hospital_id = hospital_id
        self.hospital_weight = hospital_weight
    def get_hospital_weight(self):
        return self.hospital_weight
    
class FederatedModelData:
    def __init__(self, list1=None):
        if list1 is None or len(list1) == 0:
            raise ValueError("list1 must be a non-empty list of dictionaries containing numpy arrays")
        avg_dict = {}
        for key in list1[0].keys():
            arrays = [d[key] for d in list1]
            avg_dict[key] = np.mean(arrays, axis=0)
        self.avg_dict = avg_dict
    def get_avg(self):
        return self.avg_dict