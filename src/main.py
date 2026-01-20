from blockchain.interact_contract import get_count

def main():
    count = get_count()
    print(f"Current count in contract: {count}")

if __name__ == "__main__":
    main()
