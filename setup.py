# coding: utf-8

"""
    Thirdwatch API

    The first version of the Thirdwatch API is an exciting step forward towards making it easier for developers to pass data to Thirdwatch.   # Introduction Once you've [registered your website/app](https://thirdwatch.ai) it's easy to start sending data to Thirdwatch.  All endpoints are only accessible via https and are located at `api.thirdwatch.ai`. For instance: you can send event at the moment by ```HTTP POST``` Request to the following URL with your API key in ```Header``` and ```JSON``` data in request body. ```   https://api.thirdwatch.ai/event/v1 ``` Every API request must contain ```API Key``` in header value ```X-THIRDWATCH-API-KEY```  Every event must contain your ```_userId``` (if this is not available, you can alternatively provide a ```_sessionId``` value also in ```_userId```).  # Score API The Score API is use to get an up to date cutomer trust score after you have sent transaction event and order successful. This API will provide the riskiness score of the order with reasons. Some examples of when you may want to check the score are before:    - Before Shippement of a package   - Finalizing a money transfer   - Giving access to a prearranged vacation rental   - Sending voucher on mail    ```   https://api.thirdwatch.ai/neo/v1/score?api_key=<your api key>&order_id=<Order id> ```  According to Score you can decide to take action Approve or Reject. Orders with score more than 70 will consider as Riskey orders. We'll provide some reasons also in rules section.  ## Response score API  ``` {   \"order_id\": \"OCT45671\",   \"user_id\": \"ajay_245\",   \"order_timestamp\": \"2017-05-09T09:40:45.717Z\",   \"score\": 82,   \"flag\": \"red\",     -\"reasons\": [     {         \"name\": \"_numOfFailedTransactions\",         \"display_name\": \"Number of failed transactions\",         \"flag\": \"green\",         \"value\": \"0\",         \"is_display\": true       },       {         \"name\": \"_accountAge\",         \"display_name\": \"Account age\",         \"flag\": \"red\",         \"value\": \"0\",         \"is_display\": true       },        {         \"name\": \"_numOfOrderSameIp\",         \"display_name\": \"Number of orders from same IP\",         \"flag\": \"red\",         \"value\": \"11\",         \"is_display\": true       }     ] } ``` 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "thirdwatch_api"
VERSION = "0.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Thirdwatch API",
    author_email="shashank@thirdwatch.ai",
    url="https://github.com/thirdwatch/thirdwatch-python",
    keywords=["Swagger", "Thirdwatch API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The first version of the Thirdwatch API is an exciting step forward towards making it easier for developers to pass data to Thirdwatch.   # Introduction Once you&#39;ve [registered your website/app](https://thirdwatch.ai) it&#39;s easy to start sending data to Thirdwatch.  All endpoints are only accessible via https and are located at &#x60;api.thirdwatch.ai&#x60;. For instance: you can send event at the moment by &#x60;&#x60;&#x60;HTTP POST&#x60;&#x60;&#x60; Request to the following URL with your API key in &#x60;&#x60;&#x60;Header&#x60;&#x60;&#x60; and &#x60;&#x60;&#x60;JSON&#x60;&#x60;&#x60; data in request body. &#x60;&#x60;&#x60;   https://api.thirdwatch.ai/event/v1 &#x60;&#x60;&#x60; Every API request must contain &#x60;&#x60;&#x60;API Key&#x60;&#x60;&#x60; in header value &#x60;&#x60;&#x60;X-THIRDWATCH-API-KEY&#x60;&#x60;&#x60;  Every event must contain your &#x60;&#x60;&#x60;_userId&#x60;&#x60;&#x60; (if this is not available, you can alternatively provide a &#x60;&#x60;&#x60;_sessionId&#x60;&#x60;&#x60; value also in &#x60;&#x60;&#x60;_userId&#x60;&#x60;&#x60;).  # Score API The Score API is use to get an up to date cutomer trust score after you have sent transaction event and order successful. This API will provide the riskiness score of the order with reasons. Some examples of when you may want to check the score are before:    - Before Shippement of a package   - Finalizing a money transfer   - Giving access to a prearranged vacation rental   - Sending voucher on mail    &#x60;&#x60;&#x60;   https://api.thirdwatch.ai/neo/v1/score?api_key&#x3D;&lt;your api key&gt;&amp;order_id&#x3D;&lt;Order id&gt; &#x60;&#x60;&#x60;  According to Score you can decide to take action Approve or Reject. Orders with score more than 70 will consider as Riskey orders. We&#39;ll provide some reasons also in rules section.  ## Response score API  &#x60;&#x60;&#x60; {   \&quot;order_id\&quot;: \&quot;OCT45671\&quot;,   \&quot;user_id\&quot;: \&quot;ajay_245\&quot;,   \&quot;order_timestamp\&quot;: \&quot;2017-05-09T09:40:45.717Z\&quot;,   \&quot;score\&quot;: 82,   \&quot;flag\&quot;: \&quot;red\&quot;,     -\&quot;reasons\&quot;: [     {         \&quot;name\&quot;: \&quot;_numOfFailedTransactions\&quot;,         \&quot;display_name\&quot;: \&quot;Number of failed transactions\&quot;,         \&quot;flag\&quot;: \&quot;green\&quot;,         \&quot;value\&quot;: \&quot;0\&quot;,         \&quot;is_display\&quot;: true       },       {         \&quot;name\&quot;: \&quot;_accountAge\&quot;,         \&quot;display_name\&quot;: \&quot;Account age\&quot;,         \&quot;flag\&quot;: \&quot;red\&quot;,         \&quot;value\&quot;: \&quot;0\&quot;,         \&quot;is_display\&quot;: true       },        {         \&quot;name\&quot;: \&quot;_numOfOrderSameIp\&quot;,         \&quot;display_name\&quot;: \&quot;Number of orders from same IP\&quot;,         \&quot;flag\&quot;: \&quot;red\&quot;,         \&quot;value\&quot;: \&quot;11\&quot;,         \&quot;is_display\&quot;: true       }     ] } &#x60;&#x60;&#x60; 
    """
)
