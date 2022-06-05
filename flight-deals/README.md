# Flight Deals

This tool uses the google sheet api, kiwi tequila flight search api, and signal messaging app to send a message to a user if there any available roundtrip flights for a given list of cities in the next 90 days under a price threshold. 

To do this, the tool:

1. Takes a google sheet with a list of cities and prices

<img width="538" alt="Screen Shot 2022-06-05 at 12 18 37 PM" src="https://user-images.githubusercontent.com/73619806/172060159-cf239eae-bbfa-47b4-9f19-faac90f48eaf.png">

2. Adds Iata codes (city codes) if needed

3. Saves the sheet to a pandas dataframe

4. Searches the kiwi tequila flight search api using those Iata codes flights

5. Compares those flights to the "price" column in the dataframe

6. Sends a message with flight details for any flights that meet the criteria through the signal messaging app

<img width="538" alt="Screenshot_20220605-125004" src="https://user-images.githubusercontent.com/73619806/172061423-e16ec9f8-62b2-47dd-9438-a96ba9962868.jpeg">


The project instructions from the course originally was to use the [sheety api](https://sheety.co/docs), and [twilio api](https://www.twilio.com/sms); they're both begineer friendly but they have a significant cost to use their service after a limited trial. 
It was more difficult, but I elected to use the google sheets api and signal messaging app because of cost savings and I'll be able to use the classes for those apis in other projects. 
Therefore for me, this project was mostly about how to use these two apis together, and another opporunity to use pandas. 

## Setup
This guide explains how to set up the google sheet api:
https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/

Here's resources for setting up the signal message app api.
https://github.com/bbernhard/signal-cli-rest-api
https://bbernhard.github.io/signal-cli-rest-api/

Here's how to set up the tequila flight messaging api:
https://tequila.kiwi.com/portal/docs/user_guides/tequila_getting_started
