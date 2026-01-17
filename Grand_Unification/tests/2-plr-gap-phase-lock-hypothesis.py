import pandas as pd

def get_primorial_residues(n, p_limit):
    """
    Calculates the residues of n against the primorial system up to p_limit.
    """
    primes = [2, 3, 5, 7, 11, 13]
    residues = {}
    for p in primes:
        if p > p_limit: break
        residues[p] = n % p
    return residues

def check_forward_radar(start_n, lookahead, basis_primes):
    """
    Scans forward from start_n to see which spots are structurally open (Vacuum).
    """
    results = []
    
    for step in range(2, lookahead + 2, 2): # Check only even steps (since prime+odd=even)
        candidate = start_n + step
        
        # Check specific modular layers
        is_mod30_clean = (candidate % 2 != 0) and (candidate % 3 != 0) and (candidate % 5 != 0)
        is_mod210_clean = is_mod30_clean and (candidate % 7 != 0)
        is_mod2310_clean = is_mod210_clean and (candidate % 11 != 0)
        
        # Check if it's ACTUALLY prime (Ground Truth)
        is_real_prime = True
        for p in range(2, int(candidate**0.5) + 1):
            if candidate % p == 0:
                is_real_prime = False
                break
        
        # Determine Status
        status = "BLOCKED"
        if is_real_prime:
            status = "TARGET (PRIME)"
        elif is_mod2310_clean: # It passed the local filters but failed later
            status = "IMPOSTER (Sniped)"
        elif is_mod210_clean:
             status = "Mod 210 Vac"
        elif is_mod30_clean:
             status = "Mod 30 Vac"
             
        results.append({
            "Step (+g)": step,
            "Candidate": candidate,
            "Mod 30": "OPEN" if is_mod30_clean else "X",
            "Mod 210": "OPEN" if is_mod210_clean else "X",
            "Mod 2310": "OPEN" if is_mod2310_clean else "X",
            "Actual Status": status
        })
        
    return pd.DataFrame(results)

# --- CONFIGURATION ---
start_prime = 10799
lookahead_range = 40  # Look 40 steps ahead (enough to cover the 32 gap)
basis = [2, 3, 5, 7, 11]

# Run the Radar
df = check_forward_radar(start_prime, lookahead_range, basis)

# Display just the potential landing spots (Clean Channel candidates)
print(f"--- Radar Scan from Prime {start_prime} ---")
print("Looking for the 'Gap-Phase Lock' at +32...")
print(df[df["Mod 30"] == "OPEN"]) # Show only spots that pass the basic filter