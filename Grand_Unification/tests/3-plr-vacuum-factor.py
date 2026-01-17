import pandas as pd

def get_prime_factors(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

def check_vacuum_hypothesis(composites, mod_level):
    results = []
    
    for N in composites:
        # 1. Verify N is in the Vacuum (Clean Channel) for this Mod Level
        # (It must be coprime to the primorial to be a "Vacuum Imposter")
        primes_in_mod = [2, 3, 5, 7, 11] # Simplified basis
        is_N_clean = True
        for p in primes_in_mod:
            if p >= mod_level: break
            if N % p == 0: 
                is_N_clean = False # It's not an imposter, just a messy composite
                break
        
        if not is_N_clean: continue # Skip standard composites
        
        # 2. Find Factors
        factors = get_prime_factors(N)
        
        # 3. Test if Factors are ALSO in the Vacuum
        all_factors_clean = True
        failed_factor = None
        
        for f in factors:
            # Check if factor 'f' is coprime to the basis
            for p in primes_in_mod:
                if p >= mod_level: break
                if f % p == 0:
                    all_factors_clean = False
                    failed_factor = f
                    break
        
        results.append({
            "Composite (N)": N,
            "Mod Level": f"Mod {mod_level}",
            "Factors": factors,
            "Are Factors Clean?": "YES" if all_factors_clean else "NO",
            "Search Space Savings": "Skipped ~77.1%" if all_factors_clean else "None"
        })
        
    return pd.DataFrame(results)

# --- CONFIGURATION ---
# Let's test "Imposters" - numbers that are not divisible by 2, 3, 5, 7
# Examples: 121 (11*11), 169 (13*13), 289 (17*17), 10807 (from our last test)
test_composites = [121, 143, 169, 221, 289, 323, 10807, 10837] # 10837 is prime, let's see logic
mod_basis = 30 # Test against Mod 30 rules first

df = check_vacuum_hypothesis(test_composites, mod_basis)
print(f"--- The Vacuum Factor Test (Mod {mod_basis}) ---")
print(df)