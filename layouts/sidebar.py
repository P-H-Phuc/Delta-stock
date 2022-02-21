"""Sidebar for the app"""

import dash_bootstrap_components as dbc
from dash import html, dcc

sidebar_layout_style = {
    #Layout
    "position": "fixed",
    "overflow-x": "hidden",
    "left": "0rem",
    "width": "14rem",
    "height": "100%",
    "padding-top": "1rem",
    "padding-bottom": "3px",
    "margin-right": "0.5rem",
    "background-image": "linear-gradient(180deg, black, gray)",
    "z-index": "1000"
}

sidebar_header_style = {
    "font-size": "24px",
    "font-weight": "bold",
}

sidebar_icon_style = {
    # "color": "#828282",
    "font-size": "13px",
    "margin-right": "10px",
    "margin-left": "4px"
}

sidebar_text_nav_style = {
    # 'color': '#828282', 
    'font-size':'13px',
    'font-weight': 'bold'
}

sidebar = html.Div(className='sidebar', style=sidebar_layout_style, children=[
        html.Header(
            [
                html.A(
                    html.Img(
                        src='/assets/images/logo.png', 
                        width='20%', 
                        style={'margin-left': '16px', 'margin-right': '24px'}
                        ),
                    href='/'
                    ),
                html.A('DELTA', style={'color': 'white'})
            ],
                    className='sidebar-header', 
                    style=sidebar_header_style),
        
        html.Hr(style={"color": "#81c7f5", "height": "1px"}),
        html.Br(),

        dbc.Nav(vertical=True, pills=True,
                children=[
                    dbc.NavLink(children=[
                        html.I(className='fa fa-fw fa-tachometer-alt', style=sidebar_icon_style),
                        html.A('Tổng quan thị trường', style=sidebar_text_nav_style)], 
                               className='sidebar-market-overview', href='/market-overview', active='exact'),

                    dbc.NavLink(children=[
                        html.I(className='fa fa-fw fa-snowflake', style=sidebar_icon_style),
                        html.A('Hồ sơ doanh nghiệp', style=sidebar_text_nav_style)],
                               className='sidebar-company-profile', href='/company-profile', active='exact'),

                    dbc.NavLink(children=[
                        html.I(className='fa fa-fw fa-chart-bar', style=sidebar_icon_style),
                        html.A('Hiệu suất giá', style=sidebar_text_nav_style)],
                               className='sidebar-price-performance', href='/price-performance', active='exact'),

                    dbc.NavLink(children=[
                        html.I(className='fa fa-fw fa-star', style=sidebar_icon_style),
                        html.A("Quản lý danh mục", style=sidebar_text_nav_style)],
                               className='sidebar-portfolio', href="/management-portfolio", active="exact"),

                    dbc.NavLink(children=[
                        html.I(className='fa fa-fw fa-info', style=sidebar_icon_style),
                        html.A("Về chúng tôi", style=sidebar_text_nav_style)],
                               className='sidebar-about-me', href="/about-me", active="exact")
                    ]),

        html.Footer(className='sidebar-footer',
                    children=[
                        html.H1(id='live-time', 
                                style={'color': 'black', 'font-size': '13px', 'padding-left': '10px'}),
                        dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0),
                        # html.Img(src='/assets/images/bitexco.jpg',
                        #               style={'position': 'relative', 'padding-left': '1rem', 'padding-right': '1rem', 'margin-bottom': '1rem',
                        #                      'max-width': '100%', 'height': '300px', 'display': 'inline-block'}),
                              ]),
    ]
)