def sum_d(pin_digits):
    sum_digits = 0
    for k in pin_digits.keys() :
        sum_digits += pin_digits[k]
    return sum_digits





def pin_is_ok(pin_digits):
    if pin_digits['three'] + pin_digits['five'] == 14 and \
        pin_digits['one'] == pin_digits['two']*2 - 1 and \
            pin_digits['four'] == pin_digits['two'] + 1 and \
                pin_digits['two'] + pin_digits['three'] == 10:
                if sum_d(pin_digits) == 30:
                    return True




for pin in range(0, 100000):
    this_pin = str(pin).zfill(5)
    pin_digits ={}
    pin_digits['one'] = int(this_pin[0])
    pin_digits['two'] = int(this_pin[1])
    pin_digits['three'] = int(this_pin[2])
    pin_digits['four'] = int(this_pin[3])
    pin_digits['five'] = int(this_pin[4])
    if pin_is_ok(pin_digits):
            print(pin)