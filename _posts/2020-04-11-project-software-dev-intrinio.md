---
layout: post
title: Project - Intrinio API wrapper
tags: [Projects]
excerpt_separator: <!--more-->
---

__This is a group project from Collaborative Software Development in UBC's Master of Data Science program.__ <br/>
We developed two packages (Python + R) to retrieve data from [Intrinio](https://intrinio.com/) API objects in desired formats (DataFrame or dictionary). 
<!--more-->
## Authors
- Samantha Solomon, Roc Zhang, Sirine Chahma, Aakanksha Dimri

------------------------------------------------------------------------------------
## pyntrinio (Python version)

Python package converts Intrinio objects to native python and pandas objects.

### Project's GitHub repo 
* Project's GitHub repo can be found [here](https://github.com/UBC-MDS/pyntrinio).  

### The Project
This project has been created as part of [UBC's Master of Data Science Program](https://masterdatascience.ubc.ca/). Information about the contributors can be found [here](https://github.com/UBC-MDS/pyntrinio/blob/master/CONTRIBUTORS.md). The Code of Conduct can be found [here](https://github.com/UBC-MDS/pyntrinio/blob/master/CONDUCT.md). The collaboration expectations regarding use of Github Flow can be found [here](https://github.com/UBC-MDS/pyntrinio/blob/master/CONTRIBUTING.md).

If you were to search the web for "historical stock data", or "financial statement data", the results you would come across would be a variety of web applications (such as Google Finance), and maybe some PDFs of financial statements. This is fair, as there is a massive volume of stock data, and financial statements require lots of discretion (including standards followed - US companies may choose between reporting under IFRS and US GAAP). [Intrinio](https://intrinio.com/) offers solutions to this problem with an API platform that can easily be used to extract data and perform further analysis on it.

Intrinio is an excellent source to get data into a python environment to analyse data, but a problem persists that the data can not be directly analysed from Intrinio objects. That is where pyntrinio comes in. This package will offer a variety of functions that allow users to seamlessly transform Intrinio objects into either python dictionaries or a pandas dataframe. This will enable users to make the most of Intrinio's reliable and easy-to-use API platform, as well as the analysis capabilities that are available in python's environment.

### pyntrinio in the Python Ecosystem
Python is an object-oriented programming language, which has allowed contributors of packages to make complex data types appear simple, and overall make packages easy for users to use. This has led to the popularity of some objects, such as numpy and pandas objects. These have been widely accepted and are key structures in the python environment. Most objects however, are not integrated with packages the same way that numpy and pandas have been adopted. This means that generally users will need to change the data type of objects either native python object types (such as dictionaries or lists), or to a widely accepted object. The goal of this project is to make stock and financial statement data more accessible by translating the objects into dictionaries or pandas objects (user's choice) so that the end user can focus on analysis and drawing insights from the data.

### Dependencies

**Installing Intrinio Python SDK**

Follow these steps, as outlined in the [Intrino Python documentation](https://docs.intrinio.com/documentation/python)

**Note:** 

Intrinio Python SDK should be installed prior to installing pyintrinio.

To install the SDK use PIP:

``` 
pip install intrinio-sdk 
```

Python 3.7.3 and Python packages:

- pandas==1.0.1
- intrinio-sdk==5.1.0
- pytest==5.3.5
- python-dateutil==2.8.1

### Installation:

```
pip install -i https://test.pypi.org/simple/ pyntrinio
```  
Please make sure your `pandas` package is up to date to meet the dependency requirements. 

### Coverage

Ensure that you have poetry installed in your system. To install, please see the [poetry installation instructions](https://python-poetry.org/docs/#installation).

To get the line coverage, run the following command line code :

```
poetry add --dev pytest-cov
poetry run pytest --cov=pyntrinio
```


To get the branch coverage, run the following command line code:

```
poetry add --dev pytest-cov
poetry run pytest --cov-branch --cov=pyntrinio
```
### Usage

#### API KEYS
Before using any functions included in this package, you must sign up for an appropriate [Intrinio account](https://intrinio.com/). Once you have signed up for the appropriate account, you can find your API key (which is a required argument in all functions) by doing the following:

1. In the top right corner, select `My Account`
2. In the left hand menu, select `API KEYS`
3. Copy your relevant API Key. Note that this is unique to you and should not be shared.

**Important Note**

If you are using a free version of Intrinio for educational purposes, please note that you will only have access to the [Developer Sandbox](https://product.intrinio.com/developer-sandbox) so use that API key in functions.

#### Tickers
The following entities are covered in the sandbox data for the US Fundamentals and Stock Prices data feed:  
```
['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'DWDP', 'GE', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX', 'V', 'VZ', 'WMT', 'XOM']
```
[Developer Sandbox Coverage](https://product.intrinio.com/developer-sandbox/coverage/us-fundamentals-financials-metrics-ratios-stock-prices)  

**Note:** 

The package performance does not alter for users with paid access to intrinio dataset, i.e. the functions produce expected results with company ticker(s) not listed above. For ex. say google 'GOOG' with the correct API key.

### Functions
1. **gather_financial_statement_time_series()**: This function takes in a single stock ticker symbol, the statement, the year, and a list of various periods to compare, and a string specifying if we want the output as a dictionnary or a data frame. It returns a table or a data frame (depending on the input) of the information in the selected statement, fora time-series analysis of the company specified.
2. **gather_financial_statement_company_compare()**: This function takes in a list containing the tickers of the companies we want to compare, the statement, the year and the period of the year we want to study, and a string specifying if we want the output as a dictionnary or a data frame. It returns a table or a data frame (depending on the input) of the information in the selected statement, for the selected companies at the wanted time. 
3. **gather_stock_time_series()**: This function takes in a single stock ticker symbol and returns historical stock price data from a timeframe, returned as a dictionary or a pandas dataframe depending on specification.
4. **gather_stock_returns()**: This function takes in multiple stock ticker symbols, buy-in date, sell-out date and returns a dataframe containing the historical prices at buy-in and sell-out date as well as the corresponding returns (profit/loss).

#### Examples
Some simple examples of using the function:  
```python
# to get the income statements across time of the same company
>>> from pyntrinio.pyntrinio import gather_financial_statement_time_series
>>> gather_financial_statement_time_series(api_key, ticker='AAPL',
    statement='income_statement', year=['2018', '2019'], 
    period=['Q1'], output_format='pddf')  

# to get the income statements of different companies at the same point of time
>>> from pyntrinio.pyntrinio import gather_financial_statement_company_compare()
>>> gather_financial_statement_company_compare(api_key, ticker=['AAPL', 'CSCO'],
    statement='income_statement', year='2014', period='Q1', output_format='pddf')

# to get the historical stock prices of a company
>>> from pyntrinio.pyntrinio import gather_stock_time_series
>>> gather_stock_time_series(api_key, ticker='AAPL', start_date="2017-09-30", 
    end_date="2020-02-03", output_format='pddf')  

# to get the simulated returns of a stock / several stocks
>>> from pyntrinio.pyntrinio import gather_stock_returns
>>> gather_stock_returns(api_key, ticker=['AAPL', 'CSCO'], buy_date="2017-09-30", 
    sell_date="2020-02-03")
```  

### Documentation
The official documentation is hosted on Read the Docs: <https://pyntrinio.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

### References

McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).

Oliphant, T. E. (2006). A guide to NumPy (Vol. 1). Trelgol Publishing USA.

Swagger Codegen community. 2020. *IntrinioSDK: Python Package Client for
Intrinio Api*.

Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.
<br/>
<br/>

------------------------------------------------------------------------------------

## rintrinio (R version)

R (R Core Team 2019) package converts Intrinio (Swagger Codegen
community 2020) objects and lists to dataframes.

The vignette can be found [here](https://ubc-mds.github.io/rintrinio/).<br/>

### Project's GitHub repo 
* Project's GitHub repo can be found [here](https://github.com/UBC-MDS/rintrinio).  


### The Project

This project has been created as part of [UBC’s Master of Data Science
Program](https://masterdatascience.ubc.ca/). Information about the
contributors can be found [here](https://github.com/UBC-MDS/rintrinio/blob/master/CONTRIBUTORS.md). The Code of Conduct
can be found [here](https://github.com/UBC-MDS/rintrinio/blob/master/CONDUCT.md). The collaboration expectations
regarding use of Github Flow can be found [here](https://github.com/UBC-MDS/rintrinio/blob/master/CONTRIBUTING.md).

If you were to search the web for “historical stock data”, or “financial
statement data”, the results you would come across would be a variety of
web applications (such as Google Finance), and maybe some PDFs of
financial statements. This is fair, as there is a massive volume of
stock data, and financial statements require lots of discretion
(including standards followed - US companies may choose between
reporting under IFRS and US GAAP). [Intrinio](https://intrinio.com/)
offers solutions to this problem with an API platform that can easily be
used to extract data and perform further analysis on it.

Intrinio is an excellent source to get data into the R environment to
analyse data, but a problem persists that the data can’t be directly
analysed from Intrinio objects. That is where rintrinio comes in. This
package will offer a variety of functions that allow users to seamlessly
transform Intrinio objects into dataframes. This will enable users of
the data to make the most of Intrinio’s reliable and easy-to-use API
platform, as well as the analysis capabilities that are available in R’s
environment.

### rintrinio in the R Ecosystem

R is an object-oriented programming language, which has allowed
contributors of packages to make complex data types appear simple, and
overall make packages easy for users to use. R’s native dataframe object
is extremely popular and widely accepted in the R ecosystem. Intrinio’s
API platform for R actually has a function that is supposed to return
the results as a dataframe object, but it is actually a list that is
returned. This package will transform Intrinio objects into dataframes
that will make this data ready for the end user to use.

### Installation

You can install the current version of rintrinio from github with:

``` r
library(devtools)
devtools::install_github("UBC-MDS/rintrinio")
```

## Coverage

To get the line coverage, run the following from the R Console:

``` r
if(!require(covr)) { install.packages("covr") }
library("covr")
covr::report()
```

### Dependencies

#### Getting an API Key

Before using any functions included in this package, you must sign up
for an appropriate [Intrinio account](https://intrinio.com/). Once you
have signed up for the appropriate account, you can find your API key
(which is a required argument in all functions) by doing the following:

1.  In the top right corner, select `My Account`
2.  In the left hand menu, select `API KEYS`
3.  Copy your relevant API Key. Note that this is unique to you and
    should not be shared.

If you are using a free version of Intrinio for educational purposes,
please note that you will only have access to the [Developer
Sandbox](https://product.intrinio.com/developer-sandbox) so use that API
key in functions.

Note that the API key must be of type `character` when it is used in our
functions. Hence, don’t forget to use quotation marks when you use your
API key.

#### Installing Intrinio R SDK

Please note that the Intrinio R SDK is not available via CRAN. To
install, follow these steps, as outlined in the [Intrinio R
Documentation](https://docs.intrinio.com/documentation/r). Note that
Intrinio R SDK should be installed prior to installing rintrinio.

In an R console, install `devtools` if it is not already installed:

``` r
if(!require(devtools)) { install.packages("devtools") }
```

Install Intrinio SDK from Github:

``` r
library(devtools)
devtools::install_github("intrinio/r-sdk")
```

#### Program and Package Dependencies

R version 3.6.1 and R packages:

  - knitr==1.26 (Xie 2020)
  - tidyverse==1.2.1 (Wickham 2017)
  - IntrinioSDK==0.1.0 (Swagger Codegen community 2020)
  - testthat==2.3.1 (Wickham 2011)

### Functions

1.  **gather\_financial\_statement\_time\_series()**: This function
    takes in a single stock ticker symbol, the statement, the year, and
    a vector of various periods to compare. It returns a data frame of
    the information in the selected statement, for a time-series
    analysis of the company specified.
2.  **gather\_financial\_statement\_company\_compare()**: This function
    takes in a vector containing the tickers of the companies we want to
    compare, the statement we want to focus on, and the year and the
    period of the year we want to study. It returns a dataframe of the
    information in the selected statement, for the selected companies at
    the wanted time.
3.  **gather\_stock\_time\_series()**: This function takes in a single
    stock ticker symbol and returns historical stock price data from a
    timeframe, returned as a dataframe.
4.  **gather\_stock\_returns()**: This function takes in multiple stock
    ticker symbols, buy-in date, sell-out date and returns a dataframe
    containing the historical prices at buy-in and sell-out date as well
    as the corresponding returns (profit/loss).

### Usage

``` r
library(rintrinio)

# Gather Financial Statement Time Series Function
gather_financial_statement_time_series(api_key = api_key, 
                                       ticker = 'AAPL', 
                                       statement = 'balance_sheet_statement', 
                                       year = c("2018", "2019"),
                                       period = c('Q1'))


# Gather Financial Statement Cross-Company Comparison Function
gather_financial_statement_company_compare(api_key = api_key, 
                                           ticker = c("AAPL", "CSCO"), 
                                           statement = "income_statement", 
                                           year = "2018", 
                                           period = "Q1")


# Gather Stock Price Time Series Function
gather_stock_time_series(api_key = api_key,
                         ticker = "CSCO",
                         start_date = "2020-02-01",
                         end_date = "2020-02-05")


# Gather Stock Returns Function
gather_stock_returns(api_key = api_key,
                     ticker = c("AAPL", "CSCO"),
                     buy_date = "2019-01-01",
                     sell_date = "2020-01-01")

```

If you are using a Sandbox API key, the following tickers will work in
all of the functions: ‘AAPL’, ‘AXP’, ‘BA’, ‘CAT’, ‘CSCO’, ‘CVX’, ‘DIS’,
‘DWDP’, ‘GE’, ‘GS’, ‘HD’, ‘IBM’, ‘INTC’, ‘JNJ’, ‘JPM’, ‘KO’, ‘MCD’,
‘MMM’, ‘MRK’, ‘MSFT’, ‘NKE’, ‘PFE’, ‘PG’, ‘TRV’, ‘UNH’, ‘UTX’, ‘V’,
‘VZ’, ‘WMT’, ‘XOM’

Available statements include: ‘income\_statement’,
‘balance\_sheet\_statement’, ‘cash\_flow\_statement’

### References

<div id="refs" class="references hanging-indent">

<div id="ref-R">

R Core Team. 2019. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-intrinio">

Swagger Codegen community. 2020. *IntrinioSDK: R Package Client for
Intrinio Api*.

</div>

<div id="ref-testthat">

Wickham, Hadley. 2011. “Testthat: Get Started with Testing.” *The R
Journal* 3: 5–10.
<https://journal.r-project.org/archive/2011-1/RJournal_2011-1_Wickham.pdf>.

</div>

<div id="ref-tidyverse">

———. 2017. *Tidyverse: Easily Install and Load the ’Tidyverse’*.
<https://CRAN.R-project.org/package=tidyverse>.

</div>

<div id="ref-knitr">

Xie, Yihui. 2020. *Knitr: A General-Purpose Package for Dynamic Report
Generation in R*. <https://yihui.org/knitr/>.

</div>

</div>
