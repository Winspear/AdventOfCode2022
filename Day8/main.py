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
    """

    forest_matrix = []
    visible_trees = []
    forest_matrix_transposed = []
    visible_trees_transposed = []
    visible_count = 0
    with open('trees_test.txt', 'r') as tree_file:
        for line_of_trees in tree_file.readlines():
            tree_row = [int(tree) for tree in line_of_trees.strip()]
            forest_matrix.append(tree_row)
        initialise_other_matrices(forest_matrix, visible_trees, forest_matrix_transposed, visible_trees_transposed)
        visible_from_left(forest_matrix, visible_trees)
        visible_from_right(forest_matrix, visible_trees)
        transpose_matrix(forest_matrix, forest_matrix_transposed)
        transpose_matrix(visible_trees, visible_trees_transposed)
        visible_from_left(forest_matrix_transposed, visible_trees_transposed)
        visible_from_right(forest_matrix_transposed, visible_trees_transposed)

        for row in visible_trees_transposed:
            for item in row:
                if item == 'y':
                    visible_count += 1
        print(visible_count)


def initialise_other_matrices(forest_matrix, visible_trees, forest_matrix_transposed, visible_trees_transposed):
    for row in forest_matrix:
        visible_tree_row = []
        forest_matrix_transposed_row = []
        visible_trees_transposed_row = []
        for tree in row:
            visible_tree_row.append('x')
            forest_matrix_transposed_row.append('0')
            visible_trees_transposed_row.append('0')
        visible_trees.append(visible_tree_row)
        forest_matrix_transposed.append(forest_matrix_transposed_row)
        visible_trees_transposed.append(visible_trees_transposed_row)

    for index in range(len(visible_trees[0])):
        visible_trees[0][index] = 'y'
    for index in range(len(visible_trees[0])):
        visible_trees[-1][index] = 'y'

def visible_from_left(forest_matrix, visible_trees):
    for row_index in range(len(forest_matrix)):
        previous_tree = None
        for item_index in range(len(visible_trees[0])):
            if previous_tree == None:
                visible_trees[row_index][item_index] = 'y'
                previous_tree = forest_matrix[row_index][item_index]
            elif forest_matrix[row_index][item_index] > previous_tree:
                visible_trees[row_index][item_index] = 'y'
                previous_tree = forest_matrix[row_index][item_index]
            elif forest_matrix[row_index][item_index] == previous_tree:
                continue
            else:
                break

def visible_from_right(forest_matrix, visible_trees):
    for row_index in range(len(forest_matrix)):
        previous_tree = None
        for item_index in reversed(range(len(visible_trees[0]))):
            if previous_tree == None:
                visible_trees[row_index][item_index] = 'y'
                previous_tree = forest_matrix[row_index][item_index]
            elif forest_matrix[row_index][item_index] > previous_tree:
                visible_trees[row_index][item_index] = 'y'
                previous_tree = forest_matrix[row_index][item_index]
            elif forest_matrix[row_index][item_index] == previous_tree:
                continue
            else:
                break

def transpose_matrix(matrix, transposed_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]

            
 
if __name__ == "__main__":
    main()