import json
from web3 import Web3 

infura_url = "https://ropsten.infura.io/v3/25145713e6fa4a86a494a6df57e7b251"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0xE2F6Cc45287534496f343A2182aA55fD95480C24")
print(web3.fromWei(balance, "ether"))

#reconstrução do smart contract 
abi = json.loads('[{"constant": false, "inputs": [{"name": "_l", "type": "uint256"}], "name": "setLitros", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "_p", "type": "uint256"}], "name": "setPreco", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "_volume", "type": "uint256"}], "name": "transferir", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function"}, {"inputs": [{"name": "_litros", "type": "uint256"}, {"name": "_preco", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"constant": true, "inputs": [], "name": "getLitrosComprador", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "getLitrosDono", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "getPreco", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}]') #json array that describes what the smart contract looks like
address = "0xe297628b08decfacd069b4ef09989ebd8ef83135" #address of the deployed smart contract on the blockchain

contract = web3.eth.contract(address=Web3.toChecksumAddress(address), abi=abi)
print(contract)

print(contract.functions.getLitrosComprador().call())
print(contract.functions.getLitrosDono().call())
print(contract.functions.getPreco().call())
contract.functions.setLitros(10).call()
contract.functions.setPreco(100).call()
print(contract.functions.getLitrosDono().call())
print(contract.functions.getPreco().call())