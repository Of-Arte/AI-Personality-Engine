# AI Personality Engine

An analysis and generation engine that constructs detailed AI personality profiles based on user responses. It utilizes semantic embedding comparison and sub-trait extraction to model behavioral tendencies and preferences.

## Core Features
- **Semantic Analysis**: Compares free-text responses against predefined insight categories using cosine similarity and 512-dimensional embeddings.
- **Sub-trait Extraction**: Parses qualitative responses into quantitative scores for:
    - Learning Style (Guided vs. Exploratory)
    - Decision Making (Risk & Ambiguity Tolerance)
    - Creativity (Originality vs. Procedural)
    - Communication (Formality, Empathy, Humor)
    - Ethics & Collaboration Style
- **Meta-Inference Generation**: Synthesizes raw traits into high-level behavioral profiles.
- **Profile Construction**: Generates a full narrative and structured JSON profile mapping the user's interaction style.

## Project Structure
```text
ai-personality-engine/
├── engine.py            # Core logic for analysis and profile building
├── run_summary_test.py  # Test suite with 10 simulated user scenarios
├── assessment.json      # Structured assessment data
├── outputs/             # Generated profile outputs
└── requirements.txt     # Python dependencies
```

## Installation
Ensure you have Python 3.x installed, then install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Building a Profile
Import the `build_full_profile` function from `engine.py` to process interaction data:
```python
from engine import build_full_profile

profile = { "model_preference": "GPT-4" }
responses = { "q1": "I prefer structured guidance..." }

result = build_full_profile(profile, responses)
print(result['narrative'])
```

### Running Tests
To run the automated test suite and view simulated profile generation:
```bash
python run_summary_test.py
```
Outputs will be saved to the `outputs/` directory.

## Contributing
Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on setting up the environment, running tests, and submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
