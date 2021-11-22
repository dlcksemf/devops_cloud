def tax_cal(price):
    tax = price // 11
    return tax


tax = tax_cal(20000)
print(f"부가세 : {tax}")
