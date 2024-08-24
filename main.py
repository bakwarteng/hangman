import random

def print_hangman(wrong):
    stages = [
        "\n+---+\n   |   \n   |   \n   |   \n   ===",
        "\n+---+\n O   | \n   |   \n   |   \n   ===",
        "\n+---+\n O   | \n |   | \n   |   \n   ===",
        "\n+---+\n O   | \n/|   | \n   |   \n   ===",
        "\n+---+\n O   | \n/|\\  | \n   |   \n   ===",
        "\n+---+\n O   | \n/|\\  | \n/    | \n   ===",
        "\n+---+\n O   | \n/|\\  | \n/ \\  | \n   ==="
    ]
    print(stages[wrong])

def print_word(word, guessed_letters):
    return ''.join(c if c in guessed_letters else '_' for c in word)

print("Welcome to Hangman")
print("-----------------")

wordDictionary = ["sunflower", "diamond", "dog", "rose", "elephant", "ruby", "music", "pizza", "queso", "movie", "hamster", "hello", "goodbye", "vacation", "homework"]

# Choose a random word
randomWord = random.choice(wordDictionary)
length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
max_attempts = 6
guessed_letters = set()

print("\n" + "_" * length_of_word_to_guess)

while amount_of_times_wrong < max_attempts:
    print("\nLetters guessed so far: " + ', '.join(sorted(guessed_letters)))
    
    letterGuessed = input("Guess a letter: ").lower()

    if len(letterGuessed) != 1 or not letterGuessed.isalpha():
        print("Please enter a single valid letter.")
        continue

    if letterGuessed in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(letterGuessed)

    if letterGuessed in randomWord:
        print("Good guess!")
    else:
        amount_of_times_wrong += 1
        print("Incorrect guess.")
    
    print_hangman(amount_of_times_wrong)
    current_word_display = print_word(randomWord, guessed_letters)
    print(current_word_display)

    # Check if the word is completely guessed
    if set(randomWord) == guessed_letters:
        print("Congratulations! You've guessed the word!")
        break

if amount_of_times_wrong == max_attempts:
    print(f"Game over. The word was '{randomWord}'. Thanks for playing :)")









