products = (
    ("P101", "Laptop", 55000, 8),
    ("P102", "Mouse", 800, 25),
    ("P103", "Keyboard", 1500, 12),
    ("P104", "Monitor", 12000, 5),
    ("P105", "Webcam", 2500, 18)
)

def inventory_analysis(products):
    ids = []
    lowest_value = 10000000000
    lowest_product = ""

    print("Inventory Value of Each Product:")
    for p in products:
        value = p[2] * p[3]
        print(p[1], ":", value)

    print("\nProducts with Inventory Value > ₹20,000:")
    for p in products:
        value = p[2] * p[3]
        if value > 20000:
            ids.append(p[0])
            print(p[1], ":", value)
        if value < lowest_value:
            lowest_value = value
            lowest_product = p[1]

    print("\nProduct IDs:", ids)
    print("\nProduct with lowest Inventory Value:", lowest_product, "-", lowest_value)

inventory_analysis(products)