function getComputerChoice( ) {
    let rpsChoices = ['Rock', 'Paper', 'Scissors']
    let computerChoice = rpsChoices[Math.floor(Math.random() * 3)]
    return computerChoice
}

// Game Algorithm(Conditionals)
function getResult(playerChoice, computerChoice) {
    // score result return based on win, draw, or loss
    
    let score;

    // All situations where human draws, set `score` to 0
    if (playerChoice === computerChoice) {
      score = 0  
    } else if (playerChoice === 'Rock' && computerChoice === 'Scissors') {
      score = 1
    } else if (playerChoice === "Paper" && computerChoice === "Rock") {
      score = 1
    } else if (playerChoice === "Scissors" && computerChoice === "Paper") {
      score = 1
    } else {
    // Otherwise human loses (aka set score to -1)  
      score = -1
}
}

/*
CUI Interface
*/
// console.log(getComputerChoice())
// let playerChoice= prompt("Enter your choice(Rock,Paper,Scissor): ")

// console.log(playerChoice)

// console.log(getResult())

function showResult (score, playerChoice, computerChoice) {
    
    let result = document.getElementById('result')

    switch(score){
        case -1:
            result.innerText = `You Lose!`
            break;
        case 0:
            result.innerText = `It's a Draw!`
            break;
        case 1:
            result.innerText = `You Win!`
            break;
    }
}
