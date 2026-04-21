import re

def mask(text):
    masked = text
    data = {}

    # Turkish ID Number (11 digits)
    for i, tc in enumerate(re.findall(r'\b\d{11}\b', masked)):
        token = f'[TC_ID_{i+1}]'
        data[token] = tc
        masked = masked.replace(tc, token)

    # Phone number
    for i, phone in enumerate(re.findall(r'\+90\d{10}|0\d{3}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}', masked)):
        token = f'[PHONE_{i+1}]'
        data[token] = phone
        masked = masked.replace(phone, token)

    # Email
    for i, email in enumerate(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', masked)):
        token = f'[EMAIL_{i+1}]'
        data[token] = email
        masked = masked.replace(email, token)

    # License plate
    for i, plate in enumerate(re.findall(r'\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b', masked)):
        token = f'[PLATE_{i+1}]'
        data[token] = plate
        masked = masked.replace(plate, token)

    # IBAN
    for i, iban in enumerate(re.findall(r'\bTR\d{24}\b', masked)):
        token = f'[IBAN_{i+1}]'
        data[token] = iban
        masked = masked.replace(iban, token)

    return masked, data
