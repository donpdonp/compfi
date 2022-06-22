import json
from web3 import Web3

with open(f'config.json') as file:
  config = json.load(file)

print(f"{config['network']} {config['provider']}")
web3 = Web3(Web3.HTTPProvider(config['provider']))
# print(f"connected: {web3.isConnected()}")

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
  opts = {"from": config['me_pub'], 
          "value": web3.toWei(0.1, 'ether'),
          "gas": 100000,
          "gasPrice": web3.toWei(5000, 'gwei'),
        }
  print(opts)
  # txn_hash = go.transact(opts)

  opts['nonce'] = web3.eth.get_transaction_count(config['me_pub'])
  print(f"nonce {opts['nonce']}")
  txn = go.buildTransaction(opts)
  signed_txn = web3.eth.account.signTransaction(txn, private_key=config['me_priv'])
  txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
  # txn_hash = web3.toHex(web3.keccak(signed_txn.rawTransaction))
  print(web3.toHex(txn_hash))
  print("send. waiting for receipt.")
  web3.eth.wait_for_transaction_receipt(txn_hash)
except Exception as e:
  print(f"error: {e}")
