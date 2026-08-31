def get_square_color(s: str) -> str:
    # Map letters 'a' through 'h' to numbers 1 through 8
    col_map = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8
    }
    
    # Normalize input: trim whitespace and convert uppercase to lowercase ('B4' -> 'b4')
    s = s.strip().lower()
    
    # Validation Rules:
    # 1. Input String Length must be exactly 2 char.
    # 2. First char must exist in our dictionary ('a'-'h')
    # 3. Second char must be a row digit ('1'-'8')
    if len(s) != 2 or s[0] not in col_map or not ('1' <= s[1] <= '8'):
        return "Incorrect input"
    
    # Extract mapped column value and row integer
    col = col_map[s[0]]
    row = int(s[1])
    
    # Even sum = Black, Odd sum = White
    return "Black" if (col + row) % 2 == 0 else "White"

# Execution
user_input = input("Enter square (e.g. a1): ")
print(get_square_color(user_input))