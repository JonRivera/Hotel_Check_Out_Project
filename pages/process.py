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
            I ended up using the random forest model, as I had complications uploading the XGBoost model.
             Notice the difference in auc score is marginal, but the XGBoost was the better model.

            Also, It should be noted, the Random Forest model used in this app uses 9 features and works on the validation set.
            Originally, the random forest used 22 features.
            """
        ),
        html.Img(src='assets/valset.jpeg', className='img-fluid'),
        dcc.Markdown('To get a more detailed break down on the process please click the Medium Link Below: https://medium.com/@jonatanalejandrorivera/will-you-end-up-canceling-a-booked-hotel-or-end-up-checking-out-54e85243f2d9'),
        dcc.Markdown('Plotly Dash App Code: https://github.com/JonRivera/HotelCheckOutProject/blob/master/notebooks/Unit2_Plotly_Dash_App_Code.ipynb'),


    ],
)

layout = dbc.Row([column1])