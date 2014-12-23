Give a description of the applications that are included in the project and their functions.

=====MAIN=====
The main app handles all the overhead needed for the site. Things like the home page,
contact page, 


=====SCRAPE=====
This app takes care of scraping data and storing it locally. We gather data from various
sites and then store them in our own database. There is careful error handling and 
monitoring because scraping data can be sensitive (i.e. if they change structure). When
websites change we need to be alerted and update the scraping code.

PULLING DATA
Each blog site will have its own scheduled pull time, which will be determined by how
often we are able to fetch updated data. For sites that update data regularly, we'll
get the data from them weekly. If they aren't updating data, the pull will automatically
switch to once a month, and then once every 3 months.

There are a few things we have to do for each website, and we want to make sure these
are consistent.

1. Get the page that has all the paging options
2. Get a list of all the pages that have the posts we're going to scrape
3. Get a list of all the URLs to the single posts
4. Scrape the data

STORING DATA


=====BLOG=====
The blog app is where users are going to be viewing the articles. We'll be separating
articles to be grouped by Blog, Tag, and Country. We also provide a way for the users
to search all of our articles for some specific keywords they're looking for.