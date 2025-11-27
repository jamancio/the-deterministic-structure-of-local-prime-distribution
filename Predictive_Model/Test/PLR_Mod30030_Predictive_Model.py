def is_prime_utility(n):
    """Utility to check truth for logging, NOT used for sieving."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def plr_mod30030_predictive_model():
    # Test Primes that previously failed at 121 and 169
    TEST_PRIMES = [
        7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397
    ]

    print(f"{'PRIME':<6} | {'GAP':<4} | {'CANDIDATE':<10} | {'RESULT'}")
    print("="*60)

    for p_n in TEST_PRIMES:
        true_next = 0
        curr = p_n + 2
        while True:
            if is_prime_utility(curr):
                true_next = curr
                break
            curr += 2

        gap = 2
        predicted_candidate = 0
        
        print(f"\n[ Testing p = {p_n} ] True Next: {true_next}")

        while True:
            candidate = p_n + gap
            anchor = p_n + candidate
            residue = anchor % 6
            
            # --- FILTERS (STRUCTURAL LAYERS) ---
            is_valid_mod6 = (gap % 6 == 0 and residue != 0) or (gap % 6 != 0 and residue == 0)
            is_valid_mod5 = (candidate % 5 != 0)
            is_valid_mod7 = (candidate % 7 != 0)
            is_valid_mod11 = (candidate % 11 != 0)
            is_valid_mod13 = (candidate % 13 != 0) # NEW CRITICAL FILTER

            # --- FINAL PREDICTION DECISION ---
            if is_valid_mod6 and is_valid_mod5 and is_valid_mod7 and is_valid_mod11 and is_valid_mod13:
                predicted_candidate = candidate
                break # Found the winner (the lowest-resistance number)
            
            # Logging failures to show the sieve working
            if candidate == 121 or candidate == 169 or candidate == 209:
                 print(f"   REJECTED IMPOSTER {candidate} (Mod 11/13 Filter)")
            
            gap += 2
            if gap > 50: break

        # Print the WINNER
        result_status = "PASS" if predicted_candidate == true_next else "FAIL"
        truth_label = is_prime_utility(predicted_candidate) and "PRIME" or "Composite"
        
        print("-" * 60)
        print(f"WINNER: {p_n:<6} | +{gap:<3} | {predicted_candidate:<10} | {result_status} ({truth_label})")
        print(f"   (True Next: {true_next})")

if __name__ == "__main__":
    plr_mod30030_predictive_model()