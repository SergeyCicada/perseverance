## Perseverance
___
Our Python web application is an interface that allows users to retrieve interesting facts about space and view photos taken by the Mars rover. We utilize the NASA public API to access current data and images.

Users can interact with our application in the following ways:

1. Space Facts: Users can request interesting facts about space. We make API calls to NASA to retrieve random facts related to astronomy, planets, stars, and other celestial objects. The obtained facts are displayed on the web page.

2. Mars Rover Photos: Users can access our application to view the latest photos captured by NASA's Mars rover. We utilize the NASA API to access the latest photos and display them on the web page


### Installation
1. You must get the api key from https://api.nasa.gov/ and paste it into config.py in the API_KEY field
2. To use the message sender for communication, insert your email and password into the SENDER and PASSWORD fields in config.py. This is not necessary for the main program to work.
3. sudo docker build -t perseverance_app .
4. sudo docker run --name perseverance -p 5000:5000 -d perseverance_app
5. Open a web browser and visit http://localhost:5000 to view app.

REQUIREMENTS -> requrements.txt

Attention! The application collects logs in logs.log
___

### Usage
Rover tab - additionally, on the space tab, you can look
at pictures from space and facts about them.

Space tab - on the space tab you can get photos related to space
and interesting facts about them
                        

Contacts tab - on the contacts tab you can contact the creator of this project!

___
### Author: Sergey Evgrafov

This project was created and maintained by Sergey Evgrafov