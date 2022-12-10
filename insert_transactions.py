from web3 import Web3
import sys
import random
import time
from tqdm import tqdm

num_transactions = int(sys.argv[1])

if __name__ == "__main__":
    w3 = Web3(Web3.IPCProvider('node1/geth.ipc'))
    for _ in tqdm(range(num_transactions)):
        w3.eth.sendTransaction({'from': Web3.toChecksumAddress(w3.eth.accounts[0]), 'to': Web3.toChecksumAddress("0x8dd07043fb4e6237dc06abd42545527e3f828126"), 'value': w3.toWei(10, 'ether')})
        time.sleep(random.random()*0.2)
