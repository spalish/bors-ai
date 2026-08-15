from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    price: float
    eps: float
    pe: float
    volume_ratio: float
    trend_score: float


def calculate_score(stock: Stock) -> float:
    """
    امتیاز اولیه سهم از 0 تا 100.
    فعلاً از داده‌های ورودی استفاده می‌کند.
    بعداً داده واقعی بورس به آن وصل می‌شود.
    """

    score = 0

    # P/E
    if 0 < stock.pe <= 6:
        score += 25
    elif 6 < stock.pe <= 10:
        score += 18
    elif 10 < stock.pe <= 15:
        score += 10

    # EPS مثبت
    if stock.eps > 0:
        score += 20

    # قدرت حجم معاملات
    if stock.volume_ratio >= 2:
        score += 25
    elif stock.volume_ratio >= 1.3:
        score += 15
    elif stock.volume_ratio >= 1:
        score += 8

    # روند قیمتی
    score += max(0, min(stock.trend_score, 30))

    return round(min(score, 100), 2)


def decision(score: float) -> str:
    if score >= 75:
        return "BUY"
    elif score >= 55:
        return "HOLD"
    else:
        return "SELL"


def analyze(stock: Stock) -> dict:
    score = calculate_score(stock)

    return {
        "symbol": stock.symbol,
        "score": score,
        "decision": decision(score),
    }


if __name__ == "__main__":
    sample = Stock(
        symbol="فولاد",
        price=2218,
        eps=350,
        pe=6.3,
        volume_ratio=1.6,
        trend_score=22,
    )

    result = analyze(sample)

    print("BORS-AI")
    print("-" * 30)
    print(f"سهم: {result['symbol']}")
    print(f"امتیاز: {result['score']}/100")
    print(f"تصمیم: {result['decision']}")
