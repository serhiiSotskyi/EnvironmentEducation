

// Array of questions, each containing a question text and an array of answers with correctness flags.
const questions = [
    {
        question: "Which is largest animal in the world?",
        answers: [
            { text: "Shark", correct: false},
            { text: "Blue whale", correct: true},
            { text: "Elephant", correct: false},
            { text: "Giraffe", correct: false}
        ]
    },
    {
        question: "Which is largest animal in the world?",
        answers: [
            { text: "Shark", correct: false},
            { text: "Blue whale", correct: true},
            { text: "Elephant", correct: false},
            { text: "Giraffe", correct: false}
        ]
    },
    {
        question: "Which is largest animal in the world?",
        answers: [
            { text: "Shark", correct: false},
            { text: "Blue whale", correct: true},
            { text: "Elephant", correct: false},
            { text: "Giraffe", correct: false}
        ]
    },
    {
        question: "Which is largest animal in the world?",
        answers: [
            { text: "Shark", correct: false},
            { text: "Blue whale", correct: true},
            { text: "Elephant", correct: false},
            { text: "Giraffe", correct: false}
        ]
    }
];

// Get references to DOM elements
const questionElement = document.getElementById("question");  // The element that displays the question
const answerButton = document.getElementById("answer-buttons");  // The container for answer buttons
const nextButton = document.getElementById("next-btn");  // The button to move to the next question

console.log(answerButton)
let currentQuestionIndex = 0;  // Index to keep track of the current question
let score = 0;  // Variable to keep track of the user's score

// Function to start the quiz
function startQuiz(){
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerHTML = "Next";
    showQuestion();
}

// Function to display a question
function showQuestion(){
    resetState();  // Clear previous state

    // Get the current question object
    let currentQuestion = questions[currentQuestionIndex];

    // Calculate the question number
    let questionNo = currentQuestionIndex + 1;

    // Set the question text in the HTML
    questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

    // Create buttons for each answer
    currentQuestion.answers.forEach(answer => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        answerButton.appendChild(button);

        // Set a data attribute to mark correct answers
        if(answer.correct){
            button.dataset.correct = answer.correct;
        }

        // Attach an event listener for when the button is clicked
        button.addEventListener("click", selectAnswer);
    });
}

// Function to clear the state (e.g., after displaying a question)
function resetState(){
    nextButton.style.display = "none";  // Hide the 'Next' button
    while(answerButton.firstChild){
        answerButton.removeChild(answerButton.firstChild);  // Clear answer buttons
    }
}

// Function to handle when an answer is selected
function selectAnswer(e){
    const selectBtn = e.target;
    const isCorrect = selectBtn.dataset.correct === "true";  // Check if the selected answer is correct

    // Add classes based on correctness
    if(isCorrect){
        selectBtn.classList.add("correct");
        score++;  // Increment score for correct answers
    }
    else{
        selectBtn.classList.add("incorrect");
    }

    // Disable all answer buttons and mark correct answers
    Array.from(answerButton.children).forEach(button => {
        if(button.dataset.correct === "true"){
            button.classList.add("correct");
        }
        button.disabled = true;
    });

    nextButton.style.display = "block";  // Display the 'Next' button
}

// Function to display the final score
function showScore(){
    resetState();
    questionElement.innerHTML = `You scored ${score} out of ${questions.length}`;
    nextButton.innerHTML = "Play Again";
    nextButton.style.display = "block";
}

// Function to handle the 'Next' button click
function handleNextButton(){
    currentQuestionIndex++;
    if(currentQuestionIndex < questions.length){
        showQuestion();
    } else{
        showScore();
    }
}
console.log(nextButton);
// Attach event listener to the 'Next' button
nextButton.addEventListener("click", ()=>{
    if(currentQuestionIndex < questions.length){
        handleNextButton();
    } else{
        startQuiz();
    }
});
console.log(nextButton);

startQuiz();
