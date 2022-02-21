from dash import html, dcc, dash_table
from dash.dash_table import Format, FormatTemplate
import dash_bootstrap_components as dbc
from data_source import helpers
from datetime import date

dropdown_option = helpers.dropdown_find()
list_of_symbol = helpers.get_symbols()
config = {'scrollZoom': False, 'displayModeBar': False}

#Set layout
layout_price_performance = html.Div(
        [
                #Row-1: HEADER
                dbc.Row(
                        [
                                #Drop Down for search symbol
                                dbc.Col(
                                        dcc.Dropdown(
                                                value='VNM',
                                                options = dropdown_option,
                                                placeholder="Nhập mã chứng khoán / tên công ty",
                                                id='pp-search-symbol',
                                                persistence = True,
                                                persistence_type = 'session', # memory / local
                                                ),
                                        id='search-symbol-column'
                                        ),
                            # Date Picker Range
                                dbc.Col(
                                        dcc.DatePickerRange(
                                                display_format='YYYY-MM-DD',
                                                start_date_placeholder_text = 'yyyy-mm-dd',
                                                end_date_placeholder_text = 'yyyy-mm-dd',
                                                initial_visible_month=date.today(),
                                                id='range-date',
                                                clearable=True,
                                                minimum_nights=5,
                                                min_date_allowed='2013-01-01',
                                                max_date_allowed=date.today(),
                                                persistence = True,
                                                start_date='2021-01-01',
                                                end_date='2021-12-31',
                                                persistence_type = 'session' # memory / local
                                                ),
                                        id='date-picker-column'
                                        ),
                            # Button Update View
                                dbc.Col(
                                        dbc.Button(
                                                "Xem",
                                                id="pp-update-view",
                                                n_clicks=1
                                                ),
                                        id='update-view-column'
                                        ),
                                dbc.Col(
                                        html.Div(id='pp-view-ing')
                                )
                        ],
                        id='price-performance-row-1'
                ),
                #Row-2
                dbc.Row(
                        [
                                dcc.Interval(
                                        id='pp-interval-component', 
                                        interval=1000*5, 
                                        n_intervals=0),
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='price-performance-live-price',
                                        )                 
                                ),
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='price-performance-high52w'
                                        )
                                ),
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='price-performance-low52w'
                                        )
                                ),
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='price-performance-PE'
                                        )
                                ),
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='price-performance-return-rate'
                                        )
                                ),
                        ]
                ),
                
                #ROW 3
                dbc.Row(
                        [
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='price-performance-graph-historical-price',
                                                )
                                ),
                                dbc.Col(
                                        [
                                                dcc.RadioItems(
                                                        id='radio-items-trendlines',
                                                        options=[
                                                                {'label': ' Mặc định', 'value': 'None'},
                                                                {'label': ' Xu hướng', 'value': 'ols'},
                                                                {'label': ' Trung bình trượt', 'value': 'rolling'},
                                                                {'label': ' Hồi quy cục bộ', 'value': 'lowess'},
                                                                {'label': ' Hàm mũ', 'value': 'ewm'},
                                                                {'label': ' Fama - French', 'value': 'fama_french'},
                                                                {'label': ' Xem khối lượng', 'value': 'nmVolume'},
                                                                ]
                                                        ),
                                                dcc.Input(
                                                        id='trendline-rolling-number',
                                                        type='number', placeholder='Hệ số trượt',
                                                        min=1, max=252, step=1
                                                        ),
                                                dcc.Input(
                                                        id='trendline-lowess-frac',
                                                        type='number', placeholder='Trọng số',
                                                        min=0, max=1, step=0.001
                                                ),
                                                dcc.Input(
                                                        id='trendline-ewm-halflife',
                                                        type='number', placeholder='Số mũ',
                                                        min=1, max=5, step=1
                                                )
                                                ]
                                        )
                        ]
                ),
                
                #ROW 4
                dbc.Row(
                        [
                                dash_table.DataTable(
                                        id='pp-tbl-historical-price',
                                        columns=[
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'Ngày'], id='Ngày'),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'Mở cửa'], id='Mở cửa', type='numeric', format={'specifier': '.2f'}),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'Cao nhất'], id='Cao nhất', type='numeric', format={'specifier': '.2f'}),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'Thấp nhất'], id='Thấp nhất', type='numeric', format={'specifier': '.2f'}),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'Đóng cửa'], id='Đóng cửa', type='numeric', format={'specifier': '.2f'}),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'Thay đổi'], id='Thay đổi', type='numeric', format={'specifier': '.2f'}),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', '% Thay đổi'], id='% Thay đổi', type='numeric', format=FormatTemplate.percentage(4)),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'KLGD'], id='KLGD', type='numeric', format=Format.Format().group(True)),
                                                dict(name=['DỮ LIỆU GIAO DỊCH', 'Vốn hóa'], id='Vốn hóa', type='numeric', format=Format.Format().group(True))
                                                ],
                                        merge_duplicate_headers=True,
                                        export_format='xlsx',
                                        export_headers='display',
                                        cell_selectable = False,
                                        style_table={'height': '450px', 'overflowY': 'auto', 'width': '100%'},
                                        page_size=30,
                                        style_data={'width': '100px', 'backgroundColor': 'black'},
                                        style_data_conditional=[
                                                {'if': {'filter_query': '{Thay đổi} < 0'},
                                                 'color': 'red'},
                                                {'if': {'filter_query': '{Thay đổi} > 0'},
                                                 'color': '#00FF00'},
                                                {'if': {'filter_query': '{Thay đổi} = 0'},
                                                 'color': 'yellow'},
                                                ],
                                        style_as_list_view=True,
                                        fixed_rows={"headers": True}
                                )
                        ]
                ),
                
                #ROW 5
                dbc.Row(
                        [
                                dbc.Col(
                                        dash_table.DataTable(
                                                id='pp-descriptive-stat',
                                                columns=[
                                                        dict(name=['THỐNG KÊ CƠ BẢN', 'Chỉ số'], id='Chỉ số'),
                                                        dict(name=['THỐNG KÊ CƠ BẢN', 'Mở cửa'], id='Mở cửa', type='numeric', format={'specifier': '.2f'}),
                                                        dict(name=['THỐNG KÊ CƠ BẢN', 'Cao nhất'], id='Cao nhất', type='numeric', format={'specifier': '.2f'}),
                                                        dict(name=['THỐNG KÊ CƠ BẢN', 'Thấp nhất'], id='Thấp nhất', type='numeric', format={'specifier': '.2f'}),
                                                        dict(name=['THỐNG KÊ CƠ BẢN', 'Đóng cửa'], id='Đóng cửa', type='numeric', format={'specifier': '.2f'}),
                                                        dict(name=['THỐNG KÊ CƠ BẢN', 'Thay đổi'], id='Thay đổi', type='numeric', format={'specifier': '.2f'}),
                                                        dict(name=['THỐNG KÊ CƠ BẢN', '% Thay đổi'], id='% Thay đổi', type='numeric', format={'specifier': '.2f'}),
                                                        dict(name=['THỐNG KÊ CƠ BẢN', 'KLGD'], id='KLGD', type='numeric', format=Format.Format().group(True))
                                                        ],
                                                merge_duplicate_headers=True,
                                                style_header={'backgroundColor': '#D3D3D3', 'border': '0'},
                                                style_table={'height': '380px', 'overflowY': 'auto', 'width': '100%', 'border-radius': '0.5rem'},
                                                style_data_conditional=[{'if': {'row_index': 'odd'},
                                                                         'backgroundColor': '#222'}
                                                                         ]
                                                                         )
                                        ),
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='price-performance-graph-pie-updown'
                                                )
                                        ),
                        ]
                ),
                
                #ROW 6
                dbc.Row(
                        [
                                dbc.Col(
                                        dcc.Graph(
                                                config=config,
                                                id='displot'
                                        )
                                ),
                                dbc.Col(
                                        [
                                                dcc.Graph(
                                                        config=config,
                                                        id='cummulative-graph'
                                                ),
                                        ]
                                ),
                                dbc.Col(
                                        [
                                                html.P('Value At Risk', id='text-VaR'),
                                                html.P(id='symbol-of-VaR'),
                                                html.Div(
                                                        [
                                                                html.A('Số cổ phiếu:', style={'margin-left': '15px'}),
                                                                dcc.Input(
                                                                        id='nbr-shares',
                                                                        type='number', placeholder='Nhập số cổ phiếu ',
                                                                        min=1, max=999999, step=1
                                                                )
                                                        ]
                                                ),
                                                html.Div(
                                                        [
                                                                html.A('Độ tin cậy:', style={'margin-left': '15px'}),
                                                                dcc.Input(
                                                                        id='confidence-level-VaR',
                                                                        type='number', placeholder='Từ 0 đến 1 ',
                                                                        min=0, max=1, step=0.01
                                                                )
                                                        ], style={'margin-top': '10px'}
                                                ),
                                                html.Div(
                                                        [
                                                                html.A('Số ngày:', style={'margin-left': '15px'}),
                                                                dcc.Input(
                                                                        id='days-VaR',
                                                                        type='number', placeholder='Số ngày nắm giữ ',
                                                                        min=1, max=9999, step=1
                                                                )
                                                        ], style={'margin-top': '10px'}
                                                ),
                                                dbc.Button(
                                                        "Tính",
                                                        id="calculate-VaR",
                                                        n_clicks=1
                                                ),
                                                html.Div(
                                                        [
                                                                html.P(id='hold-VaR'),
                                                                html.P(id='VaR'),
                                                        ], id='div-VaR'
                                                )
                                        ],
                                        id='VaR-col'
                                )
                        ]
                ),
        ],
        id='price-performance'
)