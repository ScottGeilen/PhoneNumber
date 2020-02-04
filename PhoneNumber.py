phone_input = input('Type your phone number: ')

def slicePhoneNumber(phone_input):
    slice_1 = phone_input[:3]
    slice_2 = phone_input[3:6]
    slice_3 = phone_input[6:10]
    slices = [slice_1, slice_2, slice_3]
    return slices

def addHyphens(phone_input):    
    area_code = phone_input[0]
    next_3 = phone_input[1]
    last_3 = phone_input[2]
    phone_number = []
    phone_number.append(area_code)
    phone_number.append(next_3)
    phone_number.append(last_3)
    new_phone = '-'.join(phone_number)
    return new_phone

phone_input = slicePhoneNumber(phone_input)
result = addHyphens(phone_input)
print(result)