const setup = () => {

let AI_SIGN = "X"
let PLAYER_SIGN = "O"
let players_turn = true;
let finish = false
let spaces = document.getElementsByClassName("spaces");
let reset_button = document.getElementById("reset");
let end_text = document.getElementById("endtext");

const begin = () =>{
    for(let i = 0; i < spaces.length;  i++){
        spaces[i].style.color = "white";
        spaces[i].addEventListener("click",()=>move(i,PLAYER_SIGN,AI_SIGN))
    }
    reset_button.addEventListener("click",()=> reset_board())
    update_board()
}


const update_board = () => {
    console.log("update board")

    get_board()
        .then(async board =>{
            console.log(board);
            for (let i = 0; i < board.length; i++) {
                if(board[i] == "X"){
                    spaces[i].style.color = "red"
                }else if(board[i] == "O"){
                    spaces[i].style.color = "lightskyblue"
                }
                spaces[i].innerText = board[i];
                if(spaces[i].innerText == 0 ){
                    spaces[i].innerText = ""
                }
            }
            let end_value = await check_for_end()
            
            if(end_value == 1){
                end_text.innerText = "YOU WIN (how did you do this)"
                set_end_parameters()
            }else if(end_value == 0){
                end_text.innerText = "DRAW"
                set_end_parameters()
            }else if(end_value == -1){
                end_text.innerText = "YOU LOSE (try again)"
                set_end_parameters()
            }
        }
        ).catch(console.log("board_error"))
    ;
}

const set_end_parameters = () => {
    players_turn = false
    finish = true
}

const move = (index,player_sign, ai_sign) => {
    
    if(players_turn && finish == false){
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
                players_turn = false;
                check_for_end()
                ai_move(ai_sign,player_sign)
                
            } else {
                console.log("Move illegal");
            }}) 
        .catch(error => console.error('Error:', error));
        }

    

    
        
}

const ai_move = (ai_sign,player_sign) => {
    if (players_turn == false && finish == false){
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
                players_turn = true;
            }else{
                console.log("invalid move from ai")
            }
            }) 
        .catch(error => console.error('Error:', error));
    }
    
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

const reset_board = () => {
    params = {}
    return fetch('http://127.0.0.1:80/reset_board', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        reset_succesful = data.result

        if(reset_succesful){
            for(let i = 0; i < spaces.length;  i++){
                spaces[i].style.color = "white";
            }
            update_board();
            finish = false
            players_turn = true
            end_text.innerText = ""
        }
        
        }) 
    .catch(error => {console.error('Error:', error)
        throw error;
    });
}

async function check_for_end(player_sign){
    params = {player_sign: player_sign}
    return fetch('http://127.0.0.1:80/check_for_end', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        const end_value = data.result;
        return end_value
        }) 
    .catch(error => {console.error('Error:', error)
        throw error;
    });
}

begin()

}
window.addEventListener("load", setup);