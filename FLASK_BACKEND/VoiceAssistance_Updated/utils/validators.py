def validate_user_text(text: str) -> str:
    """
    Validates and cleans user input text.
    Raises ValueError if invalid.
    """
    if not text:
        raise ValueError("Input text is empty")

    text = text.strip()

    if len(text) == 0:
        raise ValueError("Input text is empty")

    if len(text) > 1000:
        raise ValueError("Input text exceeds maximum length")

    return text


def safe_get_products(payload: dict) -> list:
    """
    Safely extracts product list from payload.
    Ensures correct structure.
    """
    products = payload.get("products", [])

    if not isinstance(products, list):
        return []

    cleaned = []
    for p in products:
        if not isinstance(p, dict):
            continue
        name = p.get("product")
        qty = p.get("quantity", 1)

        if not name:
            continue

        cleaned.append({
            "product": str(name),
            "quantity": qty
        })

    return cleaned
