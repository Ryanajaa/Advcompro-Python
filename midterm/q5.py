def select_flash_sale_products(products):
	criteria = [(f"{products[i]["product_name"].upper()}: ${products[i]["product_price"]}") for i in range (0,len(products)) if (products[i]["product_price"] > 20 and products[i]["shop_rating"] >= 4.5)]
	return criteria
products = [
	{"product_name": "Widget", "product_price": 25, "shop_rating": 4.7},
	{"product_name": "Gadget", "product_price": 15, "shop_rating": 4.8},
	{"product_name": "Thingamajig", "product_price": 35, "shop_rating": 4.2},
	{"product_name": "Doodad", "product_price": 45, "shop_rating": 4.9}
]

print(select_flash_sale_products(products))