#!bin/python

import os, sys

print('You are running Python: ' + sys.version)
print('From: ' + os.path.dirname(sys.executable))

from app import app
app.run(debug=True)

