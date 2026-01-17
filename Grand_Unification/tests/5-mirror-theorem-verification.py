import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# ==========================================
# PART 1: THE MIRROR THEOREM VERIFICATION
# ==========================================

def get_messiness_score(n, basis_primes):
    """
    Calculates a 'Structural Resistance' score based on divisibility.
    Higher score = More Messy (divisible by small primes).
    """
    score = 0
    for p in basis_primes:
        if n % p == 0:
            score += 1/p # Weight by size of prime (1/2 is messier than 1/5)
    return score

def verify_primorial_mirror(mod_level_primes):
    """
    Verifies if Score(x) == Score(P# - x)
    """
    P_hash = 1
    for p in mod_level_primes:
        P_hash *= p
        
    print(f"\n--- Verifying Mirror Symmetry for P# = {P_hash} ---")
    
    mirror_failures = 0
    x_vals = []
    scores_forward = []
    scores_backward = []
    
    # Check half the range (symmetry axis)
    half_range = P_hash // 2
    
    for x in range(1, half_range + 1):
        mirror_x = P_hash - x
        
        s1 = get_messiness_score(x, mod_level_primes)
        s2 = get_messiness_score(mirror_x, mod_level_primes)
        
        x_vals.append(x)
        scores_forward.append(s1)
        scores_backward.append(s2)
        
        if abs(s1 - s2) > 1e-9: # Float tolerance
            mirror_failures += 1
            print(f"FAILURE at {x} vs {mirror_x}: {s1} != {s2}")
            
    if mirror_failures == 0:
        print(f"SUCCESS: Perfect Symmetry confirmed for all {half_range} pairs.")
    else:
        print(f"FAIL: Found {mirror_failures} asymmetries.")
        
    return x_vals, scores_forward, scores_backward, P_hash

# Run Mirror Test for Mod 30 (Visual) and Mod 210 (Rigorous)
x_30, f_30, b_30, P30 = verify_primorial_mirror([2, 3, 5])
verify_primorial_mirror([2, 3, 5, 7]) # Mod 210

# Visualize Mod 30 Symmetry
plt.figure(figsize=(10, 5))
plt.plot(x_30, f_30, label='Forward (x)', linewidth=3, alpha=0.7)
plt.plot(x_30, b_30, label='Backward (30-x)', linestyle='--', linewidth=2, color='red')
plt.title(f"The Primorial Mirror: Symmetry of Structural Resistance (Mod {P30})")
plt.xlabel("Distance from Anchor (0 to 15)")
plt.ylabel("Messiness Score")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('mirror_symmetry_test.png')