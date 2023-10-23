# Prompt the user to enter a 6-letter DNA sequence
input = input("Enter a 6-letter DNA sequence (a, c, t, g): ")
user_input = input[0:6]

# Define a dictionary to store the complementary base pairs
complementary_pairs = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}

complementary_sequence = ""

    # Iterate through the user's input and find the complementary base for each letter
for letter in user_input:
    if letter in complementary_pairs:
        complementary_base = complementary_pairs[letter]
        complementary_sequence += complementary_base
    else:
        print(f"Invalid character '{letter}' in the DNA sequence. Please use only 'a', 'c', 't', or 'g'.")

    # Print the complementary DNA sequence
print("Complementary DNA sequence:", complementary_sequence)
