import os
import glob

check = 1
while check > 0:
    path = input("\nEnter the directory of lyrics: ")
    if os.path.isdir(path):
        check -= 1
    else:
        print("Folder does not exist. Try again.")

list_of_paths = []

for song in glob.glob(path + "\\*"):
    list_of_paths.append(song)

number_of_songs = len(list_of_paths)

artists = []
songs = []
years = []
for i in range(number_of_songs):
    ending = list_of_paths[i].split("\\")[-1]
    artists.append(ending.split(" -")[0])
    songs.append((ending.split("- ")[1]).split(" (")[0])
    years.append((ending.split("(")[1]).split(")")[0])

songs_dictionary = {}
songs_dictionary["artist"] = artists
songs_dictionary["name"] = songs
songs_dictionary["year"] = years

print("Songs in the list:")
for i in range(number_of_songs):
    print('"' + songs_dictionary["name"][i] + '" by ' + songs_dictionary["artist"][i] + " (" + songs_dictionary["year"][i] + ")")

print("\nWhich is most unique? Which is most repetitive?\n")

lyrics = []
for i in range(number_of_songs):
    lyrics_file = open(list_of_paths[i], "r")
    whole_text = ""
    for line in lyrics_file:
        line = line.rstrip().split()
        strline = ""
        for word in line:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace("!", "")
            word = word.replace("?", "")
            word = word.replace("\'", "")
            word = word.replace("\"", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            strline += " " + word.lower()
        whole_text += strline
    lyrics.append(whole_text)

number_of_words = []
for i in range(number_of_songs):
    text_lenght = len(lyrics[i].split())
    number_of_words.append(text_lenght)

all_words_count = {}
number_of_unique_words = []
for i in range(number_of_songs):
    for word in lyrics[i].split():
        if word in all_words_count:
            all_words_count[word] += 1
        else:
            all_words_count[word] = 1
    unique_words = len(all_words_count)   
    all_words_count = {}
    number_of_unique_words.append(unique_words)

uniqueness = []
for i in range(number_of_songs):
    percentage = number_of_unique_words[i] / number_of_words[i]
    uniqueness.append(percentage)

average = sum(uniqueness) / len(uniqueness)

print("The uniqueness of analyzed " + str(number_of_songs) + " songs is " 
+ str(int(round(average, 2) * 100)) + "% on average.")
print()
print()

most_unique = max(uniqueness)
most_repetitive = min(uniqueness)
unique_address = uniqueness.index(most_unique)
repetitive_address = uniqueness.index(most_repetitive)

#unikalumo vidurkis

print('The most unique song is "' + songs_dictionary["name"][unique_address] + '" by ' 
+ songs_dictionary["artist"][unique_address] + " (" + songs_dictionary["year"][unique_address] 
+ "). Percentage of unique words is "
+ str(int(round(uniqueness[unique_address], 2) * 100)) + "%.")

print()

print('The most repetitive song is "' + songs_dictionary["name"][repetitive_address] + '" by ' 
+ songs_dictionary["artist"][repetitive_address] + " (" + songs_dictionary["year"][repetitive_address] 
+ "). Percentage of unique words is "
+ str(int(round(uniqueness[repetitive_address], 2) * 100)) + "%.")

class Songs:
    def __init__(self, artist, song, year, lyrics):
        self.artist = artist
        self.song = song
        self.year = year
        self.lyrics = lyrics


