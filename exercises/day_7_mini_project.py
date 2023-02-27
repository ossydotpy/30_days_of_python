# accept user input, covert into a lis and delete any leading or ending whitesapce.
card = list(input("""Please input your credit card number for validation.
*WARNING: DO NOT LEAVE SPACES BETWEEN/BEFORE/AFTER NUMBERS\n>>>""")).strip()

# remove the last digit
checking_digit =  card.pop()

# reverse the items in the list
card = card.reverse()

processed = []

for index, num in enumerate(card):
    if index%2 == 0:
        doubled_num = int(num)*2
        if doubled_num >9:
            doubled_num = doubled_num-9
        processed.append(doubled_num)
    else:
        processed.append(int(num))

total = int(checking_digit)+sum(processed)

if total%10 == 0:
    print("valid credit card number!")
else:
    print("sorry you entered an invalid card number!")