import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestInitialise(unittest.TestCase):
    def setUp(self):
        self.small_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.large_matrix = [list(range(100)) for item in range(100)]

    def test_initialise_returns_matrix_of_equal_sizes(self):
        test_matrix_1 = []
        test_matrix_2 = []
        test_matrix_3 = []
        main.initialise_other_matrices(self.small_matrix, test_matrix_1, test_matrix_2, test_matrix_3)
        self.assertEqual(len(self.small_matrix), len(test_matrix_1))
        self.assertEqual(len(self.small_matrix), len(test_matrix_2))
        self.assertEqual(len(self.small_matrix), len(test_matrix_3))
        self.assertEqual(len(self.small_matrix[0]), len(test_matrix_1[0]))
        self.assertEqual(len(self.small_matrix[0]), len(test_matrix_2[0]))
        self.assertEqual(len(self.small_matrix[0]), len(test_matrix_3[0]))
        main.initialise_other_matrices(self.large_matrix, test_matrix_1, test_matrix_2, test_matrix_3)


class TestTranspose(unittest.TestCase):
    def setUp(self):
        self.small_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.large_matrix = [list(range(100)) for item in range(100)]

    def test_transpose_matrix(self):
        transposed_small_matrix = []
        transposed_big_matrix = []
        test_matrix_3 = []
        main.initialise_other_matrices(self.small_matrix, transposed_small_matrix, transposed_big_matrix, test_matrix_3)
        main.transpose_matrix(self.small_matrix, transposed_small_matrix)
        self.assertEqual(transposed_small_matrix, [[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        transposed_small_matrix = []
        transposed_big_matrix = []
        test_matrix_3 = []
        main.initialise_other_matrices(self.large_matrix, transposed_small_matrix, transposed_big_matrix, test_matrix_3)
        main.transpose_matrix(self.large_matrix, transposed_big_matrix)
        self.assertEqual(transposed_big_matrix[0], [0 for item in range(100)])
        self.assertEqual(transposed_big_matrix[30], [30 for item in range(100)])


class TestVisibleTrees(unittest.TestCase):
    def test_outside_trees_always_visible(self):
        test_matrix = [[9, 5, 5, 5, 5, 5, 5, 7] for i in range(8)]
        visible_trees = [list('x' * 8) for i in range(8)]
        main.get_visible_trees(test_matrix, visible_trees)
        for row in visible_trees:
            self.assertEqual(row[0], 'y')


    def test_large_tree_on_outside_blocks_all_later_trees(self):
        test_matrix = [[9, 5, 5, 5, 5, 5, 5, 7] for i in range(8)]
        visible_trees = [list('x' * 8) for i in range(8)]
        main.get_visible_trees(test_matrix, visible_trees)
        expected_first_row = ['y', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
        self.assertEqual(visible_trees[0], expected_first_row)

    def test_medium_tree_on_outside_blocks_smaller_trees_but_larger_trees_visible(self):
        test_matrix = [[4, 3, 3, 2, 8, 9, 5, 5] for i in range(8)]
        visible_trees = [list('x' * 8) for i in range(8)]
        main.get_visible_trees(test_matrix, visible_trees)
        expected_first_row = ['y', 'x', 'x', 'x', 'y', 'y', 'x', 'x']
        self.assertEqual(visible_trees[0], expected_first_row)


    def all_visible_if_sequentially_higher_than_the_last(self):
        test_matrix = [[1, 2, 3, 4, 5, 6, 7, 8] for i in range(8)]
        visible_trees = [list('x' * 8) for i in range(8)]
        main.get_visible_trees(test_matrix, visible_trees)
        expected_first_row = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
        

main.transpose_matrix
if __name__ == '__main__':
    unittest.main()