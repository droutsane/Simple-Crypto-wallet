from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/00848b2cf2ea4d26a4e4887966989c64"
web3 = Web3(Web3.HTTPProvider(infura_url))
web3.isConnected()
balance = web3.eth.getBalance("0x55a5A0FeEC04bCd7892975c556688EF51e95704F")
web3.fromWei(balance, 'ether')

account_1 = account
account_2 = ""

private_key = ""

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce' : '',
    'to' : account_2,
    'value' : web3.toWei(1, 'ether'),
    'gas' : 2000000,
    'gasPrice' : web3.toWei('50', 'gwei')
}

signed_trx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_trx.rawTransaction)
print(web3.toHex(tx_hash))

latest = web3.eth.blockNumber
print(web3.eth.getBlock(latest))

hash = ""
print(web3.eth.getTransactionByBlock(hash, 2))

account = web3.eth.account.create()
keystore = account.encrypt("hello")
