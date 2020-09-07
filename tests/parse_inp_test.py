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
        ** Defines an element set "E1" with one element, 1.
        *ELSET,ELSET=E1
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
        self.assertEqual(value_token.value, 'E1')

        data_line = keyword_card.children[2]
        self.assertEqual(data_line.data, 'data_line')
        self.assertEqual(len(data_line.children), 1)

        data_value = data_line.children[0]
        self.assertEqual(data_value.data, 'value')
        self.assertEqual(len(data_value.children), 1)

        data_value_token = data_value.children[0]
        self.assertEqual(data_value_token.type, 'INT')
        self.assertEqual(data_value_token.value, '1')

    def test_parse_inp_with_single_data_line_and_multiple_elements(self):
        contents = """
        ** Defines an element set "E1" with three elements: 1, 2, and 3.
        *ELSET,ELSET=E1
        1, 2, 3
        """

        tree = parse_inp(contents)

        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]

        self.assertEqual(len(keyword_card.children), 3)

        data_line = keyword_card.children[2]
        self.assertEqual(data_line.data, 'data_line')
        self.assertEqual(len(data_line.children), 3)

        # element 1
        element1 = data_line.children[0]
        self.assertEqual(element1.data, 'value')
        self.assertEqual(len(element1.children), 1)

        element1_token = element1.children[0]
        self.assertEqual(element1_token.type, 'INT')
        self.assertEqual(element1_token.value, '1')
        # ----------------------------------------------

        # element 2
        element2 = data_line.children[1]
        self.assertEqual(element2.data, 'value')
        self.assertEqual(len(element2.children), 1)

        element2_token = element2.children[0]
        self.assertEqual(element2_token.type, 'INT')
        self.assertEqual(element2_token.value, '2')
        # ----------------------------------------------

        # element 3
        element3 = data_line.children[2]
        self.assertEqual(element3.data, 'value')
        self.assertEqual(len(element3.children), 1)

        element3_token = element3.children[0]
        self.assertEqual(element3_token.type, 'INT')
        self.assertEqual(element3_token.value, '3')
        # ----------------------------------------------

    def test_parse_inp_with_multiple_data_lines(self):
        contents = """
        ** Defines an element set "E1" with three elements: 1, 2, and 3.
        *ELSET,ELSET=E1
        1, 2, 3
        4, 5, 6
        """

        tree = parse_inp(contents)

        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]

        self.assertEqual(len(keyword_card.children), 4)

        data_line = keyword_card.children[3]
        self.assertEqual(data_line.data, 'data_line')
        self.assertEqual(len(data_line.children), 3)

        # element 4
        element4 = data_line.children[0]
        self.assertEqual(element4.data, 'value')
        self.assertEqual(len(element4.children), 1)

        element4_token = element4.children[0]
        self.assertEqual(element4_token.type, 'INT')
        self.assertEqual(element4_token.value, '4')
        # ----------------------------------------------

        # element 5
        element5 = data_line.children[1]
        self.assertEqual(element5.data, 'value')
        self.assertEqual(len(element5.children), 1)

        element5_token = element5.children[0]
        self.assertEqual(element5_token.type, 'INT')
        self.assertEqual(element5_token.value, '5')
        # ----------------------------------------------

        # element 6
        element6 = data_line.children[2]
        self.assertEqual(element6.data, 'value')
        self.assertEqual(len(element6.children), 1)

        element6_token = element6.children[0]
        self.assertEqual(element6_token.type, 'INT')
        self.assertEqual(element6_token.value, '6')
        # ----------------------------------------------


if __name__ == '__main__':
    unittest.main()
