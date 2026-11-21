subscriptions = {}

while True:
    name = input("Subscription name (or 'done'): ")
    if name == "done":
        break
    cost = float(input(f"Monthly cost of {name}: $"))
    subscriptions[name] = cost

monthly_total = sum(subscriptions.values())
print(f"\nMonthly: ${monthly_total:.2f}")
print(f"Yearly:  ${monthly_total * 12:.2f}")

priciest = max(subscriptions, key=subscriptions.get)
print(f"Most expensive: {priciest} (${subscriptions[priciest]:.2f}/mo)")
