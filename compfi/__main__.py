import compfi.argument_parser
from .cmds import approve, liquidate_borrow

def main():
    args = compfi.argument_parser.parse()
    if "func" in args:
        args.func(vars(args))
    else:
        main_parser.print_help()

main()