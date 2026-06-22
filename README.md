# About
A simple AI-powered flashcard generator created using Flask and Gemini. Enter a topic and difficulty level to get 5 flashcards with questions and answers
# How to use
- Enter a topic and difficulty such as "Algebra Year 8" or "Country capitals for teenagers". 
- Click each card to flip and reveal the answer or show the question again. Use the arrows to navigate between th 5 questions. 
- Get a new set of questions by clicking "New topic".
# Setup
1. Clone the repo
2. Create a virtual environment and run `pip install -r requirements.txt`
3. Get a Gemini API key at https://aistudio.google.com/app/api-keys
4. Create a `.env` file and add `API_KEY=y<our_key_here>`
5. Run `python QuestionGenerator.py` and open the given localhost link
