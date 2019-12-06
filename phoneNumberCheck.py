def isPhoneNumber(text): # 415-555-1234
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False # missing dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me 412-222-3212 tomarrow, or at 123-343-2332 so that i can know that you are coming'
foundNumber = False
for i in range(len(message)):
    chunk = message[i: i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' +chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')

        
    
    
        
