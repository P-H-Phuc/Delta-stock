from dash import html

footer_style = {
    #Layout
    "position": "fixed",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": "1.5rem",
    "background-color": "#111",
    #Text
    "padding-top": "3px",
    "padding-right": "20px",
    "text-align": "right",
    "color": "white",
    "font-size": "11px",
    'z-index': '1001'
}

footer = html.Div(
    [
        html.P(
            'Thực hiện bởi: Nhóm Sinh viên Khoa Toán Kinh Tế | UEL'
            )
    ], 
    className="page-footer", 
    style=footer_style
)