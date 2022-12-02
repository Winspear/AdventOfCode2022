def main():
    """
    --- Day 2: Rock Paper Scissors ---

    The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

    Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

    Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

    The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

    The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

    For example, suppose you were given the following strategy guide:

    A Y
    B X
    C Z

    This strategy guide predicts and recommends the following:

        In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
        In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
        The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

    In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

    What would your total score be if everything goes exactly according to your strategy guide?
    """
    total_score = 0
    with open('rock_paper_scissors.txt', 'r') as inputs:
        for line in inputs.readlines():
            elf_input, player_input = line.split()
            elf_input = convert_symbols(elf_input)
            player_input = convert_symbols(player_input)

            round_score = decide_winner(elf_input, player_input)
            input_score = get_input_score(player_input)
            total_score += round_score + input_score
    print(f'Total Score is {total_score}')

def main_2():
    """
    --- Part Two ---

    The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

    The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

        In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
        In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
        In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

    Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

    Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
    """
    total_score = 0
    with open('rock_paper_scissors.txt', 'r') as inputs:
        for line in inputs.readlines():
            elf_input, player_raw_input = line.split()
            elf_input = convert_symbols(elf_input)
            desired_player_outcome = convert_to_outcome(player_raw_input)
            player_input = choose_player_action(elf_input, desired_player_outcome)

            round_score = decide_winner(elf_input, player_input)
            input_score = get_input_score(player_input)
            total_score += round_score + input_score
    print(f'Total Score is {total_score}')






def decide_winner(elf_input, player_input):
    if elf_input == player_input:
        return 3
    elif elf_input == 'Rock':
        return 0 if player_input == 'Scissors' else 6
    elif elf_input == 'Paper':
        return 0 if player_input == 'Rock' else 6
    elif elf_input == 'Scissors':
        return 0 if player_input == 'Paper' else 6
    else:
        raise Exception(f'Unexpected inputs - Expected one of Rock/Paper/Scissors but received {elf_input}, {player_input}') 

def get_input_score(player_input):
    match player_input:
        case "Rock":
            return 1
        case "Paper":
            return 2
        case "Scissors":
            return 3

def convert_symbols(symbol):
    match symbol:
        case "A" | "X":
            return "Rock"
        case "B" | "Y":
            return "Paper"
        case "C" | "Z":
            return "Scissors"

def convert_to_outcome(symbol):
    match symbol:
        case "X":
            return "Lose"
        case "Y":
            return "Draw"
        case "Z":
            return "Win"

def choose_player_action(elf_input, desired_player_outcome):
    if desired_player_outcome == "Draw":
        return elf_input
    else:
        if elf_input == "Rock":
            match desired_player_outcome:
                case "Lose":
                    return "Scissors"
                case "Win":
                    return "Paper"
        elif elf_input == "Paper":
            match desired_player_outcome:
                case "Lose":
                    return "Rock"
                case "Win":
                    return "Scissors"
        elif elf_input == "Scissors":
            match desired_player_outcome:
                case "Lose":
                    return "Paper"
                case "Win":
                    return "Rock"




if __name__ == "__main__":
    which_task = input('Enter 1 or 2 for the problem you are solving:')
    if which_task == '1':
        main()
    elif which_task == '2':
        main_2()
    else:
        print("Not a valid input")