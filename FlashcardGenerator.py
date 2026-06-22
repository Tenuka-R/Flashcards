from flask import Flask
app = Flask(__name__)

@app.route("/")
def flashcard():
    return """
    <div style = "
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
    ">

    <div style = "
        width: 300px;
        height: 200px;
        background-color: lightblue;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 24px;
        border-radius: 10px;
    ">
        Hello, this is text in a flashcard!
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
