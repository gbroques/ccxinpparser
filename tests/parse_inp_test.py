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

    def test_parse_inp_with_multiple_word_keyword_params_and_no_data(self):
        contents = '*NODE PRINT ,NSET=N1, FREQUENCY=0'

        tree = parse_inp(contents)

        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]
        self.assertEqual(keyword_card.data, 'keyword_card')
        self.assertEqual(len(keyword_card.children), 3)

        keyword_token = keyword_card.children[0]
        self.assertEqual(keyword_token.type, 'KEYWORD')
        self.assertEqual(keyword_token.value, '*NODE PRINT')

        nset_param = keyword_card.children[1]
        self.assertEqual(nset_param.data, 'param')
        self.assertEqual(len(nset_param.children), 2)

        nset_key = nset_param.children[0]
        self.assertEqual(nset_key.type, 'KEY')
        self.assertEqual(nset_key.value, 'NSET')

        nset_value = nset_param.children[1]
        self.assertEqual(nset_value.data, 'value')
        self.assertEqual(len(nset_value.children), 1)

        nset_value_token = nset_value.children[0]
        self.assertEqual(nset_value_token.type, 'CNAME')
        self.assertEqual(nset_value_token.value, 'N1')

        frequency_param = keyword_card.children[2]
        self.assertEqual(frequency_param.data, 'param')
        self.assertEqual(len(frequency_param.children), 2)

        frequency_key = frequency_param.children[0]
        self.assertEqual(frequency_key.type, 'KEY')
        self.assertEqual(frequency_key.value, 'FREQUENCY')

        frequency_value = frequency_param.children[1]
        self.assertEqual(frequency_value.data, 'value')
        self.assertEqual(len(frequency_value.children), 1)

        frequency_value_token = frequency_value.children[0]
        self.assertEqual(frequency_value_token.type, 'INT')
        self.assertEqual(frequency_value_token.value, '0')


if __name__ == '__main__':
    unittest.main()
