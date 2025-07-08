// variables
const cell1 = document.querySelector('.cell-1');
const cell2 = document.querySelector('.cell-2');
const cell3 = document.querySelector('.cell-3');
const cell4 = document.querySelector('.cell-4');
const cell5 = document.querySelector('.cell-5');
const cell6 = document.querySelector('.cell-6');
const cell7 = document.querySelector('.cell-7');
const cell8 = document.querySelector('.cell-8');
const cell9 = document.querySelector('.cell-9');
const resetButton = document.querySelector('.reset-button');
let cell1Value = ''
let cell2Value = ''
let cell3Value = ''
let cell4Value = ''
let cell5Value = ''
let cell6Value = ''
let cell7Value = ''
let cell8Value = ''
let cell9Value = ''


//conditions
let player = 'X';


// controls
function func1 () {
    if (player === 'X') {
        cell1.classList.add('red');
        cell1Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell1Value)
    }
    else {
        cell1.classList.add('green');
        cell1Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell1Value)
    }
}
function func2 () {
    if (player === 'X') {
        cell2.classList.add('red');
        cell2Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell2Value)
    }
    else {
        cell2.classList.add('green');
        cell2Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell2Value)
    }
}
function func3 () {
    if (player === 'X') {
        cell3.classList.add('red');
        cell3Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell3Value)
    }
    else {
        cell3.classList.add('green');
        cell3Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell3Value)
    }
}
function func4 () {
    if (player === 'X') {
        cell4.classList.add('red');
        cell4Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell4Value)
    }
    else {
        cell4.classList.add('green');
        cell4Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell4Value)
    }
}
function func5 () {
    if (player === 'X') {
        cell5.classList.add('red');
        cell5Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell5Value)
    }
    else {
        cell5.classList.add('green');
        cell5Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell5Value)
    }
}
function func6 () {
    if (player === 'X') {
        cell6.classList.add('red');
        cell6Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell6Value)
    }
    else {
        cell6.classList.add('green');
        cell6Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell6Value)
    }
}
function func7 () {
    if (player === 'X') {
        cell7.classList.add('red');
        cell7Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell7Value)
    }
    else {
        cell7.classList.add('green');
        cell7Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell7Value)
    }
}
function func8 () {
    if (player === 'X') {
        cell8.classList.add('red');
        cell8Value = 'X'
        player = 'O'
        console.log('player '+player+ ' cell '+ cell8Value)
    }
    else {
        cell8.classList.add('green');
        cell8Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell8Value)
    }
}
function func9 () {
    if (player === 'X') {
        cell9.classList.add('red');
        cell9Value = 'X'
        player = 'O'  
        console.log('player '+player+ ' cell '+ cell9Value) 
    }
    else {
        cell9.classList.add('green');
        cell9Value = 'O'
        player = 'X'
        console.log('player '+player+ ' cell '+ cell9Value)
    }
}


cell1.addEventListener('click', func1);
cell2.addEventListener('click', func2);
cell3.addEventListener('click', func3);
cell4.addEventListener('click', func4);
cell5.addEventListener('click', func5);
cell6.addEventListener('click', func6);
cell7.addEventListener('click', func7);
cell8.addEventListener('click', func8);
cell9.addEventListener('click', func9);




//reset
function reset () {
    cell1.classList.remove('red');
    cell1.classList.remove('green');
    cell2.classList.remove('red');
    cell2.classList.remove('green');
    cell3.classList.remove('red');
    cell3.classList.remove('green');
    cell4.classList.remove('red');
    cell4.classList.remove('green');
    cell5.classList.remove('red');
    cell5.classList.remove('green');
    cell6.classList.remove('red');
    cell6.classList.remove('green');
    cell7.classList.remove('red');
    cell7.classList.remove('green');
    cell8.classList.remove('red');
    cell8.classList.remove('green');
    cell9.classList.remove('red');
    cell9.classList.remove('green');
}
resetButton.addEventListener('click', reset);



//winning conditions

if(cell1Value==='X' && cell2Value==='X' && cell3Value==='X') {
    console.log('X wins');
}