import numpy as np
import matplotlib.pyplot as plt

def generate_prime_wave(x_range, primes):
    """
    Sums cosine waves for each prime to simulate 'Structural Interference'.
    Peaks = High Resistance (Messy).
    Valleys = Low Resistance (Vacuum).
    """
    # FIX: Explicitly define dtype=float to allow decimal values from cosine
    wave_sum = np.zeros_like(x_range, dtype=float)
    
    for p in primes:
        # Cosine wave peaks at multiples of p
        wave_sum += np.cos(2 * np.pi * x_range / p)
    return wave_sum

def get_plr_status(n):
    """Checks if integer n is in the PLR Clean Channel (Mod 30)."""
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return "Vacuum (Clean)"
    return "Resistance (Messy)"

# --- CONFIGURATION ---
start, end = 100, 200
resolution = 500  # Points per integer for smooth wave
x_vals = np.linspace(start, end, (end - start) * resolution)
basis_primes = [2, 3, 5]  # The Mod 30 Basis

# 1. Generate the Riemann-style Wave
y_vals = generate_prime_wave(x_vals, basis_primes)

# 2. Identify the "Deepest Valleys" (Local Minima)
# We look for integers where the wave is lowest
integers = np.arange(start, end + 1)
integer_wave_vals = generate_prime_wave(integers, basis_primes)

# 3. Visualize
plt.figure(figsize=(15, 6))

# Plot the Analog Wave (The "Music")
plt.plot(x_vals, y_vals, color='gray', alpha=0.5, label='Prime Interference Wave')

# Plot the Integers on the wave
clean_x, clean_y = [], []
messy_x, messy_y = [], []

for x, y in zip(integers, integer_wave_vals):
    status = get_plr_status(x)
    if status == "Vacuum (Clean)":
        clean_x.append(x)
        clean_y.append(y)
    else:
        messy_x.append(x)
        messy_y.append(y)

plt.scatter(messy_x, messy_y, color='red', s=30, label='Messy Channel (Peaks)')
plt.scatter(clean_x, clean_y, color='blue', s=80, zorder=5, label='PLR Vacuum (Valleys)')

plt.title(f"Riemann-PLR Unification: Wave Interference vs. Geometric Vacuum")
plt.xlabel("Number Line")
plt.ylabel("Structural Interference (Amplitude)")
plt.axhline(0, color='black', linestyle='--', alpha=0.3)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.show()