
def add_tax(price, rate=0.15):
    Calculate price with tax included.
    
    Parameters:
    - price: Original price
    - rate: Tax rate (default: 0.15 = 15%)
    
    Returns:
    - Price with tax included
    tax = price * rate
    total = price + tax
    return total

if __name__ == "__main__":
    print("Testing add_tax function:")
    print(f"Price $100 with 15% tax: ${add_tax(100):.2f}")
    print(f"Price $200 with 10% tax: ${add_tax(200, 0.10):.2f}")
