client = ""
amount = 0

def add_client(client_name, money_paid):
    client = client_name
    amount = money_paid

def better_call_saul():
    return f'{client}, Better Call Saul\n and pay {amount}$'

add_client("Kettleman", 25000)

print(better_call_saul())