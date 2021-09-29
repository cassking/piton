"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""

# Write a story with some words missing
story = """
Roses are {color1}\n
Violets are {color2}\n
Sugar is {adj}\n
And so are you
"""
def madlib(color1, color2, adj):
    madlib_story = f"""
    Roses are {color1}\n
    Violets are {color2}\n
    Sugar is {adj}\n
    And so are you
    """
    # print(madlib_story)
    return madlib_story


# Ask the user to provide the missing words
color1 = input("give me a color: ")
color2 = input("give me another color: ")
adj = input("give me and adjective:    ")

# Display the final story
print(madlib(color1, color2, adj))
