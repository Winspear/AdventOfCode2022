import unittest
import main

class TestInitialise(unittest.TestCase):
    def setUp(self):
        self.small_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.large_matrix = [list(range(100)) for item in range(100)]

    def test_initialise_returns_matrix_of_equal_sizes(self):
        test_matrix_1 = []
        test_matrix_2 = []
        test_matrix_3 = []
        test_matrix_4 = []
        test_matrix_5 = []
        test_matrix_6 = []
        main.initialise_other_matrices(self.small_matrix, test_matrix_1, test_matrix_2, test_matrix_3, test_matrix_4, test_matrix_5)
        self.assertEqual(len(self.small_matrix), len(test_matrix_1))
        self.assertEqual(len(self.small_matrix), len(test_matrix_2))
        self.assertEqual(len(self.small_matrix), len(test_matrix_3))
        self.assertEqual(len(self.small_matrix[0]), len(test_matrix_1[0]))
        self.assertEqual(len(self.small_matrix[0]), len(test_matrix_2[0]))
        self.assertEqual(len(self.small_matrix[0]), len(test_matrix_3[0]))
        main.initialise_other_matrices(self.large_matrix, test_matrix_1, test_matrix_2, test_matrix_3, test_matrix_4, test_matrix_5)


class TestTranspose(unittest.TestCase):
    def setUp(self):
        self.small_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.large_matrix = [list(range(100)) for item in range(100)]

    def test_transpose_matrix(self):
        transposed_small_matrix = []
        transposed_big_matrix = []
        test_matrix_3 = []
        viewing_distances = []
        viewing_distances_transposed = []
        main.initialise_other_matrices(self.small_matrix, transposed_small_matrix, transposed_big_matrix, test_matrix_3, viewing_distances, viewing_distances_transposed)
        main.transpose_matrix(self.small_matrix, transposed_small_matrix)
        self.assertEqual(transposed_small_matrix, [[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        transposed_small_matrix = []
        transposed_big_matrix = []
        test_matrix_3 = []
        main.initialise_other_matrices(self.large_matrix, transposed_small_matrix, transposed_big_matrix, test_matrix_3, viewing_distances, viewing_distances_transposed)
        main.transpose_matrix(self.large_matrix, transposed_big_matrix)
        self.assertEqual(transposed_big_matrix[0], [0 for item in range(100)])
        self.assertEqual(transposed_big_matrix[30], [30 for item in range(100)])


class TestVisibleTrees(unittest.TestCase):
    def setUp(self):
        self.visible_trees = [list('x' * 8) for i in range(8)]
        self.viewing_distances = [[1 for i in range(8)] for i in range(8)]

    def test_outside_trees_always_visible(self):
        test_matrix = [[9, 5, 5, 5, 5, 5, 5, 7] for i in range(8)]
        main.get_visible_trees(test_matrix, self.visible_trees)
        for row in self.visible_trees:
            self.assertEqual(row[0], 'y')

    def test_large_tree_on_outside_blocks_all_later_trees(self):
        test_matrix = [[9, 5, 5, 5, 5, 5, 5, 7] for i in range(8)]
        main.get_visible_trees(test_matrix, self.visible_trees)
        expected_first_row = ['y', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
        self.assertEqual(self.visible_trees[0], expected_first_row)

    def test_medium_tree_on_outside_blocks_smaller_trees_but_larger_trees_visible(self):
        test_matrix = [[4, 3, 3, 2, 8, 9, 5, 5] for i in range(8)]
        visible_trees = [list('x' * 8) for i in range(8)]
        main.get_visible_trees(test_matrix, self.visible_trees)
        expected_first_row = ['y', 'x', 'x', 'x', 'y', 'y', 'x', 'x']
        self.assertEqual(self.visible_trees[0], expected_first_row)

    def test_all_visible_if_sequentially_higher_than_the_last(self):
        test_matrix = [[1, 2, 3, 4, 5, 6, 7, 8] for i in range(8)]
        visible_trees = [list('x' * 8) for i in range(8)]
        main.get_visible_trees(test_matrix, self.visible_trees)
        expected_first_row = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
        self.assertEqual(self.visible_trees[0], expected_first_row)

class TestViewingDistances(unittest.TestCase):
    def setUp(self):
        self.viewing_distances = [[1 for i in range(8)] for i in range(8)]

    def test_outside_trees_return_0_viewing_distance(self):
        test_matrix = [[9, 5, 5, 5, 5, 5, 5, 7] for i in range(8)]
        expected_first_row = [0, 1, 1, 1, 1, 1, 1, 1]
        main.get_viewing_distances(test_matrix, self.viewing_distances)
        self.assertEqual(self.viewing_distances[0], expected_first_row)

    def test_inside_trees_blocked_on_all_sides_returns_1(self):
        test_matrix = [[9, 9, 9, 9, 9, 9, 9, 9] for i in range(8)]
        expected_second_row = [0, 1, 1, 1, 1, 1, 1, 1]
        main.get_viewing_distances(test_matrix, self.viewing_distances)
        self.assertEqual(self.viewing_distances[1], expected_second_row)

    def test_inside_trees_with_multiple_trees_visible_returns_higher_multiplicative(self):
        test_matrix = [[1, 2, 3, 4, 3, 2, 1, 1] for i in range(8)]
        expected_second_row = [0, 1, 1, 4, 3, 2, 1, 1]
        main.get_viewing_distances(test_matrix, self.viewing_distances)
        self.assertEqual(self.viewing_distances[1], expected_second_row)

    def test_multiplers_stack_when_going_left_and_right(self):
        test_matrix = [[1, 1, 1, 5, 4, 3, 2, 1]]
        expected = [0, 1, 1, 12, 3, 2, 1, 0]
        main.get_viewing_distances(test_matrix, self.viewing_distances)
        main.get_viewing_distances(test_matrix, self.viewing_distances, is_reversed=True)
        self.assertEqual(self.viewing_distances[0], expected)


if __name__ == '__main__':
    unittest.main()