from app import client , DB_NAME , USER_COLLECTION, PRODUCT_COLLECTION, CART_COLLECTION, ORDER_COLLECTION
from flask import session
from bson import ObjectId


def find_products():
    available_products = []
    try:
        db = client[DB_NAME]
        collection = db[PRODUCT_COLLECTION]
        products = collection.find({})
        for product in products:
            available_products.append(product)
        return available_products
    except Exception as e:
        print(f"An error occurred while fetching products: {str(e)}")
        return available_products
    
    
    
def add_to_cart(product):
    try:
        db = client[DB_NAME]
        collection = db[CART_COLLECTION]

        user_id = session.get('user_info',None)
        user_obj_id = ObjectId(user_id)
        print(user_id)

        existing_cart = collection.find_one({"user": user_obj_id})
        print("This is product in cart:", existing_cart)

        if existing_cart:
            for item in product:
                product_id = ObjectId(item['id'])
                quantity = item['quantity']

                result = collection.update_one(
                    {
                        "user": user_obj_id,
                        "items.product": product_id
                    },
                    {
                        "$inc": {
                            "items.$.quantity": quantity
                        }
                    }
                )

                if result.modified_count == 0:
                    # Product not in cart, push new item
                    collection.update_one(
                        {"user": user_obj_id},
                        {
                            "$push": {
                                "items": {
                                    "product": product_id,
                                    "quantity": quantity
                                }
                            }
                        },
                        upsert=True
                    )

        else:
            # No existing cart — create a new one
            items = [
                {
                    "product": ObjectId(item['id']),
                    "quantity": item['quantity']
                } for item in product
            ]
            collection.insert_one({
                "user": user_obj_id,
                "items": items
            })

        return {
            "message": "Products added to cart successfully.",
            "status": True
        }

    except Exception as e:
        print(f"An error occurred while adding to cart: {str(e)}")
        return {
            "message": "An error occurred while adding to cart in database.",
            "status": False
        }



def remove_from_cart(user_products):
    """
    Removes items from user's cart.

    Rules:
    - quantity == None  → remove entire product
    - quantity > 0      → remove that many
    - quantity >= existing → remove entire product
    """

    try:
        db = client[DB_NAME]
        collection = db[CART_COLLECTION]

        user_id = session.get("user_info")
        if not user_id:
            return {
                "message": "User not found in session.",
                "status": False
            }

        user_obj_id = ObjectId(user_id)

        existing_cart = collection.find_one({"user": user_obj_id})
        if not existing_cart or not existing_cart.get("items"):
            return {
                "message": "No cart found for user.",
                "status": False
            }

        # 🔥 If empty input → clear entire cart
        if not user_products:
            collection.update_one(
                {"user": user_obj_id},
                {"$set": {"items": []}}
            )
            return {
                "message": "All items removed from cart successfully.",
                "status": True
            }

        all_products = find_products()

        for user_item in user_products:
            product_name = user_item.get("product", "").strip().lower().replace(" ", "")
            raw_qty = user_item.get("quantity")

            # ✅ Quantity handling
            qty = raw_qty if isinstance(raw_qty, int) and raw_qty > 0 else None

            # 🔍 Find product ID
            product_id = None
            for p in all_products:
                if p["productName"].strip().lower().replace(" ", "") == product_name:
                    product_id = ObjectId(p["_id"])
                    break

            if not product_id:
                continue  # Skip unknown products

            # 🔍 Find item in cart
            cart_item = next(
                (x for x in existing_cart["items"] if x["product"] == product_id),
                None
            )

            if not cart_item:
                continue

            current_qty = cart_item.get("quantity", 0)

            # ❌ Remove entire product
            if qty is None or current_qty <= qty:
                collection.update_one(
                    {"user": user_obj_id},
                    {"$pull": {"items": {"product": product_id}}}
                )
            else:
                # ➖ Reduce quantity
                collection.update_one(
                    {
                        "user": user_obj_id,
                        "items.product": product_id
                    },
                    {
                        "$inc": {"items.$.quantity": -qty}
                    }
                )

        return {
            "message": "Selected products removed from cart successfully.",
            "status": True
        }

    except Exception as e:
        print("Remove cart error:", str(e))
        return {
            "message": "An error occurred while removing items from the cart.",
            "status": False
        }
