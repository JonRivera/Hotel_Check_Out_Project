# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import joblib
from joblib import load
# Imports from this application
from app import app
import pandas as pd
#load pipeline
model3 = load('assets/model3.joblib')
print('pipeline loaded')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout


def predict(lead_time,stays_in_weekend_nights,stays_in_week_nights,
               previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type):
    df = pd.DataFrame(
        columns= ['lead_time','stays_in_weekend_nights','stays_in_week_nights','previous_cancellations',
                    'booking_changes','adr','required_car_parking_spaces','country','deposit_type']
            
            ,
        data=[[lead_time,stays_in_weekend_nights,stays_in_week_nights,
               previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type]]
    )
    y_pred = model3.predict(df)[0]
    return f'Person {y_pred} Booking'

result = predict(10,20,20,20,2,100,0,'PRT','No Deposit')
print(result)
result2 = predict(10,20,20,20,2,100,0,'PRT','No Deposit')


column1 = dbc.Col(
    [
        dcc.Markdown('## Inputs', className='mb-5'), 
        dcc.Markdown('#### lead_time'),
        dcc.Slider(
                    id='lead_time', 
                    min=0,
                    max=1000,
                    step=1,
                    value = 40,
                    marks={n:str(n) for n in range(0,1001,100)},
                    className='mb-5', 
                ),
                
        dcc.Markdown('#### stays_in_weekend_nights'), 
        dcc.Input(
        id = 'stays_in_weekend_nights',
        placeholder=2,
        type='number',
        value= 2), 


        dcc.Markdown('#### stays_in_week_nights'),
         dcc.Input(
        id = 'stays_in_week_nights',
        placeholder=2,
        type='number',
        value= 2),
        
         dcc.Markdown('#### previous_cancellations'),
          dcc.Input(
        id = 'previous_cancellations',
        placeholder=2,
        type='number',
        value= 2), 

         dcc.Markdown('#### booking_changes'),
          dcc.Input(
         id = 'booking_changes',
         placeholder=2,
         type='number',
         value= 2), 

        dcc.Markdown('#### adr'),
        dcc.Input(
        id = 'adr',
        placeholder=2,
        type='number',
        value= 2), 

        
        dcc.Markdown('#### required_car_parking_spaces'),
        dcc.Input(
        id = 'required_car_parking_spaces',
        placeholder=2,
        type='number',
        value= 2), 


        dcc.Markdown('#### country'),
        dcc.Input(
        id = 'country',
        placeholder='USA',
        type='text',
        value= 'USA'), 

        
        dcc.Markdown('#### deposit_type'),
        dcc.Dropdown(
            id='deposit_type', 
            options = [
                {'label': 'No Deposit', 'value': 'No Deposit'}, 
                {'label': 'Non Refund', 'value': 'Non Refund'}, 
            ], 
            value = 'No Deposit', 
            className='mb-5', 
        ), 
        

         







        



    ],
    md=4,
)
#Adding a Gauge 
column2 = dbc.Col(
    [

        html.H2('Will the person cancel or check-out from a hotel?', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')


    ]
)

layout = dbc.Row([column1, column2])
@app.callback(
    Output('prediction-content', 'children'),
    [Input('lead_time', 'value'), Input('stays_in_weekend_nights', 'value'),Input('stays_in_week_nights', 'value'),
    Input('previous_cancellations', 'value'),Input('booking_changes', 'value'), Input('adr', 'value'),
     Input('required_car_parking_spaces', 'value'), Input('country', 'value'),Input('deposit_type', 'value') ],
)

def predict(lead_time,stays_in_weekend_nights,stays_in_week_nights,
               previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type):
    df = pd.DataFrame(
        columns= ['lead_time','stays_in_weekend_nights','stays_in_week_nights','previous_cancellations',
                    'booking_changes','adr','required_car_parking_spaces','country','deposit_type']
            
            ,
        data=[[lead_time,stays_in_weekend_nights,stays_in_week_nights,
               previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type]]
    )
    y_pred = model3.predict(df)[0]
    return f'Person {y_pred} Booking'



#decorator funnction rerun everytime this input changes, 
#when this input changes used parameter
#returns values
#that gets put into the output

# @app.callback(
#     Output(component_id='my-daq-gauge', component_property='value'),
#     [Input(component_id='slider1 ', component_property='value')]
# )
# def update_output_div(input_value):
#     return input_value
