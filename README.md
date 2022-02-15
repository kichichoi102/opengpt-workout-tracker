# opengpt-workout-tracker
Leverages Nutritionix OpenAI GPT3 NLP model to classify exercise log text and write to Google Sheets.

If a user inputs an exercise they did, eg. `ran a 10km marathon`, then this would be categorized into `Running`, and Nutritionix will approximate your `Calories spent` and `exercise duration` based on your given personal info!

## Try!
[Replit Terminal](https://replit.com/@kichichoi102/opengpt-workout-tracker?v=1)

[Example Sheets](https://docs.google.com/spreadsheets/d/1NbsVkdDllT1oTpDTaZrhtmP0zYPVN6bfJrx5W6LxpiI/edit?usp=sharing)

## Setup Nutritionix API Credentials
1. Clone repository
2. Make a Google Sheet like this: [Example Sheet](https://docs.google.com/spreadsheets/d/1NbsVkdDllT1oTpDTaZrhtmP0zYPVN6bfJrx5W6LxpiI/edit?usp=sharing)
3. Go to [Nutritionix API site](https://www.nutritionix.com/business/api), get api key and write to `APPID` and `APPKEY` in `.env` file.

## Setup Sheety
1. Connect Google Sheet to [Sheety](https://sheety.co/)
2. Get share link from Google Sheet and paste to Sheety new project
3. Allow `GET` and `POST`
4. Copy `POST URL` and add to `SHEET_ENDPOINT` in `.env`
5. Create a new Token (Authentication -> Bearer).
6. Paste `{Authorization: Bearer <your token>}` into `.env`

## Use
1. Go to directory
2. Fill out rest of personal details in `.env` (WEIGHT, HEIGHT, AGE, GENDER)
3. run `python main.py`
 
## Example
![screen-capture (3)](https://user-images.githubusercontent.com/70384232/154111525-e61de165-5175-4fee-8de2-3b49e4e6b196.gif)
