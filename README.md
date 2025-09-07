# Discord Channel & Category Deleter Bot

A simple Discord bot (using [discord.py](https://github.com/tknainoo/bot.py)) that deletes **all channels and categories** in your server.  
Useful for server resets or cleanup when you want to start fresh. ⚠️


## ⚠️ Disclaimer
- This bot **must only be used on servers you own or manage**.  
- Using it on servers without permission is against [Discord’s Terms of Service](https://discord.com/terms) and can get your account banned.  
- Use responsibly!


## ✨ Features
- Deletes all **text channels, voice channels, and categories** in your server.
- Requires the user to have **Administrator** permission.
- Simple command-based trigger: `!delete_all`.


## 🚀 Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/tknainoo/Discord-Delete-All-Channel-.git
cd discord-deleter-bot
````

### 2. Install dependencies

Make sure you have Python 3.8+ installed. Then install [discord.py](https://pypi.org/project/discord.py/):

```bash
pip install discord.py
```

### 3. Create a Discord Bot

* Go to the [Discord Developer Portal](https://discord.com/developers/applications).
* Create a new application and add a **bot** user.
* Copy your bot token.

### 4. Add bot to your server

* Under **OAuth2 > URL Generator**, enable:

  * `bot`
  * **Administrator**
* Copy the invite URL, open it in your browser, and add the bot to your server.

### 5. Configure & Run

Edit the `bot.py` file and replace:

```python
bot.run("YOUR_BOT_TOKEN")
```

with your actual bot token. Then run:

```bash
python bot.py
```


## 💻 Usage

Once the bot is online in your server, run:

```
!delete_all
```

* The bot will delete **all channels and categories**.
* You’ll still have your roles and server settings intact.



## 🛠️ Future Improvements

* Add confirmation before deleting everything.
* Optionally recreate default channels (like `#general` and a Voice Channel).
* Add a logging system to track deleted channels.



