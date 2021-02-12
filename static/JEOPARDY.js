let topicNum = 0;
let questionNum = 0;
let currentPoint = 0;
let currentLetter = 0;
let timer = null;

//Array that saves all questions and answers
const Http = new XMLHttpRequest();
const url = "/posts";
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {};

function displayQuestion() {
  if (timer != null) {
    clearInterval(timer);
  }

  currentLetter = 0;

  let topic = document.getElementById("topic-name");
  topic.innerHTML = "თემა: " + data[topicNum].name;

  let point = document.getElementById("point");
  point.innerHTML = "ქულა: " + (questionNum + 1) * 10;

  let button = document.getElementById("bigRedButton");
  button.style.display = "block";

  let input = document.getElementById("answer");
  input.style.display = "none";

  let answerButton = document.getElementById("button-1");
  answerButton.style.display = "none";

  timer = setInterval(displayLetters, 50);
}

function handleAnswer() {
  let answer = document.getElementById("answer").value;

  document.getElementById("answer").value = "";

  //Count points of the players
  if (answer == data[topicNum].questions[questionNum].answer) {
    currentPoint = currentPoint + (questionNum + 1) * 10;
  } else {
    currentPoint = currentPoint - (questionNum + 1) * 10;
  }

  //Add new li elemen to the ul element
  let node = document.createElement("li");
  let textnode = document.createTextNode(currentPoint);
  node.appendChild(textnode);
  document.getElementById("playes-1-points").appendChild(node);

  //Change the number of topic or the number of question
  if (questionNum == data[topicNum].questions.length - 1) {
    topicNum += 1;
    questionNum = 0;
  } else {
    questionNum += 1;
  }

  displayQuestion();
}

function displayLetters() {
  let question = document.getElementById("question");
  question.innerHTML = data[topicNum].questions[questionNum].question.substr(
    0,
    currentLetter
  );
  currentLetter += 1;
}

function handleStop() {
  if (timer != null) {
    clearInterval(timer);
  }
  let button = document.getElementById("bigRedButton");
  button.style.display = "none";

  let input = document.getElementById("answer");
  input.style.display = "block";

  let answerButton = document.getElementById("button-1");
  answerButton.style.display = "block";
}
