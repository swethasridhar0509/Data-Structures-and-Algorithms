# 04_Comparing Algorithms

## Algorithm Design

- **Finding a solution to the problem** - designing an algorithm.
- **Seeking the optimal solution—There can be multiple solutions to a problem,** and the aim is to find the most efficient solution.

## **Algorithm Efficiency Test**

- An algorithm cannot be judged by the **time taken** for a machine to execute it.
- Because it might vary due to different **Hardware** and **software** configurations.
- Hence, an **asymptotic analysis** is performed to test the algorithm’s efficiency.

### Asymptotic analysis

- The goal is to design data structures and algorithms that are **fast** and **memory-efficient**.
- Asymptotic analysis involves measuring the rate at which the **time (time complexity)** and **memory (space complexity)** required by the algorithm increases as the size of the input data increases.
- How to express the result?  **Asymptotic notation**.

## **Types of Asymptotic Analysis & Notation**

### **Big O Notation (O) - Worst-case analysis**

- Used to express the upper bound **(maximum time or space)** required by an algorithm, for any input.
- **How?** It focuses on worst-case scenarios.

<aside>
**Example:** For a linear search on the list `[10, 20, 30, 40, 50]`. 
-**Worst case:** Searching for `50` or an absent element, takes 5 comparisons (maximum).
-Worst case **O(n)**

</aside>

### **Omega Notation (Ω) - Best-case analysis**

- Used to express the lower bound **(minimum time or space)** required by an algorithm, for any input.
- **How?** It focuses on best-case scenarios.

<aside>
**Example:** For a linear search on the list `[10, 20, 30, 40, 50]`. 
-**Best case:** Searching for `10`, taking 1 comparison (least).
-Best case **Ω(1)**

</aside>

### **Theta Notation (Θ) - Average-case analysis**

- **Theta (Θ) notation** describes the **exact growth rate** of an algorithm's running time as the input size grows.
- How? Focuses on the average case.

<aside>
**Example:** For a linear search on the list `[10, 20, 30, 40, 50]`. 
-**Average case:** Searching for 30, taking n/2 comparison (average).
-Average case **Θ(n)**

</aside>

## Rules for expressing asymptotic analysis

1. Ignore constant terms.
2. Ignore the least significant terms.
3. Always consider the worst case. **why?** It’s better to create a system for 10 million users than 10 users.