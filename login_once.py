from playwright.sync_api import sync_playwright

def save_linkedin_session(output_path="auth.json"):
    """Open browser, prompt user to log in, save session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.linkedin.com/login")

        print("👉 Log in manually, then press Enter here")
        input()

        context.storage_state(path=output_path)
        browser.close()
    print("✅ Logged in and saved auth.json")


if __name__ == "__main__":
    save_linkedin_session()