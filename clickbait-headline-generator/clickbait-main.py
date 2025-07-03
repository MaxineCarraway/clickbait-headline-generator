# Clickbait Headline Generator

import random

#Set up the constants
object_pronouns = ['Her', 'Him', 'Them']
possesive_pronouns = ['Her', 'His', 'Their']
personal_pronouns = ['She', 'He', 'They']
cities = ["Liverpool", "Manchester", "Bristol", "Edinburgh", "Cardiff", "Glasgow", "Swansea", "Portsmouth" "Leeds", "Yorkshire", "Lancaster", "Newcastle"]
nouns = ["Ostrich", "Steering Wheel", "Bank Robber", "Toe Wrestler", "Cheese", "Tailor", "Gnome", "Bottle top", "lighthouse Keeper", "Corkscrew", "Butler", "Digital Overlord", "Hacker", "Giraffe", "Peanut"]
places = ["Barber Shop", "Tree House", "Restaurant", "Airport", "Garden", "Bandstand", "Castle", "Pier", "Fairground", "Lake", "Lavatory", "Boots"]
when = ["Soon", "This Year", "RIGHT NOW", "Later Today", "Next Week"]

def main() -> None:
    """
    Main function to generate and display clickbait headlines
    """
    print("\nClickbait Headline Generator")
    print("\nThe website that aims to ""inspire"" people into looking at ads")

    num_headlines = get_number_of_headlines()

    for _ in range(num_headlines):
        headline = generate_random_headline()
        print(headline)

    post_to_fake_website()

def get_number_of_headlines() -> int:
    """
    Prompt the user to for the number of headlines to generate

    Returns:
        int: the amount of headlines required
    """
    while True:
        response = input("\nEnter the amount of clickbait headlines you'd like to generate as a number: ")
        if response.isdigit():
            return int(response)
        print("Please enter a valid number.")

def generate_random_headline() -> str:
    """
    Generate a random clickbait headline

    Returns:
        str: output of randomised headlines
    """
    headline_type = random.randint(1,7)

    if headline_type == 1:
        return generate_millenials_vs_industry()
    if headline_type == 2:
        return generate_hidden_danger_alert()
    if headline_type ==3:
        return generate_corporate_secrets_exposed()
    if headline_type == 4:
        return generate_unbelievable_discovery()
    if headline_type == 5:
        return generate_industry_secrets_revealed()
    if headline_type == 6:
        return generate_must_have_gift_ideas()
    return generate_surprising_reasons_why() # default return

def generate_millenials_vs_industry() -> str:
    """
    Generates a headline of the format "Are Millenials killing 'X' industry?"

    Returns:
        str: randomised headlines: "Are Millenials killing {noun} industry?"
    """
    noun = random.choice(nouns)
    return f"Are Millenials killing the {noun} industry?"

def generate_hidden_danger_alert() -> str:
    """
    Generates a headline of the format "Without this 'X', 'Y' could kill you 'Z'!"

    Returns:
        str: randomised headlines: "Without this {noun}, {plural_noun} could kill you {when}!"
    """
    noun = random.choice(nouns)
    plural_noun = random.choice(nouns) + "s"
    moment = random.choice(when)
    return f"Without this {noun}, {plural_noun} could kill you {moment}!"

def generate_corporate_secrets_exposed() -> str:
    """
    Generates a headline of the format: "Big Companies Hate 'X'! See How This 'Y' 'Z' Did Something"

    Returns:
        str: randomised headlines: "Big Companies Hate {pronoun}! See How This {city} {noun1} invented a cheaper {noun2}"
    """
    pronoun = random.choice(object_pronouns)
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    city = random.choice(cities)
    return f"Big Companies Hate {pronoun}! See How This {city} {noun1} invented a cheaper {noun2}"

def generate_unbelievable_discovery() -> str:
    """
    Generate a headline of the format: "You Won't Believe What This 'X' 'Y' Found in 'Z'"

    Returns:
       str: randomised headlines: "You Won't Believe What This {city} {noun} Found in {pronoun} {place}"
    """
    city = random.choice(cities)
    noun = random.choice(nouns)
    pronoun = random.choice(possesive_pronouns)
    place = random.choice(places)
    return f"You Won't Believe What This {city} {noun} Found in {pronoun} {place}."

def generate_industry_secrets_revealed() -> str:
    """
    Generate a headline of the format: "What 'X's Don't Want You To Know About 'Y's"

    Returns:
        str: randomised headlines: "What {plural_noun1}'s Don't Want You To Know About {plural_noun2}'s"
    """
    plural_noun1 = random.choice(nouns)
    plural_noun2 = random.choice(nouns)
    return f"What {plural_noun1}'s Don't Want You To Know About {plural_noun2}'s"

def generate_must_have_gift_ideas() -> str:
    """
    Generate a headline of the format: "X Gift Ideas to Give Your Y From Z"

    Returns:
        str: randomised headlines:   "{number} Gift Ideas to Give Your {noun} From {city}
    """
    number = random.randint(3, 19)
    noun = random.choice(nouns)
    city = random.choice(cities)
    return f"{number} Gift Ideas to Give Your {noun} From {city}"

def generate_surprising_reasons_why() -> str:
    """
    Generate a headline of the format: "'X' Reasons Why 'Y' Are More Interesting Than You Think (Number 'Z' Will Surprise You!)"

    Returns:
        str: "{number1} Reasons Why {plural_noun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)"
    """
    number1 = random.randint(3, 19)
    plural_noun = random.choice(nouns) + "s"
    number2 = random.randint(1, number1)
    return f"{number1} Reasons Why {plural_noun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)"

def post_to_fake_website() -> None:
    """
    Display a fake post prompt
    """
    website = random.choice(
        ["Woobsite", "Blaggo", "Farcebuuk", "Goggles", "Tweedle", "Pastagram"]
    )
    when_choice = random.choice(when).lower()
    print(f"\nPost these to our {website} {when_choice} or you're fired!")

if __name__ == "__main__":
    main()
