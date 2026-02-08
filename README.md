# LinkedIn Bot 🚀

A semi-automatic LinkedIn posting bot that generates AI-powered, engaging LinkedIn posts and publishes them directly to your feed. Built with OpenAI's API, Playwright, and support for multi-client management.

## Features ✨

- **AI-Powered Post Generation** — Uses Azure OpenAI API to generate personalized, on-brand LinkedIn posts
- **Playwright Automation** — Automates the posting process via browser automation
- **Multi-Client Support** — Manage multiple LinkedIn accounts/brands with separate context and prompt configs
- **Session Persistence** — One-time login; sessions are saved securely
- **Post Tracking** — Maintains logs of published posts
- **Customizable Templates** — Use client-specific prompt and context files to tailor post style

## Project Structure 📁

```
linkedin-bot/
├── README.md                      # This file
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git exclusions
├── LICENSE                       # MIT License
├── auth.json                     # LinkedIn session (git-ignored)
├── posted.log                    # Posted content hashes (git-ignored)
│
├── login_once.py                 # Setup: One-time LinkedIn login
├── generate_post.py              # Step 1: Generate post via AI
├── post_to_linkedin.py           # Step 2: Automate posting to LinkedIn
│
└── clients/
    ├── client-1/
    │   ├── prompt.txt            # AI system prompt for this client
    │   ├── context.txt           # Client context/guidelines
    │   └── posts/                # Generated posts (timestamped)
    │
    └── shikhar/
        ├── prompt.txt
        ├── context.txt
        └── posts/
```

## Quick Start 🚀

### 1. Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token_here
LINKEDIN_EMAIL=your_linkedin_email@gmail.com
```

**Get GitHub Token for OpenAI API:**
1. Go to https://github.com/settings/tokens
2. Create a new token with `read:packages` permission
3. Use it as `GITHUB_TOKEN`

### 3. One-Time LinkedIn Login

```bash
python login_once.py
```

- A browser will open prompting you to log into LinkedIn manually
- Press Enter in the terminal once logged in
- Your session will be saved to `auth.json` (git-ignored)

### 4. Create a Client Profile

Create a new client directory:

```bash
mkdir -p clients/your_client_name
```

Create `clients/your_client_name/prompt.txt` (AI system prompt):

```
You are a Senior Software Developer writing engaging LinkedIn posts.
Keep posts under 150 words, professional yet human.
Include emoji stickers, mark claims as "reported" if unverified.
```

Create `clients/your_client_name/context.txt` (Client guidelines):

```
Voice: Professional, story-driven, slightly comic touch.
Avoid hype. Focus on real impact. No profanity or disrespect.
Include relevant hashtags and @mentions where appropriate.
```

### 5. Generate a Post

```bash
python generate_post.py your_client_name
```

A post will be generated and saved to `clients/your_client_name/posts/YYYY-MM-DD-HH-MM-SS.txt`

### 6. Post to LinkedIn

```bash
python post_to_linkedin.py your_client_name
```

The latest post from that client will be published to LinkedIn.

## Usage Examples 📖

### Generate and Post in One Flow

```bash
# Generate post
python generate_post.py shikhar

# Review the generated post (optional)
cat clients/shikhar/posts/2026-02-08-15-07-41.txt

# Post to LinkedIn
python post_to_linkedin.py shikhar
```

### Manage Multiple Clients

```bash
# Create a second client
mkdir -p clients/techblog

# Add their prompt and context
echo "Prompt for TechBlog..." > clients/techblog/prompt.txt
echo "Context for TechBlog..." > clients/techblog/context.txt

# Generate and post for this client
python generate_post.py techblog
python post_to_linkedin.py techblog
```

## Configuration Guide 🔧

### Customizing Post Generation

Edit `clients/your_client/prompt.txt` to control tone, style, and content guidelines.

Edit `clients/your_client/context.txt` to add client-specific details (e.g., company info, founder bios, product details).

### Disabling Demo Mode

By default, all selectors and delays are conservative. To speed up posting:
- In `post_to_linkedin.py`, reduce `slow_mo` from 50 to 10-20
- Adjust `time.sleep()` values as needed

## Security Best Practices 🔐

1. **Never commit credentials:**
   - `auth.json` is git-ignored
   - Use `.env` file for `GITHUB_TOKEN`
   - Never hardcode API keys

2. **Protect your GitHub token:**
   - Use a personal access token with minimal scope
   - Rotate tokens periodically
   - Monitor usage

3. **LinkedIn Session:**
   - `auth.json` contains session state; treat as sensitive
   - Re-run `login_once.py` if session expires

## Troubleshooting 🔨

**Error: "Could not find 'Start a post' paragraph"**
- LinkedIn UI may have changed
- Open browser in non-headless mode for debugging:
  - In `post_to_linkedin.py`, change `headless=True` to `headless=False`
  - Look for the new selector for the "Start a post" button
  - Update the selector accordingly

**Error: "Not logged in"**
- Session expired; run `login_once.py` again

**Error: "Post editor did not appear"**
- Network delay; increase `wait_until` timeout in `post_to_linkedin.py`
- Or check if LinkedIn has updated the DOM structure

**Post content is empty**
- Check that `context.txt` and `prompt.txt` exist and have content
- Verify OpenAI/GitHub token is valid and has API quota

## Contributing 🤝

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes and test thoroughly
4. Commit with clear messages: `git commit -m "Add feature X"`
5. Push and open a Pull Request

## Known Limitations ⚠️

- LinkedIn may block frequent posting; use this responsibly
- UI selectors can break if LinkedIn updates their site
- Requires manual login setup (good for security, requires initial step)
- Only works on Linux/macOS/Windows (Playwright requirement)

## Future Enhancements 🔮

- [ ] Scheduling posts (cron integration)
- [ ] Analytics dashboard (post engagement tracking)
- [ ] A/B testing (multiple post variants)
- [ ] Webhook support (trigger generation from external services)
- [ ] Support for LinkedIn Stories/Reels
- [ ] Database integration for post versioning

## License 📄

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author 👨‍💻

Built as a semi-automatic LinkedIn posting tool for managing multi-client content workflows.

---

⭐ If you find this useful, please star the repository and share feedback!
