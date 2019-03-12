# -*- coding: utf-8 -*-

# Exercise 2
# My goal with this visualization: I wanted to create a scatter plot to see the
# relationship between highway MPG and dealer cost. I predicted that there would be
# a positive correlation with highway MPG and dealer cost but based on my graph this
# is not true which is very interesting. There are a lot of cars with lower
# highway MPG but still cost a lot of money.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')

# here you are creating your data frame using a data set
df = pd.read_csv('static/data_car_2004.csv')


# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Scatter Plot'),

    # set the description underneath the heading
    html.Div(children='''
        A demo to show a scatter plot.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"

                # here you are creating the scatterplot here and using columns from your
                # column names
                go.Scatter(
                    x=df['Hwy MPG'],
                    y=df['Dealer Cost'],

                    # mode markers - this means u will see circles for each data point
                    mode='markers',

                    # here you are setting the text of what you want to appear when you hover
                    # your cursor over each data point, so you can set any column from the data set
                    # for good design, you want to set the text variable to be something that outputs a
                    # a text.... so veh name will output text rep veh name, setting the var as something like
                    # car cyl is bad design bc when you hover over the data point, all you will see is a
                    # number and you wont know which var it is


                    text=df['Vehicle Name'],  # This line sets the vehicle name as the points' labels.
                    marker={

                        # here u are able to change the look of the data points
                        'size': 10,
                        'opacity': 0.8  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                )
            ],
            'layout': {

                # here you are setting the title of your scatter plot
                'title': 'Highway MPG vs. Dealer Cost',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial

                # here you are setting the title for the x axis
                'xaxis': {'title': 'Highway MPG'},

# here           # here you are setting the title for the y axis
                'yaxis': {'title': 'Dealer Cost'},
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)