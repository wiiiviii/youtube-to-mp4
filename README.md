# youtube-to-mp4

![banner](https://offdahook.org/wee/yt-mp4-banner.png)

<h2>a simple and powerful discord bot that scans chat messages for YouTube URLs and instantly sends back the corresponding video files.</h2>

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup](#setup)
  - [1 - Create the Bot](#1---create-the-bot)
  - [2 - Get Bot Token](#2---get-bot-token)
  - [3 - Set Intents](#3---set-intents)
  - [4 - Invite Bot to Server](#4---invite-bot-to-server)
- [Installation](#installation)
- [Usage](#usage)
- [Auto-Restart](#auto-restart)
- [License](#license)

## Introduction 
With its seamless integration, youtube-to-mp4 simplifies the process of sharing YouTube videos within your Discord server. Whether you're discussing music, tutorials, or funny clips, DiscordTube ensures quick access to the content you love, enhancing the overall user experience.

## Requirements
- python
- discord
- yt-dl

## Setup

### 1 - Create the Bot
1. Go to the [Discord Developer Portal website](https://discord.com/developers/applications) and log in with your Discord account.
2. Click on the `New Application` button to create a new application for your bot.
3. Enter a name for your application and click the `Create` button.
4. In the left sidebar, click on the `Bot` tab.
5. Click on the `Add Bot` button and confirm the action by clicking `Yes, do it!` in the dialog that appears.

### 2 - Get Bot Token
Your Bot token is essential for your bot to authenticate and connect to Discord servers.
1. Under the `Token` section, click on the `Copy` button to copy the bot token to your clipboard. 
2. Save your token somewhere safe and don't share it with others

### 3 - Set Intents
**To enable necessary intents for your bot, follow these additional steps:**
1. Go back to the Discord Developer Portal and click on the `Bot` tab.
2. Under the `Privileged Gateway Intents` section, enable the intents that your bot requires. Common intents include `Presence Intent` and `Server Members Intent`. Note that certain intents require verification by Discord.

### 4 - Invite Bot to Server
1. In the left sidebar, click on the `OAuth2` tab.
2. In the `Scopes` section, select the `bot` checkbox. This will generate a URL for adding your bot to a server.
3. Scroll down to the `Bot Permissions` section and select the required permissions that your bot will need. These permissions define what your bot can do on Discord servers.
4. Copy the generated URL from the `Scopes` section.
5. Open a new browser tab and paste the URL into the address bar. This will allow you to add the bot to a server of your choice. Select a server and authorize the bot.

## Installation
1. Open a Terminal and navigate to the directory where you want to clone your bot's repository.
2. Clone the repository by running the command `git clone https://github.com/wiiiviii/youtube-to-mp4.git`.
3. Navigate into the cloned repository by running the command `cd youtube-to-mp4`.
4. Install the required dependencies by running the command `pip install -r requirements.txt`.
5. Add your token and desired prefix to the `config.py` file.
6. Run your bot by executing the appropriate command, such as `python bot.py` or `python3 bot.py`.


## Usage
**When the bot is active on your Discord server, simply post a message containing a YouTube video link.**
- the bot will `automatically detect youtube urls` and initiate the process. 
- the bot will `retrieve the video file and convert` it if necessary. 
- the bot will `send the video back to you as a file` in the same chat channel

`[prefix]check`: checks if the bot is responding

`[prefix]shutdown`: initiate bot shutdown process 

## Auto-Restart
To set up auto-restart for your bot using PM2, follow these steps:

1. Run the command `npm install pm2 -g` to install PM2 globally on your system.
2. Use `cd /path/to/your/bot` to navigate to the directory where you placed the bot 
3. Run the command `pm2 start bot.py --name examplename`, 
    - replacing `examplename` with the desired name for your PM2 process.
    - example: `pm2 start bot.py --name coolbot`
4. To verify that it started properly you can run the command `pm2 list`. this will return a list of all running PM2 processes and you can look for your bot's process with the specified name in the output.
5. Use various PM2 commands to manage your bot process:
      - To stop the process: `pm2 stop <name>` (e.g., `pm2 stop mybot`)
      - To start the process: `pm2 start <name>` (e.g., `pm2 start mybot`)
      - To restart the process: `pm2 restart <name>` (e.g., `pm2 restart mybot`)
      - To view logs: `pm2 logs <name>` (e.g., `pm2 logs mybot`)
      - For more advanced usage, refer to the [PM2 documentation](https://pm2.keymetrics.io/docs/usage/pm2-doc-single-page/).
6. Run the command `pm2 startup` to generate a command that enables PM2 to start automatically on system boot.
7. Follow the instructions provided by the command to complete the setup.

## License

[MIT © Richard McRichface.](LICENSE)
