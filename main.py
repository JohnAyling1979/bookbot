import sys
from stats import number_of_words, get_character_count, sort_dict

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def print_nicely(file, word_count, characters):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for character in characters:
    if (character["char"].isalpha()):
      print(f"{character['char']}: {character['num']}")
  print("============= END ===============")

def main():
  if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

  file = sys.argv[1]
  content = get_book_text(file)
  wc = number_of_words(content)
  cc = sort_dict(get_character_count(content))

  print_nicely(file, wc, cc)

main()
