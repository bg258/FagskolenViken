import os
import random
from pathlib import Path
from urllib.parse import quote

import requests
from dotenv import load_dotenv

# I made a small list of Bible verses for people who want some suggestions for bible verses. 
# These are categorised in three different categories. 
VERSES = [ ("John 3:16", "Love", "God's love for the world"), 
           ("1 Corinthians 13:4", "Love", "Love is patient"), 
           ("1 John 4:8", "Love", "God is love"), 
           ("Hebrews 11:1", "Faith", "The meaning of faith"), 
           ("Proverbs 3:5", "Faith", "Trust in the Lord"),
           ("Mark 11:24", "Faith", "Faith and prayer"), 
           ("Jeremiah 29:11", "Hope", "A future and a hope"),
           ("Romans 15:13", "Hope", "Joy, peace, and hope")]

# verse retrieval is a function that I have created to retrieve a bible verse from the API that does not need a API key. 
def verse_retrieval(reference):
    verse = quote(reference,  safe=":,-")
    url = "https://bible-api.com/" + verse 
    translation = {"translation" : "web"} # here we want to use the world english bible translation. Here we can add more translations in the future

    # we send a request to the API and based on the response we return an answer
    response = requests.get(url, params=translation, timeout=15)
    response.raise_for_status() # we check if we got a response
    bible_verse = response.json()

    if bible_verse.get("error"):
        raise ValueError("Unfortunately we could not find that exact bible verse. Try again!")
    if not bible_verse.get("text"):
        raise ValueError("The following bible verse has no text.")
    return bible_verse


# The second API needs an API key stored in the .env file. 
# I use it when the user wants to compare the same verse in two translations.

def compare_bible(verse, api_key):
    headers = {"api-key" : api_key}
    url = "https://rest.api.bible/v1/bibles"

    response = request.get(
        url, 
        headers=headers, 
        params = {
            "language" : "eng"
        }, 
        timeout=15
    )

    response.raise_for_status()
    bibles = response.json()["data"]

    bible = None
    translation = ["king james", "american standard", "darby"]

    for name in translation:
        for hit in bibles:
            if found in hit.get("name", "").lower() and  hit.get("id"):
                bible = hit
                break 
        if bible is not None:
            break

    # now that we have either a hit or not, can we either return our 
    # hit or return an error message to our user. 

    id_verse = f"{verse['book_id'].upper()}.{verse['chapter']}.{verse['verse']}"
    url_verse = f"https://rest.api.bible/v1/bibles/{bible['id']}/verses/{verse_id}"
    settings = { "content-type": "text", "include-verse-numbers": "false", "include-notes": "false"}

    response = requests.get(
        verse_url, 
        headers=headers, 
        params=settings, 
        timeout=15 )
    response.raise_for_status()
    content = response.json()["data"].get("content")

    if not content:
        raise ValueError("We could not load the translation you asked for. Please try again later.")
    return bible["name"], content



# the following function will print print our bible verse and will also compare two of the translations at the same time.

# This function lets the user read a verse and compare translations.
def read_verse(reference, compare=False, api_key=""):

    try:
        verse = verse_retrieval(reference)

        print(f"\n{verse['reference']} - World English Bible")
        print("-" * 45)
        print(" ".join(verse["text"].split()))

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        print("Sorry, could not get the verse:", error)
        return

    if not compare:
        return

    if not api_key:
        print("You need unfortunately an API key to compare both translations.")
        return

    verses = verse.get("verses", [])

    if len(verses) != 1:
        print("One verse at a time please :)")
        return

    try:
        name, text = compare_verse(verses[0], api_key)

        print(f"\n{verse['reference']} - {name}")
        print("-" * 45)
        print(" ".join(text.split()))

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        print("Sorry, could not compare the following verses:", error)
 


# I made a simple table to show the available Bible verses that are able to be retrieved. 
def choose_verse(bible_verses):
    print("\nHere comes a list with available bible verses: ")
    number_of_verses = 1
    for reference, topic, description in bible_verses:
        print(f"{number}. {reference} - {topic} - {description}")
        number_of_verses = number_of_verses + 1
    
    chosen_verse = input("Choose a bible verse (Enter to go back or type a number): ")
    if chosen_verse == "":
        return 
    
    try:
        number = int(chosen_verse)
        if number >= 1 and number <= len(bible_verses):
            bible_verses_final = bible_verses[number - 1]
            read_verse(bible_verses_final[0])
        else:
            print("Kindly choose another bible verse from the list... ")
    except ValueError:
        print("Invalid bible verse (number). Please try again!")




# This is the main menu where the user chooses what to do.
def main():
    load_dotenv(dotenv_path=Path(__file__).with_name(".env"))
    api_key = os.getenv("API_BIBLE_KEY", "").strip()

    while True:
        print("\n========== Bible Verses ==========")
        print("1 Browse some Bible Verses")
        print("2 Explore by topics")
        print("3 Random Bible Verse")
        print("4 Compare Translations (English)")
        print("0 Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            choose_verse(VERSES)
        elif choice == "2":
            reference = input("Enter a verse (e.g. John 3:16): ").strip()
            if reference:
                read_verse(reference)
        elif choice == "3":
            reference, topic, description = random.choice(VERSES)
            print("Random verse:", reference)
            read_verse(reference)
        elif choice == "4":
            reference = input("Verse to compare (e.g. John 3:16): ").strip()
            if reference:
                read_verse(reference, compare=True, api_key=api_key)
        else:
            print("Invalid choice. Choose a number from 0 to 4.")

        input("--- Press Enter to return to the menu ... ")

main()
