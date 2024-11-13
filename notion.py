import datetime
import json, requests
from unicodedata import name
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.environ["NOTION_TOKEN"]

databaseID ="1308842944f4819bad7bf04047749d9a"
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

emotions = {
    "happy":{"relation": [{"id":   "d3482d26e02b4eba8f09780593a2abbc"}]},
    "sad":{"relation": [{"id":     "54bf3fca417b4bc6acca1737f839dd44"}]},
    "fear":{"relation": [{"id":    "1318842944f4801484d9ce051fba0cda"}]},
    "motivated":{"relation": [{"id":"b6520518f99a41e6ab65c42475792ab3"}]},
    "relief":{"relation": [{"id":  "1308842944f480a5aba3c7e4ca78cfa0"}]},
    "curious":{"relation": [{"id": "1308842944f480a4bdafc5d35c6d28c4"}]},
    "anger":{"relation": [{"id":   "1318842944f480adb28fc5feada0af8a"}]}
}

def add_event_to_notion(name, description, date, picture_url, emotion):


    payload = {
        "parent": {"database_id": databaseID},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                    "start": date
                }
            },
            "Emotion": emotions[emotion]
        }
    }

    if description:

        payload["properties"]["Description"]={
                "rich_text": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
                }

    if picture_url:

        payload["properties"]["Pictures"] = {
                "files": [
                    {
                        "name": "Event Picture",
                        "external": {
                            "url": picture_url
                        }
                    }
                ]
            }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=payload)

    if response.status_code == 200:
        print("Event added successfully!")
    else:
        print(f"Failed to add event. Status code: {response.status_code}, {response.text}")
        raise Exception("Failed to add event")

if __name__ == "__main__":

    add_event_to_notion(
    name="Sample Event",
    description="",
    date="2024-11-13",
    picture_url="",
    emotion="happy",
    )