<div align='center'>
  <img src='/assets/images/logo.png' width='100'></img>
  
## DELTA STOCK: BUILDING DASHBOARD STOCK MARKET USING DASH PYTHON

[VISIT DELTA STOCK WEB APPLICATION](https://delta-stock.herokuapp.com/)

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/P-H-Phuc/Delta-stock)
[![](https://img.shields.io/badge/Editor-Visual_Studio_Code-informational?style=flat&logo=visual-studio-code&logoColor=blue&labelColor=9c9c9c&color=528B8B)](https://code.visualstudio.com/)
[![](https://img.shields.io/badge/Code-Python_language-informational?style=flat&logo=python&logoColor=ffdd54&labelColor=9c9c9c&color=528B8B)](https://www.python.org/)
  </div>
  
### Table of contents
1. [Introduction](#introduction)
2. [Folder Structure](#folder-structure)
3. [Getting Started](#started)
  
  <br></br>
  
# Introduction <a name="introduction"></a>
  
This project is a Interactive Stock Dashboard with Plotly Dash. This is a educational project not intented to use for any commercial purposes.

***What is Dash?***

Dash is a productive Python framework for building web applications. Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python. Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build an interactive web-based application. Dash is simple enough that you can bind a user interface around your Python code in an afternoon. Dash apps are rendered in the web browser. You can deploy your apps to servers and then share them through URLs. Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready. You can learn more [here](https://dash.plotly.com/).

# Folder Structure <a name='folder-structure'></a>

The structure of the Dash application is presented below:
  
```
- __init__.py
- index.py
- app.py
- Profile
- requirements.txt
- assets
    |-- custom.css
    |-- company_profile.css
    |-- price_performance.css
    - images
        |-- logo.png
        |-- demo
- data_source
    |-- __init__.py
    |-- helpers.py
    |-- data_load_api
               |-- __init__.py
               |-- info_stock_loader.py
               |-- historical_price_loader.py
    |-- data_storage
               |-- __init__.py
               |-- infomation_of_stock.csv
               |-- historical_price.csv
               |-- marketcap.csv
               |-- manage.py
 - layouts
    |-- __init__.py
    |-- footer.py
    |-- sidebar.py
 - pages
    |-- __init__.py
    |-- page_market_overview
               |-- __init__.py
               |-- market_overview.py
               |-- callbacks_market_overview.py
    |-- page_company_profile
               |-- __init__.py
               |-- company_profile.py
               |-- callbacks_company_profile.py
    |-- page_price_performance
               |-- __init__.py
               |-- price_performance.py
               |-- callbacks_price_performance.py
    |-- page_management_portfolio
               |-- __init__.py
               |-- company_profile.py
               |-- callbacks_management_portfolio.py
    |-- about_me
               |-- __init__.py
               |-- about_me.py
 
```

# Getting Started <a name='started'></a>

To run this project on your system:
 
 - Ensure that python3 and python3-pip are installed on your system.
 - In your terminal, navigate to the root project directory and run the following commands.
 - Install the dependencies:
  
```python
pip install -r requirements.txt
```

- To start the web server, execute (without debugging):
```python
python index.py 
```
