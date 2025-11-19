'''
Implement a function that accepts product detail like name, price and quantity using **kwargs.
- return a formatted string showing the total cost of all products.
'''

def product_details(**kwargs):
    name = kwargs.get('name')
    price = kwargs.get('price')
    quantity = kwargs.get('quantity')

    if name is None or price is None or quantity is None:
        return "Missing product details!"

    total_cost = price * quantity
    return f"Product: {name}\nPrice: {price}\nQuantity: {quantity}\nTotal Cost: {total_cost}"

# Example call
print(product_details(name="Laptop", price=50000, quantity=2))