import sys

# ==============================================================================
# PLR MOD 30 PREDICTIVE SIEVE
#
# GOAL:
# Test the "Higher Resolution" Predictive Model.
#
# LOGIC:
# 1. Start at p_n.
# 2. Iterate gaps (2, 4, 6...).
# 3. FILTER 1 (Geometry): Must fit Clean/Messy Anchor rules (Mod 6).
# 4. FILTER 2 (Mod 30): Must NOT be divisible by 5.
# 5. PREDICTION: Select the FIRST candidate that passes both filters.
# ==============================================================================

def is_prime_utility(n):
    """Utility to check truth for logging, NOT used for sieving."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def plr_mod30_predictive_sieve():
    # Test Primes known to have Imposters (23, 31, 47, 53, 61, 89)
    TEST_PRIMES = [
        23, 31, 47, 53, 61, 89, 113, 127
    ]

    print(f"{'PRIME':<6} | {'GAP':<4} | {'CANDIDATE':<10} | {'S_n%6':<6} | {'FILTER 5?':<10} | {'FINAL DECISION':<18} | {'TRUTH'}")
    print("="*85)

    for p_n in TEST_PRIMES:
        true_next = 0
        # Simple lookahead to find true next prime for verification
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
            is_div_by_5 = (candidate % 5 == 0)
            
            # --- FILTER 1: PLR Mod 6 Geometry (77% Sieve) ---
            is_valid_mod6 = False
            if gap % 6 == 0:
                if residue != 0: is_valid_mod6 = True
            else:
                if residue == 0: is_valid_mod6 = True

            # --- FILTER 2: Mod 30 Sieve (Remove Multiples of 5) ---
            is_valid_mod30 = not is_div_by_5
            
            # --- FINAL PREDICTION DECISION ---
            if is_valid_mod6 and is_valid_mod30:
                predicted_candidate = candidate
                break # Found the winner
            
            # --- LOGGING REJECTIONS ---
            final_decision = "SKIP"
            if not is_valid_mod6:
                final_decision = "REJECT (Mod 6)"
            elif not is_valid_mod30:
                final_decision = "REJECT (Mod 5)"
            
            truth_label = is_prime_utility(candidate) and "PRIME" or "Composite"
            
            print(f"{p_n:<6} | +{gap:<3} | {candidate:<10} | {residue:<6} | {str(is_div_by_5):<10} | {final_decision:<18} | {truth_label}")
            
            gap += 2
            if gap > 50: break # Safety break

        # Print the WINNER
        truth_label = is_prime_utility(predicted_candidate) and "PRIME" or "Composite"
        result_status = "PASS" if predicted_candidate == true_next else "FAIL"
        
        print("-" * 85)
        print(f"WINNER: {p_n:<6} | +{gap:<3} | {predicted_candidate:<10} | {residue:<6} | {str(is_div_by_5):<10} | {result_status:<18} | {truth_label} (Predicted)")
        print(f"   (Prediction matched True Next: {result_status})")
        print("="*85)

if __name__ == "__main__":
    plr_mod30_predictive_sieve()