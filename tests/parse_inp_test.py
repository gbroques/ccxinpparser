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

    def test_parse_inp_with_single_data_line_and_element(self):
        contents = """
        ** Defines an element set "E2" with one element, 1.
        *ELSET,ELSET=E2
        1
        """

        tree = parse_inp(contents)

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]
        self.assertEqual(keyword_card.data, 'keyword_card')
        self.assertEqual(len(keyword_card.children), 3)

        keyword_token = keyword_card.children[0]
        self.assertEqual(keyword_token.type, 'KEYWORD')
        self.assertEqual(keyword_token.value, '*ELSET')

        param = keyword_card.children[1]
        self.assertEqual(param.data, 'param')
        self.assertEqual(len(param.children), 2)

        key = param.children[0]
        self.assertEqual(key.type, 'KEY')
        self.assertEqual(key.value, 'ELSET')

        value = param.children[1]
        self.assertEqual(value.data, 'value')
        self.assertEqual(len(value.children), 1)

        value_token = value.children[0]
        self.assertEqual(value_token.type, 'CNAME')
        self.assertEqual(value_token.value, 'E2')

        data_line = keyword_card.children[2]
        self.assertEqual(data_line.data, 'data_line')
        self.assertEqual(len(data_line.children), 1)

        data_value = data_line.children[0]
        self.assertEqual(data_value.data, 'value')
        self.assertEqual(len(data_value.children), 1)

        data_value_token = data_value.children[0]
        self.assertEqual(data_value_token.type, 'INT')
        self.assertEqual(data_value_token.value, '1')


if __name__ == '__main__':
    unittest.main()
