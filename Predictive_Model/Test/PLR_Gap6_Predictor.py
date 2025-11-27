import sys

# ==============================================================================
# PLR PREDICTIVE MODEL TEST: GAP 6 LOGIC
#
# LOGIC:
# 1. Start at p_n.
# 2. Select first candidate where Gap % 6 == 0 (which is p_n + 6).
# 3. Predict Next Prime = p_n + 6.
# 4. Compare with True Next Prime.
# ==============================================================================

def gap6_predictive_model():
    # List of primes for testing (covering various gap sizes)
    PRIMES = [
        7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191
    ]

    print(f"{'PRIME (p)':<10} | {'TARGET GAP6':<12} | {'PREDICTION':<10} | {'TRUE NEXT':<10} | {'RESULT':<10}")
    print("="*65)
    
    hits = 0
    total = 0

    for i in range(len(PRIMES) - 1):
        p_n = PRIMES[i]
        true_next = PRIMES[i+1]
        
        # 1. Select Candidate divisible by 6
        # The first gap divisible by 6 is always 6.
        gap_select = 6 
        candidate = p_n + gap_select
        
        # 2. The Arithmetic (As requested)
        # "Subtract candidate to p_n" -> 6
        # "Add gap from p_n" -> p_n + 6
        prediction = candidate 
        
        # 3. Status Check
        status = "FAIL"
        if prediction == true_next:
            status = "PASS"
            hits += 1
            
        print(f"{p_n:<10} | +{gap_select:<12} | {prediction:<10} | {true_next:<10} | {status}")
        total += 1

    print("="*65)
    print(f"PREDICTIVE ACCURACY: {hits}/{total} ({hits/total*100:.1f}%)")
    print("\nOBSERVATION:")
    print("- PASS: Means the True Prime was exactly at Gap 6 (Sexy Prime).")
    print("- FAIL: Means the True Prime was closer (Twin/Cousin) or further away.")

if __name__ == "__main__":
    gap6_predictive_model()