import unittest

from ccxinpparser import parse_inp


class ParseInpTest(unittest.TestCase):

    def test_parse_inp_with_empty_string(self):
        tree = parse_inp('')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 0)

    def test_parse_inp_with_newline(self):
        tree = parse_inp('\n')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 0)

    def test_parse_inp_with_multiple_newlines(self):
        tree = parse_inp('\n\n\n\n')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 0)

    def test_parse_inp_with_windows_line_endings(self):
        tree = parse_inp('\r\n')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 0)

    def test_parse_inp_with_multiple_windows_line_endings(self):
        tree = parse_inp('\r\n\r\n\r\n\r\n')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 0)

    def test_parse_inp_propagate_positions(self):
        tree = parse_inp('**')

        self.assertEqual(tree.children[0].meta.line, 1)
        self.assertEqual(tree.children[0].meta.column, 1)
        self.assertEqual(tree.children[0].meta.start_pos, 0)
        self.assertEqual(tree.children[0].meta.end_line, 1)
        self.assertEqual(tree.children[0].meta.end_column, 3)
        self.assertEqual(tree.children[0].meta.end_pos, 2)

    def test_parse_inp_with_single_empty_comment(self):
        tree = parse_inp('**')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 1)
        self.assertEqual(tree.children[0].data, 'single_line_comment')

    def test_parse_inp_with_multiple_empty_comments(self):
        tree = parse_inp('**\r\n**\n')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 2)
        self.assertEqual(tree.children[0].data, 'single_line_comment')
        self.assertEqual(len(tree.children[0].children), 0)
        self.assertEqual(tree.children[1].data, 'single_line_comment')
        self.assertEqual(len(tree.children[1].children), 0)


if __name__ == '__main__':
    unittest.main()
