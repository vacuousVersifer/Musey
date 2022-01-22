from musescore_scraper import MuseScraper

root_path = "C:/Users/davis/OneDrive/Music/Sheet Music/"
root_url = "https://musescore.com/"

# (Fill this array with tuples with information on the peice)
# Format: (Name of Folder in root_path, URL of sheet music without the root_url part)
input = []

with MuseScraper() as ms:
  for index, tuple in enumerate(input):
    output_location = root_path + tuple[0]
    url = root_url + tuple[1]
    ms.to_pdf(url, output=output_location)

# It can time out, simply remove the peices it completed and run again