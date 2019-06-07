import sys
import argparse


def main(argv):
    parser = argparse.ArgumentParser(description='Download youtube video by demand.')
    parser.add_argument('--keyword', action='append',dest='keywords',  nargs=1,
                        help='keyword to look for')

    args = parser.parse_args(argv)
    if args.keywords:
        keywords = [word[0] for word in args.keywords]




if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
