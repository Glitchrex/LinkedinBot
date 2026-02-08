# Contributing to LinkedIn Bot 🤝

Thank you for considering contributing to LinkedIn Bot! We're excited to have you help improve this project.

## Code of Conduct

- Be respectful and inclusive
- No harassment, discrimination, or offensive language
- Help others learn and grow
- Report violations to project maintainers

## How to Contribute

### 1. Report Bugs

Found a bug? Please open an issue with:
- **Title**: Clear, concise description
- **Description**: What happened? What did you expect?
- **Steps to reproduce**: Exact steps to replicate the issue
- **Environment**: Python version, OS, Playwright version
- **Logs**: Error messages or relevant output

### 2. Suggest Features

Have an idea? Open an issue with:
- **Title**: "Feature request: [description]"
- **Description**: Why this feature would be useful
- **Use case**: Real-world scenario where it helps
- **Proposed solution**: How you'd like it to work

### 3. Submit Code Changes

#### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/linkedin-bot.git
cd linkedin-bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies with dev tools
pip install -r requirements.txt
pip install pylint black pytest  # Development tools
```

#### Make Changes

1. Create a feature branch:
   ```bash
   git checkout -b feature/my-awesome-feature
   ```

2. Make your changes:
   - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
   - Add docstrings to all functions
   - Write unit tests for new features
   - Update README.md if behavior changes

3. Format and lint your code:
   ```bash
   black *.py                # Format code
   pylint *.py               # Check for issues
   ```

4. Test your changes:
   ```bash
   # Run your script
   python generate_post.py test_client
   python post_to_linkedin.py test_client
   ```

#### Commit and Push

```bash
git add .
git commit -m "Add feature: [clear description of what changed]"
git push origin feature/my-awesome-feature
```

#### Open a Pull Request

1. Go to https://github.com/YOUR_USERNAME/linkedin-bot
2. Click "Compare & pull request"
3. Fill in the PR template:
   - **Title**: Clear, concise description
   - **Description**: Why this change? What problem does it solve?
   - **Testing**: How did you test this?
   - **Related issues**: Link any related issues

4. Wait for review and address feedback

---

## Commit Message Guidelines

Write clear, descriptive commit messages:

```
Format: [Type]: [Description]

Types:
  - feat: New feature
  - fix: Bug fix
  - docs: Documentation changes
  - style: Code style changes (no logic change)
  - refactor: Code refactoring
  - test: Test additions/changes
  - chore: Build, dependency, or config changes

Examples:
  - feat: Add scheduling support with APScheduler
  - fix: Handle LinkedIn UI selector changes
  - docs: Update README with troubleshooting section
  - refactor: Extract post generation into separate module
```

---

## Code Style

### Python Style Guide (PEP 8)

```python
# ✅ Good
def generate_post(client_name: str) -> str:
    """Generate a LinkedIn post for the given client.
    
    Args:
        client_name: Name of the client
        
    Returns:
        Generated post content
        
    Raises:
        FileNotFoundError: If client config not found
    """
    # Implementation here
    pass

# ❌ Avoid
def gen(c):
    # Generate post
    pass
```

### Docstring Format

Use Google-style docstrings:

```python
def function_name(arg1: str, arg2: int) -> bool:
    """Brief description of what the function does.
    
    Longer description if needed, explaining context
    and any important details.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
        
    Returns:
        Description of return value and type
        
    Raises:
        ValueError: When something goes wrong
        
    Example:
        >>> result = function_name("test", 42)
        >>> print(result)
        True
    """
    pass
```

---

## Testing

### Write Tests

Create `test_*.py` files for unit tests:

```python
# tests/test_generate_post.py
import unittest
from generate_post import content_hash

class TestGeneratePost(unittest.TestCase):
    def test_content_hash(self):
        text = "test content"
        hash_value = content_hash(text)
        self.assertEqual(len(hash_value), 64)  # SHA256 is 64 chars
        
    def test_hash_consistency(self):
        text = "test"
        hash1 = content_hash(text)
        hash2 = content_hash(text)
        self.assertEqual(hash1, hash2)
```

### Run Tests

```bash
pytest tests/  # If using pytest
# or
python -m unittest discover tests/
```

---

## Documentation

### Update README

If your changes affect usage, update `README.md`:
- Add new features to features section
- Update troubleshooting if you fixed known issues
- Add examples if introducing new functionality

### Update docstrings

Keep inline documentation current:
- Function docstrings must be present
- Add comments for non-obvious logic
- Remove outdated comments

---

## Areas We Need Help With

- 🐛 **Bug fixes**: Especially LinkedIn selector issues when UI changes
- 🧪 **Testing**: Add unit and integration tests
- 📚 **Documentation**: Improve guides, add examples
- ✨ **Features**: Scheduling, analytics, multi-platform support
- 🎨 **UI/UX**: Improve logging and user feedback
- 🌍 **Localization**: Support for multiple languages

---

## Review Process

1. Maintainers will review your PR within a few days
2. Feedback may be requested
3. Address feedback or discuss if you disagree
4. Once approved, your changes will be merged!

---

## Questions?

- Open a GitHub Discussion for general questions
- Comment on the issue you're working on
- Check existing issues/PRs to see if it's been discussed

---

Thank you for contributing! Every PR, issue, and suggestion helps make LinkedIn Bot better. 🙌
