#!/usr/bin/python

import SeenThis
import sys
import os
import tempfile
import subprocess

st = SeenThis.Connection()

if len(sys.argv) != 1:
    print >>sys.stderr, ("Usage: %s\nThe message is read on the standard input" % \
                         sys.argv[0])
    sys.exit(1)

# If the user redirected standard input from a file or a process
if not sys.stdin.isatty():
    message = sys.stdin.read()
# else it is an interactive user
else:
    if os.environ['EDITOR']:
        editor = os.environ['EDITOR']
    else:
        editor = 'vi'
    tmpfile = tempfile.NamedTemporaryFile(delete=True)
    try:
        run_editor = subprocess.Popen([editor, tmpfile.name],
                                      shell=False,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        result = run_editor.stdout.readlines()
        if result == []:
            result = run_editor.stderr.readlines()
        message = open(tmpfile.name).read()
    except OSError:
        print >>sys.stderr, ("Cannot run: \"%s %s\"" % (editor, tmpfile.name))
        raise
    tmpfile.close()
result = st.post(message)
print result



