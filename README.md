# 🧠 Smart Contract + Python Interaction

This project demonstrates how to **deploy an Ethereum smart contract** and **interact with it programmatically using Python** via Web3.py.

The focus of the project is on **end-to-end blockchain interaction**:
- Writing a Solidity smart contract
- Deploying it to the Sepolia testnet
- Connecting to it using Python
- Calling contract functions and reading live on-chain state

This project was built as a learning and portfolio project to showcase practical Web3 backend skills.

---

## 🚀 What This Project Does

✅ Deploys a simple Solidity smart contract  
✅ Connects Python to Ethereum via an RPC provider  
✅ Loads the contract using its address + ABI  
✅ Calls a read-only contract function from Python  
✅ Retrieves and prints live blockchain data  

The result is a working example of **Python ↔ Ethereum smart contract interaction**.

---

## 🧱 Smart Contract

The Solidity contract is intentionally simple to focus on interaction rather than complexity.

Example capabilities:
- Stores a value on-chain (e.g. a counter)
- Exposes a public read function
- Can be extended with write functions later

The contract was deployed to the **Sepolia Ethereum testnet**.

---

## 🐍 Python Interaction (Web3.py)

Python is used as the off-chain backend to interact with the deployed contract.

Using Web3.py, the Python code:
- Connects to Sepolia via an RPC URL
- Loads the deployed contract using a minimal ABI
- Calls a read-only function
- Prints the current on-chain value

This demonstrates how backend systems can safely read blockchain state without sending transactions or paying gas.

---

## 📓 Colab Notebook

The file: Smart_Contract_Python_Interaction.ipynb

contains a **fully working Google Colab notebook** that demonstrates:
- Installing dependencies
- Connecting to Ethereum
- Loading the contract
- Calling contract functions
- Viewing live output

Colab was intentionally used to avoid local environment friction and clearly demonstrate a working Python → blockchain pipeline.

---

## 🛠 Tech Stack

- **Solidity** – Smart contract development  
- **Ethereum (Sepolia testnet)** – Blockchain network  
- **Python** – Off-chain interaction  
- **Web3.py** – Ethereum RPC interface  
- **Google Colab** – Python execution environment  

---

## 📁 Project Structure

├── contracts/
│ └── Counter.sol
├── Smart_Contract_Python_Interaction.ipynb
└── README.md

---

## 🔐 Notes on Security

- RPC URLs and API keys are **not committed** to the repository
- Any secrets are handled via environment variables or temporary Colab configuration
- This project uses **read-only contract calls** for safety

---

## 🎯 Purpose of This Project

This project is designed to show:
- Practical understanding of smart contracts
- Ability to deploy and interact with contracts on a testnet
- Comfort using Python as a Web3 backend tool
- Clear separation between on-chain and off-chain logic

It serves as a **foundational Web3 portfolio project** and a stepping stone toward more advanced contract interaction and DeFi-style systems.

---

## 🌱 Possible Extensions

- Sending transactions from Python (write functions)
- Interacting with an ERC-20 token contract
- Adding event listening
- Building a small AI-style explanation layer
- Refactoring notebook code into Python modules

---

## ✅ Status

**Complete**  
The core goal of Python ↔ smart contract interaction has been successfully implemented and demonstrated.






