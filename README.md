# keepass2wordslist

As the name suggest this is a python command line tool generates a words list from your keepass file. It depends on pykeepass to open the the passed keepass databases (file) and dumps passwords to the standard output discarding any usernames, email information, or additional data stored in the keepass file.

Usage

% python3 keepass2wordslist.py filename password -v -o output_filename

Example

% python3 keepass2wordslist.py keepass.kdbx thefilestrongpassword