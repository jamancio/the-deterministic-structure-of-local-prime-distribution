import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def get_smallest_prime_factor(n):
    if n < 2: return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return i
    return n  # If prime, return itself

# 1. Find a "Long Drought" (Gap >= 30) after 10,000
current = 10000
while True:
    if is_prime(current):
        start_prime = current
        # Find next prime
        next_val = current + 1
        while not is_prime(next_val):
            next_val += 1
        end_prime = next_val
        gap = end_prime - start_prime
        
        if gap >= 30:
            break
        current = next_val
    else:
        current += 1

# 2. Dissect the Blockade
blockade_range = list(range(start_prime, end_prime + 1))
blockade_factors = []
colors = []

for n in blockade_range:
    spf = get_smallest_prime_factor(n)
    blockade_factors.append(spf)
    
    if n == start_prime or n == end_prime:
        colors.append('gold') # The Primes (Vacuum)
    elif spf <= 3: 
        colors.append('red') # Messy Channel (Blocked by 2 or 3)
    else:
        colors.append('blue') # Clean Channel Blocked (Sniped by 5, 7, 11...)

# 3. Visualize the Anatomy of the Gap
plt.figure(figsize=(14, 6))
bars = plt.bar(blockade_range, blockade_factors, color=colors)

# Add text for the "Snipers" (Higher factors blocking the clean channel)
for n, spf, color in zip(blockade_range, blockade_factors, colors):
    if color == 'blue':
        plt.text(n, spf, str(spf), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title(f"Anatomy of a Prime Drought: Gap of {gap} between {start_prime} and {end_prime}")
plt.xlabel("Number Line (The Blockade)")
plt.ylabel("Blocking Prime (Smallest Factor)")
plt.legend(["Red = Messy Channel (2, 3)", "Blue = Clean Channel Blocked", "Gold = Prime"])
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.savefig('prime_drought_anatomy.png')
plt.show()

print(f"Gap Found: {gap}")
print(f"Start: {start_prime}, End: {end_prime}")
print(f"Blockade Factors: {blockade_factors}")
