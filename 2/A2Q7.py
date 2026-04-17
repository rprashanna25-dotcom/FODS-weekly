# Function to count characters in a sentence
def key_value(sentence):
    count_dict = {}
    
    for char in sentence:
        if char != " ":              #  To ignore spaces
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
                
    return count_dict

# For user to input sentence
user_sentence = input("Enter a sentence: ").strip()

#  To call the function and display result
result = key_value(user_sentence)

# Display output vertically
print("\nCharacter counts (excluding spaces):")
for char, count in result.items():
    print(f"{char}: {count}")