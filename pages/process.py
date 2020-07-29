# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process
            I ended up using the random forest model, as I had complications uploading the xgboost model.

            Notice the difference in auc score is marginal, but the xgboost was the better model.

            Also, It should be noted, the random forest model used in this app uses 9 features, and it improved compared to the random forest I originally worked with
            that had 22 features.
            


            """
        ),
        html.Img(src='assets/ROC.jpeg', className='img-fluid'),



    ],
)

layout = dbc.Row([column1])