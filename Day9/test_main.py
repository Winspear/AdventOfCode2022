import unittest
import main


class TestMoveHeadAndTail(unittest.TestCase):
    def test_circular_head_moves_dont_move_tail(self):
        head_position = 0 + 0j
        tail_position = 0 + 0j
        tail_positions = set()
        tail_positions.add(tail_position)
        text_input = "R 1, U 1, L 2, D 2, R 2, U 2"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(head_position, tail_position)
                tail_positions.add(tail_position)
        self.assertEqual(tail_positions, {(0 + 0j)})

    def test_straight_up(self):
        head_position = 0 + 0j
        tail_position = 0 + 0j
        tail_positions = set()
        tail_positions.add(tail_position)
        text_input = "U 6"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(head_position, tail_position)
                tail_positions.add(tail_position)
        self.assertEqual(tail_positions, {0 + 0j, 0 + 1j, 0 + 2j, 0 + 3j, 0 + 4j, 0 + 5j})

    def test_diagonal_right_ladder_movements(self):
        head_position = 0 + 0j
        tail_position = 0 + 0j
        tail_positions = set()
        tail_positions.add(tail_position)
        text_input = "U 1, R 1, U 1, R 1, U 1, R 1"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(head_position, tail_position)
                tail_positions.add(tail_position)
        self.assertEqual(tail_positions, {0 + 0j, 1 + 1j, 2 + 2j})

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
        head_position = 0 + 0j
        tail_position = 0 + 0j
        tail_positions = set()
        tail_positions.add(tail_position)
        text_input = "D 1, L 1, D 1, L 1, D 1, L 1"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(head_position, tail_position)
                tail_positions.add(tail_position)
        self.assertEqual(tail_positions, {0 + 0j, -1 -1j,-2 -2j})

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
        # Y....
        head_position = 0 + 0j
        tail_position = 0 + 0j
        tail_positions = set()
        tail_positions.add(tail_position)
        text_input = "U 3, R 3, U 3"
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                head_position = main.move_head(direction, head_position)
                tail_position = main.move_tail(head_position, tail_position)
                tail_positions.add(tail_position)
        self.assertEqual(tail_positions, {0 + 0j, 0 + 1j, 0 + 2j, 1 + 3j, 2 + 3j, 3 + 4j, 3 + 5j})


class TestLongRopes(unittest.TestCase):
    # These tests incrementally test the examples provided in the description of part 2
    def test_R4(self):
        tail_positions = set()
        tail_positions.add(0 + 0j)
        text_input = "R 4"
        positions = [0 + 0j] * 10
        for item in text_input.split(','):
            direction, movements = item.split(" ")
            for i in range(int(movements)):
                for knot_index in range(len(positions)):
                    if knot_index == 0:
                        positions[0] = main.move_head(direction, positions[0])
                    else:
                        positions[knot_index] = main.move_tail(positions[knot_index - 1], positions[knot_index])
                        previous_head_position = positions[knot_index]
                        if knot_index == 9:
                            tail_positions.add(positions[knot_index])
        self.assertEqual(positions,[4 + 0j, 3 + 0j, 2 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])

    def test_U4(self):
        tail_positions = set()
        tail_positions.add(0 + 0j)
        text_input = "R 4, U 4"
        positions = [0 + 0j] * 10
        for item in text_input.split(','):
            direction, movements = item.strip().split(" ")
            for i in range(int(movements)):
                for knot_index in range(len(positions)):
                    if knot_index == 0:
                        positions[0] = main.move_head(direction, positions[0])
                    else:
                        positions[knot_index] = main.move_tail(positions[knot_index - 1], positions[knot_index])
                        previous_head_position = positions[knot_index]
                        if knot_index == 9:
                            tail_positions.add(positions[knot_index])
        self.assertEqual(positions, [4 + 4j, 4 + 3j, 4 + 2j, 3 + 2j, 2 + 2j, 1 + 1j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])

    # def test_small_ladder(self):
    #     """ ......
    #         ......
    #         .....H
    #         .54321
    #         6.....
    #     """
    #     tail_positions = set()
    #     tail_positions.add(0 + 0j)
    #     text_input = "R 5, U 2"
    #     positions = [0 + 0j] * 10
    #     for item in text_input.split(','):
    #         direction, movements = item.strip().split(" ")
    #         for i in range(int(movements)):
    #             for knot_index in range(len(positions)):
    #                 if knot_index == 0:
    #                     positions[0] = main.move_head(direction, positions[0])
    #                 else:
    #                     positions[knot_index] = main.move_tail(positions[knot_index - 1], positions[knot_index])
    #                     previous_head_position = positions[knot_index]
    #                     if knot_index == 9:
    #                         tail_positions.add(positions[knot_index])
    #     self.assertEqual(positions, [5 + 2j, 5 + 1j, 4 + 1j, 3 + 1j, 2 + 1j, 1 + 1j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])



if __name__ == '__main__':
    unittest.main()







