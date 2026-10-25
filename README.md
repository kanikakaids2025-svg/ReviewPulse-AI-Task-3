# ReviewPulse AI — Task 3: Intelligent Feature

A Streamlit prototype that predicts product-review sentiment with VADER and demonstrates input validation, error handling, evaluation examples, and known failure cases.

## Features
- Positive / Negative / Neutral prediction
- Sentiment and compound scores
- Input validation for empty and overly long reviews
- A small hand-labelled evaluation set with example accuracy
- Failure-case examples for sarcasm, mixed sentiment, negation, and context-dependent slang
- Friendly error messages if the model fails to load or an analysis fails

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. (Optional) Create and activate a virtual environment.
4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the dashboard:
   ```bash
   python -m streamlit run app.py
   ```

## Evaluation note
The evaluation set is a small demonstration, not a statistically representative benchmark. Accuracy is calculated against the included expected labels. VADER is rule-based and can struggle with sarcasm, mixed opinions, slang, and context.

## Technology
Python, Streamlit, VADER Sentiment, pandas.
