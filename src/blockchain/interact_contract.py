import sys
sys.path.append("src")

import os
from web3 import Web3
from dotenv import load_dotenv
from blockchain.contract_abi import CONTRACT_ABI

# Load .env
load_dotenv()
RPC_URL = os.getenv("RPC_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    raise Exception("Web3 connection failed")

# Convert contract address to checksum format
contract_address = w3.to_checksum_address(CONTRACT_ADDRESS)

# Load contract
contract = w3.eth.contract(address=contract_address, abi=CONTRACT_ABI)

# Call read-only function
def get_count():
    return contract.functions.getCount().call()

if __name__ == "__main__":
    count = get_count()
    print(f"Current count in contract: {count}")
