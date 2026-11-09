# Reflection
# 1. I would use .get() if the key might not exist because it will still allow the program to run, therefore it
# wont create any more errors. If I know the key exists, then I would use braket notation to get the key's value.

# 2. This exercise reminds me of how you can sort data into categories and add them up. Python is useful when you
# have a large amount of data because it can automatically go through a lot of data and add them up without having
# to do everything manually


print("--Exercise 1--")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"]) # Accessing value using bracket notation
print(customer["email"]) # Accessing value using bracket notation
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# --- Exercise 2 : Update eand add---
print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email","Email not found"))

print("--- Exercise 3---")

#New version
print(customer.get("email","no email on file")) 

# # Older version (still used in some codebases)
try:
    print(customer["email"]) #using bracket notation, which raises 
except KeyError as error:
    print(f"KeyError Caught:error")

print("--- Exercise 4---")
for key, value in customer.items():
    print(f"Key {key} : {value}")

# Without .items(), the loop only prints the keys, not the values.
for item in customer:
    print(item)

print("--- Exercise 5---")
tier_discounts = {"bronze" : 0,
                  "silver" : 0.05,
                  "gold": 0.10,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")  # platinum
print(f"Discount: {discount_rate * 100:.0f}%")  # 15%
print(f"Final price: ${final_price:.2f}")  # $170.00
      

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate  # assuming a purchase of $300 for each customer
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

print("--- Exercise 7---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("---Exercise 8---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
sales_by_region = {} #empty dictionary to hold sales total by region
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")