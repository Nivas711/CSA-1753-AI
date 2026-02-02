def vacuum_agent(location, A, B):
    actions = []
    
    while A == "Dirty" or B == "Dirty":
        if location == 'A':
            if A == "Dirty":
                A = "Clean"
                actions.append("Suck A")
            else:
                location = 'B'
                actions.append("Move Right")
        elif location == 'B':
            if B == "Dirty":
                B = "Clean"
                actions.append("Suck B")
            else:
                location = 'A'
                actions.append("Move Left")
    
    return actions

# Initial state
location = 'A'
A = "Dirty"
B = "Dirty"

result = vacuum_agent(location, A, B)

print("Actions taken:")
for step in result:
    print(step)
