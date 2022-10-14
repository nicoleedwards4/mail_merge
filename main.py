# read the names in as a list
with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()

for name in names:

    # read the starting letter
    with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        letter_lines = starting_letter.readlines()

    # replace [name] in letter
    stripped_name = name.strip()
    letter_lines[0] = letter_lines[0].replace("[name]", stripped_name)

    # determine saved file name
    save_file = f"Output/ReadyToSend/{stripped_name}.txt"

    with open(save_file, mode="w") as letter:
        letter.writelines(letter_lines)
