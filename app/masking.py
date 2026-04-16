import re

def maskele(metin):
    original = metin
    masked = metin
    veri = {}

    # TC Kimlik No (11 hane)
    tcno_list = re.findall(r'\b\d{11}\b', masked)
    for i, tcno in enumerate(tcno_list):
        token = f'[TCNO_{i+1}]'
        veri[token] = tcno
        masked = masked.replace(tcno, token)

    # Telefon numarası
    tel_list = re.findall(r'(\+90|0)?\s*[\(\[]?\d{3}[\)\]]?\s*[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}', masked)
    for i, tel in enumerate(tel_list):
        token = f'[TEL_{i+1}]'
        veri[token] = tel
        masked = masked.replace(tel, token)

    # E-posta
    email_list = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', masked)
    for i, email in enumerate(email_list):
        token = f'[EMAIL_{i+1}]'
        veri[token] = email
        masked = masked.replace(email, token)

    # Plaka (örn: 34 ABC 123)
    plaka_list = re.findall(r'\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b', masked)
    for i, plaka in enumerate(plaka_list):
        token = f'[PLAKA_{i+1}]'
        veri[token] = plaka
        masked = masked.replace(plaka, token)

    # IBAN
    iban_list = re.findall(r'\bTR\d{2}\s?(\d{4}\s?){5}\d{2}\b', masked)
    for i, iban in enumerate(iban_list):
        token = f'[IBAN_{i+1}]'
        veri[token] = iban
        masked = masked.replace(iban, token)

    return masked, veri
