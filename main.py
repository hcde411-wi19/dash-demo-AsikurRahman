# -*- coding: utf-8 -*-

# when you run any of the code from the exercises, you can run it from here on main.py
#

# Note: import the app of what you are working on
# from initial_demo import app
from exercise2 import app
# from exercise2 import app
# from exercise2 import app

server = app.server

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



