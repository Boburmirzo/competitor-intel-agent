import os
import time
import json
from dotenv import load_dotenv
from arcadepy import Arcade

# === LOAD ENV VARIABLES ===
load_dotenv()  # Loads variables from a .env file into the environment

# === CONFIGURATION ===
ARCADE_API_KEY = os.getenv("ARCADE_API_KEY")  # or hardcode it if needed
ARCADE_USER_ID = os.getenv("ARCADE_USER_ID")
TOPIC = "AI agents in customer support"  # Change this to any research topic
PARENT_TITLE = "Research Notes"  # Notion parent page title to group content under

# === INIT ARCADE CLIENT ===
arcade = Arcade(api_key=ARCADE_API_KEY)

# === STEP 0: AUTHORIZE NOTION ===
print("🔐 Checking Notion authorization...")
auth_response = arcade.tools.authorize(
    tool_name="NotionToolkit.CreatePage",
    user_id=ARCADE_USER_ID,
)

if auth_response.status != "completed":
    print(f"👉 Visit this link to authorize Notion access:\n{auth_response.url}")
    arcade.auth.wait_for_completion(auth_response)
    print("✅ Notion access authorized.")

# === STEP 1: GOOGLE SEARCH ===
print(f"🔍 Searching Google for: {TOPIC}")
search_results = arcade.tools.execute(
    tool_name="Search.SearchGoogle",
    input={"query": TOPIC, "n_results": 5},
    user_id=ARCADE_USER_ID,
)

search_data = json.loads(search_results.output.value)

# === STEP 2: SCRAPE AND SUMMARIZE EACH LINK ===
summaries = []
print("🧠 Scraping and summarizing results...")

for result in search_data:
    title = result.get("title", "No Title")
    url = result.get("link", "")
    print(f"  ➤ Scraping: {title} — {url}")

    try:
        scrape_result = arcade.tools.execute(
            tool_name="Web.ScrapeURL",
            input={"url": url},
            user_id=ARCADE_USER_ID,
        )
        page_content = scrape_result.output.value.get("markdown", "").strip()
    except Exception as e:
        print(f"  ⚠️ Failed to scrape {url}: {e}")
        page_content = ""

    if not page_content:
        summary_text = "⚠️ Could not extract content from this URL."
    else:
        summary_prompt = f"Summarize the following article in 3 short bullet points:\n\n{page_content[:6000]}"  # trim to avoid token overflow
        summary_response = arcade.chat.completions.create(
            messages=[{"role": "user", "content": summary_prompt}],
            model="gpt-4o",
        )
        summary_text = summary_response.choices[0].message.content.strip()

    summaries.append({"title": title, "url": url, "summary": summary_text})
    time.sleep(1)


# === STEP 3: COMBINE SUMMARIES ===

notion_content = "\n\n---\n\n".join(
    f"**{item['title']}**\n{item['url']}\n\n{item['summary']}" for item in summaries
)
print(notion_content)

# === STEP 4: CREATE NOTION PAGE WITH CONTENT ===
print("📝 Creating Notion page with all content...")
notion_response = arcade.tools.execute(
    tool_name="NotionToolkit.CreatePage",
    input={
        "parent_title": PARENT_TITLE,
        "title": TOPIC,
        "content": notion_content,
    },
    user_id=ARCADE_USER_ID,
)

print("✅ Notion page created!")
print(f"📄 Title: {TOPIC}")

# === DONE ===
print(f"\n✅ Research complete. Notes saved in Notion page titled: '{TOPIC}'")
