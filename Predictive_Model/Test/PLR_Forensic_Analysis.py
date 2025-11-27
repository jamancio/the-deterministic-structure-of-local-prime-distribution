import time

# ==============================================================================
# PLR FORENSIC ANALYSIS: THE BLIND SIEVE
#
# GOAL:
# Demonstrate the PLR selection logic WITHOUT a primality check.
#
# METHOD:
# 1. Take a prime p_n.
# 2. Generate generic candidates (p_n + 2, p_n + 4, p_n + 6...)
# 3. Apply Modulo-Phase Lock to ACCEPT or REJECT.
# 4. Stop at the first ACCEPTED candidate.
# 5. Compare with the TRUE prime to see if we found a Prime or a "Law I Failure".
# ==============================================================================

# Hardcoded primes for the forensic test (First 25)
PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113
]

def forensic_test():
    print("="*80)
    print(f"{'CURRENT (p)':<10} | {'GAP (g)':<8} | {'CANDIDATE':<10} | {'ANCHOR (Mod 6)':<15} | {'STATUS'}")
    print("="*80)

    for i in range(len(PRIMES) - 1):
        p_n = PRIMES[i]
        true_next = PRIMES[i+1]

        # SKIP p=2, 3 (Asymptotic Domain starts at p>3)
        if p_n <= 3: 
            continue

        print(f"\n[Testing p = {p_n}]")

        # --- THE BLIND GENERATOR ---
        # We don't know the next prime. We just guess odd numbers.
        gap = 2
        while True:
            candidate = p_n + gap
            anchor = p_n + candidate
            residue = anchor % 6
            
            # --- THE PLR GEOMETRIC FILTER ---
            # Rule 1: Clean Phase (Gap not div by 6) -> Must be Anchor 0
            # Rule 2: Messy Phase (Gap div by 6)     -> Must be Anchor 2 or 4
            
            status = "REJECT (Blocked)"
            is_accepted = False

            if gap % 6 == 0:
                # Gap is 6, 12, 18... MUST be Messy (Residue != 0)
                if residue != 0:
                    status = "ACCEPT (Geometric Fit)"
                    is_accepted = True
                else:
                    status = "REJECT (Clean Anchor)"
            else:
                # Gap is 2, 4, 8... MUST be Clean (Residue == 0)
                if residue == 0:
                    status = "ACCEPT (Geometric Fit)"
                    is_accepted = True
                else:
                    status = "REJECT (Messy Anchor)"

            # Print the Forensic Trace
            print(f"{'':<10} | +{gap:<7} | {candidate:<10} | {residue:<15} | {status}")

            if is_accepted:
                # --- RESULT ANALYSIS ---
                if candidate == true_next:
                    print(f">>> SUCCESS: Geometric Prediction matched True Prime.")
                else:
                    # This is the critical "Law I Failure" / "Imposter" moment
                    print(f">>> FAILURE: Sieve selected {candidate}, but True Prime is {true_next}.")
                    print(f"    (Reason: {candidate} is a Composite that passed the Geometric Filter)")
                break

            gap += 2
            
            # Safety break for demo purposes
            if gap > 50: break

if __name__ == "__main__":
    forensic_test()