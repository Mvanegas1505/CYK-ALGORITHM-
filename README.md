# CYK Algorithm implementation

## Project Overview

This project implements the Cocke-Younger-Kasami (CYK) algorithm based on Kozen's approach (1997, Lecture 27). The program determines whether a given string belongs to the language generated by a context-free grammar (CFG) in Chomsky Normal Form (CNF).

## Theoretical Background

### Context-Free Grammars (CFGs)

A context-free grammar (CFG) is a formal grammar that defines a set of strings (a language). It consists of four components:

*   **N (Nonterminals):** A finite set of variables or symbols that can be replaced by other symbols (e.g., A, B, S).
*   **Σ (Terminals):** A finite set of symbols that form the actual strings of the language (e.g., a, b, c). Σ and N are disjoint sets.
*   **P (Productions):** A finite set of rules of the form A → α, where A ∈ N and α ∈ (N ∪ Σ)*.
*   **S (Start Symbol):** A special nonterminal symbol (S ∈ N) that represents the starting point for generating strings.

**Chomsky Normal Form (CNF):** A CFG is in CNF if all its production rules are of one of the following two forms:

1.  A → BC, where A, B, and C are nonterminals.
2.  A → a, where A is a nonterminal and a is a terminal.

**Example CFG (in CNF):**

*   N = {S, A, B}
*   Σ = {a, b}
*   P = {S → AB, A → a, B → b}
*   S is the start symbol.

This grammar generates the language {ab}.

## Assignment: CYK Algorithm Implementation

This assignment implements the CKY algorithm, as presented in [Kozen, Lecture 27] (1).

**Input:**

*   A context-free grammar *G* = (*N*, Σ, *P*, *S*) in Chomsky Normal Form (CNF).
*   A string *x* ∈ Σ*.

**Output:**

*   A decision (yes/no) indicating whether *x* ∈ *L*(G).

**Assumptions:**

*   The grammar *G* is in Chomsky Normal Form (CNF).
*   The capital letter 'S' is the initial symbol.
*   Nonterminals are capital letters.
*   Terminals are lowercase letters.

## Input/Output Specification

#### Input Format

The program receives input consisting of multiple test cases. Each case defines a CFG in CNF and a set of strings to be analyzed. The input format is:

*   A single line with a positive integer *n* (*n* > 0), indicating the number of test cases.

*   For each test case:

    *   A single line with two space-separated integers, *k* and *m*. *k* is the number of nonterminals (*k* = |*N*|), and *m* is the number of strings to test.

    *   *k* lines, each representing a production rule:

        ```
        <nonterminal> <derivation alternatives separated by spaces>
        ```

        Example:

        ```
        S AB AC
        A a
        B b
        C c
        ```

    *   *m* lines, each with a string to test.

**Example Input:**
```
1
3 2
S AB AC
A a
B b
ab
ac
```
#### Output Format

For each test case, print *m* lines. Print `yes` if the string is generated by the grammar, and `no` otherwise.

**Example Output:**
```
yes
yes
```
#### Input/Output Examples

Here are more examples:

**Example 1:**

**Input (in `input.txt`):**
```
3
5 5
S AB BA SS AC BD
C SB
D SA
A a
B b
aabbab
aabb
ab
aa
b
4 3
S AB AC SS
C SB
A a
B b
abab
aaabbbaabbab
aabab
2 6
S AS b
A a
ab
aaaaaaaa
aaaaaaaaaab
b
bb
abb
```
**Output:**
```
yes
no
yes
no
yes
no
no
no
yes
yes
no
yes
yes
yes
no
```
## Implementation Details

#### Code Highlights

The program uses these key functions:

*   `generate_pairs(n)`: Generates pairs (i, j) for the CKY table.
*   `index_of_position(table, position)`: Returns the index of a position in the table.
*   `main()`: Handles input, CKY execution, and output.

#### Code Snippet (Key Logic in `main()`):

```python
for m in range(2, n + 1):
    for i in range(n - m + 1):
        position = index_of_position(table, (i, i + m))
        table[position][1] = ""
        for j in range(i + 1, i + m):
            for p in productions:
                derivations = productions[p]
                for d in derivations:
                    pos1 = index_of_position(table, (i, j))
                    pos2 = index_of_position(table, (j, i + m))
                    Tij = table[pos1][1]
                    Tjim = table[pos2][1]
                    if d[0] in Tij and d[1] in Tjim:
                        pos3 = index_of_position(table, (i, i + m))
                        table[pos3][1] = table[pos3][1] + p

fposition = index_of_position(table, (0, n))
Tn = table[fposition][1]
if "S" in Tn:
    print("yes")
else:
    print("no")
```

## Example Usage
Save the code as main.py and create input.txt. Run:
```
python main.py

```
## References 

[1] Kozen, Dexter C. Automata and Computability. Springer, Third printing, 1997 [2012]. Undergraduate Texts in Computer Science. https://doi.org/10.1007/978-1-4612-1844-9.

## Developers 
[Pablo Cabrejos Múnera]
[Martin Vanegas Ospina]

Thank you for your hard work!!!


