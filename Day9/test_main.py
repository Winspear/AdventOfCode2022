import unittest
import main


class TestMoveHeadAndTail(unittest.TestCase):
    def test_circular_head_moves_dont_move_tail(self):
        head_position = {0:0}
        tail_position = {0:0}
        tail_positions = set()
        tail_positions.add(tuple({0:0}.items()))
        text_input = "R 1, U 1, L 2, D 2, R 2, U 2"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                old_head_position = head_position
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(old_head_position, head_position, tail_position)
                tail_positions.add(tuple(tail_position.items()))
        self.assertEqual(tail_positions, {((0, 0),)})

    def test_diagonal_right_ladder_movements(self):
        head_position = {0:0}
        tail_position = {0:0}
        tail_positions = set()
        tail_positions.add(tuple({0:0}.items()))
        text_input = "U 1, R 1, U 1, R 1, U 1, R 1"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                old_head_position = head_position
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(old_head_position, head_position, tail_position)
                tail_positions.add(tuple(tail_position.items()))
        self.assertEqual(tail_positions, {((0, 0),), ((1, 1),), ((2, 2),)})

    def test_diagonal_left_ladder_movements(self):
        # ....Y
        # ...Y.
        # ..Y..
        # .Y...
        # .....
        # .....
        # .....
        # .....
        # .....
        # .....
        head_position = {0:0}
        tail_position = {0:0}
        tail_positions = set()
        tail_positions.add(tuple({0:0}.items()))
        text_input = "D 1, L 1, D 1, L 1, D 1, L 1"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                old_head_position = head_position
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(old_head_position, head_position, tail_position)
                tail_positions.add(tuple(tail_position.items()))
        self.assertEqual(tail_positions, {((0, 0),), ((-1, -1),), ((-2, -2),)})

    def test_long_diagonal_movements(self):
        # .....
        # .....
        # .....
        # .....
        # ...Y.
        # ...Y.
        # .YY..
        # Y....
        # Y....
        # .....
        head_position = {0:0}
        tail_position = {0:0}
        tail_positions = set()
        tail_positions.add(tuple({0:0}.items()))
        text_input = "U 3, R 3, U 3"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                old_head_position = head_position
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(old_head_position, head_position, tail_position)
                tail_positions.add(tuple(tail_position.items()))
        self.assertEqual(tail_positions, {((0, 0),), ((0, 1),), ((0, 2),), ((1, 3),), ((2, 3),), ((3, 4),), ((3, 5),)})





if __name__ == '__main__':
    unittest.main()







