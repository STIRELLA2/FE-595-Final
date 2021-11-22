pip install sec-api

from sec_api import QueryApi

queryApi = QueryApi(api_key="d191139bb32063ab9166076e9b1aeba63695494ed678797194a79b5bd2b1d1d2")

query = {
  "query": { "query_string": { 
      "query": "ticker:TRV AND filedAt:{2020-01-01 TO 2020-12-31} AND formType:\"10-k\"" 
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)

from sec_api import ExtractorApi

extractorApi = ExtractorApi("d191139bb32063ab9166076e9b1aeba63695494ed678797194a79b5bd2b1d1d2")

# 10-K filing
filing_url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/86312/000008631220000011/trv-12312019x10k.htm"

# get the standardized and cleaned text of section 1A "Risk Factors"
section_text = extractorApi.get_section(filing_url, "1", "text")

print(section_text)
