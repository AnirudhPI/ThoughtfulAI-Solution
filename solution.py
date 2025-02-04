def sort(width, height, length, mass):
    volume = width * height * length
    
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"

test_cases = [
    (100, 100, 100, 10),  
    (200, 50, 50, 10),    
    (50, 50, 50, 30),     
    (200, 200, 200, 25),  
    (150, 149, 149, 19),  
    (149, 149, 149, 19),
]

for w, h, l, m in test_cases:
    print(f"sort({w}, {h}, {l}, {m}) -> {sort(w, h, l, m)}")
