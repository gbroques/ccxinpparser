import unittest

from ccxinpparser import parse_inp


class DataLineTest(unittest.TestCase):

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
        ** Defines an element set "E1" with 6 elements: 1, 2, 3, 4, 5, and 6.
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

    def test_parse_inp_with_data_continuation_line(self):
        contents = """
        ** The nodes corresponding to element 1 span two lines.
        *ELEMENT,ELSET=Eall,TYPE=C3D20R
        1, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
           16,17,18,19,20
        """

        tree = parse_inp(contents)

        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]

        self.assertEqual(len(keyword_card.children), 4)

        data_line = keyword_card.children[3]
        self.assertEqual(data_line.data, 'data_line')
        self.assertEqual(len(data_line.children), 21)

        # element number
        element_number = data_line.children[0]
        self.assertEqual(element_number.data, 'value')
        self.assertEqual(len(element_number.children), 1)

        element_number_token = element_number.children[0]
        self.assertEqual(element_number_token.type, 'INT')
        self.assertEqual(element_number_token.value, '1')
        # ----------------------------------------------

        # element 14
        element14 = data_line.children[14]
        self.assertEqual(element14.data, 'value')
        self.assertEqual(len(element14.children), 1)

        element14_token = element14.children[0]
        self.assertEqual(element14_token.type, 'INT')
        self.assertEqual(element14_token.value, '14')
        # ----------------------------------------------

        # element 18
        element18 = data_line.children[18]
        self.assertEqual(element18.data, 'value')
        self.assertEqual(len(element18.children), 1)

        element18_token = element18.children[0]
        self.assertEqual(element18_token.type, 'INT')
        self.assertEqual(element18_token.value, '18')
        # ----------------------------------------------

    def test_parse_inp_with_multiple_data_continuation_line(self):
        contents = """
        *ELEMENT,ELSET=Etest,TYPE=S4
        1, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
           16,17,18,19,20
        2, 10, 11, 12
        3, 17, 22,
           55, 100
        ** random comment
        """

        tree = parse_inp(contents)

        self.assertEqual(len(tree.children), 1)

        keyword_card = tree.children[0]

        self.assertEqual(len(keyword_card.children), 6)

        # second data line assertions
        second_data_line = keyword_card.children[4]
        self.assertEqual(second_data_line.data, 'data_line')
        self.assertEqual(len(second_data_line.children), 4)

        # element number of second data line
        element_number = second_data_line.children[0]
        self.assertEqual(element_number.data, 'value')
        self.assertEqual(len(element_number.children), 1)

        element_number_token = element_number.children[0]
        self.assertEqual(element_number_token.type, 'INT')
        self.assertEqual(element_number_token.value, '2')
        # ----------------------------------------------

        # third data line assertions
        third_data_line = keyword_card.children[5]
        self.assertEqual(third_data_line.data, 'data_line')
        self.assertEqual(len(third_data_line.children), 5)

        # element 22
        element22 = third_data_line.children[2]
        self.assertEqual(element22.data, 'value')
        self.assertEqual(len(element22.children), 1)

        element22_token = element22.children[0]
        self.assertEqual(element22_token.type, 'INT')
        self.assertEqual(element22_token.value, '22')

        # element 100
        element100 = third_data_line.children[4]
        self.assertEqual(element100.data, 'value')
        self.assertEqual(len(element100.children), 1)

        element100_token = element100.children[0]
        self.assertEqual(element100_token.type, 'INT')
        self.assertEqual(element100_token.value, '100')
        # ---------------------------------------------


if __name__ == '__main__':
    unittest.main()
