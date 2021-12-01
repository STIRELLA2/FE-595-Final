from flask import (Flask, render_template, flash,
                    request, jsonify, Markup)
import json
from nltk.tokenize import RegexpTokenizer
import re
import sec_api
import socketio
from sec_api import FullTextSearchApi
from sec_api import XbrlApi
from sec_api import ExtractorApi
from sec_api import RenderApi


app = Flask(__name__) # "__main__"


@app.route('/grp8', methods=['GET', 'POST'])
def flask_import():
  return """<html>
  <h1>FA595 Final Project<h1><br><br>
<h2>Group 8: Zemin Li, Sherri Putnam, Spencer Tirella</h2>
  <title>FA595 Grp 8 Final Project</title>
</head>
  <body>
 <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_1542b"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/NASDAQ-AAPL/" rel="noopener" target="_blank"><span class="black-text">595 Final Project</span></a> by Group 8</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 980,
  "height": 610,
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": true,
  "withdateranges": true,
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "calendar": true,
  "studies": [
    "BB@tv-basicstudies",
    "Volume@tv-basicstudies"
  ],
  "container_id": "tradingview_1542b"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->
</p>
  </body>
  </html>
  """



  

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
