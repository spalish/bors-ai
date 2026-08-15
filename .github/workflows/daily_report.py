from datetime import datetime
from market_data import get_market_watch


def create_report():
    print("BORS-AI DAILY REPORT")
    print("=" * 50)

    try:
        data = get_market_watch()

        print("Market data received successfully.")
        print(f"Generated at: {datetime.now().isoformat()}")

        if isinstance(data, dict):
            print(f"Response keys: {list(data.keys())}")

        elif isinstance(data, list):
            print(f"Number of records: {len(data)}")

        else:
            print(f"Data type: {type(data).__name__}")

        return data

    except Exception as error:
        print("ERROR")
        print(error)
        return None


if __name__ == "__main__":
    create_report()
