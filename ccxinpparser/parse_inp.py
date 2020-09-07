from pathlib import Path
import re

from lark import Lark, Tree


def parse_inp(contents: str, debug: bool = False) -> Tree:
    path_to_grammar = Path(__file__).parent / 'inp.lark'
    with open(path_to_grammar, mode='r', encoding='UTF-8') as f:
        parser = Lark(f.read(), propagate_positions=True, debug=debug, parser='lalr')

    contents_without_missing_values = re.sub(r',[ \t]*,', ', 0,', contents)
    return parser.parse(contents_without_missing_values)


__all__ = ['parse_inp']
