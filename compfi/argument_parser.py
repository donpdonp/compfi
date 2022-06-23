import argparse
from .cmds import approve, liquidate_borrow

def parse():
    main_parser = argparse.ArgumentParser(description='compound.finance tool')
    cmd_parser = main_parser.add_subparsers(help='commands')

    lb_parser = cmd_parser.add_parser('liquidateBorrow', help='call liquidateBorrow')
    lb_parser.add_argument("addr")
    lb_parser.set_defaults(func=liquidate_borrow.go)

    ap_parser = cmd_parser.add_parser('approve', help='call approve')
    ap_parser.set_defaults(func=approve.go)
    ap_parser.add_argument("addr")
    
    return main_parser.parse_args()
