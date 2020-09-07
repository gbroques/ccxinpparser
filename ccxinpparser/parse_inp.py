from pathlib import Path

from lark import Lark, Tree


def parse_inp(contents: str, debug: bool = False) -> Tree:
    path_to_grammar = Path(__file__).parent / 'inp.lark'
    with open(path_to_grammar, mode='r', encoding='UTF-8') as f:
        parser = Lark(f.read(), propagate_positions=True, debug=debug)

    return parser.parse(contents)


__all__ = ['parse_inp']
