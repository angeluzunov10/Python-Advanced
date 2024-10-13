def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    text_to_print = ""
    products_bought = []
    for product, data in products.items():
        if len(products_bought) == 5:
            break
        if len(products) < 0:
            break
        (product_price, product_quantity) = data
        total_price = product_price * product_quantity
        if total_price < budget:
            budget -= total_price
            products_bought.append(product)
            text_to_print += f"You bought {product} for {total_price:.2f} leva.\n"
        else:
            continue
    return text_to_print


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10)))
