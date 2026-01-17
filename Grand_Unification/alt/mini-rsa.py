import time
import random

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def generate_semiprime(bits):
    """Generates a semiprime N = p * q with 'bits' size."""
    while True:
        p = random.getrandbits(bits // 2)
        if is_prime(p):
            break
    while True:
        q = random.getrandbits(bits // 2)
        if is_prime(q) and p != q:
            break
    return p * q, p, q

def brute_force_attack(N):
    """Standard attack: Checks every odd number."""
    checks = 0
    start_time = time.time()
    
    # Start checking from 3, steps of 2
    limit = int(N**0.5) + 1
    for d in range(3, limit, 2):
        checks += 1
        if N % d == 0:
            return d, checks, time.time() - start_time
    return None, checks, time.time() - start_time

def plr_vacuum_attack(N):
    """PLR Attack: Checks only Mod 30 Clean Channel."""
    checks = 0
    start_time = time.time()
    
    # The 8 clean residues in Mod 30
    # We skip 22 out of every 30 numbers (73.3% reduction)
    clean_residues = [1, 7, 11, 13, 17, 19, 23, 29]
    gap_pattern = [6, 4, 2, 4, 2, 4, 6, 2] # Distances between residues
    
    limit = int(N**0.5) + 1
    d = 7 # Start at first non-trivial residue
    gap_idx = 0
    
    while d < limit:
        checks += 1
        if N % d == 0:
            return d, checks, time.time() - start_time
        
        # Jump to next Clean Channel spot
        d += gap_pattern[gap_idx]
        gap_idx = (gap_idx + 1) % 8
        
    return None, checks, time.time() - start_time

# --- RUN THE BATTLE ---
# Generate a 40-bit Key (approx 1 Trillion)
# This is small enough for a quick test, but large enough to see the gap.
key_size = 40
print(f"Generating {key_size}-bit RSA Key...")
target_N, real_p, real_q = generate_semiprime(key_size)
print(f"Target N: {target_N} (Factors: {real_p} * {real_q})")
print("-" * 50)

# Run Brute Force
print("Running Brute Force Attack...")
bf_factor, bf_checks, bf_time = brute_force_attack(target_N)
print(f"Brute Force Found: {bf_factor}")
print(f"Checks Needed: {bf_checks:,}")
print(f"Time Taken: {bf_time:.4f}s")
print("-" * 50)

# Run PLR Vacuum Attack
print("Running PLR Vacuum Attack (Mod 30)...")
plr_factor, plr_checks, plr_time = plr_vacuum_attack(target_N)
print(f"PLR Vacuum Found: {plr_factor}")
print(f"Checks Needed: {plr_checks:,}")
print(f"Time Taken: {plr_time:.4f}s")

# Calculate The Advantage
savings = 100 * (1 - (plr_checks / bf_checks))
speedup = bf_checks / plr_checks
print("-" * 50)
print(f"PLR ADVANTAGE REPORT:")
print(f"Search Space Removed: {savings:.2f}%")
print(f"Speedup Factor: {speedup:.2f}x Faster")