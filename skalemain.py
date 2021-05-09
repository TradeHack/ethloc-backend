from web3 import Web3
from SkaleABI import contractABI, tokenABI # local file
from solc import compile_standard
from testdata import *
from config import *
from time import sleep


def getTransactionDict():

    global nonce
    nonce = w3.eth.getTransactionCount(my_account_address)
    return {
        'chainId': 0x1ee6072383c0a,
        'gas': 2100000,
        'gasPrice': w3.toWei('0.00001', 'gwei'),
        'nonce': nonce,
    }


private_key = PRIVATE_KEY
ENDPOINT = skale_endpoint

w3 = Web3(Web3.HTTPProvider(ENDPOINT))
nonce = w3.eth.getTransactionCount(my_account_address)

skale_contract_address = "0xd2B714a30C473eD3a20D228709EEFea6814835eF"
tdhk_contract_address = "0xD4d30a3f584dd2408AdB138F9Ba8f9049723Ef1a"

skale_contract = w3.eth.contract(address=skale_contract_address, abi=contractABI)
tdhk_contract = w3.eth.contract(address=tdhk_contract_address, abi=tokenABI)


# approve TDHK tokens to spend by our contract - after exporter chooses the token
print("Nonce: ", nonce)
approve_tx = tdhk_contract.functions.approve(skale_contract_address, amount_).buildTransaction(getTransactionDict())
signed_approve_txn = w3.eth.account.signTransaction(approve_tx, private_key=private_key)
w3.eth.sendRawTransaction(signed_approve_txn.rawTransaction)
print(signed_approve_txn)
sleep(4)

# create new escrow (new deal)
print("Nonce: ", nonce)
create_escrow_tx = skale_contract.functions.create_escrow(importerAddress_, amount_, token_, exporterReference_, fforwarder_, expiryDate_, incoterms_).buildTransaction(getTransactionDict())
signed_escrow_txn = w3.eth.account.signTransaction(create_escrow_tx, private_key=private_key)
w3.eth.sendRawTransaction(signed_escrow_txn.rawTransaction)
print(signed_escrow_txn)
sleep(4)

# get current escrow id (our escrow id) which is number of all escrows created in the contract
escrowId_ = skale_contract.functions.getCurrentEscrowId().call()
print("Escrow ID: ", escrowId_)

# fund newly created escrow - importer
print("Nonce: ", nonce)
fund_escrow_tx = skale_contract.functions.fund_escrow(importerReference_, escrowId_).buildTransaction(getTransactionDict())
fund_escrow_txn = w3.eth.account.signTransaction(fund_escrow_tx, private_key=private_key) # TODO change private key to importer private key
w3.eth.sendRawTransaction(fund_escrow_txn.rawTransaction)
print(fund_escrow_txn)
sleep(4)

# sign escrow (also from the point of view of exporter as skETH is very deficit resource)
print("Nonce: ", nonce)
sign_escrow_tx = skale_contract.functions.sign_escrow(fforwarderReference_, escrowId_).buildTransaction(getTransactionDict())
sign_escrow_txn = w3.eth.account.signTransaction(sign_escrow_tx, private_key=private_key)
w3.eth.sendRawTransaction(sign_escrow_txn.rawTransaction)
print(signed_approve_txn)
sleep(4)

# get address of token (just to test functionality of this function)
getTokenAddress = skale_contract.functions.getTokenAddress(escrowId_).call()
print("Token address: ", getTokenAddress)

# close escrow (after the goods shipped succesfully!)
print("Nonce: ", nonce)
close_escrow_tx = skale_contract.functions.close_escrow(escrowId_).buildTransaction(getTransactionDict())
close_escrow_txn = w3.eth.account.signTransaction(close_escrow_tx, private_key=private_key)
w3.eth.sendRawTransaction(close_escrow_txn.rawTransaction)
print(signed_approve_txn)
sleep(4)