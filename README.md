Some notes on how a real project would be improved in no particular order:

## 1. .env file shouldn't be committed into git.
Configuration files with secrets should never be committed, as they pose a security risk.
Instead, we should use an example.env and instruct the user to copy it and enter their credentials manually. 
This also allows each user to have their own credentials, which can be revoked if necessary.

## 2. Scaling
When visiting pages on a large scale, scaling needs to be considered.

## 3. Ensuring correct results:
Scrapy by default uses HTTP requests to visit the websites. 
While this works fine most of the time, it can lead to incorrect results 
when pages are written as Single Page Applications or rely on JavaScript to load more data later on.

## 4. Scaling the project
If the desire is to scrape on a larger scale, then there are several challenges that need to be addressed. 
1. Distributing the load. As the number of sites we need to process increases, it will be necessary to parallelize the scraping process. 
Scrapy uses multiple threads, but only one core by deafault. Using different approaches such as python's multiprocessing, docker's --scale, or kubernetes for very large scales, we can scale the extraction process arbitrarily. 
2. Separating the scraping and visiting. If the data processing is heavy, we can lighten the load on Scrapy by separating the visit component from the processing. 
If we set up an API where we can send the resulting pages to be processed, we can heavily increase the concurrency of the Scrapy requests. 
Scaling of the API then becomes very easy, for beginner needs, we can just use a `docker-compose up --scale=n` command and go from there. 
This also helps by allowing us to have specialized systems for certain workloads, such as machine learning, where we need a GPU and we preferably want to use it as efficiently as possible.
3. Storing a large frontier. The frontier is a list of URLs that are in queue to be visited and can often exceed the size of system RAM if the scraping system reaches a high enough URL count. 
This is often solved by storing the frontier on a disk, or sharing it between multiple systems.
