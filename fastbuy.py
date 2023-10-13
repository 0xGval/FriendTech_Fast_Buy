import json
import os
from dotenv import load_dotenv
from web3 import Web3

# Load environment variables
load_dotenv()

# Connect to Basechain (or your L2 Ethereum chain)
w3 = Web3(Web3.HTTPProvider('[YOUR RPC GOES HERE]'))

# Ensure you're connected
if not w3.is_connected():
    print("Error: Not connected to the Ethereum node!")
    exit()

# Load ABI and private key
with open("abi.json", "r") as file:
    data = json.load(file)
    contract_abi = data['abi']

private_key = os.getenv('PRIVATE_KEY')

# Your account that will interact with the contract
my_address = w3.eth.account.from_key(private_key).address

# Smart contract details
contract_address = '0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4'

# Setting up the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Get user input for number of shares
shares_amount = int(input("Enter the number of shares you want to buy: "))
shares_subject = w3.to_checksum_address(input("Enter the address of the shares subject you want to buy from: "))

# Get the share price after fee
share_price_after_fee = contract.functions.getBuyPriceAfterFee(shares_subject, shares_amount).call()

# Display a summary of the transaction details to the user and ask for confirmation
print(f"\nTransaction Summary:")
print(f"Target: {shares_subject}")
print(f"Shares quantity: {shares_amount}")
print(f"Total Shares Price: {w3.from_wei(share_price_after_fee, 'ether')} ETH")
print("______________________________________________________")
final_confirmation = input("Do you want to proceed with the purchase? (yes/no): ")


if final_confirmation.lower() == 'yes':
    # Create transaction for buying the shares
    transaction = contract.functions.buyShares(shares_subject, shares_amount).build_transaction({
        'chainId': 8453,  # Replace with appropriate Basechain chainId
        'gas': 120000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': w3.eth.get_transaction_count(my_address),
        'value': share_price_after_fee  # This is how much ETH you're sending with the transaction for the shares
    })


    # Sign the transaction
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)

    #Send the transaction and get the transaction hash
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Print the BASESCAN link for the transaction
    print(f"Transaction sent:\nhttps://basescan.org/tx/{tx_hash.hex()}")

    # Optional: If you want to wait for the transactions to be mined
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Check the transaction status
    if receipt['status'] == 1:
        print("Transaction was successful!")
    else:
        print("Transaction failed!")
else:
    print("Purchase canceled.")