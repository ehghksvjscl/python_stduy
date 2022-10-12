import datetime
import hashlib
import json
from re import M


class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()

            if hash_operation.startswith("0000"):
                check_proof = True
            else:
                new_proof += 1

            return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


blockchain = Blockchain()
# 마지막 chain block
previous_block = blockchain.get_previous_block()
# 1
previous_proof = previous_block["proof"]

proof = blockchain.proof_of_work(previous_proof)
print(proof)
previous_hash = blockchain.hash(previous_block)
block = blockchain.create_block(proof, previous_hash)
print(blockchain.chain)
