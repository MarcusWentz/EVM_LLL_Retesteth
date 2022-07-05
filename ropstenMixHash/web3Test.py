from web3 import Web3
import json
import os

infura_ropsten_testnet_url_API =  str(os.environ['ropstenInfuraAPI']);
web3 = Web3(Web3.HTTPProvider(infura_ropsten_testnet_url_API))

print("Last PoW Block:")
print("difficulty block header: " + str(web3.eth.getBlock(12350712).difficulty) )
print("First PoS Block")
print("difficulty block header: " + str(web3.eth.getBlock(12350713).difficulty) )
print("Selected block PoS")
print("difficulty block header: " + str(web3.eth.getBlock(12424058).difficulty) )
print("mixHash storing prevrandao: " + str(int(web3.eth.getBlock(12424058).mixHash.hex(),16)) )
