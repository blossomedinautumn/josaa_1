# JOSAA-Data-Analysis
This project empowers aspiring engineers navigating the Joint Seat Allocation Authority (JoSAA) by providing historical data insights and interactive visualizations.
It aims to efficiently extract relevant data from the JoSAA website, meticulously removing inconsistencies and transforming it into a clean, structured format for analysis.
It also unveils trends and patterns within the data, focusing on institute cutoffs and seat allotment across different programs and years.
The project presents visualizations crafted using a user-friendly frontend framework to enable users to explore historical cutoff and seat allotment trends.
THe project facilitates informed decision-making by allowing users to:
Compare cutoffs between different institutes and programs over time.
Identify trends in seat allotment patterns.


## Tech Stack/Frameworks:
- Frontend: HTML, CSS, JavaScript
* Backend: Django
+ Database: SQLite
- Data Scraping: Selenium, Beautiful Soup
* Data Cleaning: NumPy, Pandas
+ Data Visualization: Chart.js

## Command to run the project locally
- python manage.py runserver
- Then run the server locally on port 8000

## Home page
The home page provides a user-friendly interface for students to make informed decisions about their college applications
It provides features to:
- View year-wise cutoffs
- Analyze gender-wise cut-off trends
- Explore round-wise cut-off analysis

- ![Home page](https://github.com/blossomedinautumn/josaa_1/tree/main/static/images/home-1.png)

## View all Institutes
- Upon clicking this option(General Information of engineering colleges in india), a list of all IITs,NITs,IIITs,and other colleges that take part in JOSAA counselling is shown along with their NIRF Rankings(2023), Location their established year and their official website.
- ![Institute wise cutoff list](https://github.com/blossomedinautumn/josaa_1/tree/main/static/images/institute-wise.png)
 
## View Opening and Closing Ranks of 2023
- Upon clicking Opening and Closing Ranks 2023 users experience a JOSAA-like user interface which allows them to see opening and closing ranks of all institutes,for all branches,seat type, rounds .
- ![Opening Closing ranks](https://github.com/blossomedinautumn/josaa_1/tree/main/static/images/or-cr-1.png)

## Analyze year wise cut-off trends
- Yearwise cutoff trends highlight the trends of various programs offered by a particular institute over the years. This helps understand the popularity and perception of programs offered by the institute, and helps us predict the expected cutoff for a given year.
- ![Year wise trends](https://github.com/blossomedinautumn/josaa_1/tree/main/static/images/year-wise-1.png)
  
- Upon selecting the institute, branch and seat category, user will get the detailed year-wise cut-off analysis based on the parameters.

## Roundwise cut-off Analysis
- Round trends highlight the general trend of closing ranks throughout the rounds of the counselling process. This helps understand the likely range of changes to the closing ranks throught the counselling proces.
- Users can get the round wise analysis of any institute by selecting the institute,seat type and branch. 
- Users will get line graphs depicting the roundwise trends for each year at that institute.
- ![roundwise trends](https://github.com/blossomedinautumn/josaa_1/tree/main/static/images/round-wise-1.png)







