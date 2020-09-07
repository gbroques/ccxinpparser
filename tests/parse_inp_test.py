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

    # def test_float(self):
    #     contents = '*SOME KEYWORD, AKEY=+3.00000e+00'

    #     tree = parse_inp(contents)

    #     print(tree)

    def test_parse_inp(self):
        contents = """

        **
        **   Structure: disk with plate.
        **   Test objective: combination of axisymmetric elements with
        **                   plane stress elements.
        **
        *NODE, NSET=Nall
            1,  2.00000e+00, -7.45058e-09,  0.00000e+00 
            2,  2.00000e+00,  1.00000e+00,  0.00000e+00 
            3,  1.00000e+00,  1.00000e+00,  0.00000e+00 

        """

        tree = parse_inp(contents)
        self.assertEqual(tree.data, 'start')
        self.assertEqual(len(tree.children), 1)

        # *NODE Keyword Card
        node = tree.children[0]
        self.assertEqual(len(node.children), 7)

        node_keyword = node.children[0]
        self.assertEqual(node_keyword.type, 'KEYWORD')
        self.assertEqual(node_keyword.value, '*NODE')

        # nset_param = keyword_card.children[1]
        # self.assertEqual(nset_param.data, 'param')
        # self.assertEqual(len(nset_param.children), 2)

        # nset_key = nset_param.children[0]
        # self.assertEqual(nset_key.type, 'KEY')
        # self.assertEqual(nset_key.value, 'NSET')

        # nset_value = nset_param.children[1]
        # self.assertEqual(nset_value.data, 'value')
        # self.assertEqual(len(nset_value.children), 1)

        # nset_value_token = nset_value.children[0]
        # self.assertEqual(nset_value_token.type, 'CNAME')
        # self.assertEqual(nset_value_token.value, 'N1')


        print(tree.pretty())


if __name__ == '__main__':
    unittest.main()
