import requests
from typing import Optional


def get_stock_price(symbol: str) -> Optional[float]:
    """
    دریافت قیمت پایانی سهم.
    
    این تابع فعلاً ساختار اتصال به منبع داده را آماده می‌کند.
    منبع واقعی داده را در مرحله بعد به آن وصل می‌کنیم.
    """

    symbol = symbol.strip()

    if not symbol:
        return None

    # فعلاً مقدار None برمی‌گردانیم.
    # در مرحله بعد API/منبع داده واقعی بورس ایران را وصل می‌کنیم.
    return None


def get_market_status() -> str:
    """
    وضعیت کلی بازار.
    """

    return "UNKNOWN"


if __name__ == "__main__":
    print("BORS-AI Market Data")
    print("-" * 30)

    symbol = "فولاد"

    price = get_stock_price(symbol)

    print(f"سهم: {symbol}")
    print(f"قیمت: {price}")
    print(f"وضعیت بازار: {get_market_status()}")
