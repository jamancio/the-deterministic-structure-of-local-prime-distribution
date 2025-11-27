import sys

# ==============================================================================
# PLR TEST: THE "CLEAN ANCHOR" PREDICTOR
#
# GOAL:
# Test the hypothesis: "The next prime is the first candidate where Anchor == 0 mod 6".
#
# LOGIC:
# 1. Iterate gaps g = 2, 4, 6...
# 2. Calculate Anchor = p_n + (p_n + g)
# 3. IF Anchor % 6 == 0: SELECT as WINNER (Stop).
# 4. Compare Winner with True Next Prime.
# ==============================================================================

def clean_anchor_bias_test():
    # Larger sample to see if the rule holds or breaks
    PRIMES = [
        23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151
    ]
    
    # Utility to get true next prime from the list
    def get_true_next(idx):
        if idx + 1 < len(PRIMES):
            return PRIMES[idx+1]
        return None

    print(f"{'PRIME':<6} | {'TRUE NEXT':<10} | {'PREDICTED':<10} | {'GAP':<4} | {'RESULT':<10}")
    print("="*60)

    correct_count = 0
    total_count = 0

    for i in range(len(PRIMES) - 1):
        p_n = PRIMES[i]
        true_next = get_true_next(i)
        
        # --- THE PREDICTOR ---
        # Find first candidate where Anchor % 6 == 0
        gap = 2
        predicted = None
        
        while True:
            candidate = p_n + gap
            anchor = p_n + candidate
            
            if anchor % 6 == 0:
                predicted = candidate
                break # Found our "Clean" winner
            
            gap += 2
            if gap > 100: break # Safety

        # --- VERIFICATION ---
        status = "FAIL"
        if predicted == true_next:
            status = "PASS"
            correct_count += 1
        else:
            # Analyze why it failed
            # If True Next was a Sexy Prime, Anchor would be 2 or 4.
            pass

        print(f"{p_n:<6} | {true_next:<10} | {predicted:<10} | {gap:<4} | {status:<10}")
        total_count += 1

    print("="*60)
    print(f"ACCURACY: {correct_count}/{total_count} ({correct_count/total_count*100:.2f}%)")

if __name__ == "__main__":
    clean_anchor_bias_test()