import random
import art
import hangman_words
    
print(art.logo)
lives = 6
selected_word = random.choice(hangman_words.word_list)
display = []
length = len(selected_word)
for i in range(len(selected_word)):
    display += "_"
print(display)
end = False
while end == False:
    guess = input("Guess a letter: ").lower()
    if guess in display:
            print(f"You have already guessed {guess}")
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if guess == letter:
            display[position] = guess
             
    if guess not in selected_word :
        lives -= 1
        print("This letter is not in the word. You lose a life.")
        print(art.stages[lives])
    print(display)
    if lives == 0:
        print("You Lose")

        break
    elif "_" not in display:
        end = True 
        print(f"".join(display),"was the word") 
        print("You win")
        