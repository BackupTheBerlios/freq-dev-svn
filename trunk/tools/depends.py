import sys

tw='You need have it installed to use freQ-bot\n=== Visit http://twistedmatrix.com/ to get info about Twisted...\n'

try: import twisted
except:
 sys.stdout.write('=== py-TwistedCore not found...\n=== '+tw+'\n')
 sys.exit(1)

try: import twisted.words.protocols.jabber
except:
 sys.stdout.write('=== py-TwistedWords not found...\n=== '+tw+'\n')
 sys.exit(1)
 
try: import twisted.web
except:
 sys.stdout.write('=== py-TwistedWeb not found...\n=== '+tw+'\n')
 sys.exit(1)
