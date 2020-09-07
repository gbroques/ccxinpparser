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

    def test_parse_inp_with_single_keyword_line_without_params_or_data(self):
        contents = '*STEP'

        tree = parse_inp(contents)

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]
        self.assertEqual(keyword_card.data, 'keyword_card')
        self.assertEqual(len(keyword_card.children), 1)

        keyword_token = keyword_card.children[0]
        self.assertEqual(keyword_token.type, 'KEYWORD')
        self.assertEqual(keyword_token.value, '*STEP')

    def test_parse_inp_with_single_keyword_line_with_params_and_no_data(self):
        contents = '*INCLUDE,INPUT=/home/guido/test/beam.spc'

        tree = parse_inp(contents)

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]
        self.assertEqual(keyword_card.data, 'keyword_card')
        self.assertEqual(len(keyword_card.children), 2)

        keyword_token = keyword_card.children[0]
        self.assertEqual(keyword_token.type, 'KEYWORD')
        self.assertEqual(keyword_token.value, '*INCLUDE')

        param = keyword_card.children[1]
        self.assertEqual(param.data, 'param')
        self.assertEqual(len(param.children), 2)

        key = param.children[0]
        self.assertEqual(key.type, 'KEY')
        self.assertEqual(key.value, 'INPUT')

        value = param.children[1]
        self.assertEqual(value.data, 'value')
        self.assertEqual(len(value.children), 1)

        value_token = value.children[0]
        self.assertEqual(value_token.type, 'PATH')
        self.assertEqual(value_token.value, '/home/guido/test/beam.spc')


if __name__ == '__main__':
    unittest.main()
