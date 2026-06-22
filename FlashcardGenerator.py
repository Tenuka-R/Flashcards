from flask import Flask

app = Flask(__name__)

@app.route("/")
def flashcard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background-color: #1a1a2e;
                font-family: 'Georgia', serif;
            }

            .card-container {
                width: 400px;
                height: 250px;
                perspective: 1000px;
                cursor: pointer;
            }

            .card {
                width: 100%;
                height: 100%;
                position: relative;
                transform-style: preserve-3d;
                transition: transform 0.6s ease;
            }

            .card.flipped {
                transform: rotateY(180deg);
            }

            .front, .back {
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                border-radius: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                font-size: 22px;
                padding: 20px;
                box-sizing: border-box;
                box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            }

            .front {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }

            .back {
                background: linear-gradient(135deg, #f093fb, #f5576c);
                color: white;
                transform: rotateY(180deg);
            }

            .hint {
                position: absolute;
                bottom: 20px;
                font-size: 12px;
                color: rgba(255,255,255,0.6);
                letter-spacing: 1px;
            }

            .controls {
                display: flex;
                align-items: center;
                gap: 20px;
                margin-top: 30px;
            }

            .arrow {
                background: none;
                border: 2px solid rgba(255,255,255,0.4);
                color: white;
                font-size: 20px;
                width: 45px;
                height: 45px;
                border-radius: 50%;
                cursor: pointer;
                transition: background 0.2s;
            }

            .arrow:hover {
                background: rgba(255,255,255,0.15);
            }

            .dots {
                display: flex;
                gap: 8px;
            }

            .dot {
                width: 10px;
                height: 10px;
                border-radius: 50%;
                background: rgba(255,255,255,0.3);
                cursor: pointer;
                transition: background 0.2s;
            }

            .dot.active {
                background: white;
            }

            .counter {
                color: rgba(255,255,255,0.6);
                font-size: 14px;
                margin-top: 12px;
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>

        <div class="card-container" onclick="toggleFlip()">
            <div class="card" id="card">
                <div class="front" id="front">
                    Loading...
                    <span class="hint">CLICK TO FLIP</span>
                </div>
                <div class="back" id="back">
                    Loading...
                    <span class="hint">CLICK TO FLIP BACK</span>
                </div>
            </div>
        </div>

        <div class="controls">
            <button class="arrow" onclick="changeCard(-1)">&#8592;</button>
            <div class="dots" id="dots"></div>
            <button class="arrow" onclick="changeCard(1)">&#8594;</button>
        </div>

        <div class="counter" id="counter"></div>

        <script>
            const cards = [
                { question: "Question 1", answer: "Answer 1" },
                { question: "Question 2", answer: "Answer 2" },
                { question: "Question 3", answer: "Answer 3" },
                { question: "Question 4", answer: "Answer 4" },
                { question: "Question 5", answer: "Answer 5" }
            ];

            let current = 0;

            function renderDots() {
                const dotsEl = document.getElementById("dots");
                dotsEl.innerHTML = "";
                cards.forEach((_, i) => {
                    const dot = document.createElement("div");
                    dot.className = "dot" + (i === current ? " active" : "");
                    dot.onclick = () => goToCard(i);
                    dotsEl.appendChild(dot);
                });
            }

            function updateCard() {
                document.getElementById("card").classList.remove("flipped");
                setTimeout(() => {
                    document.getElementById("front").childNodes[0].textContent = cards[current].question;
                    document.getElementById("back").childNodes[0].textContent = cards[current].answer;
                }, 300);
                document.getElementById("counter").textContent = (current + 1) + " / " + cards.length;
                renderDots();
            }

            function toggleFlip() {
                document.getElementById("card").classList.toggle("flipped");
            }

            function changeCard(dir) {
                current = (current + dir + cards.length) % cards.length;
                updateCard();
            }

            function goToCard(i) {
                current = i;
                updateCard();
            }

            updateCard();
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
    
    