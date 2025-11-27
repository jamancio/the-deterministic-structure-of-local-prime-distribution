import sys

# ==============================================================================
# PLR FORENSIC GAP ANALYSIS: PREDICTION vs TRUTH
#
# GOAL:
# Analyze the specific geometric gaps when the PLR model fails.
# Is there a pattern in the "Error Delta" (True Gap - Predicted Gap)?
#
# LOGIC:
# 1. Blindly select the first candidate that fits the PLR Geometry.
# 2. Check if it is the True Next Prime.
# 3. If WRONG: Calculate the gap to the False Candidate vs. True Prime.
# ==============================================================================

def get_true_next_prime(current_prime):
    """Simple utility to find the next prime for verification."""
    n = current_prime + 2
    while True:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            return n
        n += 2

def gap_delta_analysis():
    # We test a range of primes where we know "Imposters" lurk
    # 23, 31, 47, 53, etc. are known stress points.
    TEST_RANGE_START = 23
    TEST_RANGE_END = 500
    
    # Generate primes in range
    primes = []
    curr = TEST_RANGE_START
    if curr % 2 == 0: curr += 1
    while curr < TEST_RANGE_END:
        if get_true_next_prime(curr - 2) == curr:
            primes.append(curr)
        curr += 2

    print(f"{'PRIME':<6} | {'PREDICTED':<10} | {'TRUE NEXT':<10} | {'PRED GAP':<8} | {'TRUE GAP':<8} | {'DELTA (Error)':<12} | {'RESULT'}")
    print("="*90)

    for p_n in primes:
        true_next = get_true_next_prime(p_n)
        
        # --- BLIND PREDICTION ENGINE ---
        # Find first geometric fit (Anchor 0 for non-mult-6, Anchor 2/4 for mult-6)
        gap = 2
        predicted_candidate = 0
        
        while True:
            candidate = p_n + gap
            anchor = p_n + candidate
            residue = anchor % 6
            
            # Geometric Filter
            if gap % 6 == 0:
                # Gap 6, 12... allows Messy Anchor
                if residue != 0: 
                    predicted_candidate = candidate
                    break
            else:
                # Gap 2, 4... allows Clean Anchor
                if residue == 0:
                    predicted_candidate = candidate
                    break
            
            gap += 2
        
        # --- GAP ANALYSIS ---
        pred_gap = predicted_candidate - p_n
        true_gap = true_next - p_n
        delta = true_gap - pred_gap # How far off were we?
        
        status = "PASS"
        if predicted_candidate != true_next:
            status = "FAIL"
        
        # Formatting for visibility
        delta_str = f"+{delta}" if delta > 0 else "0"
        
        print(f"{p_n:<6} | {predicted_candidate:<10} | {true_next:<10} | {pred_gap:<8} | {true_gap:<8} | {delta_str:<12} | {status}")

if __name__ == "__main__":
    gap_delta_analysis()