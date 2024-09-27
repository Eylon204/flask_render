import http.client

conn = http.client.HTTPSConnection("linkedin-data-scraper.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ae3b0c227cmsh62c171ce95d37d9p1d5a2fjsn6c7e05fc24f0",
    'x-rapidapi-host': "linkedin-data-scraper.p.rapidapi.com"
}

conn.request("GET", "/company_insights?link=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fgoogle", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))