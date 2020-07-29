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
model0= load('assets/model0.joblib')
print('pipeline loaded')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout


# def predict(lead_time,stays_in_weekend_nights,stays_in_week_nights,
#                previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type):
#     df = pd.DataFrame(
#         columns= ['lead_time','stays_in_weekend_nights','stays_in_week_nights','previous_cancellations',
#                     'booking_changes','adr','required_car_parking_spaces','country','deposit_type']
            
#             ,
#         data=[[lead_time,stays_in_weekend_nights,stays_in_week_nights,
#                previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type]]
#     )
#     y_pred = model0.predict(df)[0]
#     return f'Person {y_pred} Booking'

# result = predict(10,20,20,20,2,100,0,'PRT','No Deposit')
# print(result)
# result2 = predict(10,20,20,20,2,100,0,'PRT','No Deposit')


column1 = dbc.Col(
    [
        dcc.Markdown('## Inputs', className='mb-5'), 
        dcc.Markdown('#### lead_time'),
        dcc.Slider(
                    id='lead_time', 
                    min=0,
                    max=150,
                    step=1,
                    value = 0,
                    marks={n:str(n) for n in range(0,150,10)},
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
        placeholder=0,
        type='number',
        value= 0), 

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


        dcc.Markdown('#### Country by Alpha-3 code'),
        dcc.Dropdown(
        # dcc.Input(
        id = 'country',
        options = [{'label': 'PRT', 'value': 'PRT'}, {'label': 'GBR', 'value': 'GBR'}, {'label': 'FRA', 'value': 'FRA'},
             {'label': 'ESP', 'value': 'ESP'}, {'label': 'DEU', 'value': 'DEU'}, {'label': 'ITA', 'value': 'ITA'}, 
             {'label': 'IRL', 'value': 'IRL'}, {'label': 'BEL', 'value': 'BEL'}, {'label': 'BRA', 'value': 'BRA'},
              {'label': 'NLD', 'value': 'NLD'}, {'label': 'USA', 'value': 'USA'}, {'label': 'CHE', 'value': 'CHE'},
               {'label': 'CN', 'value': 'CN'}, {'label': 'AUT', 'value': 'AUT'}, {'label': 'SWE', 'value': 'SWE'},
                {'label': 'CHN', 'value': 'CHN'}, {'label': 'POL', 'value': 'POL'}, {'label': 'ISR', 'value': 'ISR'}, 
                {'label': 'RUS', 'value': 'RUS'}, {'label': 'NOR', 'value': 'NOR'}, {'label': 'ROU', 'value': 'ROU'}, 
                {'label': 'FIN', 'value': 'FIN'}, {'label': 'DNK', 'value': 'DNK'}, {'label': 'AUS', 'value': 'AUS'}, 
                {'label': 'AGO', 'value': 'AGO'}, {'label': 'LUX', 'value': 'LUX'}, {'label': 'MAR', 'value': 'MAR'}, 
                {'label': 'TUR', 'value': 'TUR'}, {'label': 'HUN', 'value': 'HUN'}, {'label': 'ARG', 'value': 'ARG'}, 
                {'label': 'JPN', 'value': 'JPN'}, {'label': 'CZE', 'value': 'CZE'}, {'label': 'IND', 'value': 'IND'},
                 {'label': 'KOR', 'value': 'KOR'}, {'label': 'GRC', 'value': 'GRC'}, {'label': 'DZA', 'value': 'DZA'},
                  {'label': 'SRB', 'value': 'SRB'}, {'label': 'HRV', 'value': 'HRV'}, {'label': 'MEX', 'value': 'MEX'},
                   {'label': 'IRN', 'value': 'IRN'}, {'label': 'EST', 'value': 'EST'}, {'label': 'LTU', 'value': 'LTU'},
                    {'label': 'ZAF', 'value': 'ZAF'}, {'label': 'BGR', 'value': 'BGR'}, {'label': 'NZL', 'value': 'NZL'},
                     {'label': 'COL', 'value': 'COL'}, {'label': 'UKR', 'value': 'UKR'}, {'label': 'MOZ', 'value': 'MOZ'}, 
                     {'label': 'CHL', 'value': 'CHL'}, {'label': 'SVK', 'value': 'SVK'}, {'label': 'THA', 'value': 'THA'}, 
                     {'label': 'SVN', 'value': 'SVN'}, {'label': 'ISL', 'value': 'ISL'}, {'label': 'LVA', 'value': 'LVA'},
                      {'label': 'TWN', 'value': 'TWN'}, {'label': 'CYP', 'value': 'CYP'}, {'label': 'ARE', 'value': 'ARE'},
                       {'label': 'SAU', 'value': 'SAU'}, {'label': 'PHL', 'value': 'PHL'}, {'label': 'TUN', 'value': 'TUN'}, 
                       {'label': 'SGP', 'value': 'SGP'}, {'label': 'IDN', 'value': 'IDN'}, {'label': 'NGA', 'value': 'NGA'},
                        {'label': 'URY', 'value': 'URY'}, {'label': 'EGY', 'value': 'EGY'}, {'label': 'LBN', 'value': 'LBN'}, 
                        {'label': 'PER', 'value': 'PER'}, {'label': 'HKG', 'value': 'HKG'}, {'label': 'MYS', 'value': 'MYS'}, 
                        {'label': 'ECU', 'value': 'ECU'}, {'label': 'VEN', 'value': 'VEN'}, {'label': 'BLR', 'value': 'BLR'}, 
                        {'label': 'CPV', 'value': 'CPV'}, {'label': 'GEO', 'value': 'GEO'}, {'label': 'JOR', 'value': 'JOR'}, 
                        {'label': 'KAZ', 'value': 'KAZ'}, {'label': 'CRI', 'value': 'CRI'}, {'label': 'OMN', 'value': 'OMN'},
                         {'label': 'MLT', 'value': 'MLT'}, {'label': 'GIB', 'value': 'GIB'}, {'label': 'AZE', 'value': 'AZE'},
                          {'label': 'MAC', 'value': 'MAC'}, {'label': 'KWT', 'value': 'KWT'}, {'label': 'QAT', 'value': 'QAT'},
                           {'label': 'PAK', 'value': 'PAK'}, {'label': 'DOM', 'value': 'DOM'}, {'label': 'IRQ', 'value': 'IRQ'},
                            {'label': 'BIH', 'value': 'BIH'}, {'label': 'PRI', 'value': 'PRI'}, {'label': 'BGD', 'value': 'BGD'}, 
                            {'label': 'MDV', 'value': 'MDV'}, {'label': 'ALB', 'value': 'ALB'}, {'label': 'SEN', 'value': 'SEN'}, 
                            {'label': 'BOL', 'value': 'BOL'}, {'label': 'CMR', 'value': 'CMR'}, {'label': 'MKD', 'value': 'MKD'},
                             {'label': 'PAN', 'value': 'PAN'}, {'label': 'GNB', 'value': 'GNB'}, {'label': 'TJK', 'value': 'TJK'}, 
                             {'label': 'VNM', 'value': 'VNM'}, {'label': 'JEY', 'value': 'JEY'}, {'label': 'LBY', 'value': 'LBY'}, 
                             {'label': 'ARM', 'value': 'ARM'}, {'label': 'CUB', 'value': 'CUB'}, {'label': 'AND', 'value': 'AND'}, 
                             {'label': 'MUS', 'value': 'MUS'}, {'label': 'LKA', 'value': 'LKA'}, {'label': 'KEN', 'value': 'KEN'}, 
                             {'label': 'CIV', 'value': 'CIV'}, {'label': 'JAM', 'value': 'JAM'}, {'label': 'FRO', 'value': 'FRO'},
                              {'label': 'BHR', 'value': 'BHR'}, {'label': 'MNE', 'value': 'MNE'}, {'label': 'TZA', 'value': 'TZA'},
                               {'label': 'SUR', 'value': 'SUR'}, {'label': 'CAF', 'value': 'CAF'}, {'label': 'PRY', 'value': 'PRY'}, 
                               {'label': 'UZB', 'value': 'UZB'}, {'label': 'GAB', 'value': 'GAB'}, {'label': 'ZWE', 'value': 'ZWE'},
                                {'label': 'BRB', 'value': 'BRB'}, {'label': 'MCO', 'value': 'MCO'}, {'label': 'GHA', 'value': 'GHA'}, 
                                {'label': 'GTM', 'value': 'GTM'}, {'label': 'SYR', 'value': 'SYR'}, {'label': 'ETH', 'value': 'ETH'},
                                 {'label': 'LIE', 'value': 'LIE'}, {'label': 'BEN', 'value': 'BEN'}, {'label': 'TMP', 'value': 'TMP'}, 
                                 {'label': 'GGY', 'value': 'GGY'}, {'label': 'MYT', 'value': 'MYT'}, {'label': 'LAO', 'value': 'LAO'},
                                  {'label': 'GLP', 'value': 'GLP'}, {'label': 'ZMB', 'value': 'ZMB'}, {'label': 'KHM', 'value': 'KHM'}, 
                                  {'label': 'UGA', 'value': 'UGA'}, {'label': 'MWI', 'value': 'MWI'}, {'label': 'KNA', 'value': 'KNA'},
                                   {'label': 'TGO', 'value': 'TGO'}, {'label': 'ATA', 'value': 'ATA'}, {'label': 'STP', 'value': 'STP'}, 
                                   {'label': 'SLV', 'value': 'SLV'}, {'label': 'COM', 'value': 'COM'}, {'label': 'SYC', 'value': 'SYC'}, 
                                   {'label': 'IMN', 'value': 'IMN'}, {'label': 'ABW', 'value': 'ABW'}, {'label': 'RWA', 'value': 'RWA'}, 
                                   {'label': 'BDI', 'value': 'BDI'}, {'label': 'NPL', 'value': 'NPL'}, {'label': 'SDN', 'value': 'SDN'}, 
                                   {'label': 'SLE', 'value': 'SLE'}, {'label': 'BHS', 'value': 'BHS'}, {'label': 'MMR', 'value': 'MMR'}, 
                                   {'label': 'LCA', 'value': 'LCA'}, {'label': 'AIA', 'value': 'AIA'}, {'label': 'MDG', 'value': 'MDG'},
                                    {'label': 'KIR', 'value': 'KIR'}, {'label': 'ASM', 'value': 'ASM'}, {'label': 'NAM', 'value': 'NAM'},
                                     {'label': 'CYM', 'value': 'CYM'}, {'label': 'VGB', 'value': 'VGB'}, {'label': 'BWA', 'value': 'BWA'},
                                      {'label': 'PLW', 'value': 'PLW'}, {'label': 'BFA', 'value': 'BFA'}, {'label': 'SMR', 'value': 'SMR'},
                                       {'label': 'PYF', 'value': 'PYF'}, {'label': 'NCL', 'value': 'NCL'}, {'label': 'ATF', 'value': 'ATF'},
                                        {'label': 'MLI', 'value': 'MLI'}, {'label': 'FJI', 'value': 'FJI'}, {'label': 'NIC', 'value': 'NIC'},
                                         {'label': 'UMI', 'value': 'UMI'}, {'label': 'DJI', 'value': 'DJI'}, {'label': 'HND', 'value': 'HND'},
                                          {'label': 'MRT', 'value': 'MRT'}, {'label': 'DMA', 'value': 'DMA'}, {'label': 'GUY', 'value': 'GUY'}],
            value = 'USA',
            className='mb-5'),
        # placeholder='USA',
        # type='text',
        # value= 'USA'), 

        
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
        html.Div(id='prediction-content', className='lead'),

        html.Img(src='assets/reception.jpg', className='img-fluid'),

        dcc.Markdown('lead time means: days that elapsed between the entering date of the booking into the PMS and the expected arrival date'),
    ]
)

layout = dbc.Row([column1, column2])
@app.callback(
    Output('prediction-content', 'children'),
    [Input('lead_time', 'value'), Input('stays_in_weekend_nights', 'value'),Input('stays_in_week_nights', 'value'),
    Input('previous_cancellations', 'value'),Input('booking_changes', 'value'), Input('adr', 'value'),
     Input('required_car_parking_spaces', 'value'), Input('country', 'value'),Input('deposit_type', 'value') ],
)

# def predict(lead_time,stays_in_weekend_nights,stays_in_week_nights,
#                previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type):
#     df = pd.DataFrame(
#         columns= ['lead_time','stays_in_weekend_nights','stays_in_week_nights','previous_cancellations',
#                     'booking_changes','adr','required_car_parking_spaces','country','deposit_type']
            
#             ,
#         data=[[lead_time,stays_in_weekend_nights,stays_in_week_nights,
#                previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type]]
#     )
#     y_pred = model0.predict(df)[0]
#     return f'Person {y_pred} Booking'

def predict(lead_time,stays_in_weekend_nights,stays_in_week_nights,
               previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type):
    df = pd.DataFrame(
        columns= ['lead_time','stays_in_weekend_nights','stays_in_week_nights',
                  'previous_cancellations','booking_changes','adr','required_car_parking_spaces',
                  'country','deposit_type']
            
            ,
        data=[[lead_time,stays_in_weekend_nights,stays_in_week_nights,
               previous_cancellations,booking_changes,adr,required_car_parking_spaces,country,deposit_type]]
    )
    y_pred_probab0 = round(model0.predict_proba(df)[0][1],2)
    y_pred = model0.predict(df)[0]
    #print(f' Probabillity that person checked-out {y_pred_probab0}%')
    return f'Person is predicted to {y_pred} Booking and has a {y_pred_probab0*100}% chance of Checking Out'