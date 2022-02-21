import dash
import dash_bootstrap_components as dbc

#Create the APP
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.CYBORG,
        {
            "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
            "rel": "stylesheet",
            "integrity": "sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==",
            "crossorigin": "anonymous",
            "referrerpolicy": "no-referrer",
        },
    ], 
    suppress_callback_exceptions=True,
    update_title=None,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1",
        }
    ],
)

#Name of app
app.title = 'Web Application of K18413'

#Server
server = app.server