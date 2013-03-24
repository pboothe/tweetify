Converts a text file (ideally one of poetry) into a bunch of text files in a
subdirectory named "tweets".  It attempts to divid the poem up by stanza, and
then has some logic to slice the stanza up by line, and if that's not enough,
to subdivide each line (hopefully on , or . or, failing that, on spaces, or,
failing that, with a hypen semi-randomly placed).  Only really been tested of
"Song of Myself" by Walt Whitman, where it did an excellent job.

I'm the author, and I'm putting this code in the public domain.  CC-0 - http://creativecommons.org/publicdomain/zero/1.0/

To use this code, type
    python3 stanzafy.py < filecontainingthepoem
For example, to turn "Song of Myself" into tweets, type:
    python3 stanzafy.py < songofmyself.txt
