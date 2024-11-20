# Python Discord Bot for Life and Finance Tracker Notion Templates Integration

This project connects a Life Tracker and a Finance Tracker templates made with Notion, allowing entries creation via commands sent to the discord bot script. The script is hosted on an AWS Linux server, ensuring reliable and scalable performance.

## Features

**Life Tracker Integration**: Automates the addition of life events into a Notion database, to be able to track them and organize the by emotions.

**Finance Tracker Integration**: Tracks financial transactions, including name, amount, and category, including both expenses and incomes.

**Discord bot**: Makes it easier to add new entries to both templates on the go, without the need of Notions Mobile App which is slow most times.

**AWS Hosting**: The script is deployed on an AWS Linux server for continuous operation.

## Requirements
- Python 3.9+
- Linux Server
- Notion API Key
- Discord Bot Token
- Notion Database IDs for Life and Finance trackers templates


## Installation

- ### Clone the repository to your AWS server:
```
git clone <repository-url>  
cd <repository-folder>  
```

- ### Set up the virtual environment:
```
python3.9 -m venv env  
source env/bin/activate  
pip install -r reqs.txt  
```
## Configuration

- ### Create a .env file in the root directory:
```
touch .env  
```
- ### Add your Notion API Key and database IDs:

```
NOTION_TOKEN=your-notion-api-key  
BOT_TOKEN=your-discord-bot-token
```

- ### Variables:

Rememeber to replace the variables *databaseID_exp* and *databaseID_le* with your template's IDs and also replace the dictionaries containing the DB relations IDs.


## Usage


- ### Run the script:

```
python3 discord_bot.py  
```

- ### On discord:

Write the following command and send it as a message for adding entries to the Life Tracker:

```
$add_ev "name" "description" "YYYY-MM-DD or nothing for today" "emotion"
```

For Finance Tracker:

```
$add_exp "name" "YYYY-MM-DD or nothing for today" "amount" "category"
```

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.