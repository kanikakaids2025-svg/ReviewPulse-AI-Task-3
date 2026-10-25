import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(page_title="ReviewPulse AI | Task 3", page_icon="💬", layout="wide")

@st.cache_resource
def load_analyzer():
    return SentimentIntensityAnalyzer()

try:
    analyzer = load_analyzer()
except Exception as exc:
    st.error("The sentiment model could not be loaded. Please install the requirements and restart the app.")
    st.code(str(exc))
    st.stop()


def predict_sentiment(text: str):
    """Return sentiment label and VADER scores, with input validation."""
    if not isinstance(text, str):
        raise TypeError("Review must be text.")
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Please enter a review before analyzing.")
    if len(cleaned) > 5000:
        raise ValueError("Review is too long. Please keep it under 5,000 characters.")
    scores = analyzer.polarity_scores(cleaned)
    compound = scores["compound"]
    if compound >= 0.05:
        label = "Positive"
    elif compound <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    return label, scores

st.title("💬 ReviewPulse AI — Intelligent Sentiment Analyzer")
st.caption("Task 3: Intelligent Feature • Input validation • Evaluation examples • Failure-case testing")

with st.sidebar:
    st.header("About this model")
    st.write("This prototype uses VADER, a rule-based sentiment model designed for English text.")
    st.write("Compound score: −1 (most negative) to +1 (most positive).")
    st.info("This is a prototype, not a guarantee of a reviewer's true meaning. Sarcasm and context can cause mistakes.")

input_tab, eval_tab, failure_tab = st.tabs(["🔎 Analyze a review", "📊 Evaluation examples", "🧪 Failure cases"])

with input_tab:
    st.subheader("Enter a product review")
    review = st.text_area("Review text", placeholder="Example: This product is amazing. I love it!", height=150, max_chars=5500)
    if len(review) > 5000:
        st.warning(f"Your review has {len(review)} characters. The maximum allowed length is 5,000.")
    if st.button("Analyze sentiment", type="primary"):
        try:
            label, scores = predict_sentiment(review)
            st.subheader("Prediction")
            if label == "Positive":
                st.success("Positive 😊")
            elif label == "Negative":
                st.error("Negative 😞")
            else:
                st.info("Neutral 😐")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Positive score", f'{scores["pos"]:.2f}')
            c2.metric("Neutral score", f'{scores["neu"]:.2f}')
            c3.metric("Negative score", f'{scores["neg"]:.2f}')
            c4.metric("Compound score", f'{scores["compound"]:.3f}')
        except (ValueError, TypeError) as exc:
            st.warning(str(exc))
        except Exception as exc:
            st.error("Unexpected error while analyzing this review. Please try a shorter English review.")
            st.caption(f"Technical detail: {exc}")

with eval_tab:
    st.subheader("Built-in evaluation set")
    st.write("These hand-labelled examples provide a simple demonstration. Results may vary because VADER is a general-purpose rule-based model.")
    examples = [
        {"Review": "Absolutely love this product! It works perfectly.", "Expected": "Positive"},
        {"Review": "Great quality and fast delivery.", "Expected": "Positive"},
        {"Review": "This is terrible and stopped working immediately.", "Expected": "Negative"},
        {"Review": "Very disappointing. I would not recommend it.", "Expected": "Negative"},
        {"Review": "The package arrived today.", "Expected": "Neutral"},
        {"Review": "The item is black and has three buttons.", "Expected": "Neutral"},
        {"Review": "I expected better, but it is okay.", "Expected": "Negative"},
        {"Review": "Not bad at all, actually quite useful!", "Expected": "Positive"},
    ]
    rows = []
    for item in examples:
        try:
            predicted, scores = predict_sentiment(item["Review"])
            rows.append({"Review": item["Review"], "Expected": item["Expected"], "Predicted": predicted, "Correct?": "✅ Yes" if predicted == item["Expected"] else "❌ No", "Compound": round(scores["compound"], 3)})
        except Exception as exc:
            rows.append({"Review": item["Review"], "Expected": item["Expected"], "Predicted": "Error", "Correct?": "❌ No", "Compound": str(exc)})
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)
    accuracy = sum(row["Predicted"] == row["Expected"] for row in rows) / len(rows) * 100
    a, b = st.columns(2)
    a.metric("Example-set accuracy", f"{accuracy:.1f}%")
    b.metric("Examples tested", len(rows))
    st.caption("Accuracy is calculated only on these small demonstration examples; it is not a benchmark for all product reviews.")

with failure_tab:
    st.subheader("Failure-case demonstrations")
    st.write("These examples show situations where sentiment models may misunderstand meaning or context.")
    failure_examples = [
        ("Sarcasm", "Amazing... it broke after one hour 🙄", "Sarcasm can sound positive even when the meaning is negative."),
        ("Mixed sentiment", "The camera is excellent, but the battery is awful.", "A single overall label can hide mixed opinions about different features."),
        ("Negation", "I do not dislike this product.", "Negation can change the meaning and may be interpreted imperfectly."),
        ("Context-dependent", "That is sick!", "Slang may be positive or negative depending on context."),
    ]
    for category, text, explanation in failure_examples:
        with st.expander(category):
            st.write(f"**Review:** {text}")
            try:
                label, scores = predict_sentiment(text)
                st.write(f"**Model prediction:** {label} (compound: {scores['compound']:.3f})")
            except Exception as exc:
                st.warning(str(exc))
            st.write(f"**Possible limitation:** {explanation}")
    st.markdown("#### Input error tests")
    st.write("Try submitting an empty review in the Analyze tab, or paste more than 5,000 characters to see input validation.")

st.divider()
st.caption("Task 3 — Intelligent Feature | Python • Streamlit • VADER • pandas")
