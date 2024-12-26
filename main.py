# Generate each of the cells for i and j positions
def generate_pairs(n):
    list = []
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j and (j, i) not in list:
                list.append((i, j))

    return list

# Return the index where the position (i, j) is found
def index_of_position(table, position):
    i = 0
    for pair in table:
        if pair[0] == position:
            return i
        i += 1

def main():
    # Read the input.txt file
    with open("input.txt") as input:

        # Read the number of cases
        cases = int(input.readline().strip())

        while 0 < cases:

            # Read the number of nonterminals and the number of strings
            k, m = input.readline().strip().split()
            k, m = int(k), int(m)

            # Dictionary where the key is the nonterminal and the value is a
            # list of the derivations alternatives for each production
            productions = {}

            # List that stores the strings to be analyzed
            strings = []

            # Read and store the productions
            while 0 < k:
                production = input.readline().strip().split()
                key = production.pop(0)
                productions[key] = production
                k -= 1

            # Read and store the strings
            while 0 < m:
                strings.append(input.readline().strip())
                m -= 1

            # Analyze each of the strings stored
            for string in strings:

                # Define the pairs (i,j) that will represent the cells of table T
                pairs = generate_pairs(len(string))

                # Add every pair to the table followed by an empty string
                table = []
                for pair in pairs:
                    table.append([pair, ""])

                n = len(string)

                # Iterating through the subtrings of length = 1 of the variable "string"
                for i in range(n):
                    position = index_of_position(table, (i, i + 1))

                    # Initialize as empty the value of the cell in "position"
                    table[position][1] = ""

                    # Iterating through the productions and saving them in variable "derivations"
                    for p in productions:
                        derivations = productions[p]

                        # For each derivation, if the production derives the substring in the i position,
                        # the production is saved in position (i, i+1) of table
                        for d in derivations:
                            if d == string[i]:
                                table[position][1] = table[position][1] + p

                # Iterating through the subtrings of length >= 2 of the variable "string"
                for m in range(2, n + 1):
                    for i in range(n - m + 1):
                        position = index_of_position(table, (i, i + m))

                        # The values in table positions (i, i + m) are initiliazed as empty
                        table[position][1] = ""

                        # For all ways to break up the variable "string"
                        for j in range(i + 1, i + m):
                            for p in productions:
                                derivations = productions[p]
                                for d in derivations:

                                    # For each derivation, both values in (i, j) and (j,i + m) are saved in "pos1" and "pos2"
                                    pos1 = index_of_position(table, (i, j))
                                    pos2 = index_of_position(table, (j, i + m))

                                    # The productions of "pos1" and "pos2" are saved in "Tij" and "Tjim" respectively
                                    Tij = table[pos1][1]
                                    Tjim = table[pos2][1]

                                    # Check if "Tij" and "Tjim" are contained in the split of the "d"
                                    # derivation "d[0]" and "d[1]" respectively
                                    if d[0] in Tij and d[1] in Tjim:

                                        # The derivation is added in the position (i, i + m) in the table
                                        pos3 = index_of_position(table, (i, i + m))
                                        table[pos3][1] = table[pos3][1] + p

                # Determine if the cell (0, n) contains "S" and print the result
                fposition = index_of_position(table, (0, n))
                Tn = table[fposition][1]
                if "S" in Tn:
                    print("yes")
                else:
                    print("no")

            cases -= 1

    input.close()

if __name__ == "__main__":
    main()