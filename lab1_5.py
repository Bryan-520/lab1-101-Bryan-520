def check_multiple(number: int) -> bool: 
    return number % 3 == 0 and number % 5 == 0

def check_password(input_string: str) -> str:
    secret = "password"
    if input_string == secret:
        return "access granted"
    else:
        return "access denied"

def calculate_federal_tax(salary: float) -> float:
    if salary <= 11000:
        return salary * 0.10
    elif salary <= 44725:
        return salary * 0.12
    elif salary <= 95375:
        return salary * 0.22
    else:
        return salary * 0.24