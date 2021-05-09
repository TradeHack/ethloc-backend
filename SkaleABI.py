contractABI = [
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "close_escrow",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_importerAddress",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "_token",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_exporterReference",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_fforwarder",
				"type": "address"
			},
			{
				"internalType": "uint64",
				"name": "_expiryDate",
				"type": "uint64"
			},
			{
				"internalType": "string",
				"name": "_incoterms",
				"type": "string"
			}
		],
		"name": "create_escrow",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_importerReference",
				"type": "string"
			},
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "fund_escrow",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_fforwarderReference",
				"type": "string"
			},
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "sign_escrow",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "getCurrentEscrowId",
		"outputs": [
			{
				"internalType": "uint64",
				"name": "escrowId_",
				"type": "uint64"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getDeal",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "importer",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "contract ERC20",
						"name": "tokenContract",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "exporterReference",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "fforwarder",
						"type": "address"
					},
					{
						"internalType": "uint64",
						"name": "expiryDate",
						"type": "uint64"
					},
					{
						"internalType": "string",
						"name": "incoterms",
						"type": "string"
					},
					{
						"internalType": "address payable",
						"name": "exporter",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "importerReference",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "fforwarderReference",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "signed",
						"type": "bool"
					},
					{
						"internalType": "bool",
						"name": "filled",
						"type": "bool"
					},
					{
						"internalType": "bool",
						"name": "closed",
						"type": "bool"
					}
				],
				"internalType": "struct Deal",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getExpiryDate",
		"outputs": [
			{
				"internalType": "uint64",
				"name": "expiryDate",
				"type": "uint64"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getExporter",
		"outputs": [
			{
				"internalType": "address",
				"name": "exporterAddress",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getExporterReference",
		"outputs": [
			{
				"internalType": "string",
				"name": "exporterReference",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getFForwarder",
		"outputs": [
			{
				"internalType": "address",
				"name": "fforwarderAddress",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getFForwarderReference",
		"outputs": [
			{
				"internalType": "string",
				"name": "fforwarderReference",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getImporter",
		"outputs": [
			{
				"internalType": "address",
				"name": "importerAddress",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getImporterReference",
		"outputs": [
			{
				"internalType": "string",
				"name": "importerReference",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getIncoterms",
		"outputs": [
			{
				"internalType": "string",
				"name": "incoterms",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getTokenAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "tokenAddress",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "getTokenAmount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "tokenAmount",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "isClosed",
		"outputs": [
			{
				"internalType": "bool",
				"name": "isEscrowClosed",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "isFunded",
		"outputs": [
			{
				"internalType": "bool",
				"name": "isEscrowFilled",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "_escrowId",
				"type": "uint64"
			}
		],
		"name": "isSigned",
		"outputs": [
			{
				"internalType": "bool",
				"name": "isEscrowSigned",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

tokenABI = """[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name_",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "symbol_",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "subtractedValue",
				"type": "uint256"
			}
		],
		"name": "decreaseAllowance",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "addedValue",
				"type": "uint256"
			}
		],
		"name": "increaseAllowance",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "recipient",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "recipient",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""