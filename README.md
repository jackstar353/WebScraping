# WebScraping
Web scraping Pyton program that scrapes Job website for python developer jobs and exports the data to a csv file.

Requests - downloads the data from the web server (HTTP protocol) and saves the response .

The response variable contains all the html data that can then be used to extract whatever information you need.

Beautiful Soup library is used to parse the html data.

Title, company name , location, salary and job summary are extracted to a python dictionary.

Pandas is used to load the data into a dataframe and export to csv.

