from asyncio import sleep
from config import *
from SkaleABI import contractABI, tokenABI
import os
import json
from web3 import Web3
from solc import compile_standard
from credentials import *

from testdata import *
from time import sleep
from datetime import datetime

from flask import Flask, render_template, request


nonce = 0
def getTransactionDict(account_address):

    global nonce
    nonce = w3.eth.getTransactionCount(account_address)
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

    deals = {}
    escrowsNumber = skale_contract.functions.getCurrentEscrowId().call()
    for _escrowId in range(1, escrowsNumber):
        if skale_contract.functions.getImporter(_escrowId).call():
            deals[_escrowId] = list(skale_contract.functions.getDeal(_escrowId).call())
            deals[_escrowId][5] = datetime.utcfromtimestamp(deals[_escrowId][5]).strftime('%Y-%m-%d')
            deals[_escrowId][2] = 'TDHK'
    
    return render_template('dashboard.html',
            deals=deals)


@app.route("/create-transaction", methods=["GET", "POST"])
def show_template():

    if request.method == 'GET':
        return render_template("create-transaction.html")
    elif request.method == 'POST':
        private_key = exporterPrivateKey
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
                                                                  incoterms_).buildTransaction(getTransactionDict(exporterAddress))
        signed_escrow_txn = w3.eth.account.signTransaction(
            create_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(signed_escrow_txn.rawTransaction)
        sleep(4)

        deals = {}
        escrowsNumber = skale_contract.functions.getCurrentEscrowId().call()
        for _escrowId in range(1, escrowsNumber):
            if skale_contract.functions.getImporter(_escrowId).call():
                deals[_escrowId] = list(skale_contract.functions.getDeal(_escrowId).call())
                deals[_escrowId][5] = datetime.utcfromtimestamp(deals[_escrowId][5]).strftime('%Y-%m-%d')
                deals[_escrowId][2] = 'TDHK'
        
        return render_template('dashboard.html',
                deals=deals)


# fund created escrow
@app.route("/fund-escrow", methods=["GET", "POST"])
def fund_escrow():

    # data = request.form
    # amount_ = data["amount"]

    if request.method == "GET":

        escrowId_ = int(request.args.get("escrow_id"))

        details = list(skale_contract.functions.getDeal(escrowId_).call())
        details[5] = datetime.utcfromtimestamp(details[5]).strftime('%Y-%m-%d')
        details[2] = 'TDHK'
        
        # Retrieve data from escrow to be funded to populate to view

        return render_template(
            "fund-escrow.html", id=escrowId_, details=details)

    elif request.method == "POST":

        private_key = importerPrivateKey

        approve_tx = tdhk_contract.functions.approve(
            skale_contract_address, amount_).buildTransaction(getTransactionDict(importerAddress))
        signed_approve_txn = w3.eth.account.signTransaction(
            approve_tx, private_key=private_key)
        w3.eth.sendRawTransaction(signed_approve_txn.rawTransaction)
        sleep(4)

        # Fund escrow
        data = request.form
        escrowId_ = int(data["importer-confirm"])
        importerReference_ = data["importerReference"]

        fund_escrow_tx = skale_contract.functions.fund_escrow(
            importerReference_, escrowId_).buildTransaction(getTransactionDict(importerAddress))
        fund_escrow_txn = w3.eth.account.signTransaction(
            fund_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(fund_escrow_txn.rawTransaction)
        sleep(4)
        
        deals = {}
        escrowsNumber = skale_contract.functions.getCurrentEscrowId().call()
        for _escrowId in range(1, escrowsNumber):
            if skale_contract.functions.getImporter(_escrowId).call():
                print(deals)
                deals[_escrowId] = list(skale_contract.functions.getDeal(_escrowId).call())
                deals[_escrowId][5] = datetime.utcfromtimestamp(deals[_escrowId][5]).strftime('%Y-%m-%d')
                deals[_escrowId][2] = 'TDHK'
        
        return render_template('dashboard.html',
                deals=deals)


# sign escrow
@app.route("/sign-escrow", methods=["GET", "POST"])
def sign_escrow():
    if request.method == "GET":
        escrowId_ = int(request.args.get("escrow_id"))

        details = list(skale_contract.functions.getDeal(escrowId_).call())
        details[5] = datetime.utcfromtimestamp(details[5]).strftime('%Y-%m-%d')
        details[2] = 'TDHK'
        return render_template("sign-escrow.html", id=escrowId_, details=details)
    elif request.method == "POST":
        private_key = fforwarderPrivateKey
        data = request.form
        fforwarderReference_ = data["fforwarderReference"]
        escrowId_ = int(data["fforwarder-confirm"])

        sign_escrow_tx = skale_contract.functions.sign_escrow(
            fforwarderReference_, escrowId_).buildTransaction(getTransactionDict(fforwarderAddress))
        sign_escrow_txn = w3.eth.account.signTransaction(
            sign_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(sign_escrow_txn.rawTransaction)
        sleep(4)
        
        deals = {}
        escrowsNumber = skale_contract.functions.getCurrentEscrowId().call()
        for _escrowId in range(1, escrowsNumber):
            if skale_contract.functions.getImporter(_escrowId).call():
                deals[_escrowId] = list(skale_contract.functions.getDeal(_escrowId).call())
                deals[_escrowId][5] = datetime.utcfromtimestamp(deals[_escrowId][5]).strftime('%Y-%m-%d')
                deals[_escrowId][2] = 'TDHK'
        
        return render_template('dashboard.html',
                deals=deals)


# close escrow (after the goods shipped succesfully!)
@app.route("/close-escrow", methods=["GET", "POST"])
def close_escrow():

    if request.method == "GET":
        escrowId_ = int(request.args.get("escrow_id"))

        details = list(skale_contract.functions.getDeal(escrowId_).call())
        details[5] = datetime.utcfromtimestamp(details[5]).strftime('%Y-%m-%d')
        details[2] = 'TDHK'
        return render_template("close-escrow.html", id=escrowId_, details=details)
    elif request.method == "POST":
        private_key = fforwarderPrivateKey
        escrowId_ = int(request.form["fforwarder-confirm"])

        close_escrow_tx = skale_contract.functions.close_escrow(
            escrowId_).buildTransaction(getTransactionDict(fforwarderAddress))
        close_escrow_txn = w3.eth.account.signTransaction(
            close_escrow_tx, private_key=private_key)
        w3.eth.sendRawTransaction(close_escrow_txn.rawTransaction)
        sleep(4)
        
        deals = {}
        escrowsNumber = skale_contract.functions.getCurrentEscrowId().call()
        for _escrowId in range(1, escrowsNumber):
            if skale_contract.functions.getImporter(_escrowId).call():
                deals[_escrowId] = list(skale_contract.functions.getDeal(_escrowId).call())
                deals[_escrowId][5] = datetime.utcfromtimestamp(deals[_escrowId][5]).strftime('%Y-%m-%d')
                deals[_escrowId][2] = 'TDHK'
        
        return render_template('dashboard.html',
                deals=deals)


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)