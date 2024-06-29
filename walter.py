product_color = ""
price_per_packet = 0

def cook(color, price):
    product_color = color
    price_per_packet = price

def say_my_name():
    return "Heisenberg"

def sell():
    return f'{product_color} colored - sold {price_per_packet}$ per ounce'

cook("blue", 40000)
print(sell())
print(say_my_name())
