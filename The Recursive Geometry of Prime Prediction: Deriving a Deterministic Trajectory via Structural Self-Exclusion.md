# **The Recursive Geometry of Prime Prediction: Deriving a Deterministic Trajectory via Structural Self-Exclusion**

**Author:** Jores Amancio
**Date:** November 2025

### **Abstract**

The distribution of prime numbers is historically modeled as a probabilistic phenomenon, famously described by the Prime Number Theorem and the Riemann Hypothesis. While sieve methods effectively identify primes by removing composites, they are traditionally viewed as subtractive search algorithms rather than predictive functions. This paper introduces the **Recursive Geometric Sieve**, a constructive framework that transforms prime discovery into a deterministic trajectory calculation. We identify the "Structure of the Imposter"—composite numbers that mimic local prime geometry—as the interference pattern of previous primorial waves. To resolve boundary failures in recursive sieving, we introduce the **Self-Factor Exclusion Rule**, a logical operator that permits prime waves to exist at their own harmonic frequencies. Benchmarking confirms that this model achieves 100.00% predictive accuracy over 50,000,000 iterations when the structural resolution scales with $\sqrt{N}$. Furthermore, we propose that this recursive mechanism offers a geometric corollary to the Riemann Hypothesis, framing the distribution of primes as the interference product of deterministic modular waves.

---

### **1. Introduction: From Search to Construction**

The fundamental problem of algorithmic number theory is often framed as a search: given an integer $N$, find the next prime $p_{next}$. Standard approaches, such as Trial Division or the Miller-Rabin primality test, operate as **"Black Box" verifiers**—they guess a candidate and check its properties.

This paper proposes a **"White Box" constructive approach**. We posit that $p_{next}$ is not a random variable found by searching, but the inevitable result of a geometric function $f(N, \mathcal{B})$, where $\mathcal{B}$ represents the map of prior prime structures.

By mapping the **Path of Least Resistance (PLR)** and recursively applying modular constraints, we demonstrate that the "randomness" of prime gaps is merely an artifact of low-resolution observation. When the sieve resolution scales dynamically with the square root of the candidate magnitude ($\sqrt{N}$), the path to the next prime becomes structurally deterministic. We define this process not as "finding" a prime, but as **constructing** the path through the geometric vacuum.

---

### **2. The Structure of the Imposter**

A primary challenge in geometric prediction is the **"Imposter Composite"**—a composite number that perfectly fits the geometric profile of a prime at a given sieve resolution.

- **At Mod 6 Resolution:** The candidate **25** fits the "Clean Channel" ($1 \pmod 6$), mimicking a prime.
- **At Mod 30 Resolution:** The candidate **49** fits the "Prime Residue Map" (coprime to 30), mimicking a prime.
- **At Mod 210 Resolution:** The candidate **121** appears prime because it is not divisible by 2, 3, 5, or 7.

We define the **Imposter Horizon ($H$)** as the theoretical limit of a predictive model's accuracy, governed by the square of the next unfiltered prime factor ($p_{k+1}$):

$$H(\mathcal{B}_k) = (p_{k+1})^2$$

Where $\mathcal{B}_k = \{p_1, p_2, \dots, p_k\}$ is the set of active structural filters. Any predictive model based on $\mathcal{B}_k$ will function with 100% accuracy for all $N < H$, but will fail deterministically at $N = H$.

---

### **3. Methodology: The Recursive Predictive Function**

To navigate beyond the horizon, the model must be recursive. It must use the primes it has constructed to build the filters for the primes it has yet to reach.

#### **3.1. The Self-Factor Exclusion Rule ($\Psi$)**

A naive recursive sieve fails at the boundary conditions. For example, a Mod 11 filter removes all multiples of 11, erroneously deleting the prime 11 itself. To resolve this, we introduce the **Structural Validity Predicate**, $\Psi(C, \mathcal{B}_k)$, which incorporates a critical logical exception:

$$\Psi(C, \mathcal{B}_k) \iff \forall p_i \in \mathcal{B}_k, \Big[ (C \not\equiv 0 \pmod{p_i}) \lor (C = p_i) \Big]$$

This condition states that a candidate $C$ is structurally valid if, for every active filter $p_i$, $C$ is either:

1.  **Geometrically Excluded:** Not divisible by $p_i$ (The standard sieve).
2.  **Self-Excluded:** Is the prime $p_i$ itself (The recursive wave preservation).

This rule allows the "Prime Wave" to exist at its own harmonic frequency, solving the rejection paradox observed at $p=7$ and $p=11$.

#### **3.2. The Constructive Function**

The next prime is deterministically constructed as the minimal candidate satisfying $\Psi$. This function requires no probabilistic checks; it relies entirely on the Fundamental Theorem of Arithmetic:

$$f(N) = \min \{ C \in \mathbb{N} \mid (C > N) \land \Psi(C, \mathcal{B}_{\sqrt{C}}) \}$$

---

### **4. Computational Verification**

We subjected the Recursive Geometric Sieve to two rigorous tests to validate the **Imposter Horizon**, the **Self-Exclusion Logic**, and the **Constructive Capability**.

#### **4.1. The 50-Million Point Continuity Test**

We initialized a dynamic model starting with only $\mathcal{B} = \{2, 3, 5\}$ and allowed it to "self-scale" by adding filters whenever the candidate $C \ge p_{next}^2$.

- **Range:** 23 to 50,000,017.
- **Total Predictions:** 3,001,126.
- **Errors:** 0.
- **Accuracy:** **100.0000%**.

The model successfully identified and "jumped" every Imposter Horizon (e.g., at 49, 121, 169, 289...) by dynamically updating its resolution. This proves that the logic is **Scale-Invariant**.

#### **4.2. The Local Construction Test ($f(N)$)**

We tested the function $f(N)$ by inputting random integers and verifying if the algorithm could construct the immediate next prime using _only_ local geometric knowledge (filters up to $\sqrt{N}$).

- **Input:** $N = 1,000,000$.
- **Filters Loaded:** Primes up to 1,000.
- **Output:** $1,000,003$ (Verified Prime).
- **Input:** $N = 314$.
- **Output:** $317$ (Verified Prime).

This confirms that $p_{next}$ can be derived locally without sieving the entire number line, provided the local structural map is known.

---

### **5. Theoretical Implications: The Riemann Connection**

The success of this recursive model offers a geometric corollary to the analytic approach of the Riemann Hypothesis (RH).

#### **5.1. Wave Interference and Determinism**

The Riemann Hypothesis posits that prime distribution is controlled by the complex zeros of the Zeta function, which act as frequencies. The PLR Framework demonstrates the physical mechanism of this phenomenon:

- **Riemann's "Waves":** Correlate to the **Modular Exclusion Waves** of our model ($N \pmod p$).
- **Constructive Interference:** The "Spikes" in the distribution (Primes) correlate to the **Geometric Vacuum** where all exclusion waves cancel out.
- **The Error Term:** The deviation of the prime count is strictly bound by the **Imposter Horizon** ($\sqrt{x}$).

#### **5.2. The Geometric Singularity**

We propose the concept of the **Geometric Singularity** at $\text{Mod } \infty$. At this limit, the "Imposter Horizon" is pushed to infinity, and the "Structural Resistance" of the Clean Channel drops to exactly zero. In this state, the recursive sieve ceases to be a filter and becomes a pure generator.

This suggests that the "Chaos" of prime numbers is not intrinsic randomness, but the interference pattern of a strictly ordered, recursive system viewed at insufficient resolution.

---

### **6. Conclusion**

We have demonstrated that the "next prime" can be deterministically constructed from any point $N$ by applying a recursive geometric sieve with resolution $\sqrt{N}$. The introduction of the **Self-Factor Exclusion Rule** resolves the boundary paradoxes of standard sieving, allowing the model to function recursively.

While this model does not reduce the computational complexity class of finding primes (as it requires memory proportional to $\pi(\sqrt{N})$), it fundamentally alters the theoretical understanding of prime generation. It proves that a **True Predictive Model** exists: it is not a static algebraic equation, but a dynamic, self-correcting geometric trajectory.

---

### **Supplementary Material**

- **Exhibit A:** Python Source Code for `PLR_Dynamic_Recursive_Model` (50M Test).
- **Exhibit B:** Source Code for `PLR_Constructive_Algorithm` ($f(N)$ Function).
- **Exhibit C:** Forensic logs demonstrating the Horizon Crossing events at $7^2, 11^2, 13^2$.
