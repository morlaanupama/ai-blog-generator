import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    blog = ""

    if request.method == "POST":

        topic = request.form["topic"]

        prompt = f"""
        Write a professional blog on {topic}.

        Include:
        - Catchy title
        - Introduction
        - Headings
        - Conclusion

        Around 500 words.
        """

        response = model.generate_content(prompt)

        blog = response.text

    return render_template("index.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
