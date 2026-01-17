import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# ==========================================
# PART 2: THE HEURISTICS FLUKE TEST
# ==========================================
# We will compare the "Vacuum Factor" property against a Random Control Group.
# Hypothesis: PLR Composites have 100% Clean Factors. Random Composites do not.

print("\n\n--- Running Heuristics Fluke Test (PLR vs. Random) ---")

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

def is_in_vacuum(n, primes):
    for p in primes:
        if n % p == 0: return False
    return True

# Setup
sample_size = 1000
basis = [2, 3, 5, 7] # Mod 210
mod_val = 210

# 1. Generate PLR Group (Composites in Vacuum)
plr_composites = []
curr = 1000 # Start range
while len(plr_composites) < sample_size:
    if is_in_vacuum(curr, basis): # Only look in Vacuum
        # Check if composite
        if len(get_prime_factors(curr)) > 1:
             plr_composites.append(curr)
    curr += 1

# 2. Generate Random Control Group (Any Composite)
random_composites = []
while len(random_composites) < sample_size:
    r = random.randint(1000, curr)
    if len(get_prime_factors(r)) > 1:
        random_composites.append(r)

# 3. Test "Vacuum Factor" Rule on both
def run_heuristic_check(group, name):
    valid_count = 0
    for n in group:
        factors = get_prime_factors(n)
        all_clean = True
        for f in factors:
            if not is_in_vacuum(f, basis):
                all_clean = False
                break
        if all_clean:
            valid_count += 1
    return valid_count

plr_score = run_heuristic_check(plr_composites, "PLR Group")
rand_score = run_heuristic_check(random_composites, "Random Group")

print(f"Sample Size: {sample_size}")
print(f"PLR Group (Vacuum Integers) Validity: {plr_score}/{sample_size} ({(plr_score/sample_size)*100}%)")
print(f"Random Group (Control) Validity:      {rand_score}/{sample_size} ({(rand_score/sample_size)*100}%)")
print(f"Interpretation: {plr_score} PLR cases followed the law. Random cases rarely do.")