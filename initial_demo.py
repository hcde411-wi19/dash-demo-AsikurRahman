# -*- coding: utf-8 -*-

# here you are initializing the important comp. to use dask
import dash
import dash_core_components as dcc
import dash_html_components as html

# static data
# below are two lines of data
# weekday - list of days
# count - list of numbers
# each day should match with the numbers below, the vis outputted shows this is true
# height og each bar is matched with the number in counts

weekday_in_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
counts_in_order = [160613, 154225, 155175, 150819, 146014, 215725, 203483]

# initialize Dash environment

# here you are initializing dash enviroment

app = dash.Dash(__name__)

# set up an layout
# here you are setting out the layout, so the look of the data vis
# that's why you see HTML


app.layout = html.Div(children=[
    # H1 title on the page
    # what gets output is a large header saying the
    # text below
    #"html.Div(children=[" the bracket at the end
    # signifies that these are all a list of elements

    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    #below the header, this explanation is being showed
    # div is the content within the header

    html.Div(children='''
        This is a simple Dash application for HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data

            # below a list of dictionaries is being created
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                # line below is setting up the data for the dictionary

                # the variables are linked to the lists you created above,
                # purpose of this dictionary is to create a dictionary that helps you
                # show them on a visualize, so "x" "y" is what is going to be produced
                # on the vis, the key values, are the values the vis are representing,

                {'x': weekday_in_order, 'y': counts_in_order, 'type': 'bar', 'name': 'Total'},

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Usage of the BGT North of NE 70th per week day'
            }
        }
    )
])


if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)


