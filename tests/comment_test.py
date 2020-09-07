import unittest

from ccxinpparser import parse_inp


class CommentTest(unittest.TestCase):

    def test_parse_inp_with_single_empty_comment(self):
        tree = parse_inp('**')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 0)

    def test_parse_inp_with_multiple_empty_comments(self):
        tree = parse_inp('**\r\n**\n')

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 0)


if __name__ == '__main__':
    unittest.main()
