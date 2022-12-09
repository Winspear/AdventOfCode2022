def main():
    """
    --- Day 8: Treetop Tree House ---

    The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

    First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

    The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

    30373
    25512
    65332
    33549
    35390

    Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

    A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

    All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

        The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
        The top-middle 5 is visible from the top and right.
        The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
        The left-middle 5 is visible, but only from the right.
        The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
        The right-middle 3 is visible from the right.
        In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

    With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

    Consider your map; how many trees are visible from outside the grid?
        --- Part Two ---

    Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

    To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

    The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

    In the example above, consider the middle 5 in the second row:

    30373
    25512
    65332
    33549
    35390

        Looking up, its view is not blocked; it can see 1 tree (of height 3).
        Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
        Looking right, its view is not blocked; it can see 2 trees.
        Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

    A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

    However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

    30373
    25512
    65332
    33549
    35390

        Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
        Looking left, its view is not blocked; it can see 2 trees.
        Looking down, its view is also not blocked; it can see 1 tree.
        Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

    This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

    Consider each tree on your map. What is the highest scenic score possible for any tree?

        """

    forest_matrix = []
    visible_trees = []
    forest_matrix_transposed = []
    visible_trees_transposed = []
    viewing_distances = []
    viewing_distances_transposed = []
    visible_count = 0
    with open('trees_test.txt', 'r') as tree_file:
        for line_of_trees in tree_file.readlines():
            tree_row = [int(tree) for tree in line_of_trees.strip()]
            forest_matrix.append(tree_row)
        initialise_other_matrices(forest_matrix, visible_trees, forest_matrix_transposed, visible_trees_transposed, viewing_distances, viewing_distances_transposed)
        get_visible_trees(forest_matrix, visible_trees)
        get_visible_trees(forest_matrix, visible_trees, is_reversed=True)
        get_viewing_distances(forest_matrix, viewing_distances)
        get_viewing_distances(forest_matrix, viewing_distances, is_reversed=True)
        transpose_matrix(forest_matrix, forest_matrix_transposed)
        transpose_matrix(visible_trees, visible_trees_transposed)
        transpose_matrix(viewing_distances, viewing_distances_transposed)
        get_visible_trees(forest_matrix_transposed, visible_trees_transposed)
        get_visible_trees(forest_matrix_transposed, visible_trees_transposed, is_reversed=True)
        get_viewing_distances(forest_matrix_transposed, viewing_distances_transposed)
        get_viewing_distances(forest_matrix_transposed, viewing_distances_transposed, is_reversed=True)

        for row in visible_trees_transposed:
            for item in row:
                if item == 'y':
                    visible_count += 1
        print(visible_count)
        print(viewing_distances)


def initialise_other_matrices(forest_matrix, visible_trees, forest_matrix_transposed, visible_trees_transposed, viewing_distances, viewing_distances_transposed):
    for row in forest_matrix:
        visible_tree_row = []
        forest_matrix_transposed_row = []
        visible_trees_transposed_row = []
        viewing_distances_row = []
        viewing_distances_transposed_row = []
        for tree in row:
            visible_tree_row.append('x')
            forest_matrix_transposed_row.append('0')
            visible_trees_transposed_row.append('0')
            viewing_distances_row.append(1)
            viewing_distances_transposed_row.append(1)
        visible_trees.append(visible_tree_row)
        forest_matrix_transposed.append(forest_matrix_transposed_row)
        visible_trees_transposed.append(visible_trees_transposed_row)
        viewing_distances.append(viewing_distances_row)
        viewing_distances_transposed.append(viewing_distances_transposed_row)

    for index in range(len(visible_trees[0])):
        visible_trees[0][index] = 'y'
    for index in range(len(visible_trees[0])):
        visible_trees[-1][index] = 'y'

def get_visible_trees(forest_matrix, visible_trees, is_reversed=False):
    if not is_reversed:
        iterator = range(len(visible_trees[0]))
    else:
        iterator = list(reversed(range(len(visible_trees[0]))))
    for row_index in range(len(visible_trees[0])):
        previous_tree = None
        for column_index in iterator:
            if previous_tree == None:
                visible_trees[row_index][column_index] = 'y'
                previous_tree = forest_matrix[row_index][column_index]
            elif forest_matrix[row_index][column_index] > previous_tree:
                visible_trees[row_index][column_index] = 'y'
                previous_tree = forest_matrix[row_index][column_index]
            elif forest_matrix[row_index][column_index] <= previous_tree:
                continue

def get_viewing_distances(forest_matrix, viewing_distances, is_reversed=False):
    if not is_reversed:
        iterator = range(len(viewing_distances[0]))
    else:
        iterator = list(reversed(range(len(viewing_distances[0]))))
    for row_index in range(len(forest_matrix[0])):
        previous_tree = None
        for column_index in iterator:
            if previous_tree == None:
                viewing_distances[row_index][column_index] *= 0
                previous_tree = forest_matrix[row_index][column_index]
            elif forest_matrix[row_index][column_index] > previous_tree:
                viewing_distances[row_index][column_index] *= how_many_trees_before_next_blocker(forest_matrix, row_index, column_index, is_reversed)
            elif forest_matrix[row_index][column_index] <= previous_tree:
                continue


def how_many_trees_before_next_blocker(forest_matrix, row_index, column_index, is_reversed):
    multiplier = 1
    try:
        while True:
            start_tree = forest_matrix[row_index][column_index]
            if not is_reversed:
                next_tree = forest_matrix[row_index][column_index + multiplier]
            else:
                if column_index - multiplier >= 0:
                    next_tree = forest_matrix[row_index][column_index - multiplier]
                else:
                    return multiplier
            if start_tree > next_tree:
                multiplier += 1
            else:
                return multiplier
    except IndexError:
        return multiplier - 1

def transpose_matrix(matrix, transposed_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]

            
 
if __name__ == "__main__":
    main()