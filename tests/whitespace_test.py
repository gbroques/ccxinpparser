import unittest

from ccxinpparser import parse_inp


class WhitespaceTest(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
