import pandas as pd

def get_smallest_prime_factor(n):
    if n < 2: return None
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0: return i
        if n % (i + 2) == 0: return i + 2
    return n

def hunt_high_order_blockade(start_n, min_gap_size):
    """
    Finds the first prime gap of at least min_gap_size and 
    dissects the modular 'Snipers' responsible for the drought.
    """
    current = start_n
    while True:
        # Find a prime to start the gap
        if get_smallest_prime_factor(current) == current:
            p1 = current
            # Look for the next prime
            p2_candidate = p1 + 1
            while get_smallest_prime_factor(p2_candidate) != p2_candidate:
                p2_candidate += 1
            
            p2 = p2_candidate
            gap = p2 - p1
            
            if gap >= min_gap_size:
                # Dissect the gap
                dissection = []
                for n in range(p1 + 1, p2):
                    spf = get_smallest_prime_factor(n)
                    # Classify the type of resistance
                    if spf <= 3:
                        res_type = "Base (2,3)"
                    elif spf <= 30: # 5, 7, 11, 13, 17, 19, 23, 29
                        res_type = f"Sniper (P={spf})"
                    else:
                        res_type = f"Deep Sniper (P={spf})"
                    
                    dissection.append({"Number": n, "SPF": spf, "Type": res_type})
                
                return p1, p2, gap, pd.DataFrame(dissection)
        current += 1

# --- RUN THE SEARCH ---
target_min_gap = 40
start_search = 10000

print(f"Scanning for a High-Order Blockade (Gap >= {target_min_gap}) after {start_search}...")
p_start, p_end, actual_gap, df_dissect = hunt_high_order_blockade(start_search, target_min_gap)

print(f"\n--- BLOCKADE FOUND ---")
print(f"Gap Size: {actual_gap}")
print(f"Interval: [{p_start} to {p_end}]")
print("\nDissection of the 'Clean Channel' Snipers in this gap:")
# We only show the numbers that are NOT divisible by 2 or 3 (The 'Clean' spots that were blocked)
clean_channel_blocks = df_dissect[df_dissect["Type"] != "Base (2,3)"]
print(clean_channel_blocks.to_string(index=False))