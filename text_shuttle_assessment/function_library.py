def strip_skintone_mod(input_array):
    if "emoji" in input_array:
        print("emoji")
        return "emoji"
    else:
        return ""


def extract_skintone_modifiers(input_array):
    if "emoji" in input_array:
        substrings = input_array.split()
        sorted_substrings = []
        
        for substring in substrings:

            if substring == "human":
                index_emoji = substrings.index(substring) + 1
                index_skintone_mod = substrings.index(substring) + 2

                if substrings[index_emoji] == "emoji":
                    sorted_substrings.append(
                        f'human emoji : {substrings[index_skintone_mod]}')
            continue
        print(sorted_substrings)
        
