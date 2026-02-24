# Contributing to AI Personality Engine

First off, thank you for considering contributing to the AI Personality Engine! It's people like you that make open source such a great community to learn, inspire, and create.

## Developing

1. **Fork and Clone the Repo:**
   - Fork the repository on GitHub.
   - Clone your fork locally.

2. **Set up the Environment:**
   Ensure you have Python 3.x installed. Then, set up a virtual environment and install the dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Running Tests:**
   The project includes a test suite that simulates user scenarios and generates output profiles. Before submitting a pull request, run the test script and ensure everything is working correctly:
   ```bash
   python run_summary_test.py
   ```
   Check the `outputs/` directory to review the generated profiles.

4. **Making Changes:**
   - Create a new branch for your feature or bug fix.
   - Write clear, concise code adhering to Python best practices (PEP 8).
   - Ensure type hints and docstrings are added/updated for any public functions or classes.

5. **Submitting a Pull Request:**
   - Push your branch to your fork.
   - Open a pull request against the `main` branch of this repository.
   - Clearly describe the problem you solved or the feature you added in the pull request description.

We look forward to reviewing your contributions!
