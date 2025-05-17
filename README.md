# 🧠 AI-Powered Research Assistant Agent with Arcade

Writers spend hours researching a topic, gathering sources, and organizing notes before drafting content. This process is repetitive and time-consuming.

This Arcade agent automates content research for writers by:

- Taking a topic input
- Searching Google for relevant articles links
- Scrapes content from each link
- Summarizing the top results
- Storing notes and references directly in a Notion page

![AI-Powered Research Assistant Agent with Arcade](/assets/Arcade%20Research%20Assitant%20Demo.gif)

Built using [Arcade.dev](https://docs.arcade.dev/toolkits) toolkits:
- 🔎 [Search.GoogleSearch](https://docs.arcade.dev/toolkits/search/google_search)
- 🌐 [Web.ScrapeURL](https://docs.arcade.dev/toolkits/development/web/web)
- 📓 [NotionToolkit.CreatePage](https://docs.arcade.dev/toolkits/productivity/notion)

---

## 🚀 How It Works

1. User defines a topic
2. Agent:
   - Performs Google search
   - Scrapes article content from each link
   - Summarizes each using LLM like gpt4-0
   - Formats all findings into a Notion page

---

## 🧰 Requirements

- Python 3.13
- Create an [Arcade account](https://api.arcade.dev/signup?utm_source=docs&utm_medium=page&utm_campaign=call-tools-directly) and obtain [Arcade API key](https://docs.arcade.dev/home/api-keys)

---

## 🔧 Setup

1. Clone this repo:

```bash
git clone https://github.com/your-org/research-assistant-agent.git
cd research-assistant-agent
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
python main.py
```

## 📝 Output Example (in Notion)

A Notion page like: https://www.notion.so/AI-agents-in-customer-support-1f68d15fe66c815592a7f6d75e6b0516


## ⚠️ Notes

- Page scraping uses Web.ScrapeURL, which may not work on login-protected or paywalled sites.
- Notion authorization is requested on first run via Arcade OAuth.

## 👨‍💻 Author

Built by @boburmirzo with ❤️ and [Arcade.dev](https://www.arcade.dev/)