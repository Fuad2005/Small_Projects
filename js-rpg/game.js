//variables
const player = document.getElementById('player')
const board = document.querySelector('.game')
const weapon = document.querySelector('.weapon')
let speed = 10
let playerPos = {
    x: parseInt(window.innerWidth / 2),
    y: parseInt(window.innerHeight / 2)
}
let playerVel = {
    x: 0,
    y: 0
}



//functions
function spawnCoin() {
    for(i=0; i<5; i++){
        const coin = document.createElement('div')
        coin.classList.add('coin')
        coin.style.top = Math.random() * 100 + '%'
        coin.style.left = Math.random() * 100 + '%'
        board.appendChild(coin)
    }
}

function run() {
    playerPos.x += playerVel.x
    playerPos.y += playerVel.y

    player.style.left = playerPos.x + 'px'
    player.style.top = playerPos.y + 'px'
    requestAnimationFrame(run)

}





function init() {
    spawnCoin()
    run()
}



init()


window.addEventListener('keydown', function(e){
    switch(e.key){
        case 'w': playerVel.y = -2; player.style.rotate = '0deg'; break;
        case 's': playerVel.y = 2; player.style.rotate = '180deg';break;
        case 'd': playerVel.x = 2; player.style.rotate = '90deg'; break;
        case 'a': playerVel.x = -2; player.style.rotate = '-90deg'; break;
    }
})
window.addEventListener('keyup', function(e){
    switch(e.key){
        case 'w': playerVel.y = 0; break;
        case 's': playerVel.y = 0; break;
        case 'd': playerVel.x = 0; break;
        case 'a': playerVel.x = 0; break;
    }
})

window.addEventListener('keypress', function(e){
    console.log(e.keyCode)
    if(e.keyCode===32){
        weapon.classList.add('attackAction')
        setTimeout(() => {
            weapon.classList.remove('attackAction')
        }, 100)
    }
})