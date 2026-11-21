subscriptions = {}

while True:
    name = input("Subscription name (or 'done'): ")
    if name == "done":
        break
    cost = float(input(f"Monthly cost of {name}: $"))
    subscriptions[name] = cost
    
    if subscriptions:
        monthly_total = sum(subscriptions.values())
        print(f"\nMonthly: ${monthly_total:.2f}")
        print(f"Yearly:  ${monthly_total * 12:.2f}")
        expensive = max(subscriptions, key=subscriptions.get)
        print(f"Most expensive: {expensive} (${subscriptions[expensive]:.2f}/mo)")
    else:
        print("No subscriptions entered. Exiting.")
