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
Marketing, strategy, and leadership teams often miss timely competitor updates due to scattered sources and manual tracking.

**Solution:**  
This AI agent automates that entire workflow and delivers weekly summaries straight to Notion.

---

<!-- ![AI-Powered Research Assistant Agent with Arcade](/assets/Arcade%20Research%20Assitant%20Demo.gif) -->

Built using [Arcade.dev](https://docs.arcade.dev/toolkits) toolkits:
- 🔎 [Search.GoogleSearch](https://docs.arcade.dev/toolkits/search/google_search)
- 🌐 [Web.ScrapeURL](https://docs.arcade.dev/toolkits/development/web/web)
- 📓 [NotionToolkit.CreatePage](https://docs.arcade.dev/toolkits/productivity/notion)

---

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

## 👨‍💻 Author

Built by @boburmirzo with ❤️ and [Arcade.dev](https://www.arcade.dev/)