"""
key-value pairs
"""

customer = {
    "name": "Shiv Shar",
    "age": 20,
    "is_verified": True
}
# note the keys should be unique

print(customer["name"])
# if the key is not present it will throw keyError :

try:
    print(customer["sex"])
except KeyError as e:
    print(f"KeyError : {e}")

print(customer.get("age"))

# get doesn't throw keyError , rather it gives None
print(customer.get("sex"))
