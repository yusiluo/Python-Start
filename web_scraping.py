"""WEB SCRAPING"""
from bs4 import BeautifulSoup
import requests



# http://www.simplyhired.com/search?q=data+scientist&l=Seattle%2C+WA
# job ids inside jobs -> card js-job -> card-link js-job-link


# http://www.careerbuilder.com/jobs?keywords=data+scientist&location=Seattle%2C+WA
# job ids inside jobs -> job-row -> row

# http://www.indeed.com/jobs?q=data+scientist&l=Seattle%2C+WA
# job ids inside <td id="resultsCol"> -> <div ... class="row result"

# http://www.monster.com/jobs/search/?q=data-scientist&where=Seattle__2C-WA
# <div class="js_result_container clearfix" -> <div class="jobTitle"> -> href=""
