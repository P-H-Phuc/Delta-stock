#Call packages required
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Output, Input, State
from data_source import helpers
from app import app

#Template
template_default = 'plotly_dark'
plot_bgcolor = 'rgba(0,0,0,0)'
paper_bgcolor = 'rgba(0,0,0,0)'
font_title = dict(color='#dea500', family='Arial')
font_chart = dict(color='#666', size=10)
margin_chart = dict(l=20, r=20, b=10, t=60, pad=0)
hover_label = dict(font_size=12, font_color='#000')
color_chart = '#3399FF'
return_none = {
            'layout': go.Layout(
                xaxis =  {                                     
                    'visible': False
                },
                yaxis = {                              
                    'visible': False
                },
                template=template_default,
                paper_bgcolor=paper_bgcolor,
                plot_bgcolor=plot_bgcolor)
}

#Live price
@app.callback(
    Output('company-profile-live-price', 'figure'),
    Input('update-view', 'n_clicks'),
    State('cp-interval-component', 'n_intervals'),
    State('search-symbol', 'value')
)
def live_price(n, x, symbol):
    #If not symbol
    if symbol is None:
        return return_none

    api = f'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:{symbol}&fields=date,time,close,change,pctChange&size=2'
    data = helpers.get_api(api)
    if len(data) != 2:
        return return_none
    data_today, data_ago = data[0], data[1]
    fig = go.Figure(
        data=[
            go.Indicator(
                mode='number+delta',
                value=data_today['close'],
                title = {"text": f"<b style='font-size=14px; color: #dea500'>Giá</b><br><span style='font-size:14px;color:gray'>{data_today['time']} {data_today['date']}</span><br><span style='font-size:13px;color:#CCC'>Phần trăm thay đổi: {data_today['pctChange']}%</span><br>"},
                delta = {'reference': data_ago['close']},
                domain = {'x': [0, 1], 'y': [0.4, 1]}
            )
        ],
        layout={
            'template': template_default,
            "height": 300,
            "width":250,
            "showlegend": True,
            "plot_bgcolor": plot_bgcolor,
            "paper_bgcolor": paper_bgcolor,
            "font": font_chart,
        },
    )
    return fig

#MarketCap
@app.callback(
    Output('company-profile-marketCap', 'figure'),
    Input('update-view', 'n_clicks'),
    Input('cp-interval-component', 'n_intervals'),
    State('search-symbol', 'value')
)
def live_marketCap(n_clicks, x, symbol):
    #If not symbol
    if symbol is None:
        return return_none

    api = f'https://finfo-api.vndirect.com.vn/v4/ratios/latest?filter=itemCode:51003&where=code:{symbol}&order=reportDate&fields=value'
    data = helpers.get_api(api)
    if len(data) != 1:
        return return_none
    value = data[0]['value']
    fig = go.Figure(
        data=[
            go.Indicator(
                mode='number',
                value=value,
                title = {"text": f"<b style='font-size=14px; color: #dea500'>Vốn hóa</b>"},
                domain = {'x': [0, 1], 'y': [0, 1]}
            )
        ],
        layout={
            'template': template_default,
            "height": 250,
            "width": 250,
            "showlegend": True,
            "plot_bgcolor": plot_bgcolor,
            "paper_bgcolor": paper_bgcolor,
            "font": font_chart,
        },
    )
    return fig

#Beta
@app.callback(
    Output('company-profile-beta', 'figure'),
    Input('update-view', 'n_clicks'),
    Input('cp-interval-component', 'n_intervals'),
    State('search-symbol', 'value')
)
def live_beta(n_clicks, x, symbol):
    #If not symbol
    if symbol is None:
        return return_none

    api = f'https://finfo-api.vndirect.com.vn/v4/ratios/latest?filter=itemCode:51007&where=code:{symbol}&order=reportDate&fields=value'
    data = helpers.get_api(api)
    if len(data) == 0:
        return return_none
    value = data[0]['value']
    fig = go.Figure(
        data=[
            go.Indicator(
                mode='number',
                value=value,
                title = {"text": f"<b style='font-size=14px; color: #dea500'>Beta</b>"},
                domain = {'x': [0, 1], 'y': [0, 1]}
            )
        ],
        layout={
            'template': template_default,
            "height": 250,
            "width": 250,
            "showlegend": True,
            "plot_bgcolor": plot_bgcolor,
            "paper_bgcolor": paper_bgcolor,
            "font": font_chart,
        },
    )
    return fig

#Image Company
@app.callback(
    Output('companyImage', 'src'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def get_image(n_clicks, symbol):
    return f'https://finance.vietstock.vn/image/{symbol}'

#Company Name
@app.callback(
    Output('companyName', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def companyName(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 1]

#Company Name English
@app.callback(
    Output('companyNameEng', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def companyNameEng(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 2]

#vnSummary
@app.callback(
    Output('vnSummary', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def vnSummary(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 12]

#Symbol
@app.callback(
    Output('symbol', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def symbol(n_clicks, symbol):
    if symbol is None:
        return None
    return symbol

#floor
@app.callback(
    Output('floor', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def floor(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    floor = df.iat[0, 10]
    if floor == 'HOSE':
        return 'Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh - HOSE'
    elif floor == 'HNX':
        return 'Sở Giao dịch Chứng khoán Hà Nội - HNX'
    return None

#listedDate
@app.callback(
    Output('listedDate', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def listedDate(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 11]

#foundDate
@app.callback(
    Output('foundDate', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def foundDate(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 4]

#industryName
@app.callback(
    Output('industryName', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def industryName(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 9]

#phone
@app.callback(
    Output('phone', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def phone(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 5]

#email
@app.callback(
    Output('email', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def email(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 6]

#website
@app.callback(
    [Output(component_id='website', component_property='children'),
    Output(component_id='website-img', component_property='href')],
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def website(n_clicks, symbol):
    if symbol is None:
        return None, None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 8], 'https://' + df.iat[0, 8]

#vnAddress
@app.callback(
    Output('vnAddress', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def vnAddress(n_clicks, symbol):
    if symbol is None:
        return None
    df = helpers.get_information_of_(symbol)
    return df.iat[0, 7]

#history
@app.callback(
    Output('history', 'children'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def history(n_clicks, symbol):
    if symbol is None:
        return None
    api = f'https://finfo-api.vndirect.com.vn/v4/company_notes?q=code:{symbol}~locale:VN&fields=history'
    data = helpers.get_api(api)
    history = data[0]['history']
    history = history.replace('<br>', '\n')
    return history

#Shareholders
def select_shareholders(symbol):
    api = f'https://finfo-api.vndirect.com.vn/v4/shareholders?sort=ownershipPct:desc&q=code:{symbol}'
    data = helpers.get_api(api)
    list_of_dicts = helpers.filter_drivers(data, ['shareholderName', 'numberOfShares', 'ownershipPct', 'roleType'])
    df = pd.DataFrame(list_of_dicts)
    df = df.sort_values(by='numberOfShares', ascending=False)
    df['ownershipPct'] = round(df['ownershipPct'] / 100, 5)
    x = round(1 - df['ownershipPct'].sum(), 3)
    different = {
        'shareholderName': 'Khác',
        'numberOfShares': None,
        'ownershipPct': x,
        'roleType': None
    }
    df = df.append(different, ignore_index=True)
    df = df.rename(columns={'shareholderName': 'Tên cổ đông', 'numberOfShares': 'Số cổ phiếu', 'ownershipPct': 'Tỷ lệ', 'roleType': 'Vai trò'})
    return df

#tbl shareholders
@app.callback(
    Output(component_id='tbl-shareholders', component_property='data'),
    Input(component_id='update-view', component_property='n_clicks'),
    State(component_id='search-symbol', component_property='value')
)
def tbl_shareholders(n_clicks, symbol):
    if symbol is None:
        return None
    df = select_shareholders(symbol)
    return df.to_dict('records')

#graph shareholders
@app.callback(
    Output(component_id='graph-shareholders', component_property='figure'),
    Input(component_id='update-view', component_property='n_clicks'),
    State(component_id='search-symbol', component_property='value')
)
def graph_shareholders(n_clicks, symbol):
    if symbol is None:
        return return_none
    #set data
    df_shareholders = select_shareholders(symbol)
    df_shareholders['pct'] = round(df_shareholders['Tỷ lệ'] * 100, 3)
    df_shareholders['pct'] = df_shareholders['pct'].map(str) + '%'
    fig = px.bar(df_shareholders.head(5), x='Tên cổ đông', y='Số cổ phiếu',
                 template=template_default, text='pct')
    fig.update_layout(title=dict(
                                 font=font_title,
                                 text='<b style="font-size: 14px">Top 5 nắm giữ cổ phiếu nhiều nhất </b>'),
                      font=font_chart,
                      margin=margin_chart,
                      hoverlabel=hover_label,
                      plot_bgcolor=plot_bgcolor,
                      paper_bgcolor=paper_bgcolor)

    fig.update_traces(hovertemplate=
                      '<b>Tên :</b> %{x}<br>' +\
                      '<b>Số cổ phiếu :</b> %{y}')
    fig.update_yaxes(title=None, showgrid=True)
    fig.update_xaxes(title=None, visible=False)
    return fig

#Graph historical price
@app.callback(
    Output('company-profile-graph-historical-price', 'figure'), 
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def graph_historical_price(n_clicks, symbol):
    if symbol is None:
        return return_none

    #set data
    df_filtered = helpers.get_historical_price_of_(symbol, start_date=None, end_date=None)
    min, max = df_filtered['close'].min(), df_filtered['close'].max()
    customdata = np.stack((df_filtered['symbol'], df_filtered['change']), axis=-1)
    #fig
    fig = px.line(df_filtered, x=df_filtered.index, y='close', range_y=(min - 1, max + 1), template=template_default)

    fig.update_layout(
        #title
        title=dict(
            font=font_title,
            text='<b style="font-size: 14px">Dữ liệu giao dịch</b><br><b style="color: #aaa; font-size:10px">Đơn vị: 1000 VND</b>'
            ),
        #font
        font=font_chart,
        margin=margin_chart,
        hoverlabel=hover_label,
        plot_bgcolor=plot_bgcolor,
        paper_bgcolor=paper_bgcolor)

    fig.update_traces(line_color=color_chart,
                      customdata=customdata,
                      hovertemplate=
                      '<b>Mã : %{customdata[0]}</b><br>' +\
                      '<b>Ngày :</b> %{x}<br>' +\
                      '<b>Giá :</b> %{y}<br>' +\
                      '<b>+/- :</b> %{customdata[1]}')

    fig.update_xaxes(title=None, showgrid=True,
                     rangeslider=dict(thickness=0.05, bgcolor='#444'),
                     rangeselector=dict(
                                        buttons=list([
                                                      dict(count=5, label="1w", step="day", stepmode="backward"),
                                                      dict(count=1, label="1m", step="month", stepmode="backward"),
                                                      dict(count=3, label="3m", step="month", stepmode="backward"),
                                                      dict(count=6, label="6m", step="month", stepmode="backward"),
                                                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                                                      dict(count=1, label="1y", step="year", stepmode="backward"),
                                                      dict(count=2, label="2y", step="year", stepmode="backward"),
                                                      dict(count=5, label="5y", step="year", stepmode="backward"),
                                                      dict(label="Max", step="all")
                                                      ]),
                                        activecolor='#dea500',
                                        bgcolor='#0A1929',
                                        bordercolor='#666',
                                        borderwidth=1,
                                        font_size=11,
                                        font_color="white",
                                        x=0.6)
                     )

    fig.update_yaxes(title=None)
    return fig

#Graph histogram
@app.callback(
    Output('company-profile-graph-histogram', 'figure'), 
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def graph_histogram(n_clicks, symbol):
    if symbol is None:
        return return_none
    #set data
    df_filtered = helpers.get_historical_price_of_(symbol, None, None)
    fig = px.histogram(df_filtered, y='close', nbins=30, 
                       color_discrete_sequence = [color_chart] , template=template_default)
    fig.update_layout(title=dict(
                                 font=font_title,
                                 text='<b style="font-size: 14px">Phối bố giá</b>'),
                      font=font_chart,
                      margin=margin_chart,
                      hoverlabel=hover_label,
                      plot_bgcolor=plot_bgcolor,
                      paper_bgcolor=paper_bgcolor)

    fig.update_traces(hovertemplate=
                      '<b>Giá :</b> %{y}<br>' +\
                      '<b>Số lượng :</b> %{x}')
    fig.update_xaxes(title=None, showgrid=True)
    fig.update_yaxes(title=None, visible=False)

    return fig

@app.callback(
    Output('company-profile-tbl-historical-price', 'data'),
    Input('update-view', 'n_clicks'),
    State('search-symbol', 'value')
)
def tbl_historical_price(n, symbol,):
    if symbol is None:
        return None
    df = helpers.get_historical_price_of_(symbol, None, None)
    df['date_1'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    df = df.sort_values(by=['date_1'], ascending=False)
    df = df.rename(columns={
        'date_1': 'Ngày',
        'open': 'Mở cửa',
        'high': 'Cao nhất',
        'low': 'Thấp nhất',
        'close': 'Đóng cửa',
        'nmVolume': 'Khối lượng khớp lệnh',
        'change': 'Thay đổi',
        'pctChange': 'Phần trăm thay đổi'
    })
    return df.to_dict('records')

#updated
@app.callback(Output('view-ing', 'children'),
              Input('update-view', 'n_clicks'),
              State('search-symbol', 'value'))
def view_ing(n, symbol):
    return 'Đang xem: ' + symbol 
    