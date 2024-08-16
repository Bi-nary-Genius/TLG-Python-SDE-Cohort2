#!/usr/bin/python3
import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character: ")
    data = requests.get(f"{AOIF_CHAR}{got_charToLookup}").json()

    name = data["name"] or data["aliases"][0]
    book_titles = [requests.get(url).json()["name"] for url in data["books"] + data["povBooks"]]
    house_titles = [requests.get(url).json()["name"] for url in data["allegiances"]]

    print(f"NAME: {name}")
    print("BOOKS:")
    for book in book_titles:
        print(f"• {book}")

    if house_titles:
        print("HOUSES:")
        for house in house_titles:
            print(f"• {house}")

if __name__ == "__main__":
    main()

