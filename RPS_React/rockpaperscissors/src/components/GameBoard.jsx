import React from 'react'
import './GameBoard.css'
import rock from '../imgs/rock.png'
import paper from '../imgs/paper.png'
import scissors from '../imgs/scissors.png'
import rock2 from '../imgs/rock2.png'
import paper2 from '../imgs/paper2.png'
import scissors2 from '../imgs/scissors2.png'

function GameBoard() {

    const [player1, setPlayer1] = React.useState(1)
    const [player2, setPlayer2] = React.useState(1)
    const [p1Icon, setP1Icon] = React.useState(null)
    const [p2Icon, setP2Icon] = React.useState(null)
    const inputRef = React.useRef(null)
    const [p1Score, setP1Score] = React.useState(0)
    const [p2Score, setP2Score] = React.useState(0)
    React.useEffect(() => {
        if (player1 === 1) {
            setP1Icon(rock)
        } else if (player1 === 2) {
            setP1Icon(paper)
        } else if (player1 === 3) {
            setP1Icon(scissors)
        }
        if (player2 === 1) {
            setP2Icon(rock2)
        } else if (player2 === 2) {
            setP2Icon(paper2)
        } else if (player2 === 3) {
            setP2Icon(scissors2)
        }
    }, [player1, player2])

    const winConditionCheck = React.useCallback((p1, p2) => {
        if (p1 === 1 && p2 === 3) {
            setP1Score(p1Score + 1)
        } else if (p1 === 2 && p2 === 1) {
            setP1Score(p1Score + 1)
        } else if (p1 === 3 && p2 === 2) {
            setP1Score(p1Score + 1)
        } else if (p1 === 1 && p2 === 2) {
            setP2Score(p2Score + 1)
        } else if (p1 === 2 && p2 === 3) {
            setP2Score(p2Score + 1)
        } else if (p1 === 3 && p2 === 1) {
            setP2Score(p2Score + 1)
        } else {
            console.log('draw')
        }
    }, [p1Score, p2Score])

    const playerInputHandler = React.useCallback((value) => {
        setPlayer1(value)

        for(let i = 0; i < 50; i++) {
            setTimeout(() => {
                setPlayer2(Math.floor(Math.random() * 3) + 1)
            }, 20 * i)
        }

        inputRef.current.style.display = 'none'
        setTimeout(() => {
        inputRef.current.style.display = 'flex'
        }, 1000)
        setTimeout(() => {
            console.log(player1, player2)
            winConditionCheck(player1, player2)
        }, 1000)
    }, [winConditionCheck, player1, player2])

  return (
    <>
    
    <div className="game-box">
        
        <div className="player1">
            <img src={p1Icon} alt="rock" />
        </div>

        <div className='p1-score'>{p1Score}</div>
        <div className='p2-score'>{p2Score}</div>

        <div className="player2">
            <img src={p2Icon} alt="rock2" />
        </div>
    </div>
    <div ref={inputRef} className='input-box'>
        <div className='p1-input' onClick={() =>{playerInputHandler(1)}}><img src={rock} alt='rock'/></div>
        <div className='p1-input' onClick={() =>{playerInputHandler(2)}}><img src={paper} alt='paper'/></div>
        <div className='p1-input' onClick={() =>{playerInputHandler(3)}}><img src={scissors} alt='scissors'/></div>
    </div>
    </>

  )
}

export default GameBoard