import requests
import os


NOTION_TOKEN = os.environ["NOTION_TOKEN"]

databaseID_le ="1308842944f4819bad7bf04047749d9a"
databaseID_exp ="12e8842944f480548fb3ce513335e8bb"

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

months = {
    "11":{"relation": [{"id":"12e8842944f4802a9371d951622b615e"}]},
    "12":{"relation": [{"id":"12e8842944f4809699abfd729f4eaf61"}]}
    }

categories = ["Treats", "Taxes", "Personal", "Groceries", "Car", "Charity"]

def add_event_to_notion(name, description, date, picture_url, emotion):


    payload = {
        "parent": {"database_id": databaseID_le},
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

def add_expense(name, date, amount, category):

    if category not in categories:

        raise Exception(f"Category should be one of the following: {categories}")

    payload = {
        "parent": {"database_id": databaseID_exp},
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
            "Months": months[date[5:7]],
            "Amount":{
                "number": amount
                },
            "Category": {
                "select": {
                    "name": category
                }
            }
        }
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=payload)

    if response.status_code == 200:
        print("Expense added successfully!")
    else:
        print(f"Failed to add event. Status code: {response.status_code}, {response.text}")
        raise Exception("Failed to add event")


if __name__ == "__main__":

    add_expense(
    name="Sample expense",
    date="2024-11-18",
    amount=15,
    category="Car"
    )