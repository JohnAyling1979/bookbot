def number_of_words(content):
  return len(content.split())

def get_character_count(content):
  characters = {}

  for word in content.split():
    for letter in list(word):
      lower_letter = letter.lower()
      if lower_letter in characters:
        characters[lower_letter] += 1
      else:
        characters[lower_letter] = 1

  return characters

def sort_dict(characters):
  sorted_list = []
  for letter in characters:
    sorted_list.append({"char": letter, "num": characters[letter]})

  return sorted(sorted_list, key=lambda item: item["num"], reverse=True)
