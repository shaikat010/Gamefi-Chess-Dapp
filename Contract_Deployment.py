import web3
from web3 import Web3
from solcx import compile_source

# Solidity source code
with open("Game_Status.sol", "r") as f:
    contract_source_code = f.read()

# Compile the contract
compiled_sol = compile_source(contract_source_code, output_values=["abi", "bin"])

# Retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# Get bytecode / bin
bytecode = contract_interface["bin"]

# Get ABI
abi = contract_interface["abi"]

# Web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

# Deploy the contract with constructor arguments
game_status = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = game_status.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Instantiate the contract at the deployed address
game_status = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# Interact with the contract using its functions
def store_result(winner):
    game_status.functions.storeResult(winner).transact()
    print("Status has been added to the blockchain smart contract!")
    print('--------------------------------------------------------')
    print(f"The status is  {winner}")

def get_game_status():
    student = game_status.functions.get_status().call()
    return student

store_result("Black is the winner!")
print(get_game_status())