# How to View Data
Since the example site is blocking scraping requests, the easiest way to view the data is to install the project for development and run tests (`flats_project/spider/tests/test_flats.py`).
This will fill the example data into the database, allowing you to view the data.

# Some notes on how a real project would be improved in no particular order:

## 1. Environment Management
### 1.1 `.env` file shouldn't be committed into Git
Configuration files with secrets should never be committed, as they pose a security risk.
Instead, we should use an `example.env` and instruct the user to copy it and enter their credentials manually. 
This also allows each user to have their own credentials, which can be revoked if necessary.

In this case, I committed it, as per "homework" instructions. 

### 1.2 Separate configurations for development, production, etc.
We should use different `.env` files for development, production, etc.

## 2. Scaling
When visiting pages on a large scale, scaling needs to be considered.

## 3. Ensuring Correct Results
Scrapy, by default, uses HTTP requests to visit websites. 
While this works fine most of the time, it can lead to incorrect results 
when pages are written as Single Page Applications or rely on JavaScript to load more data later on. 
Scrapy provides middleware with which we can use a headless browser instead of using raw HTTP requests. 

## 4. Scaling the Project
If the desire is to scrape on a larger scale, then there are several challenges that need to be addressed:
1. Distributing the load. As the number of sites we need to process increases, it will be necessary to parallelize the scraping process. 
Scrapy uses multiple threads, but only one core by default. Using different approaches such as Python's multiprocessing, Docker's `--scale`, or Kubernetes for very large scales, we can scale the extraction process arbitrarily. 
2. Separating the scraping and visiting. If the data processing is heavy, we can lighten the load on Scrapy by separating the visit component from the processing. 
If we set up an API where we can send the resulting pages to be processed, we can significantly increase the concurrency of the Scrapy requests. 
Scaling of the API then becomes very easy; for beginner needs, we can just use a `docker-compose up --scale=n` command and go from there. 
This also helps by allowing us to have specialized systems for certain workloads, such as machine learning, where we need a GPU and we preferably want to use it as efficiently as possible.
3. Storing a large frontier. The frontier is a list of URLs that are in the queue to be visited and can often exceed the size of system RAM if the scraping system reaches a high enough URL count. 
This is often solved by storing the frontier on a disk, or sharing it between multiple systems.

## 5. Project Structure
Some services have shared code, such as the Flat object. I decided it's best to share the configuration and other common logic in this case, but this does mean that the projects aren't as separate as they could otherwise be. 
In this case, one of two things would make sense:
- Have the projects in the same folder with the common logic in the `pyproject` folder. 
- Keep the projects in separate folders and expose the common logic to those services.

Both approaches have merits. The first case seems simpler for smaller projects, but can have negative downsides, 
such as a larger Docker image due to more dependencies and can get quite messy when they scale. 
When choosing this approach, it's critical to find the right time to change to a different paradigm before it's too late.  
The benefits are quite major, however, as it is a lot more forgiving when implementing changes to the data model, etc., as there is no need to sync any library version, pull requests, or deploys.

The second way is more appropriate for larger projects, where the separation of concerns becomes a higher priority. 
It allows teams to only focus on the modules they're working with. 
In such a case, everything else they're only using is only exposed through a public interface. 
This scales better when teams get larger and there are many services.

## 6. Database Shouldn't Be Exposed Outside of Docker Network
I left the port exposed to the outside for development purposes. 
This is a bad security practice; all services should be as closed off as possible, to reduce exposure to malicious actors.

# Development
1. Create a venv (PyCharm CTRL+SHIFT+A -> select Python interpreter -> follow the setup for a new venv).
2. Open a new terminal and install `requirements.txt`:
`pip install -r flats_project/requirements.txt`
3. To connect to the database, you will need to `docker-compose up` and make sure it's exposed (uncomment the ports section in the Postgres service in `docker-compose`).

Congratulations, you are ready to run the project!

### Running Tests:
When creating the run config for your tests, make sure to set the environment to DEVELOPMENT, to load the environment variables from the `.env` file directly.
In production, they will be provided by `docker-compose`.
