# FriendTech_Fast_Buy
Simple python script to quickly buy shares on Friend.Tech from console and be able to access chats in app from the FT account associated to the imported wallet



### Prerequisites

**Environment**: Python 3.x

**Dependencies**:

- web3: For Ethereum blockchain interaction.
- dotenv: For environment variable management.

Install with `pip install python-dotenv web3`

**Configuration Files**:

1. '.env': Contains your Ethereum private key. A template (sample.env) is provided for reference.
2. 'abi.json': ABI for the Ethereum contract.

### Getting Started

**Repository Setup**:
- Clone the repository to your local machine.

**Environment Configuration:**:
- rename sample.env to .env and add the private key of the wallet you want to use

> "Consider using a dedicated account (and private key) for security purposes"

**Contracts  Configuration:**:
- Ensure the friend.tech contract's ABI is saved as abi.json in the root directory.

**RPC  Configuration:**:
- Add your RPC to the buy.py file in place of the placeholder.

**Executing Script**:
- Once you completed the steps above, run the script with `python fastbuy.py`
- Follow the on-screen prompts for share acquisition details.
- Review the transaction summary and confirm to proceed.

### Fastbuy Flow

<img width="743" alt="image" src="https://github.com/giovall/FriendTech_Fast_Buy/assets/122178427/0e4388ec-5797-4c38-92d4-333786578903">

> "Typical flow on console"


**Setup**:
- Import libraries: json, os, dotenv, web3.
- Load .env to retrieve the private key.
- Connect to Base Chain
  
**Verification**:
- Check Ethereum node connection. If failed, exit.

**Data Retrieval**:
- Load contract's ABI from abi.json.
- Extract the user's Ethereum address from the private key.
  
**Contract Initialization**:
- Create a contract instance using its ABI and predefined address.

**User Input**:
- Get desired number of shares.
- Get the Ethereum address of the share subject.
  
**Price Calculation**:
- Call getBuyPriceAfterFee to determine total cost for shares.
- Convert and display the price in ETH to the user.

**Purchase Confirmation**:
- Present a summarized transaction to the user.
- Ask the user if they wish to proceed with the purchase.
  
**Transaction Execution (If Confirmed)**:

- Construct the transaction with details like chainId, gas, etc.
- Sign the transaction using the private key.
- Send the transaction to the Ethereum network.
- Provide a BASESCAN link for the user to monitor the transaction.
- Wait for the transaction's completion and display its status.

> "I hardcoded gas value as follows: Gwei=10 Gas Limit=120000. You can adjust them in the fastbuy.py file"




**If the user declines**, display "Purchase canceled".


**Disclaimer: Please interact with the software at your own risk, I am not responsible for any financial loss or any downside caused by it. I cannot guarantee any results from it. The software is not an offering from me. I share no responsibility for the usage and outcome of this now open-sourced software.**
