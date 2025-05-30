import re
from typing import Dict, Optional

US_STATE_ABBREVIATIONS = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
}

def parse_address(address: str, country: str = 'US') -> Optional[Dict[str, str]]:
    """
    Robust parser handling both comma and space separated addresses
    """
    # Match state and ZIP at the end
    pattern = r'''
        ^\s*
        (?P<address_part>.*?)          # Street + city
        [,\s]*                         # Consume trailing commas/spaces before state
        (?P<state>[A-Za-z]{2})         # State (2 letters)
        \s+                            # Required space
        (?P<zip>\d{5}(?:-\d{4})?)      # ZIP
        \s*$
    '''
    match = re.match(pattern, address, re.IGNORECASE | re.VERBOSE)
    if not match:
        return None
    
    state = match.group('state').upper()
    if state not in US_STATE_ABBREVIATIONS:
        return None
    
    # Split address_part into street/city
    address_part = match.group('address_part').strip()
    if ',' in address_part:
        street, city = map(str.strip, address_part.rsplit(',', 1))
        city = city.strip().rstrip(',')
    else:
        # Split on last space if no comma
        parts = address_part.rsplit(' ', 1)
        street = parts[0] if len(parts) > 1 else ''
        city = parts[-1] if len(parts) > 1 else address_part

    return {
        'street': street,
        'city': city,
        'state': state,
        'zip': match.group('zip')
    }

def standardize_address(address: str, country: str = 'US') -> Optional[str]:
    parsed = parse_address(address, country)
    if not parsed:
        return None

    street = re.sub(r'\s+', ' ', parsed['street'].strip()).title()
    city = parsed['city'].strip().title()
    state = parsed['state'].upper()
    zip_code = parsed['zip']

    return f"{street}, {city}, {state} {zip_code}"

def validate_address(address: str, country: str = 'US') -> bool:
    """
    Validate address structure and state abbreviation
    """
    parsed = parse_address(address, country)
    if not parsed:
        return False
    return True

