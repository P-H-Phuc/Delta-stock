#Call packages required
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import statsmodels.api as sm
import datetime
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from dash import Output, Input, State
from data_source import helpers
from app import app
#Template
template_default = 'plotly_dark'
font_title = dict(color='white', family='Arial')
font_chart = dict(color='#999', size=10)
margin_chart = dict(l=20, r=10, b=10, t=60, pad=0)
hover_label = dict(font_size=12, font_color='white')
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
                )
            }
            
#Live price-------------------------
@app.callback(
    Output('price-performance-live-price', 'figure'),
    Input('pp-update-view', 'n_clicks'),
    State('pp-interval-component', 'n_intervals'),
    State('pp-search-symbol', 'value')
)
def live_price(n_clicks, x, symbol):
    #If not symbol
    if symbol is None:
        return return_none

    api = f'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:{symbol}&fields=date,time,close,change,pctChange&size=2'
    data = helpers.get_api(api)
    data_today = data[0]
    data_ago = data[1]
    fig = go.Figure(
        data=[
            go.Indicator(
                mode='number+delta',
                value=data_today['close'],
                title = {"text": f"<b>Giá</b><br><span style='font-size:14px;color:#ccc'>{data_today['time']} {data_today['date']}</span><br><span style='font-size:13px;color:#CCC'>Phần trăm thay đổi: {data_today['pctChange']}%</span>"},
                delta = {'reference': data_ago['close'], 'position': 'top'},
                domain = {'x': [0, 1], 'y': [0, 1]},
            )
        ],
        layout={
            'template': template_default,        
            "showlegend": True,
            'width': 250,
            'height': 235,
            "paper_bgcolor": 'rgba(0,0,0,0)',
            'plot_bgcolor': 'rgba(0,0,0,0)'
            # "font": font_chart,
        },
    )
    return fig

#High 52 week-------------------------
@app.callback(
    Output('price-performance-high52w', 'figure'),
    Input('pp-update-view', 'n_clicks'),
    State('pp-interval-component', 'n_intervals'),
    State('pp-search-symbol', 'value')
)
def high52(n_clicks, x, symbol):
    #If not symbol
    if symbol is None:
        return return_none

    api = f'https://finfo-api.vndirect.com.vn/v4/ratios/latest?filter=itemCode:51001,&where=code:{symbol}&order=reportDate&fields=value,reportDate'
    data = helpers.get_api(api)
    value = data[0]['value'] / 1000
    fig = go.Figure(
        data=[
            go.Indicator(
                mode='number',
                value=value,
                title = {"text": f"<b>Cao nhất 52 tuần</b><br><span style='font-size:14px;color:#ccc'>Ngày báo cáo: {data[0]['reportDate']}</span>"},
                domain = {'x': [0, 1], 'y': [0.5, 1]},
                delta={'valueformat':'000.2f'},
                number_valueformat = ':10.2f',
            )
        ],
        layout={
            'template': template_default,
            'width': 250,
      'height': 235,
            "showlegend": True,
            "font": font_chart,
        },
    )
    return fig

#Low 52 week-------------------------
@app.callback(
  Output('price-performance-low52w', 'figure'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-interval-component', 'n_intervals'),
  State('pp-search-symbol', 'value')
)
def low52w(n, x, symbol):
  if symbol is None:
    return return_none

  api = f'https://finfo-api.vndirect.com.vn/v4/ratios/latest?filter=itemCode:51002&where=code:{symbol}&order=reportDate&fields=value,reportDate'
  data = helpers.get_api(api)
  value = data[0]['value'] / 1000
  fig = go.Figure(
    data=[
      go.Indicator(
        mode='number',
        value=value,
        title = {"text": f"<b>Thấp nhất 52 tuần</b><br><span style='font-size:14px;color:#ccc'>Ngày báo cáo: {data[0]['reportDate']}</span>"},
        domain = {'x': [0, 1], 'y': [0.5, 1]},
        delta={'valueformat':'.2f'},
        number_valueformat = '.2f',
        )
        ],
    layout={
      'template': template_default,
      'width': 250,
      'height': 235,
      "showlegend": True,  
      "font": font_chart,
      }
    )
  return fig

#PE-------------------------
@app.callback(
  Output('price-performance-PE', 'figure'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-interval-component', 'n_intervals'),
  State('pp-search-symbol', 'value')
)
def pe(n, x, symbol):
  if symbol is None:
    return return_none

  api = f'https://finfo-api.vndirect.com.vn/v4/ratios/latest?filter=itemCode:51006&where=code:{symbol}&order=reportDate&fields=value,reportDate'
  data = helpers.get_api(api)
  if len(data) == 0:
    return None
  value = data[0]['value']
  fig = go.Figure(
    data=[
      go.Indicator(
        mode='number',
        value=value,
        title = {"text": f"<b>P/E tra cứu</b><br><span style='font-size:14px;color:#ccc'>Ngày báo cáo: {data[0]['reportDate']}</span>"},
        domain = {'x': [0, 1], 'y': [0.5, 1]},
        number = {'valueformat':'.2f'}
        )
        ],
    layout={
      'template': template_default,
      "height": 235,
      "width":250,
      "showlegend": True,  
      "font": font_chart,
      }
    )
  return fig

#return rate-------------------------
@app.callback(
  Output('price-performance-return-rate', 'figure'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-interval-component', 'n_intervals'),
  State('pp-search-symbol', 'value')
)
def return_rate(n, x, symbol):
  if symbol is None:
    return return_none

  api = f'https://finfo-api.vndirect.com.vn/v4/ratios/latest?filter=itemCode:51033&where=code:{symbol}&order=reportDate&fields=value,reportDate'
  data = helpers.get_api(api)
  if len(data) != 1:
    return return_none
  value = data[0]['value']
  fig = go.Figure(
    data=[
      go.Indicator(
        mode='number',
        value=value,
        title = {"text": f"<b>Tỷ suất cổ tức</b><br><span style='font-size:14px;color:#ccc'>Ngày báo cáo: {data[0]['reportDate']}</span>"},
        domain = {'x': [0, 1], 'y': [0.5, 1]},
        number = {'valueformat':'002.2f'}
        )
        ],
    layout={
      'template': template_default,
      'width': 250,
      'height': 235,
      "showlegend": True,  
      "font": font_chart,
      }
    )
  return fig

#Price historical graph-------------------------
@app.callback(
  Output('price-performance-graph-historical-price', 'figure'),
  Input('pp-update-view', 'n_clicks'),
  Input('radio-items-trendlines', 'value'),
  Input('trendline-rolling-number', 'value'),
  Input('trendline-lowess-frac', 'value'),
  Input('trendline-ewm-halflife', 'value'),
  State('pp-search-symbol', 'value'),
  State('range-date', 'start_date'),
  State('range-date', 'end_date')
)
def pp_graph_historical_price(n, trend_line, nbr_rolling, frac_lowess, halflife, symbol, start_date, end_date):
  if symbol is None:
    return return_none
  #set data
  df = helpers.get_historical_price_of_(symbol, start_date, end_date)
  df['nbr_time'] = df.index.map(datetime.date.toordinal)
  customdata = np.stack((df['symbol'], df['change']), axis=-1)

  #fig default
  fig = px.scatter(
    df, 
    x=df.index,
    y='close', 
    color_discrete_sequence=[color_chart],
    template=template_default
    )
  
  #OLS
  if trend_line == 'ols':
    # setup for linear regression using sm.OLS
    Y=df['close']
    X=df['nbr_time']
    X=sm.add_constant(X)
    trend = sm.OLS(Y,X).fit().fittedvalues
    fig.add_trace(go.Scatter(x=df.index, y=trend, mode='lines', name='OLS'))

  #Moving Average
  elif trend_line == 'rolling':
    fig = px.scatter(
      df, x=df.index, y='close',
      color_discrete_sequence=[color_chart],
      template=template_default,
      trendline='rolling', trendline_options=dict(window=1 if nbr_rolling is None else nbr_rolling), trendline_color_override='#DCD800')

  #LOWESS
  elif trend_line == 'lowess':
    fig = px.scatter(
      df, x=df.index, y='close',
      color_discrete_sequence=[color_chart],
      template=template_default,
      trendline='lowess', trendline_options=dict(frac=0.6666 if frac_lowess is None else frac_lowess), trendline_color_override='#DCD800')
  
  #Exponential
  elif trend_line == 'ewm':
    fig = px.scatter(
      df, x=df.index, y='close',
      color_discrete_sequence=[color_chart],
      template=template_default,
      trendline='ewm', trendline_options=dict(halflife=1 if halflife is None else halflife), trendline_color_override='#DCD800')
  
  #Fama-French
  elif trend_line == 'fama_french':
    Y=df['close']
    X=df[['open', 'high', 'nmVolume']]
    X=sm.add_constant(X)
    trend = sm.OLS(Y,X).fit().fittedvalues
    fig.add_trace(go.Scatter(x=df.index, y=trend, mode='lines', name='Fama - French'))

  #View nmVolume
  elif trend_line == 'nmVolume':
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Bar(x=df.index, y=df['nmVolume'], name='Khối lượng'), 
      secondary_y=True)

    fig.add_trace(go.Scatter(x=df.index, y=df['close'], name='Giá'), 
      secondary_y=False)

    fig.update_layout(
      #title
      title=dict(
        font=font_title,
        text=f'<b style="font-size: 14px">Dữ liệu lịch sử của {symbol}</b><br><b style="color: #aaa; font-size:10px">Đơn vị: 1000 VND | 1 CP</b>'
        ),
      #font
      font=font_chart,
      showlegend=False,
      margin=margin_chart,
      hoverlabel=hover_label,
      hovermode='x unified',
      paper_bgcolor='black',
      plot_bgcolor='black',
      )

    fig.update_xaxes(
      title=None, showgrid=False,
      rangeslider=dict(thickness=0.05, bgcolor='#444'),
      rangeselector=dict(
        buttons=list(
          [
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="2y", step="year", stepmode="backward"),
            dict(label='Max', step="all")
            ]
            ),
            activecolor='#dea500',
            bgcolor='black',
            bordercolor='#666',
            borderwidth=1,
            font_size=11,
            font_color="white",
            x=0.75)
            )
    fig.update_yaxes(title=None, showgrid=False, secondary_y=False)
    fig.update_yaxes(title=None, showgrid=False, secondary_y=True)
    return fig

  fig.update_traces(
    mode='lines',
    customdata=customdata,
    hovertemplate=
    '<b>%{customdata[0]}</b><br>' +\
    '<b>Date :</b> %{x}<br>' +\
    '<b>Price :</b> %{y}<br>' +\
    '<b>+/- :</b> %{customdata[1]}'
    )

  fig.update_layout(
    #title
    title=dict(
      font=font_title,
      text=f'<b style="font-size: 14px">Dữ liệu lịch sử của {symbol}</b><br><b style="color: #aaa; font-size:10px">Đơn vị: 1000 VND</b>'
      ),
    #font
    font=font_chart,
    showlegend=False,
    margin=margin_chart,
    hoverlabel=hover_label,
    hovermode='x unified',
    )

  fig.update_xaxes(
    title=None, showgrid=True,
    rangeslider=dict(thickness=0.05, bgcolor='#444'),
    rangeselector=dict(
      buttons=list(
        [
          dict(count=1, label="1m", step="month", stepmode="backward"),
          dict(count=3, label="3m", step="month", stepmode="backward"),
          dict(count=6, label="6m", step="month", stepmode="backward"),
          dict(count=1, label="YTD", step="year", stepmode="todate"),
          dict(count=1, label="1y", step="year", stepmode="backward"),
          dict(count=2, label="2y", step="year", stepmode="backward"),
          dict(label='Max', step="all")
          ]
          ),
          activecolor='#dea500',
          bgcolor='#0A1929',
          bordercolor='#666',
          borderwidth=1,
          font_size=11,
          font_color="white",
          x=0.75)
          )
  fig.update_yaxes(title=None)

  return fig

#Historical price table-------------------------
@app.callback(
    Output('pp-tbl-historical-price', 'data'),
    Input('pp-update-view', 'n_clicks'),
    State('pp-search-symbol', 'value'),
    State('range-date', 'start_date'),
    State('range-date', 'end_date')
)
def pp_tbl_historical_price(n, symbol, start_date, end_date):
    if symbol is None:
        return None
    #Set data
    df_price = helpers.get_historical_price_of_(symbol, start_date, end_date)
    df_price['pctChange'] = df_price['pctChange']/100
    df_mkc = helpers.get_marketcap_of_(symbol, start_date, end_date)
    df_mkc['marketCap'] = round(df_mkc['marketCap'] / 1e9, 3)
    df_mkc = df_mkc[['date', 'marketCap']]
    #Merge
    df = df_price.merge(df_mkc, how='left', on=['date'])
    df = df.sort_values(by=['date'], ascending=False)
    df = df.rename(columns={
        'date': 'Ngày',
        'open': 'Mở cửa',
        'high': 'Cao nhất',
        'low': 'Thấp nhất',
        'close': 'Đóng cửa',
        'change': 'Thay đổi',
        'pctChange': '% Thay đổi',
        'nmVolume': 'KLGD',
        'marketCap': 'Vốn hóa'
    })
    return df.to_dict('records')

#Descriptive stat-------------------------
@app.callback(
  Output('pp-descriptive-stat', 'data'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-search-symbol', 'value'),
  State('range-date', 'start_date'),
  State('range-date', 'end_date')
)
def descriptive_stat(n, symbol, start_date, end_date):
  if symbol is None:
    return None
  #Set data
  df = helpers.get_historical_price_of_(symbol, start_date, end_date)
  stat = df.describe()
  stat.reset_index(drop=False, inplace=True)
  stat['nmVolume'] = round(stat['nmVolume'], 2)
  stat = stat.rename(columns={
    'index': 'Chỉ số',
    'open' : 'Mở cửa',
    'high': 'Cao nhất',
    'low': 'Thấp nhất',
    'close': 'Đóng cửa',
    'change': 'Thay đổi',
    'pctChange': '% Thay đổi',
    'nmVolume': 'KLGD',
  })
  return stat.to_dict('records')

#Plot pie of closing price-------------------------
@app.callback(
  Output('price-performance-graph-pie-updown', 'figure'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-search-symbol', 'value'),
  State('range-date', 'start_date'),
  State('range-date', 'end_date')
)
def plot_pie_updown(n, symbol, start_date, end_date):
  if symbol is None:
    return return_none
  #Set data
  df = helpers.get_historical_price_of_(symbol, start_date, end_date)
  values = [(df['change'] > 0).sum(), (df['change'] < 0).sum(), (df['change'] == 0).sum()]
  labels = ['Tăng giá', 'Giảm giá', 'Đứng giá']
  colors = ['#FF0000', '#00FF00', 'yellow']
  #Figure
  fig = px.pie(names=labels, values=values, color_discrete_sequence=colors, template='plotly_dark')
  fig.update_traces(
    hole=.6, 
    hovertemplate= 
    '<b>%{label}</b><br>' +\
    '<b>Số lần :</b> %{value}'
    )
  fig.update_layout(
    title=None,
    margin=dict(l=20, r=20, b=20, t=20, pad=1),
    hoverlabel=dict(font_size=14, font_color='#000'),
    # Add annotations in the center of the donut pies.
    annotations=[dict(text=f'<b>{symbol}</b>', xanchor='center', font_size=32, showarrow=False, font_color='#3399ff')],
    showlegend=False,
  )
  return fig

#Displot
@app.callback(
  Output('displot', 'figure'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-search-symbol', 'value'),
  State('range-date', 'start_date'),
  State('range-date', 'end_date')
)
def pp_displot(n, symbol, start_date, end_date):
  if symbol is None:
    return return_none
  import plotly.figure_factory as ff
  df = helpers.get_historical_price_of_(symbol, start_date, end_date)
  fig_dummy = ff.create_distplot([df.change], ['Lợi nhuận'], curve_type = 'normal')
  normal_x = fig_dummy.data[1]['x']
  normal_y = fig_dummy.data[1]['y']
  fig = make_subplots(specs=[[{"secondary_y": True}]])
  hist = px.histogram(df, x="change")
  fig.add_trace(go.Histogram(x=hist.data[0].x,
                             y=hist.data[0].y,
                             marker_color= color_chart,
                             name='Tần số'), 
                secondary_y=False)
  fig.add_trace(go.Scatter(x=normal_x, 
                           y=normal_y,
                           mode = 'lines',
                           line = dict(color='#00FF00', width = 2),
                           name = 'Normal'), 
                secondary_y=True)
  fig.update_layout(title=dict(font=font_title,
                               text=f'<b style="font-size: 14px">Phân phối lợi nhuận</b>'),
                    font=font_chart,
                    showlegend=False,
                    margin=margin_chart,
                    hoverlabel=hover_label,
                    hovermode='x unified',
                    paper_bgcolor='black',
                    plot_bgcolor='black'
                    )

  fig.update_traces(hovertemplate=
                      '<b>Y :</b> %{y}<br>' +\
                      '<b>X :</b> %{x}',
                    opacity=0.75)
  fig.update_xaxes(visible=True, title=None, showgrid=False,tickmode='linear')
  fig.update_yaxes(visible=True, title='Tần số', secondary_y=False, showgrid=False)
  fig.update_yaxes(visible=True, title='Normal', secondary_y=True, showgrid=False, zeroline=False)
  return fig

#Cummulative value graph
@app.callback(
  Output('cummulative-graph', 'figure'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-search-symbol', 'value'),
  State('range-date', 'start_date'),
  State('range-date', 'end_date')
)
def  cummulative_graph(n, symbol, start_date, end_date):
  if symbol is None:
    return return_none
  df = helpers.get_historical_price_of_(symbol, start_date, end_date)
  df['rets'] = np.log(df['close']) - np.log(df['close'].shift(1))
  df['cummulative'] = round((1 + df['rets']).cumprod(), 3)

  fig = px.line(df, x=df.index, y='cummulative', 
    template=template_default, color_discrete_sequence=[color_chart])
  fig.update_traces(
    hovertemplate=
    '<b>Date :</b> %{x}<br>' +\
    '<b>Giá trị :</b> %{y}'
    )

  fig.update_layout(
    #title
    title=dict(
      font=font_title,
      text=f'<b style="font-size: 14px">Giá trị tích lũy</b><br><b style="color: #aaa; font-size:10px">Đầu tư : 1 đvt</b>'
      ),
    #font
    font=font_chart,
    showlegend=False,
    margin=margin_chart,
    hoverlabel=hover_label,
    )

  fig.update_xaxes(title=None, showgrid=False)
  fig.update_yaxes(title=None)
  return fig

#Symbol VaR
@app.callback(
  Output('symbol-of-VaR', 'children'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-search-symbol', 'value')
)
def symbol_of_VaR(n, symbol):
  return symbol

#VaR
@app.callback(
  Output('hold-VaR', 'children'),
  Output('VaR', 'children'),
  Input('calculate-VaR', 'n_clicks'),
  State('pp-search-symbol', 'value'),
  State('range-date', 'start_date'),
  State('range-date', 'end_date'),
  State('nbr-shares', 'value'),
  State('confidence-level-VaR', 'value'),
  State('days-VaR', 'value'),
)
def VaR(n, symbol, start_date, end_date, shares, confidence_level, days):
  from scipy.stats import norm
  from math import sqrt
  if symbol is None:
    return None, None
  if shares is None:
    return None, None
  if confidence_level is None:
    return None, None
  if days is None:
    return None, None
  df = helpers.get_historical_price_of_(symbol, start_date, end_date)
  ret = df['close'].pct_change(1).dropna()
  z = norm.ppf(confidence_level)
  position = shares*df['close'][-1]
  VaR = position*z*np.std(ret)*sqrt(days)
  return f'- Nắm giữ: {position} nghìn VNĐ', f'- VaR: {round(VaR, 4)} in {days} days.'

@app.callback(
  Output('pp-view-ing', 'children'),
  Input('pp-update-view', 'n_clicks'),
  State('pp-search-symbol', 'value')
)
def pp_view_ing(n, symbol):
  return 'Bạn đang xem: ' + str(symbol)