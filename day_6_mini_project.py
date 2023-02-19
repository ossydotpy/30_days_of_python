print("""
Welcome to noob's online CC validator
""")
card_number =  input("""Please input your credit card number for validation.
*WARNING: DO NOT LEAVE SPACES BETWEEN/BEFORE/AFTER NUMBERS\n>>>
""")

numbers = list(card_number)
popped = numbers.pop()
numbers.reverse()

processed = []

for index, num in enumerate(numbers):
    if index%2 ==0:
        doubled = int(num)*2
        if doubled >9:
            doubled = doubled-9
        processed.append(doubled)
    else:
        processed.append(int(num))

total = int(popped)+sum(processed)

if total%10 == 0:
    print("valid credit card number!")
else:
    print("sorry you entered an invalid card number!")