import sys
import time

# ==============================================================================
# PLR DYNAMIC RECURSIVE MODEL (Updated with Progress & Accuracy)
#
# GOAL:
# 1. Dynamically scale resolution (add filters when horizon is crossed).
# 2. Track and display Accuracy % of the prediction.
# 3. Show progress status during execution.
# ==============================================================================

def get_prime_bank(limit):
    """Generates a bank of primes to use as filters."""
    sieve = [True] * (limit + 1)
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p*p, limit + 1, p):
                sieve[i] = False
    return [p for p in range(2, limit + 1) if sieve[p]]

def plr_dynamic_model_updated(target_limit=50000):
    print(f"Initializing PLR Dynamic Model up to {target_limit}...")
    
    # 1. Initialize Knowledge Base
    # Need primes up to sqrt(target_limit) + buffer
    filter_bank = get_prime_bank(int(target_limit**0.5) + 100)
    
    # 2. Start State (Mod 30)
    active_filters = [2, 3, 5] 
    next_filter_idx = 3 # Next is 7
    horizon = filter_bank[next_filter_idx] ** 2 
    
    # Stats
    total_predictions = 0
    correct_predictions = 0
    
    print(f"{'CURRENT':<10} | {'HORIZON':<10} | {'FILTERS':<15} | {'PREDICTION':<12} | {'STATUS'}")
    print("="*80)

    current_p = 23
    start_time = time.time()
    
    while current_p < target_limit:
        # --- THE PREDICTIVE STEP ---
        gap = 2
        while True:
            candidate = current_p + gap
            
            # --- INTELLIGENT SCALING ---
            if candidate >= horizon:
                new_filter = filter_bank[next_filter_idx]
                active_filters.append(new_filter)
                next_filter_idx += 1
                
                # Update Horizon
                if next_filter_idx < len(filter_bank):
                    horizon = filter_bank[next_filter_idx] ** 2
                else:
                    horizon = float('inf') # Should not happen if bank is big enough
                
                print(f"[SYSTEM] Horizon Crossed! Added Filter {new_filter}. New Horizon: {horizon}")

            # --- RECURSIVE SELF-EXCLUSION FILTER ---
            is_valid = True
            for f in active_filters:
                # Reject if divisible by f AND not equal to f
                if candidate % f == 0 and candidate != f:
                    is_valid = False
                    break
            
            if is_valid:
                predicted_next = candidate
                break
            
            gap += 2
            
        # --- VERIFICATION ---
        # Check if prediction is actually prime (Truth)
        is_correct = True
        if predicted_next < 2: 
            is_correct = False
        else:
            for i in range(2, int(predicted_next**0.5)+1):
                if predicted_next % i == 0:
                    is_correct = False
                    break
        
        if is_correct:
            correct_predictions += 1
        
        total_predictions += 1
        status = "PASS" if is_correct else "FAIL"
        
        # --- PROGRESS & LOGGING ---
        # Print every ~10% or specific count to avoid spamming
        if total_predictions % 500000 == 0 or current_p < 100:
             accuracy = (correct_predictions / total_predictions) * 100
             print(f"{current_p:<10} | {horizon:<10} | Count: {len(active_filters):<8} | {predicted_next:<12} | {status} (Acc: {accuracy:.2f}%)")
        
        current_p = predicted_next

    # Final Stats
    end_time = time.time()
    final_accuracy = (correct_predictions / total_predictions) * 100 if total_predictions > 0 else 0
    
    print("="*80)
    print(f"TEST COMPLETE.")
    print(f"Range: 23 to {current_p}")
    print(f"Total Predictions: {total_predictions}")
    print(f"Correct Predictions: {correct_predictions}")
    print(f"FINAL ACCURACY: {final_accuracy:.4f}%")
    print(f"Time Elapsed: {end_time - start_time:.4f} seconds")
    print("="*80)

if __name__ == "__main__":
    # Running up to 50,000 for demonstration
    plr_dynamic_model_updated(target_limit=50000000)