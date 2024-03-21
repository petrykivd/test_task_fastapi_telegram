# FastAPI Telegram Sender

This web service is built using FastAPI to receive POST requests with JSON data and send messages to Telegram.

## How to Run

1. **Install Dependencies:**

    Install the required libraries using `pip`:

    ```
    pip install -r requirements.txt
    ```

2. **Get your Telegram Bot Token:**

    - Contact [@BotFather](https://t.me/BotFather) on Telegram and create a new bot.
    - Take note of the token you receive; you'll need it later.

3. **Run the Web Server:**

    Start the web server using `uvicorn`:

    ```
    uvicorn main:app --reload
    ```

    The web server will be available at `http://127.0.0.1:8000`.

4. **Send a POST Request:**

    Send a POST request to `http://127.0.0.1:8000/send_message`, providing JSON data with your bot token, chat ID, and message text:

    ```json
    {
      "bottoken": "YOUR_BOT_TOKEN",
      "chatid": "YOUR_CHAT_ID",
      "message": "YOUR_MESSAGE_TEXT"
    }
    ```

    Replace `YOUR_BOT_TOKEN` with your bot's token and `YOUR_CHAT_ID` with the chat ID where you want to send the message.
![image](https://github.com/petrykivd/test_task_fastapi_telegram/assets/111526221/f6edcd38-1c77-4f63-9b56-6b23799ce376)
   

6. **Check the Result:**

    Verify if the message is successfully sent to the specified chat in Telegram.

## Important Notes!

- Make sure your Telegram bot has permission to send messages to the specified chat.
