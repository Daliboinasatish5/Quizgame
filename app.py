from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# A pool of 50 questions from different categories
questions_pool = [
    {"question": "Which cricket team has won the most ICC World Cups?", "a": "India", "b": "Australia", "c": "West Indies", "d": "England", "correct": "b"},
    {"question": "Who directed the movie 'Inception'?", "a": "Steven Spielberg", "b": "James Cameron", "c": "Christopher Nolan", "d": "Quentin Tarantino", "correct": "c"},
    {"question": "What is the capital of France?", "a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome", "correct": "c"},
    {"question": "Which planet is known as the Red Planet?", "a": "Earth", "b": "Jupiter", "c": "Mars", "d": "Venus", "correct": "c"},
    {"question": "Which programming language is known as the language of the web?", "a": "Python", "b": "C++", "c": "JavaScript", "d": "Java", "correct": "c"},
    {"question": "What is the capital of Germany?", "a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome", "correct": "a"},
    {"question": "Which cricket player is known as the Master Blaster?", "a": "Virat Kohli", "b": "Brian Lara", "c": "Sachin Tendulkar", "d": "Ricky Ponting", "correct": "c"},
    {"question": "Who played the character of Jack in Titanic?", "a": "Brad Pitt", "b": "Tom Cruise", "c": "Leonardo DiCaprio", "d": "Matt Damon", "correct": "c"},
    {"question": "Which element has the chemical symbol 'O'?", "a": "Oxygen", "b": "Gold", "c": "Silver", "d": "Iron", "correct": "a"},
    {"question": "Who wrote 'Pride and Prejudice'?", "a": "Charlotte Bronte", "b": "Jane Austen", "c": "George Eliot", "d": "Virginia Woolf", "correct": "b"},
    # ... add more questions here to make it a pool of 50 questions ...
]

@app.route('/')
def enter():
    return render_template('enter.html')

@app.route('/quiz')
def quiz():
    return render_template('index.html')

@app.route('/quiz_data')
def quiz_data():
    selected_questions = random.sample(questions_pool, 5)
    questions_with_index = [{'index': questions_pool.index(q), **q} for q in selected_questions]
    return jsonify(questions_with_index)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_index = data['question_index']
    answer = data['answer']
    correct_answer = questions_pool[question_index]['correct']
    is_correct = (answer == correct_answer)
    return jsonify({'correct': is_correct})

@app.route('/results')
def results():
    score = request.args.get('score', 0, type=int)
    return render_template('results.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
