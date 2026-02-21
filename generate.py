#!/usr/bin/env python3
"""Generates all quiz HTML files from the template and quiz data."""
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, 'quiz-template.html'), 'r') as f:
    TEMPLATE = f.read()

with open(os.path.join(DIR, 'quiz-data.json'), 'r') as f:
    QUIZZES = json.load(f)

for quiz in QUIZZES:
    quiz_json = json.dumps({
        'title': quiz['title'],
        'questions': quiz['questions']
    }, indent=2)

    html = TEMPLATE
    html = html.replace('{{QUIZ_TITLE}}', quiz['title'])
    html = html.replace('{{CX_LIFECYCLE}}', quiz['cx_lifecycle'])
    html = html.replace('{{DIFFICULTY}}', quiz['difficulty'])
    html = html.replace('{{QUESTION_COUNT}}', str(len(quiz['questions'])))
    html = html.replace('{{DIFFICULTY_SHORT}}', quiz['difficulty_short'])
    html = html.replace('{{QUIZ_DATA_JSON}}', quiz_json)

    out_path = os.path.join(DIR, quiz['filename'])
    with open(out_path, 'w') as f:
        f.write(html)

    print(f"Created: {quiz['filename']} ({len(quiz['questions'])} questions)")

print(f"\nDone! Generated {len(QUIZZES)} quiz files.")
