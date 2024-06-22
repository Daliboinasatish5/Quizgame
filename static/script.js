let questions = [];
let currentQuestion = 0;
let score = 0;

document.addEventListener('DOMContentLoaded', (event) => {
    loadQuiz();
});

function loadQuiz() {
    fetch('/quiz_data')
        .then(response => response.json())
        .then(data => {
            questions = data;
            displayQuestion();
        });
}

function displayQuestion() {
    if (currentQuestion < questions.length) {
        const currentQuizData = questions[currentQuestion];
        document.getElementById('quiz').innerHTML = `
            <div class="question">${currentQuizData.question}</div>
            <ul class="answers">
                <li>
                    <input type="radio" name="answer" id="a" value="a">
                    <label for="a">${currentQuizData.a}</label>
                </li>
                <li>
                    <input type="radio" name="answer" id="b" value="b">
                    <label for="b">${currentQuizData.b}</label>
                </li>
                <li>
                    <input type="radio" name="answer" id="c" value="c">
                    <label for="c">${currentQuizData.c}</label>
                </li>
                <li>
                    <input type="radio" name="answer" id="d" value="d">
                    <label for="d">${currentQuizData.d}</label>
                </li>
            </ul>
        `;
    } else {
        showResults();
    }
}

document.getElementById('submit').addEventListener('click', () => {
    const answer = document.querySelector('input[name="answer"]:checked');
    if (answer) {
        checkAnswer(answer.value);
    } else {
        alert("Please select an answer before submitting.");
    }
});

function checkAnswer(answer) {
    fetch('/check_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            question_index: questions[currentQuestion].index,
            answer: answer
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.correct) {
            score++;
        }
        currentQuestion++;
        displayQuestion();
    });
}

function showResults() {
    window.location.href = `/results?score=${score}`;
}




