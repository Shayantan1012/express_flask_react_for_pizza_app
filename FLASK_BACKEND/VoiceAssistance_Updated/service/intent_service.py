from app.db_repository import find_products, add_to_cart, remove_from_cart
from VoiceAssistance_Updated.prompts.response_prompt import generate_response


class IntentService:
    """
    Business logic layer.

    Rules:
    - NO session handling
    - NO memory handling
    - NO LLM logic decisions
    - LLM is used ONLY for wording responses
    """

    def __init__(self, payload: dict):
        self.payload = payload or {}
        self.intent = self.payload.get("intent", "")
        self.products = self.payload.get("products", [])

    # -------------------------------------------------
    # MAIN DISPATCHER (SINGLE ENTRY POINT)
    # -------------------------------------------------
    def handle(self) -> dict:
        if self.intent == "add_cart":
            return self.order_service()

        if self.intent == "remove_from_cart":
            return self.remove_from_cart_query()

        if self.intent == "watch_cart":
            return self.watch_cart_service()

        if self.intent in ("search_in_product", "product_query"):
            return self.product_query()

        if self.intent == "price_intent":
            return self.price_query()

        if self.intent == "send_menu":
            return self.send_menu_service()

        if self.intent == "home_page":
            return self.home_page_service()

        if self.intent == "payment":
            return self.payment_service()

        if self.intent == "log_in":
            return self.login_service()

        if self.intent == "new_user":
            return self.new_user_service()

        # Fallback
        return self.other_service()

    # -------------------------------------------------
    # ADD TO CART (WITH LOOPING)
    # -------------------------------------------------
    def order_service(self) -> dict:
        # 🔁 Missing product
        if not self.products:
            return generate_response(
                intent="add_cart",
                context={"status": "missing_products"}
            )

        db_products = find_products()
        available_items = []
        unavailable_items = []

        for item in self.products:
            name = item.get("product", "").strip().lower().replace(" ", "")
            quantity = item.get("quantity")

            # 🔁 Missing quantity
            if quantity is None:
                return generate_response(
                    intent="add_cart",
                    context={
                        "status": "missing_quantity",
                        "product": item.get("product")
                    }
                )

            match = next(
                (p for p in db_products
                 if p["productName"].lower().replace(" ", "") == name),
                None
            )

            if not match or match["quantity"] < quantity:
                unavailable_items.append(item.get("product"))
            else:
                available_items.append({
                    "product": match["productName"],
                    "quantity": quantity,
                    "id": str(match["_id"])
                })

        # 🔁 Unavailable items
        if unavailable_items:
            return generate_response(
                intent="add_cart",
                context={
                    "status": "unavailable",
                    "items": unavailable_items
                }
            )

        # ✅ All info present → perform DB action
        print("Available items added to cart:", available_items)

        add_to_cart(available_items)
        

        return generate_response(
            intent="add_cart",
            context={
                "status": "added",
                "items": available_items
            }
        )

    # -------------------------------------------------
    # REMOVE FROM CART
    # -------------------------------------------------
    def remove_from_cart_query(self) -> dict:
        if not self.products:
            return generate_response(
                intent="remove_from_cart",
                context={"status": "missing_products"}
            )

        remove_from_cart(self.products)

        return generate_response(
            intent="remove_from_cart",
            context={
                "status": "removed",
                "items": self.products
            }
        )

    # -------------------------------------------------
    # WATCH CART
    # -------------------------------------------------
    def watch_cart_service(self) -> dict:
        return generate_response(
            intent="watch_cart",
            context={"status": "shown"}
        )

    # -------------------------------------------------
    # PRODUCT SEARCH / AVAILABILITY
    # -------------------------------------------------
    def product_query(self) -> dict:
        db_products = find_products()

        found_items = []
        not_found_items = []

        for item in self.products:
            name = item.get("product", "").strip().lower().replace(" ", "")
            requested_qty = item.get("quantity")  # may be None

            match = next(
                (p for p in db_products
                if p["productName"].lower().replace(" ", "") == name),
                None
            )

            # ❌ Product not found at all
            if not match:
                not_found_items.append(item.get("product"))
                continue

            # ❌ Product exists but not in stock or zero quantity
            if not match.get("inStock", False) or match.get("quantity", 0) <= 0:
                not_found_items.append(match["productName"])
                continue

            # ❌ Requested quantity more than available
            if requested_qty is not None and requested_qty > match["quantity"]:
                not_found_items.append(match["productName"])
                continue

            # ✅ Product is available
            found_items.append(match["productName"])

        print("FOUND ITEMS:", found_items)
        print("NOT FOUND ITEMS:", not_found_items)

        return generate_response(
            intent="product_query",
            context={
                "found": found_items,
                "not_found": not_found_items
            }
        )

    # -------------------------------------------------
    # PRICE QUERY
    # -------------------------------------------------
    def price_query(self) -> dict:
        db_products = find_products()
        prices = []
        not_found_items = []

        for item in self.products:
            name = item.get("product", "").strip().lower().replace(" ", "")
            match = next(
                (p for p in db_products
                 if p["productName"].lower().replace(" ", "") == name),
                None
            )

            if match:
                prices.append({
                    "product": match["productName"],
                    "price": match["price"]
                })
            else:
                not_found_items.append(item.get("product"))

        return generate_response(
            intent="price_intent",
            context={
                "prices": prices,
                "not_found": not_found_items
            }
        )

    # -------------------------------------------------
    # MENU / HOME / PAYMENT / AUTH
    # -------------------------------------------------
    def send_menu_service(self) -> dict:
        return generate_response(
            intent="send_menu",
            context={"status": "shown"}
        )

    def home_page_service(self) -> dict:
        return generate_response(
            intent="home_page",
            context={"status": "shown"}
        )

    def payment_service(self) -> dict:
        return generate_response(
            intent="payment",
            context={"status": "redirect"}
        )

    def login_service(self) -> dict:
        return generate_response(
            intent="log_in",
            context={"status": "redirect"}
        )

    def new_user_service(self) -> dict:
        return generate_response(
            intent="new_user",
            context={"status": "redirect"}
        )

    # -------------------------------------------------
    # FALLBACK
    # -------------------------------------------------
    def other_service(self) -> dict:
        return generate_response(
            intent="other_queries",
            context={"status": "generic"}
        )
