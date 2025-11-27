def is_prime_utility(n):
    """Utility to check truth for logging, NOT used for sieving."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def plr_self_factor_exclusion_test():
    # Test the problematic initial primes to verify the fix
    TEST_PRIMES = [7, 11, 13, 17, 19, 23, 29] 
    
    print(f"{'PRIME':<6} | {'PREDICTED':<10} | {'TRUE NEXT':<10} | {'RESULT'}")
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
        
        while True:
            candidate = p_n + gap
            anchor = p_n + candidate
            residue = anchor % 6
            
            # --- FILTERS WITH SELF-EXCLUSION (The Structural Fix) ---
            
            # Mod 6 Geometry is fixed
            is_valid_mod6 = (gap % 6 == 0 and residue != 0) or (gap % 6 != 0 and residue == 0)
            
            # SELF-FACTOR EXCLUSION LOGIC: (Reject only if C is a COMPOSITE multiple of Pk)
            # The filter must PASS the prime Pk if the candidate equals Pk.
            is_valid_mod5 = (candidate % 5 != 0) or (candidate == 5)
            is_valid_mod7 = (candidate % 7 != 0) or (candidate == 7)
            is_valid_mod11 = (candidate % 11 != 0) or (candidate == 11)
            is_valid_mod13 = (candidate % 13 != 0) or (candidate == 13)

            # --- FINAL PREDICTION DECISION ---
            if is_valid_mod6 and is_valid_mod5 and is_valid_mod7 and is_valid_mod11 and is_valid_mod13:
                predicted_candidate = candidate
                break 
            
            gap += 2
            if gap > 20: break # Safety break

        # Print the WINNER
        result_status = "PASS" if predicted_candidate == true_next else "FAIL"
        
        print(f"{p_n:<6} | {predicted_candidate:<10} | {true_next:<10} | {result_status}")

if __name__ == "__main__":
    plr_self_factor_exclusion_test()