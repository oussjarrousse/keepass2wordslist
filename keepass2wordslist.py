#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys, argparse, logging

from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError

loglevel = logging.INFO

# Gather our code in a main() function
def main(args):
    try:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
        logging.debug("Extracting passwords from: {}".format(args.filename))
        if args.output is None:
            logging.debug("Dumping unique passwords to stdout")
        else:
            logging.debug("Dumping unique passwords to {}").format(args.output)

        #Opening the keepass file
        kp = PyKeePass(args.filename, password=args.password, keyfile=args.key)
    except CredentialsError as e:
        logging.info('Incorrect Password')
        exit(1)
    except FileNotFoundError as e:
        logging.info('File {} not found'.format(args.filename))
        exit(1)
    try:
        #Iterating over all entries
        passwords = set()
        for entry in kp.entries:
            passwords.add(entry.password)

        #filtering
        passwords.remove(None)

        #sorting
        passwords = list(passwords)
        passwords.sort()

        #exporting
        if args.output is None:
            for password in passwords:
                print(password)
        else:
            with open(args.output, 'w') as f:
                for password in passwords:
                    f.write("{}\n".format(password))
    except Exception as e:
        logging.error(e)
        exit(2)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser( 
                        description = "Takes a KeePass file and generates a wordlist",
                        epilog = "",
                        fromfile_prefix_chars = '@' )
    parser.add_argument(
                        "filename",
                        help = "the path to a keepass file",
                        metavar = "INPUT")
    parser.add_argument(
                        "password",
                        help = "The password of the keepass file",
                        metavar = "PASSWORD")
    parser.add_argument("-k",
                        "--key",
                        default=None,
                        help="certificate",
                        type=argparse.FileType('r'))
    parser.add_argument(
                        "-v",
                        "--verbose",
                        help="increase output verbosity",
                        action="store_true")
    parser.add_argument(
                        "-o",
                        "--output",
                        help="output filename",
                        type=argparse.FileType('w'))
    args = parser.parse_args()
  
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
  
    main(args)
