#!/usr/bin/env node
// Generates all quiz HTML files from the template and quiz data
const fs = require('fs');
const path = require('path');

const TEMPLATE = fs.readFileSync(path.join(__dirname, 'quiz-template.html'), 'utf8');
const QUIZZES = require('./quiz-data.json');

for (const quiz of QUIZZES) {
  const html = TEMPLATE
    .replace(/\{\{QUIZ_TITLE\}\}/g, quiz.title)
    .replace(/\{\{CX_LIFECYCLE\}\}/g, quiz.cx_lifecycle)
    .replace(/\{\{DIFFICULTY\}\}/g, quiz.difficulty)
    .replace(/\{\{QUESTION_COUNT\}\}/g, String(quiz.questions.length))
    .replace(/\{\{DIFFICULTY_SHORT\}\}/g, quiz.difficulty_short)
    .replace('{{QUIZ_DATA_JSON}}', JSON.stringify({ title: quiz.title, questions: quiz.questions }, null, 2));

  const outPath = path.join(__dirname, quiz.filename);
  fs.writeFileSync(outPath, html);
  console.log(`Created: ${quiz.filename} (${quiz.questions.length} questions)`);
}

console.log(`\nDone! Generated ${QUIZZES.length} quiz files.`);
