

def fee_calculator(amount):
    service_fee = 17
    if amount.isdigit():
        if amount[-3:] == "000":
            if len(amount) == 5:
                if amount == "50000":
                    return "300"
                elif amount == "24000":
                    return "400"
                elif amount == "18000":
                    return "300"
                elif amount == "12000":
                    return "200"
                else:
                    return str(service_fee*int(amount[0:2]))
            elif len(amount) == 4:
                if amount == "6000":
                    return "100"
                elif amount == "3000":
                    return "50"
                elif amount == "9000":
                    return "150"
                else:
                    return str(service_fee*int(amount[0]))
            else:
                return "amount is too little or too much"
        else:
            return "Amount must be in thousands"
    else:
        return "Amount must be an integer"

print(fee_calculator("5000"))
print(fee_calculator("6000"))
print(fee_calculator("50000"))
print(fee_calculator("24000"))
print(fee_calculator("12000"))
print(fee_calculator("8000"))
