from itertools import zip_longest
def main():
    """--- Day 5: Supply Stacks ---

    The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

    The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

    The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

    They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3 

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2

    In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

    Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

    [D]        
    [N] [C]    
    [Z] [M] [P]
     1   2   3 

    In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

            [Z]
            [N]
        [C] [D]
        [M] [P]
     1   2   3

    Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

            [Z]
            [N]
    [M]     [D]
    [C]     [P]
     1   2   3

    Finally, one crate is moved from stack 1 to stack 2:

            [Z]
            [N]
            [D]
    [C] [M] [P]
     1   2   3

    The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    with open('stacks_test.txt', 'r') as crates:
        crate_diagram = []
        instructions = []
        for line in crates:
            crate_diagram.append(line)
            if line == "\n":
                break
        for line in crates:
            instructions.append(line)
        all_columns = list(zip_longest(*[line for line in crate_diagram], fillvalue=''))
        crate_stacks = get_crate_stacks(all_columns)
        final_state = follow_instructions(crate_stacks, instructions)
        top_configuration = ''.join([crate_stack[0] for crate_stack in final_state])
    print(f'The top of all the crates is {top_configuration}')


def follow_instructions(crate_stacks: list, instructions: list, move_crates_one_at_a_time=True):
    for line in instructions:
        split_line = line.split(' ')
        # Create a list similar to [1, 2, 3] where the first element is the number of crates to move, the second the stack to move from,
        # and the third the target crate stack
        instructions = [int(split_line[1]), int(split_line[3]), int(split_line[5].replace('\n', ''))]
        crate_stack_to_move_from = crate_stacks[instructions[1] - 1]
        target_crate_stack = crate_stacks[instructions[2] - 1]
        if move_crates_one_at_a_time:
            for i in range(instructions[0]):
                crate = crate_stack_to_move_from.pop(0)
                target_crate_stack.insert(0, crate)
        else:
            print(crate_stack_to_move_from, ' moving from this')
            print(target_crate_stack, ' moving to this')
            crates = crate_stack_to_move_from[0:instructions[0]]
            print('moving these crates ', crates)
            del crate_stack_to_move_from[0:instructions[0]]
            print(crate_stack_to_move_from, ' now its moved, stack is this')
            crate_stacks[instructions[2] - 1] = crates + crate_stacks[instructions[2] - 1]
            print(crate_stacks[instructions[2] - 1], ' now its moved, target is this')
    return crate_stacks


def get_crate_stacks(all_columns: list):
    crate_stacks = []
    for item in all_columns:
        for element in item:
            if element.isdigit():
                crate_stacks.append([element for element in item if element.strip() != ''])
    return crate_stacks


def main_2():
    """
    As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

    Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

    The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

    Again considering the example above, the crates begin in the same configuration:

        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3 

    Moving a single crate from stack 2 to stack 1 behaves the same as before:

    [D]        
    [N] [C]    
    [Z] [M] [P]
     1   2   3 

    However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

            [D]
            [N]
        [C] [Z]
        [M] [P]
     1   2   3

    Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

            [D]
            [N]
    [C]     [Z]
    [M]     [P]
     1   2   3

    Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

            [D]
            [N]
            [Z]
    [M] [C] [P]
     1   2   3

    In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

    Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    with open('stacks.txt', 'r') as crates:
        crate_diagram = []
        instructions = []
        for line in crates:
            crate_diagram.append(line)
            if line == "\n":
                break
        for line in crates:
            instructions.append(line)
        all_columns = list(zip_longest(*[line for line in crate_diagram], fillvalue=''))
        crate_stacks = get_crate_stacks(all_columns)
        final_state = follow_instructions(crate_stacks, instructions, move_crates_one_at_a_time=False)
        top_configuration = ''.join([crate_stack[0] for crate_stack in final_state])
    print(f'The top of all the crates is {top_configuration}')


if __name__ == "__main__":
    which_task = input('Enter 1 or 2 for the problem you are solving:')
    if which_task == '1':
        main()
    elif which_task == '2':
        main_2()
    else:
        print("Not a valid input")
	