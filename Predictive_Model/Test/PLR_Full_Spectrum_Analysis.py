import sys

# ==============================================================================
# PLR FULL SPECTRUM ANALYSIS (NO STOPS)
#
# GOAL:
# Show the Geometric Decision for the ENTIRE candidate pool (Next 10 Odd Numbers).
# Do NOT stop when a winner is found.
# Do NOT stop when the true prime is found.
#
# COLUMNS:
# - STATUS: The Blind Sieve's decision (ACCEPT/REJECT).
# - TRUTH:  Whether the number is actually Prime (for forensic comparison only).
# ==============================================================================

def is_prime_utility(n):
    """Utility for the 'Truth' column only. The Sieve does NOT see this."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def full_spectrum_analysis():
    # The starting primes to analyze
    TEST_PRIMES = [
        5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
        83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
    ]
    
    # CONSTRAINT: Show exactly 10 candidates per prime
    POOL_SIZE = 10 

    print(f"{'GAP':<4} | {'CANDIDATE':<10} | {'ANCHOR':<8} | {'PLR DECISION':<18} | {'TRUTH':<10} | {'NOTES'}")
    print("="*100)

    for p_n in TEST_PRIMES:
        print(f"\n[ PRIME: {p_n} ] Analyzing next {POOL_SIZE} candidates...")
        print("-" * 100)

        winner_already_declared = False
        
        # Iterate through the next POOL_SIZE odd numbers (gap 2, 4, 6 ... 20)
        for k in range(1, POOL_SIZE + 1):
            gap = k * 2
            candidate = p_n + gap
            anchor = p_n + candidate
            residue = anchor % 6
            
            # --- 1. THE BLIND SIEVE LOGIC ---
            # Rule: If Gap%6==0, Anchor must be Messy. If Gap%6!=0, Anchor must be Clean.
            decision = "REJECT"
            
            if gap % 6 == 0:
                if residue != 0: decision = "ACCEPT"
            else:
                if residue == 0: decision = "ACCEPT"

            # --- 2. THE FORENSIC TRUTH (For Reporting Only) ---
            truth = "Composite"
            if is_prime_utility(candidate):
                truth = "PRIME"

            # --- 3. ANNOTATION ---
            note = ""
            
            # Identify the FIRST Geometric Accept (The Sieve's Prediction)
            if decision == "ACCEPT" and not winner_already_declared:
                note += "<< PREDICTED WINNER "
                winner_already_declared = True
                if truth == "PRIME":
                    note += "(CORRECT)"
                else:
                    note += "(IMPOSTER/FAILURE)"
            
            # Identify the True Prime (if it wasn't the winner)
            if truth == "PRIME" and "PREDICTED WINNER" not in note:
                 note += "<< MISSED PRIME"

            # Identify Secondary Imposters (Composites accepted later in the pool)
            if decision == "ACCEPT" and truth == "Composite" and "PREDICTED WINNER" not in note:
                note += "(Secondary Imposter)"

            # --- PRINT ROW ---
            # Format: Gap | Cand | Anchor | Decision | Truth | Note
            print(f"+{gap:<3} | {candidate:<10} | {residue:<8} | {decision:<18} | {truth:<10} | {note}")

if __name__ == "__main__":
    full_spectrum_analysis()