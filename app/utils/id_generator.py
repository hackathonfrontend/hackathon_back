import random
import string

def generate_random_alphanumeric_id(length: int = 5) -> str:
    """Generates a random alphanumeric ID of a given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_random_numeric_id(length: int = 5) -> int:
    """Generates a random numeric ID of a given length."""
    range_start = 10**(length-1)
    range_end = 10**length - 1
    return random.randint(range_start, range_end)

# Specific generator for manga room to allow for future customization if needed
def generate_manga_room_id() -> int:
    return generate_random_numeric_id(length=5)
