from . import argument_parser
from .cmds import approve, liquidate_borrow


def main():
    parser = argument_parser.build()
    args = parser.parse_args()
    if "func" in args:
        args.func(vars(args))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
