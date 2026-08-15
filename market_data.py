import requests


BASE_URL = "https://cdn.tsetmc.com"


def _get(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Android 12; Mobile) "
            "AppleWebKit/537.36 Chrome/120 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def search_symbol(symbol: str):
    """
    پیدا کردن نماد و InsCode از روی نام نماد
    """
    symbol = symbol.strip()

    url = f"{BASE_URL}/api/Instrument/InstrumentSearch/{symbol}"
    data = _get(url)

    return data


def get_closing_price(ins_code: str):
    """
    دریافت اطلاعات قیمت یک نماد
    """
    url = f"{BASE_URL}/api/ClosingPrice/GetClosingPriceInfo/{ins_code}"
    data = _get(url)

    return data


def get_market_watch():
    """
    دریافت دیده‌بان بازار
    """
    url = (
        f"{BASE_URL}/api/ClosingPrice/GetMarketWatch"
        "?market=0"
        "&paperTypes[0]=1"
        "&paperTypes[1]=2"
        "&paperTypes[2]=3"
        "&paperTypes[3]=4"
        "&paperTypes[4]=5"
        "&paperTypes[5]=6"
        "&paperTypes[6]=7"
        "&paperTypes[7]=8"
        "&paperTypes[8]=9"
        "&withBestLimits=false"
        "&hEven=0"
        "&RefID=0"
    )

    return _get(url)


if __name__ == "__main__":
    print("BORS-AI")
    print("=" * 40)

    print("اتصال به داده بازار...")

    try:
        market = get_market_watch()

        print("اتصال موفق بود ✅")
        print(f"نوع داده دریافتی: {type(market).__name__}")

    except Exception as error:
        print("خطا در دریافت اطلاعات ❌")
        print(error)
