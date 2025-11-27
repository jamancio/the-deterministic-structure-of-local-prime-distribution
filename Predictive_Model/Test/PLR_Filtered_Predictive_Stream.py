import sys

# ==============================================================================
# PLR PREDICTIVE STREAM (FILTERED)
#
# GOAL:
# Simulate the "Predictive Model" view by REMOVING all candidates that fail
# the PLR Geometric Sieve.
#
# LOGIC:
# 1. Generate odd number gaps (2, 4, 6...).
# 2. Apply PLR Geometry.
# 3. IF REJECT: Skip entirely (Do not show). Record as "Noise Removed".
# 4. IF ACCEPT: Display as a valid "Prediction Candidate".
# 5. Compare with Truth only for forensic labeling.
# ==============================================================================

def is_prime_utility(n):
    """Used ONLY for the 'Truth' label. The model does not use this for filtering."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def filtered_predictive_stream():
    # Test Primes known to have "Imposters" nearby
    TEST_PRIMES = [
        5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
        83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
    ]
    
    # How many "Valid" candidates to show per prime?
    # We want to see the winner + the next few possibilities.
    SHOW_VALID_COUNT = 5 

    print(f"{'GAP':<4} | {'CANDIDATE':<10} | {'ANCHOR':<8} | {'PREDICTION STATUS':<20} | {'TRUTH':<10}")
    print("="*85)

    for p_n in TEST_PRIMES:
        print(f"\n[ PRIME: {p_n} ] generating filtered stream...")
        print("-" * 85)

        valid_candidates_found = 0
        noise_removed = 0
        gap = 2
        
        # We loop until we find enough VALID candidates
        while valid_candidates_found < SHOW_VALID_COUNT:
            candidate = p_n + gap
            anchor = p_n + candidate
            residue = anchor % 6
            
            # --- 1. THE GEOMETRIC SIEVE (The 77% Filter) ---
            is_geometrically_valid = False
            
            if gap % 6 == 0:
                # Gap 6, 12... allows Messy Anchor (Residue 2 or 4)
                if residue != 0: is_geometrically_valid = True
            else:
                # Gap 2, 4... allows Clean Anchor (Residue 0)
                if residue == 0: is_geometrically_valid = True

            # --- 2. FILTER ACTION ---
            if not is_geometrically_valid:
                # This candidate is impossible. REMOVE IT.
                noise_removed += 1
                gap += 2
                continue 

            # --- 3. DISPLAY SURVIVORS ---
            # If we are here, the number passed the sieve.
            # It is indistinguishable from a prime to the geometry.
            
            truth = "Composite"
            if is_prime_utility(candidate):
                truth = "PRIME"

            # Label the first valid one as the "Primary Prediction"
            status = "Candidate Option"
            if valid_candidates_found == 0:
                status = ">>> PRIMARY PREDICTION"
                if truth == "Composite":
                    status += " (FAIL)"
                else:
                    status += " (SUCCESS)"

            print(f"+{gap:<3} | {candidate:<10} | {residue:<8} | {status:<20} | {truth:<10}")

            valid_candidates_found += 1
            gap += 2
        
        # Stats for this prime
        total_scanned = valid_candidates_found + noise_removed
        reduction = (noise_removed / total_scanned) * 100
        print(f"... (Noise Removed: {noise_removed}/{total_scanned} | Sieve Efficiency: {reduction:.1f}%)")

    print("\n" + "="*85)
    print("ANALYSIS: The list above shows ONLY what the PLR Model 'sees'.")
    print("Notice that Composites (like 25, 35) appear as valid candidates.")

if __name__ == "__main__":
    filtered_predictive_stream()