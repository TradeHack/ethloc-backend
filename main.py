from asyncio import sleep
from config import *
from SkaleABI import contractABI, tokenABI
import os
import json
from web3 import Web3
from solc import compile_standard

from testdata import *
from time import sleep
from datetime import datetime

from flask import Flask, render_template, request


nonce = 0
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

skale_contract_address = "0xC5fb803982B0EAb832198C7982713B6CD4bF5C0E"
tdhk_contract_address = "0xD4d30a3f584dd2408AdB138F9Ba8f9049723Ef1a"

skale_contract = w3.eth.contract(
    address=skale_contract_address, abi=contractABI)
tdhk_contract = w3.eth.contract(address=tdhk_contract_address, abi=tokenABI)

# get current escrow id (our escrow id) which is number of all escrows created in the contract
escrowId_ = skale_contract.functions.getCurrentEscrowId().call()
print("Escrow ID: ", escrowId_)


app = Flask(__name__)


@app.route('/')
def root():


    importerAddress = "0xF411c83AA11D7d22670334B1E7f4D9DDE3f9f485"
    deals = {}
    escrowsNumber = skale_contract.functions.getCurrentEscrowId().call()
    for _escrowId in range(1, escrowsNumber):
        if skale_contract.functions.getImporter(_escrowId).call():
            deals[_escrowId] = list(skale_contract.functions.getDeal(_escrowId).call())
            deals[_escrowId][5] = datetime.utcfromtimestamp(deals[_escrowId][5]).strftime('%Y-%m-%d')
            deals[_escrowId][2] = 'TDHK'
    
    print(deals)
    return render_template('dashboard.html',
            deals=deals, role="importer")


@app.route("/create-transaction", methods=["GET", "POST"])
def show_template():

    if request.method == 'GET':
        return render_template("create-transaction.html")
    elif request.method == 'POST':
        data = request.form
        importerAddress_ = data["importerAddress"]
        amount_ = int(data["amount"])
        # tokenName = data["currency"]
        token_ = tdhk_contract_address
        exporterReference_ = data["exporterReference"]
        fforwarder_ = data["fforwarder"]
        expiryDate_ = int(datetime.timestamp(datetime.strptime(data["expiryDate"], '%Y-%m-%d')))
        incoterms_ = data["incoterms"]
        create_escrow_tx = skale_contract.functions.create_escrow(importerAddress_,
                                                                  amount_,
                                                                  token_,
                                                                  exporterReference_,
                                                                  fforwarder_,
                                                                  expiryDate_,
                                                                  incoterms_).buildTransaction(getTransactionDict())
        signed_escrow_txn = w3.eth.account.signTransaction(
            create_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(signed_escrow_txn.rawTransaction)
        sleep(4)
        return ("It works!")


# approve TDHK tokens to spend by our contract
@app.route("/approve-tokens", methods=["GET", "POST"])
def approve_tokens():
    pass


# fund newly created escrow (right now importer is exporter as skETH tokens (ETH of SKALE is available just for me, but if we need we can ask for more tokens on different accounts))
@app.route("/fund-escrow", methods=["GET", "POST"])
def fund_escrow():

    # data = request.form
    # amount_ = data["amount"]


    if request.method == "GET":

        escrowId_ = int(request.args.get("escrow_id"))

        details = list(skale_contract.functions.getDeal(escrowId_).call())
        print(details)
        details[5] = datetime.utcfromtimestamp(details[5]).strftime('%Y-%m-%d')
        details[2] = 'TDHK'
        
        # Retrieve data from escrow to be funded to populate to view

        return render_template(
            "fund-escrow.html", id=escrowId_, details=details)

    elif request.method == "POST":

        data

        # Approve token specified in newly created escrow
        #tokenAddress_ = # TODO

        approve_tx = tdhk_contract.functions.approve(
            skale_contract_address, amount_).buildTransaction(getTransactionDict())
        signed_approve_txn = w3.eth.account.signTransaction(
            approve_tx, private_key=private_key)
        w3.eth.sendRawTransaction(signed_approve_txn.rawTransaction)
        sleep(4)

        # Fund escrow
        data = request.form
        escrowId_ = data["escrowId"]
        importerReference_ = data["importerReference"]

        fund_escrow_tx = skale_contract.functions.fund_escrow(
            importerReference_, escrowId_).buildTransaction(getTransactionDict())
        fund_escrow_txn = w3.eth.account.signTransaction(
            fund_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(fund_escrow_txn.rawTransaction)
        sleep(4)


# sign escrow (also from the point of view of exporter as skETH is very deficit resource)
@app.route("/sign-escrow", methods=["GET", "POST"])
def sign_escrow():
    if request.method == "GET":
        return render_template("sign.html")
    elif request.method == "POST":
        data = request.form
        escrowId_ = data["escrowId"]
        fforwarderReference_ = data["fforwarderReference"]

        sign_escrow_tx = skale_contract.functions.sign_escrow(
            fforwarderReference_, escrowId_).buildTransaction(getTransactionDict())
        sign_escrow_txn = w3.eth.account.signTransaction(
            sign_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(sign_escrow_txn.rawTransaction)
        sleep(4)


# close escrow (after the goods shipped succesfully!)
@app.route("/close-escrow", methods=["GET", "POST"])
def close_escrow():

    if request.method == "GET":
        return render_template("close.html")
    elif request.method == "POST":
        escrowId_ = request.form["escrowId"]

        close_escrow_tx = skale_contract.functions.close_escrow(
            escrowId_).buildTransaction(getTransactionDict())
        close_escrow_txn = w3.eth.account.signTransaction(
            close_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(close_escrow_txn.rawTransaction)
        sleep(4)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)