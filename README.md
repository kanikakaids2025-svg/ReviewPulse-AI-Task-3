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
8. Final Application

ReviewPulse AI is a beginner-friendly sentiment analysis application that analyzes customer product reviews and identifies their sentiment as positive, negative, or neutral.

9. Problem Statement

Online shopping platforms contain thousands of customer reviews. Reading every review manually takes time. This application helps users quickly understand customer opinions through sentiment analysis.

10. Methodology

The application follows these steps:

1. The user enters a product review.
2. The application checks whether the input is empty.
3. VADER sentiment analysis processes the review text.
4. The application identifies the sentiment as positive, negative, or neutral.
5. The result is displayed through a simple Streamlit interface.

11. Demo Examples

Positive review:
"This product is excellent. I really love it!"

Negative review:
"The product quality is poor and disappointing."

Neutral review:
"The package arrived yesterday."

The application can analyze these reviews and display the predicted sentiment.

12. Evaluation and Error Handling

The application includes evaluation examples and failure cases to demonstrate how sentiment predictions work.

If the user submits an empty review, the application displays a warning asking them to enter a review.

Sarcasm, mixed opinions, negation, and context-dependent sentences may lead to incorrect predictions.

13. Limitations

- Predictions may not always be accurate.
- Sarcasm and complex sentences can be difficult to understand.
- The meaning of a review may depend on its context.
- The application may not understand every product-specific expression.
- The results should not be treated as guaranteed facts.

14. Ethics and Responsible AI

- Use predictions as guidance, not as a replacement for human judgment.
- Do not enter personal or confidential information.
- Remember that sentiment predictions can be incorrect.
- Avoid making important decisions about customers or sellers based only on AI predictions.
- Review results carefully before using them.

15. How to Run the Application

Install the required dependencies:

python -m pip install -r requirements.txt

Start the Streamlit application:

python -m streamlit run app.py

The application will open in the web browser.

16. Future Enhancements

- Improve sentiment prediction accuracy.
- Test with more diverse product reviews.
- Add more evaluation examples.
- Explore advanced machine-learning models.
- Deploy the application online.

17. Conclusion

ReviewPulse AI demonstrates how Natural Language Processing and sentiment analysis can help users understand customer opinions. The application combines a simple interface, evaluation examples, error handling, and responsible AI guidelines in one beginner-friendly project.
