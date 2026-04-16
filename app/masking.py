import re

def mask(text):
    masked = text
    data = {}

    # Turkish ID Number (11 digits)
    tc_list = re.findall(r'\b\d{11}\b', masked)
    for i, tc in enumerate(tc_list):
        token = f'[TC_ID_{i+1}]'
        data[token] = tc
        masked = masked.replace(tc, token)

    # Phone number
    phone_list = re.findall(r'(\+90|0)?\s*[\(\[]?\d{3}[\)\]]?\s*[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}', masked)
    for i, phone in enumerate(phone_list):
        token = f'[PHONE_{i+1}]'
        data[token] = phone
        masked = masked.replace(phone, token)

    # Email
    email_list = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', masked)
    for i, email in enumerate(email_list):
        token = f'[EMAIL_{i+1}]'
        data[token] = email
        masked = masked.replace(email, token)

    # License plate (e.g. 34 ABC 123)
    plate_list = re.findall(r'\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b', masked)
    for i, plate in enumerate(plate_list):
        token = f'[PLATE_{i+1}]'
        data[token] = plate
        masked = masked.replace(plate, token)

    # IBAN
    iban_list = re.findall(r'\bTR\d{2}\s?(\d{4}\s?){5}\d{2}\b', masked)
    for i, iban in enumerate(iban_list):
        token = f'[IBAN_{i+1}]'
        data[token] = iban
        masked = masked.replace(iban, token)

    return masked, data
