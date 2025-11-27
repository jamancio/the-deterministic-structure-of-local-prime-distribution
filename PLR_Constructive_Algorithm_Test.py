import sys
import math

# ==============================================================================
# PLR CONSTRUCTIVE ALGORITHM: f(N) -> p_next
#
# GOAL:
# Demonstrate the "Magic Formula" approach.
# Input ANY number N.
# Construct the Next Prime using purely Geometric Exclusion.
# ==============================================================================

def get_prime_bank(limit):
    """Generates the 'Map' of structural filters up to limit."""
    # Standard Sieve of Eratosthenes for initialization
    sieve = [True] * (limit + 1)
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p*p, limit + 1, p):
                sieve[i] = False
    return [p for p in range(2, limit + 1) if sieve[p]]

def is_prime_standard(n):
    """Standard Trial Division for TRUTH verification only."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def PLR_Construct_Next_Prime(start_number, verbose=True):
    """
    The Constructive Function f(N).
    Finds the next prime after start_number using Recursive Geometric Filtering.
    """
    # 1. ESTABLISH KNOWLEDGE BASE
    # To predict up to N, we need filters up to sqrt(N + gap_buffer).
    # We estimate a small buffer for the gap.
    root_limit = int((start_number + 200)**0.5) + 5
    filters = get_prime_bank(root_limit)
    
    if verbose:
        print(f"\n[INPUT] N = {start_number}")
        print(f"[SETUP] Loaded {len(filters)} Structural Filters (Max Filter: {filters[-1]})")
        print(f"[SETUP] Safe Horizon: {filters[-1]}^2 = {filters[-1]**2}")

    # 2. INITIALIZE SCAN
    # Start checking from the next odd number
    candidate = start_number + 1 if start_number % 2 == 0 else start_number + 2
    
    while True:
        # --- THE CONSTRUCTIVE STEP (Applying Rules) ---
        is_structurally_valid = True
        rejection_reason = ""
        
        # Rule 1: Base Mod 6 Geometry (The "Clean Channel")
        # (Optimized: We only check 2 and 3 explicitly if not in bank, 
        # but usually we iterate filters. Let's use the Filter Bank approach).
        
        for p in filters:
            # SELF-FACTOR EXCLUSION RULE:
            # Reject if divisible by p AND candidate != p
            if candidate % p == 0:
                if candidate == p:
                    continue # It is the prime itself (Valid)
                else:
                    is_structurally_valid = False
                    # Optional: Capture reason for the "Imposter" log
                    if verbose and candidate % 6 != 0 and candidate % 5 != 0: 
                        # Only log interesting imposters (not simple 2,3,5 multiples)
                        rejection_reason = f"Divisible by {p}"
                    break
        
        # --- DECISION ---
        if is_structurally_valid:
            # If it survived all filters, it IS the prime (within Horizon).
            return candidate
        
        else:
            # Forensic Logging for "Difficult" Imposters
            if verbose and rejection_reason:
                 print(f"   -> Skipped Imposter {candidate:<6} [{rejection_reason}]")

        candidate += 2

# --- TESTING THE ALGORITHM ---
def run_random_tests():
    test_points = [
        100,        # Low range
        1000,       # Mid range
        5000,       # Mod 30030 range
        100000,     # High range
        1000000     # 1 Million range
    ]
    
    print(f"{'INPUT (N)':<10} | {'CONSTRUCTED PRIME':<20} | {'TRUTH CHECK':<15}")
    print("="*60)
    
    for n in test_points:
        # Run the Function
        constructed_p = PLR_Construct_Next_Prime(n, verbose=False)
        
        # Verify Truth
        is_valid = is_prime_standard(constructed_p)
        status = "PASS" if is_valid else "FAIL"
        
        print(f"{n:<10} | {constructed_p:<20} | {status:<15}")

    print("="*60)
    print("Specific Forensic Test on a Known Imposter Zone (around 120):")

    result = PLR_Construct_Next_Prime(412524523623525, verbose=True)
    
    print("-" * 60)
    print(f"CONSTRUCTED PRIME: {result}")
    print("="*60)

if __name__ == "__main__":
    run_random_tests()