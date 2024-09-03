def apply_discount(product_prices):
    final_price = [(i * 90/100 if i > 100 else i * 95/100) for i in product_prices]
    return(final_price)

product_prices = [120, 80, 150, 60]
print(apply_discount(product_prices))