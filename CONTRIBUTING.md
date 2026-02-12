# Contributing to Jira Manager

Thank you for your interest in contributing to Jira Manager! 🎉

## Getting Started

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/jira-manager.git
   cd jira-manager
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Jira Credentials**
   ```bash
   cp config.ini.example config.ini
   # Edit config.ini with your test Jira instance credentials
   ```

## Development Workflow

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write clean, documented code
   - Follow PEP 8 style guidelines
   - Add type hints where applicable
   - Update docstrings

3. **Write Tests**
   - Add tests for new features in `tests/`
   - Ensure all tests pass:
     ```bash
     pytest tests/ -v
     ```

4. **Check Code Quality**
   ```bash
   # Run tests with coverage
   pytest tests/ --cov=src/jira_manager --cov-report=term-missing
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add amazing new feature"
   ```

   Use conventional commit messages:
   - `feat:` new feature
   - `fix:` bug fix
   - `docs:` documentation changes
   - `test:` adding tests
   - `refactor:` code refactoring

6. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub.

## Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints for function parameters and return values
- Write descriptive docstrings for all public methods
- Keep functions focused and single-purpose
- Use meaningful variable names

## Testing Guidelines

- Write unit tests for all new functionality
- Mock external Jira API calls in tests
- Aim for >80% code coverage
- Test both success and error cases
- Use descriptive test names

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Questions about the codebase
- Suggestions for improvements

Thank you for contributing! 
