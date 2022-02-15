# opengpt-workout-tracker
Leverages Nutritionix OpenAI GPT3 NLP model to classify exercise log text and write to Google Sheets

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
