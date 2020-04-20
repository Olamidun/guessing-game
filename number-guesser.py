def level_determinant():
    level_check = input("Enter easy, medium, or hard to choose a level: ")
    if level_check == 'easy':
        def easy_level():
            secret_number = 9
            guess_count = 0
            guess_limit = 6
            number_of_guesses_left = 6
            while guess_count < guess_limit:
                try:
                    user_guess = int(input('Enter guess number: '))
                    guess_count += 1
                    number_of_guesses_left -= 1
                    if user_guess in range(1, 11):
                        if user_guess == secret_number:
                            print('You got it right!')
                            break
                        else:
                            print(f'That was wrong, you have {number_of_guesses_left} guess(es) left')
                    else:
                        print('Please enter a number between 1-10')
                except ValueError:
                    number_of_guesses_left = number_of_guesses_left
                    print('Please make sure you enter an integer')
            else:
                print('Game over!')
        easy_level()
    elif level_check == 'medium':
        def medium_level():
            secret_number = 15
            guess_medium = 0
            guess_limit_medium = 4
            number_of_guesses_left = 4
            while guess_medium < guess_limit_medium:
                try:
                    user_guess = int(input('Enter guess number: '))
                    guess_medium += 1
                    number_of_guesses_left -= 1
                    if user_guess in range(1, 21):
                        if user_guess == secret_number:
                            print('You got it right!')
                            break
                        else:
                            print(f'That was wrong, you have {number_of_guesses_left} guess(es) left')
                except ValueError:
                    number_of_guesses_left = number_of_guesses_left
                    print('Please make sure you enter a number')
            else:
                print('Game over!')
        medium_level()
    elif level_check == 'hard':
        def hard_level():
            secret_number = 35
            guesses_count_hard = 0
            guess_limit_hard = 3
            number_of_guesses_left = 3
            while guesses_count_hard < guess_limit_hard:
                try:
                    user_guess = int(input('Enter guess number: '))
                    guesses_count_hard += 1
                    number_of_guesses_left -= 1
                    if user_guess in range(1, 51):
                        if user_guess == secret_number:
                            print('You got it right')
                            break
                        else:
                            print(f'That was wrong!, you have {number_of_guesses_left} guess(es) left')
                except ValueError:
                    number_of_guesses_left = number_of_guesses_left
                    print('Please make sure you enter a number')
            else:
                print('Game over!')
        hard_level()
    else:
        print('Rerun the code to enter the valid level value')


level_determinant()

