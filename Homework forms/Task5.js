function addQuestion(event) {
    event.preventDefault();
    let questionInput = document.getElementById('questionInput');
    let corAnswerInput = document.getElementById('corAnswerInput');
    let wrAnswerInput = document.getElementById('wrAnswerInput');


    let listItem = document.createElement('li');
    let question = document.createElement('div');
    let corAnswer = document.createElement('div');
    let wrAnswer = document.createElement('div');


    question.textContent = 'Question: ' + questionInput.value;
    corAnswer.textContent = 'Correct answer: ' + corAnswerInput.value;
    wrAnswer.textContent = 'Wrong answer: ' + wrAnswerInput.value;


    listItem.appendChild(question);
    listItem.appendChild(corAnswer);
    listItem.appendChild(wrAnswer);


    let questionList = document.getElementById('questionList');
    questionList.appendChild(listItem);

    questionInput.value = '';
    corAnswerInput.value = '';
    wrAnswerInput.value = '';
    return false;
}
