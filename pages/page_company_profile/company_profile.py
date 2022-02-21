from dash import html, dcc, dash_table, Output, Input
from dash.dash_table import Format, FormatTemplate
import dash_bootstrap_components as dbc
from data_source import helpers
from app import app

dropdown_option = helpers.dropdown_find()
list_of_symbol = helpers.get_symbols()

tab_basic_info = html.Div(
    [
        dbc.Col([
            dcc.Interval( 
                id='cp-interval-component', 
                interval=1000*5, 
                n_intervals=0
                ),
            dcc.Graph(
                id='company-profile-live-price',
                config={'scrollZoom': False, 'displayModeBar': False}
                ),
            dcc.Graph(
                id='company-profile-marketCap',
                config={'scrollZoom': False, 'displayModeBar': False}
                ),
            dcc.Graph(
                id='company-profile-beta',
                config={'scrollZoom': False, 'displayModeBar': False}
                ),
                ]),
        dbc.Col([
            html.Div([
                html.A(html.Img(id='companyImage'), id='website-img'),
                html.H1(id='companyName'),
                html.H2(id='companyNameEng'),
                html.H3(id='vnSummary'),
                html.H2('Thông tin niêm yết', id='info-listed'),
                html.H5([
                    html.A('Mã chứng khoán: '),
                    html.A(id='symbol')
                    ]),
                html.H5([
                    html.A(id='floor')
                    ]),
                html.H5([
                    html.A('Ngày niêm yết: '),
                    html.A(id='listedDate')
                    ]),
                html.H2('Thông tin cơ bản', 'info-fundamental'),
                html.H5([
                    html.A('Ngày thành lập: '),
                    html.A(id='foundDate')
                    ]),
                html.H5([
                    html.A('Lĩnh vực: '), 
                    html.A(id='industryName')
                    ]),
                html.H5([
                    html.A('Điện thoại: '),
                    html.A(id='phone')
                    ]),
                html.H5([
                    html.A('Email: '),
                    html.A(id='email')
                    ]),
                html.H5([
                    html.A('Website: '),
                    html.A(id='website')
                    ]),
                html.H5([
                    html.A('Địa chỉ: '),
                    html.A(id='vnAddress')
                    ]),
                html.H5([
                    html.A('Lịch sử thành lập: '),
                    html.H6(id='history')
                    ])
                ])
            ],
            id='basic-info'
            )
    ]
)

tab_shareholders = html.Div([
    dbc.Row(
        dbc.Col([
            dash_table.DataTable(
                id='tbl-shareholders',
                columns=[
                    dict(name='Tên cổ đông', id='Tên cổ đông'),
                    dict(name='Số cổ phiếu', id='Số cổ phiếu', type='numeric', format=Format.Format().group(True)),
                    dict(name='Tỷ lệ', id='Tỷ lệ', type='numeric', format=FormatTemplate.percentage(2)),
                    dict(name='Vai trò', id='Vai trò')
                    ],
                cell_selectable = False,
                style_header={'backgroundColor': '#211551', 'border': '0'},
                style_table={'height': '500px', 'overflowY': 'auto', 'width': '100%', 'border-radius': '0.5rem'},
                style_cell_conditional=[
                    {'if': {'column_id': ['Tên cổ đông', 'Vai trò']},
                    'textAlign': 'left'}],
                style_data_conditional=[
                    {'if': {'row_index': 'odd'},
                    'backgroundColor': '#222'}],
                style_as_list_view=True,
                fixed_rows={"headers": True}
            )
            ])
    ),
    dbc.Col(
        dcc.Graph(
            id='graph-shareholders',
            config={'scrollZoom': False, 'displayModeBar': False}
            )
        )
    ]
)

tab_historical_data = html.Div([
    #Chart Historical Price
    dbc.Row([
        dcc.Graph(
            id='company-profile-graph-historical-price',
            config={'scrollZoom': False, 'displayModeBar': False}
            ),
        #Chart Histogram
        dcc.Graph(
            id='company-profile-graph-histogram',
            config={'scrollZoom': False, 'displayModeBar': False}
            )
        ]),
    dbc.Row([
        dash_table.DataTable(
            id='company-profile-tbl-historical-price',
            columns=[
                dict(name='Ngày', id='Ngày'),
                dict(name='Mở cửa', id='Mở cửa'),
                dict(name='Cao nhất', id='Cao nhất'),
                dict(name='Thấp nhất', id='Thấp nhất'),
                dict(name='Đóng cửa', id='Đóng cửa'),
                dict(name='Khối lượng khớp lệnh', id='Khối lượng khớp lệnh', format=Format.Format().group(True)),
                dict(name='Thay đổi', id='Thay đổi'),
                dict(name='Phần trăm thay đổi', id='Phần trăm thay đổi')
                ],
            page_size=100,
            cell_selectable = False,
            style_table={'height': '332px', 'overflowY': 'auto', 'backgroundColor': '#111', 'width': '100%'},
            style_data_conditional=[
                {'if': {'row_index': 'odd'},
                 'backgroundColor': '#222'}],
            style_as_list_view=True,
            fixed_rows={"headers": True}
            )
            ]),
    ]
)

#Layout of page
layout_company_profile = html.Div([
    #Row 1: HEADER
    html.Div([
        #Drop Down for search symbol
        dbc.Col(
            dcc.Dropdown(
                options = dropdown_option,
                placeholder="Nhập mã chứng khoán / tên công ty",
                id='search-symbol',
                persistence = True,
                persistence_type = 'session',
                value='VNM'
                ),
            id='search-symbol-column'
            ),
        #Button Update View
        dbc.Col(
            dbc.Button(
                "Xem",
                id="update-view",
                n_clicks=1
                ),
            id='update-view-column'
            ),
        #Show view_ing symbol
        dbc.Col(
            html.Div(id='view-ing'),
            id='time-update-view-column'
            )
        ],
        id='company-profile-row-1'
        ),
    #Row 2
    dcc.Tabs(
        id="company-profile-tabs",
        value='tab-1',
        children=[
            dcc.Tab(
                label='THÔNG TIN CƠ BẢN',
                value='tab-1',
                id='tab-basic-info',
                selected_className='tab--selected'
            ),
            dcc.Tab(
                label='THÔNG TIN CỔ ĐÔNG',
                value='tab-2',
                id='tab-basic-info',
                selected_className='tab--selected'
            ),
            dcc.Tab(
                label='DỮ LIỆU GIAO DỊCH',
                value='tab-3',
                id='tab-basic-info',
                selected_className='tab--selected'
            ),
        ]),
    html.Div(id='company-profile-output-tab')
    ],
    id='company-profile'
)

#Callback output layout of tab
@app.callback(Output('company-profile-output-tab', 'children'),
              Input('company-profile-tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return tab_basic_info
    elif tab == 'tab-2':
        return tab_shareholders
    elif tab == 'tab-3':
        return tab_historical_data