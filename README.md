# 🕵️‍♂️ CompetitorIntel Agent

An AI-powered agent that helps companies monitor competitors’ websites, product updates, and announcements—automatically.

Instead of manually tracking blog posts and feature launches, this bot:
- Searches Google for recent competitor news
- Scrapes article content
- Summarizes the key takeaways using LLM
- Saves everything in a structured Notion page

---

## 🧠 Real-World Use Case

**Problem:**  
Marketing, strategy, and leadership teams often miss timely competitor updates due to scattered sources and manual tracking. Oftentimes such tools is not free to use.

**Solution:**  
This AI agent automates that entire workflow and delivers weekly summaries straight to Notion.

![CompetitorIntel Agent GIF](/output/Arcade%20Demo%20GIF.gif)

---

Built using [Arcade.dev](https://docs.arcade.dev/toolkits) toolkits:
- 🔎 [Search.GoogleSearch](https://docs.arcade.dev/toolkits/search/google_search)
- 🌐 [Web.ScrapeURL](https://docs.arcade.dev/toolkits/development/web/web)
- 📓 [NotionToolkit.CreatePage](https://docs.arcade.dev/toolkits/productivity/notion)

---

## Wath the video tutorial

[CompetitorIntel Agent Video Tutorial](https://drive.google.com/file/d/19cjP7XNyCe7QlCVhzPWjK2TSfNOBw4_p/view?usp=sharing)

## 🧰 Requirements

- Python 3.13
- Create an [Arcade account](https://api.arcade.dev/signup?utm_source=docs&utm_medium=page&utm_campaign=call-tools-directly) and obtain [Arcade API key](https://docs.arcade.dev/home/api-keys)

---

## 🔧 Setup

1. Clone this repo:

```bash
git clone https://github.com/Boburmirzo/competitor-intel-agent.git
cd competitor-intel-agent
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate     # On macOS/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```


4. Create a .env file with your credentials

```bash
ARCADE_API_KEY=your_arcade_api_key
ARCADE_USER_ID=your_email@example.com
```

5. Run the agent

```bash
python competitor_tracker.py
```

## 📝 Output Example (in Notion)

A Notion page like: https://www.notion.so/Competitor-Intelligence-1f78d15fe66c80d98317dde8f517a8b3
Or you can check output [exported to PDF](/output/Competitor%20Intelligence%20Sample%20Output.pdf).


## ⚠️ Notes

- Page scraping uses Web.ScrapeURL, which may not work on login-protected or paywalled sites.
- Notion authorization is requested on first run via Arcade OAuth.

## 🚀 Future Improvements

Here are a few ideas to further improve the project:

- Slack Integration for Real-Time Alerts

Integrate with Slack using [Arcade Slack tool](https://docs.arcade.dev/toolkits/social-communication/slack) to send real-time notifications to the #marketing channel when key events occur.

- Social Media Data Collection

Implement automated data collection from platforms like X and LinkedIn to track competitor's brand mentions.

## 👨‍💻 Author

Built by @boburmirzo with ❤️ and [Arcade.dev](https://www.arcade.dev/)