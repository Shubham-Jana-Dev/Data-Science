const prompt = require('prompt-sync')();
function getRandomInt(min, max){
   return Math.floor(Math.random() * (max - min + 1)) + min; 
}

const Cturn = getRandomInt(1,3);
let turn = parseInt(prompt("Enter 1 for stone, 2 for paper, 3 for scissor :-)"))
console.log("You: ",turn);
console.log("Computer: ",Cturn);
if(turn == Cturn){
    console.log("Draw.... :|")

} else if( turn == 1 && Cturn == 2){
    console.log("You win... :)");
}else if( Cturn == 1 && turn == 2){
    console.log("Computer win... :(");
}else if( Cturn == 3 && turn == 2){
    console.log("Computer win... :(");
}else if( turn == 3 && Cturn == 2){
    console.log("You win... :)");
}else if( turn == 3 && Cturn == 1){
    console.log("You win... :)");
}else{
    console.log("Computer win... :(");
}