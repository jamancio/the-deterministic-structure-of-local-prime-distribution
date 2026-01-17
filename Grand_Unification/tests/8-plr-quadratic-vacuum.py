import pandas as pd

def get_gaussian_plr_map(start, count):
    """
    Maps the intersection of the PLR Vacuum (Mod 30) 
    and the Gaussian Vacuum (Mod 4).
    """
    results = []
    n = start
    while len(results) < count:
        # 1. Standard PLR Check (Clean Channel)
        is_plr_clean = (n % 2 != 0 and n % 3 != 0 and n % 5 != 0)
        
        # 2. Gaussian Check (Fermat's Rule: 1 mod 4)
        gaussian_status = "Quadratic Prime (1 mod 4)" if n % 4 == 1 else "Inert (3 mod 4)"
        
        # 3. Sum of Squares search
        sum_of_squares = None
        limit = int(n**0.5) + 1
        for x in range(1, limit):
            y_sq = n - x**2
            y = int(y_sq**0.5)
            if y**2 == y_sq:
                sum_of_squares = f"{x}^2 + {y}^2"
                break
        
        if is_plr_clean:
            results.append({
                "Number |": n,
                "PLR | ": "Vacuum",
                "Gaussian |": gaussian_status,
                "Sum_of_Squares": sum_of_squares if sum_of_squares else "BLOCKADE"
            })
        n += 1
    return pd.DataFrame(results)

# Run for first 15 Vacuum numbers
df = get_gaussian_plr_map(1, 15)
print(df.to_string(index=False))