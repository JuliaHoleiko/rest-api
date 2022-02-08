from flask import Flack

app = Flack (__name__)

from controller import *

if __name__ == '__main__':
    app.run()