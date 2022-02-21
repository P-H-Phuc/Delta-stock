from dash import html, dcc, Output, Input

#Create the APP--------------------
from app import app, server

# Describe the layout/ UI of the app---------------------

from layouts import sidebar, footer
from pages.page_market_overview import market_overview 
from pages.page_price_performance import price_performance
from pages.page_company_profile import company_profile
from pages.page_management_portfolio import management_portfolio
from pages.about_me import about_me

index_layout = html.Div(
    [
        dcc.Location(id="url"),
        sidebar.sidebar,
        footer.footer,
        html.Div(
            id='page-content', 
            className='page-content', 
            style={"margin-left": "14.2rem", "height": "100%"}
            )
    ], style={'background-color': '#444'}
)           
app.layout = index_layout
app.validation_layout = html.Div(
    [
        index_layout,
        market_overview.layout_market_overview,
        company_profile.layout_company_profile,
        price_performance.layout_price_performance,
        management_portfolio.layout_management_portfolio,
        about_me.about_me_layout
    ]
)

#CALLBACK-------------------------
from pages.page_company_profile import callbacks_company_profile
from pages.page_price_performance import callback_price_performance

#Live time
@app.callback(
    Output('live-time', 'children'),
    Input('interval-component', 'n_intervals')
)
def live_time(n):
    from datetime import timedelta, timezone, datetime
    tz_hanoi = timezone(timedelta(hours=7))
    dt2 = datetime.now(tz_hanoi)
    return str(dt2.strftime('%A, %d %b %Y %H:%M:%S'))

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):

    if pathname == "/market-overview":
        return market_overview.layout_market_overview

    elif pathname == "/company-profile":
        return company_profile.layout_company_profile

    elif pathname == "/price-performance":
        return price_performance.layout_price_performance

    elif pathname == "/management-portfolio":
        return management_portfolio.layout_management_portfolio

    elif pathname == "/about-me":
        return about_me.about_me_layout

    else:
        return price_performance.layout_price_performance

#-------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9999)