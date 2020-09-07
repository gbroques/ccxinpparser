import unittest

from ccxinpparser import parse_inp


class ParseInpTest(unittest.TestCase):

    def test_parse_inp_propagate_positions(self):
        contents = '*STEP'

        tree = parse_inp(contents)

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]

        self.assertEqual(keyword_card.meta.line, 1)
        self.assertEqual(keyword_card.meta.column, 1)
        self.assertEqual(keyword_card.meta.start_pos, 0)
        self.assertEqual(keyword_card.meta.end_line, 1)
        self.assertEqual(keyword_card.meta.end_column, 6)
        self.assertEqual(keyword_card.meta.end_pos, 5)


if __name__ == '__main__':
    unittest.main()
