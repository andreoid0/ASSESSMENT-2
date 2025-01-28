money = 50  
usb_price = 6  

usb_count = money // usb_price

remaining_money = money % usb_price

print(f"She can buy {usb_count} USB sticks.")
print(f"She will have £{remaining_money} left.")