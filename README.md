# Sentimentally: Our 2018 Patriot Hacks Hackathon Project
### Selected for the "Best Use of Open Source Intelligence" by the Verizon sponsor

![webp net-resizeimage 2](https://user-images.githubusercontent.com/12478151/46925824-1670ce80-cffc-11e8-9e6a-5d1f9961c810.png)

__________________________________________________________________________________
## Inspiration
The end goal was to learn something new. Something that we didn't all have experience with, even if it meant not completing a project in time.

## What it does
The user enters a keyword and clicks "submit." Then, the program displays the top 6 most relevant tweets containing that keyword and places each tweet in its own flash card that is displayed as a cover flow on the home page. On each card, there is also a score of the polarity and subjectivity of each tweet to determine the overall attitude towards the keyword that was entered. Below the cover flow, there's a horizontal bar graph that displays the average polarity of all 6 tweets. This graph and the tweets on the cards change for every new keyword entered.

## How we built it
Nabdeep did all of the front-end UI work. This included the cover flow animation and the bar graph. Nathaniel, Tarun, and I (Edward) worked together to get the Twitter Search API working so that the tweets can be fetched and stored for display. Lastly, I connected the fetched tweets from the API to the front end HTML display using Flask in conjunction with python. Overall, however, the team contributed equally to all parts of the project.

## Challenges we ran into
The first major challenge we ran into was getting the Twitter Search API to work properly. Multiple errors were given until we realized there existed a much simpler method to fetch these tweets while still using the API. Second, getting an overall understanding of how to integrate Flask to connect the API's results to the front-end's HTML files was challenging as this required an understanding of HTML, Python, and Flask syntax.

## Accomplishments that we're proud of
We are very proud to have gotten the Twitter Search API working in the first place. We were pretty lucky to have discovered a simpler version of what we were trying to do. We're also proud to have a great UI thanks to Nabdeep. Lastly, we are proud to have a working project that successfully does what we wanted it to do, all within 36 hours.

## What we learned
We learned how to easily fetch tweets through keywords using the API, how to implement new front-end designs with CSS and Javascript, and how to use Flask to connect our python files to the HTML files, passing information between the two, such as the text entered by the user and the fetched tweets.

## What's next for Sentimentally
While we were pretty satisfied with the UI, it can still be better, especially the text on the cards themselves, and the bar graph on the bottom of the page. Next, we would love to see what other areas we could apply this kind of capability of determining polarity and subjectivity among user input, and perhaps apply it to some kind of prediction software. A great application for this software that our team saw was for companies wanting to determine the effectiveness of their campaigns by gauging the attitudes of the public. Something new that we would do is rather than determining the average sentiment score from the top 6 tweets, why not do so for all tweets? We would then have the cards in the cover flow be dynamically created so that the user could scroll through all of them.

## Built With
Back-end: Python, Flask, Javascript, Twitter Seach API, textblob, tweepy



Front-end: HTML, CSS, Javascript, Chart.js, Swiper.js

## Important Notes
If you clone this repository, download the required packages, and run as a Python application, the default home page will be: http://127.0.0.1:5000/ This shows plain text and is NOT the project. Instead type "profile" at the end of that like so: http://127.0.0.1:5000/profile/ This will take you to our project. This is a small error that we will fix.

Also, when downloading tweepy, be aware that it is NOT compatible with Python 3.7. Inside the streaming.py file, change all variables named async to _async. 
