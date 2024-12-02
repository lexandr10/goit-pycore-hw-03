import re

def normalize_phone(phone_number):
    pattern = r"[^\d+]"
    clean_number = re.sub(pattern, '', phone_number.strip())
    match = re.search(r'(\+?)(\d{1,2})?(\d+)', clean_number)

    has_plus = match.group(1) == '+'  
    country_code = match.group(2)    
    main_number = match.group(3)     
    
   
    if has_plus and country_code == '38':
        return clean_number
    elif has_plus == False and country_code != '38': 
        return f'+38{clean_number}'
    else: return re.sub(r"^\+", "+38",clean_number) if has_plus else f'+{country_code}{main_number}'



raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)