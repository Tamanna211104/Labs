import requests

# AniList API URL
url = "https://graphql.anilist.co"

# Genre options
genre_options = ["action", "romance", "drama", "comedy"]

# Prompt the user to enter their genre preference
print("Please select your genre preference: ")
for index, genre in enumerate(genre_options):
    print(f"{index + 1}. {genre.title()}")
selection = int(input("Enter the number corresponding to your genre preference: "))

# GraphQL query to retrieve anime titles based on genre
query = """
query ($genre: String) {
  Page {
    media (type: ANIME, genre: $genre, sort: POPULARITY_DESC) {
      title {
        romaji
      }
    }
  }
}
"""

# Variables for the query
variables = {
    "genre": genre_options[selection-1].lower()
}

# Make a POST request to the AniList API
response = requests.post(url, json={'query': query, 'variables': variables})

# Convert the response to JSON format
data = response.json()

# List to store anime suggestions
suggestions = []

# Loop through the anime titles and add them to the list of suggestions
for anime in data['data']['Page']['media']:
    suggestions.append(anime['title']['romaji'])

# Print the list of anime suggestions
if len(suggestions) == 0:
    print("No anime found for your selected genre.")
else:
    print(f"Here are some anime suggestions based on your selected genre ({genre_options[selection-1]}):")
    for suggestion in suggestions:
        print(suggestion)
