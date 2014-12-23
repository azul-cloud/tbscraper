Give a description of the applications that are included in the project and their functions.

=====MAIN=====
The main app handles all the overhead needed for the site. Things like the home page,
contact page, 


=====SCRAPE=====
This app takes care of scraping data and storing it locally. We gather data from various
sites and then store them in our own database. There is careful error handling and 
monitoring because scraping data can be sensitive (i.e. if they change structure). When
websites change we need to be alerted and update the scraping code.


=====BLOG=====
The blog app is where users are going to be viewing the articles. We'll be separating
articles to be grouped by Blog, Tag, and Country. We also provide a way for the users
to search all of our articles for some specific keywords they're looking for.