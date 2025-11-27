import sys

# ==============================================================================
# PLR FORENSIC CANDIDATE ANALYZER (NO PRIMALITY CHECK)
#
# GOAL:
# List ALL candidates for the first 25 primes.
# Show exactly which ones are blocked by geometry vs. allowed.
# Identify where the "Blind Sieve" fails (selects a composite).
# ==============================================================================

def forensic_candidate_analysis():
    # The "Truth" (used only for verification/logging, NOT for selection)
    PRIMES = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113
    ]

    print(f"{'GAP':<4} | {'CANDIDATE':<10} | {'ANCHOR (Mod 6)':<15} | {'PLR DECISION':<20} | {'NOTE'}")
    print("="*85)

    total_failures = 0

    for i in range(len(PRIMES) - 1):
        p_n = PRIMES[i]
        true_next = PRIMES[i+1]

        # Skip non-asymptotic (2,3)
        if p_n <= 3: continue

        print(f"\n[ PRIME: {p_n} ] Target: {true_next}")
        print("-" * 85)

        gap = 2
        winner_found = False
        winner_value = None

        while True:
            candidate = p_n + gap
            anchor = p_n + candidate
            residue = anchor % 6
            
            # --- THE GEOMETRIC FILTER ---
            # Rule 1: Clean Phase (Gap % 6 != 0) -> Requires Anchor 0
            # Rule 2: Messy Phase (Gap % 6 == 0) -> Requires Anchor 2 or 4
            
            status = "REJECT"
            
            if gap % 6 == 0:
                if residue != 0: status = "ACCEPT" # Messy Anchor allowed
            else:
                if residue == 0: status = "ACCEPT" # Clean Anchor allowed

            # --- LOGGING THE ROW ---
            note = ""
            row_color = ""
            
            # Identify Key Events
            if candidate == true_next:
                note = "<< TRUE PRIME"
            
            if status == "ACCEPT" and not winner_found:
                winner_found = True
                winner_value = candidate
                if candidate == true_next:
                    note = "<< PREDICTED WINNER (CORRECT)"
                else:
                    note = "<< PREDICTED WINNER (IMPOSTER!)"

            print(f"+{gap:<3} | {candidate:<10} | {residue:<15} | {status:<20} | {note}")

            # Stop Condition: We stop only after we have seen BOTH the winner AND the true prime
            # (In case the winner was 25 but the prime was 29, we want to see both lines)
            if candidate >= true_next and winner_found:
                break
                
            gap += 2
        
        # Summary for this Prime
        if winner_value != true_next:
            print(f"\n[!] FAILURE: Predicted {winner_value} (Composite), but True Prime is {true_next}.")
            total_failures += 1

    print("\n" + "="*85)
    print(f"ANALYSIS COMPLETE.")
    print(f"Total Prediction Failures (Imposters Selected): {total_failures}")
    print("Note: Failures occur when a Composite Number fits the Geometric Profile perfectly.")

if __name__ == "__main__":
    forensic_candidate_analysis()