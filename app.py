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
   
  return f"""<html>

  <h1>FA595 Final Project<h1><br><br>
<h2>Group 8: Zemin Li, Sherri Putnam, Spencer Tirella</h2>
<h3> The below application is designed to accept a stock ticker, pull the company's 2020 10K filing from the SEC Edgar database, and return the sentiment analysis score for the company's comments in section 1A "Risk Factors" of the filing.</h3>
  <title>FA595 Grp 8 Final Project
  </title>
</head>
    <form action="/text" method="post">
    Enter Your Ticker:<br>
    <input type="text" name="text_input" value="">
    <br>
    <input type="submit" value="Submit">
  </form>
  
  <tr>{score}</tr>  
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

@app.before_request
def before():
    print('FE 595 Group 8: Zemin Li, Sherri Putnam, Spencer Tirella')

@app.route('/ticker', methods=['GET', 'POST'])
def sec():
  tickerfromuser={'string':request.json['string']}
  tickerfromuser2=json.dumps(tickerfromuser)
  
  ## Grab the URL to the 2020 10K for a given ticker
  from sec_api import QueryApi
  queryApi = QueryApi(api_key="bddda2de3ae47b101a2c2a2a94c09591ab98481b5a2fe1a7fda21ab0c14809f6")

  query = {
   "query": { "query_string": { 
        "query": "ticker:tickerfromuser2 AND filedAt:{2020-01-01 TO 2020-12-31} AND formType:\"10-k\"" 
     } },
    "from": "0",
    "size": "10",
    "sort": [{ "filedAt": { "order": "desc" } }]
    }
  
  filings = queryApi.get_filings(query)

## Take the URL to the 10K and extract section 1 Management Commentary
  from sec_api import ExtractorApi

  extractorApi = ExtractorApi("bddda2de3ae47b101a2c2a2a94c09591ab98481b5a2fe1a7fda21ab0c14809f6")

# 10-K filing
  filing_url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/86312/000008631220000011/tickerfromuser2-12312019x10k.htm"

# get the standardized and cleaned text of section 1A "Risk Factors"
  section_text = extractorApi.get_section(filing_url, "1A", "text")

  import nltk
  nltk.download('vader_lexicon')
  from nltk.sentiment.vader import SentimentIntensityAnalyzer
  sid=SentimentIntensityAnalyzer()
  sentence=section_text
  score=sid.polarity_scores(sentence)
  
  return jsonify({'score':score},{'section':section_text})


#Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3333)
