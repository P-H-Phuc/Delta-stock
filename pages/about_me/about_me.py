import imp
from dash import html, dcc

about_me_layout = html.Div(
    [
        html.Div([
            html.P(html.Img(src='/assets/images/logo.png', style={'width': '100px', 'margin-top': '20px'})),
            html.P('CHỨNG KHOÁN: DỰ ÁN XÂY DỰNG DASHBOARD SỬ DỤNG DASH PYTHON', style={'color': 'orange', 'font-weight': 'bold'}),
            html.P('Thực hiện bởi Nhóm sinh viên Khoa Toán Kinh tế | Trường đại học Kinh tế - Luật'),
            html.P([
                html.A(html.Img(src='https://badges.frapsoft.com/os/v2/open-source.svg?v=103'), href='https://github.com/P-H-Phuc', style={'margin-right': '10px'}),
                html.A(html.Img(src='https://img.shields.io/badge/Code-Python_language-informational?style=flat&logo=python&logoColor=ffdd54&labelColor=9c9c9c&color=528B8B'), style={'margin-right': '10px'}),
                html.A(html.Img(src='https://img.shields.io/badge/Editor-Visual_Studio_Code-informational?style=flat&logo=visual-studio-code&logoColor=blue&labelColor=9c9c9c&color=528B8B'), style={'margin-right': '10px'}),
            ])
        ], style={'text-align': 'center'}),

        html.H3('Nội dung'),
        html.H4('1. Giới thiệu'),
        html.P('Dự án này là một trang thông tin các mã giao dịch chứng khoán trên thị trường chứng khoán Việt Nam. Người dùng chọn một ký hiệu chứng khoán và các giá trị ngày, tháng, năm để trực quan hóa dữ liệu. Thêm vào đó tính toán các mô hình hồi quy đơn giản như Trung bình trượt, Hồi quy cục bộ, Hàm mũ, Fama French. Đây là kết quả nghiên cứu của nhóm để hoàn thành dự án kết thúc môn học không nhằm mục đích sử dụng cho bất kì mục đích thương mại nào.'),
        html.H4('2. Giới thiệu khung làm việc của Dash | Plotly'),
        html.P('Dash là một khuôn khổ Python hiệu quả để xây dựng các ứng dụng web. Được viết trên Flask, Plotly.js và React.js, Dash lý tưởng để xây dựng các ứng dụng trực quan hóa dữ liệu với giao diện người dùng tùy chỉnh cao bằng Python thuần túy. Nó đặc biệt phù hợp cho bất kỳ ai làm việc với dữ liệu bằng Python. Thông qua một vài mẫu đơn giản, Dash loại bỏ tất cả các công nghệ và giao thức cần thiết để xây dựng một ứng dụng dựa trên web tương tác. Dash đủ đơn giản để bạn có thể liên kết giao diện người dùng xung quanh mã Python của mình trong một buổi chiều. Ứng dụng Dash được hiển thị trong trình duyệt web. Bạn có thể triển khai ứng dụng của mình tới các máy chủ và sau đó chia sẻ chúng thông qua các URL. Vì các ứng dụng Dash được xem trong trình duyệt web, nên Dash vốn đã sẵn sàng cho nhiều nền tảng và thiết bị di động.'),
        html.H4('3. Demo'),
        html.Img(src='/assets/images/demo/information_tab1.PNG', style={'width': '400px', 'margin-left': '10px', 'margin-bottom': '10px'}),
        html.Img(src='/assets/images/demo/information_tab2.PNG', style={'width': '400px', 'margin-left': '10px', 'margin-bottom': '10px'}),
        html.Img(src='/assets/images/demo/information_tab3.PNG', style={'width': '400px', 'margin-left': '10px', 'margin-bottom': '10px'}),
        html.Img(src='/assets/images/demo/price-performance.PNG', style={'width': '400px', 'margin-left': '10px', 'margin-bottom': '10px'}),
        html.Img(src='/assets/images/demo/price-performance1.PNG', style={'width': '400px', 'margin-left': '10px', 'margin-bottom': '10px'}),
        html.Img(src='/assets/images/demo/price-performance2.PNG', style={'width': '400px', 'margin-left': '10px', 'margin-bottom': '10px'}),
        html.Img(src='/assets/images/demo/price-performance3.PNG', style={'width': '400px', 'margin-left': '10px', 'margin-bottom': '10px'}),
    ]
)