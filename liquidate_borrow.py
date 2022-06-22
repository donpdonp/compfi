import json
from web3 import Web3

with open(f'config.json') as file:
  config = json.load(file)

print(config['provider'])
web3 = Web3(Web3.HTTPProvider(config['provider']))
print(f"connected: {web3.isConnected()}")

with open(f'compound-config/networks/{config["network"]}-abi.json') as file:
  compound_abi = json.load(file)

with open(f'compound-config/networks/{config["network"]}.json') as file:
  compound_networks= json.load(file)

cETH_address= compound_networks['Contracts']['cETH']
ceth_abi = compound_abi["cETH"]
contract = web3.eth.contract(address=cETH_address, abi=ceth_abi)

c_token_collateral = cETH_address
go = contract.functions.liquidateBorrow(config['borrower'], c_token_collateral)
try:
  print(f"estimateGas {go.estimateGas()}")
  txn_hash = go.transact({"from": config['me']})
  print(txn_hash)
  web3.eth.wait_for_transaction_receipt(txn_hash)
except Exception as e:
  print(f"error: {e}")
