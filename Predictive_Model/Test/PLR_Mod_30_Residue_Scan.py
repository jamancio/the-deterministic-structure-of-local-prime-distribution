import sys

# ==============================================================================
# PLR MOD 30 RESIDUE SCANNER
#
# GOAL:
# Test the hypothesis: "Skip candidate if its Mod 30 residue indicates composite."
#
# LOGIC:
# 1. Start at p_n.
# 2. Iterate gaps (2, 4, 6...).
# 3. Calculate Residue R = candidate % 30.
# 4. IF R is in {1, 7, 11, 13, 17, 19, 23, 29}:
#       -> STOP and PREDICT (This is a "Potential Prime").
#    ELSE:
#       -> SKIP (This is definitely Composite).
# ==============================================================================

def is_prime_utility(n):
    """Truth label only."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def mod30_residue_scan():
    TEST_PRIMES = [
      5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
      41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
      83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
      139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
      193, 197, 199, 211, 223, 227, 229,
      233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
    ]
    
    # The set of residues that CANNOT be divided by 2, 3, or 5.
    # Any number with a different residue is GUARANTEED composite.
    PRIME_RESIDUES = {1, 7, 11, 13, 17, 19, 23, 29}

    print(f"{'PRIME':<6} | {'GAP':<4} | {'CANDIDATE':<10} | {'MOD 30':<8} | {'ACTION':<20} | {'TRUTH'}")
    print("="*85)

    for p_n in TEST_PRIMES:
        true_next = 0
        curr = p_n + 2
        while True:
            if is_prime_utility(curr):
                true_next = curr
                break
            curr += 2

        print(f"\n[ Testing p = {p_n} ]")

        gap = 2
        while True:
            candidate = p_n + gap
            residue = candidate % 30
            
            # --- THE NEW LOGIC ---
            if residue in PRIME_RESIDUES:
                action = "SELECT (Clean Residue)"
                truth = is_prime_utility(candidate) and "PRIME" or "Composite"
                
                print(f"{p_n:<6} | +{gap:<3} | {candidate:<10} | {residue:<8} | {action:<20} | {truth}")
                
                # Check if we won or failed
                if candidate == true_next:
                    print(f">>> SUCCESS: Stopped at True Prime.")
                else:
                    print(f">>> FAILURE: Stopped at Imposter {candidate} (Residue {residue} mimics prime).")
                break
            else:
                action = "SKIP (Dirty Residue)"
                truth = "Composite" # Guaranteed
                print(f"{p_n:<6} | +{gap:<3} | {candidate:<10} | {residue:<8} | {action:<20} | {truth}")
            
            gap += 2
            if gap > 50: break

if __name__ == "__main__":
    mod30_residue_scan()