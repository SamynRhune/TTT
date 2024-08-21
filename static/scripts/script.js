const setup = () => {

const AI_SIGN = "X"
const PLAYER_SIGN = "O"
let spaces = document.getElementsByClassName("spaces");

for(let i = 0; i < spaces.length;  i++){
    spaces[i].style.color = "white";
    spaces[i].addEventListener("click",()=>move(i,PLAYER_SIGN,AI_SIGN))
    spaces[i].addEventListener('contextmenu', function(ev) {
        ev.preventDefault();
        move(i,AI_SIGN)
        return false;
    }, false);
    

}

const update_board = () => {
    console.log("update board")

    get_board()
        .then(board =>{
            console.log(board);
            for (let i = 0; i < board.length; i++) {
                spaces[i].innerText = board[i];
                if(spaces[i] != 0 ){
                    spaces[i].style.color = "black"
                }
            }
        }
        ).catch(console.log("board_error"))
    ;
}

const move = (index,player_sign, ai_sign) => {
    
    params = {index : index,
              sign : player_sign
            }
    

    fetch('http://127.0.0.1:80/player_move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        valid_move = data.result; 
    

        if (valid_move) {
            //spaces[index].innerText = player_sign;
            update_board()
            ai_move(ai_sign,player_sign)
            
        } else {
            console.log("Move illegal");
        }}) 
    .catch(error => console.error('Error:', error));

    
        
}

const ai_move = (ai_sign,player_sign) => {
    params = {ai_sign : ai_sign,
        player_sign : player_sign
      }

    fetch('http://127.0.0.1:80/ai_move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        valid_move = data.result;  
        
        if(valid_move){
            update_board()
        }else{
            console.log("invalid move from ai")
        }
        }) 
    .catch(error => console.error('Error:', error));
}

const get_board = () => {
    params = {}
    return fetch('http://127.0.0.1:80/get_board', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        const board = data.result;
        return board
        }) 
    .catch(error => {console.error('Error:', error)
        throw error;
    });
}



}
window.addEventListener("load", setup);