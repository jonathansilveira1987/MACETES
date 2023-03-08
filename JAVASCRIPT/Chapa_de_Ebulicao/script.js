let brickRowCount = 4;
let brickCloumnCount = 7;
let brickWidth = 72;
let brickHeight = 24;
let brickPadding = 12;
let brickOffsetTop = 32;
let brickOffsetLeft = 32;
//Create variables to take score
let score = 0;

//Creating arrays for the bricks
let bricks = [];
for (c = 0; c < brickCloumnCount; c++) {
    bricks[c] = [];
    for (r = 0; r < brickRowCount; r++) {
        //set the x and y position of the 
        bricks[c][r] = { x: 0, y: 0, status: 1 };
    }
}

document.addEventListener('keydown', keyDownHandler, false);
document.addEventListener('keyup', keyUpHandler, false);
document.addEventListener('mousemove', mouseMoveHandler, false);

function keyDownHandler(e) {
    if (e.keyCode === 39) {
        rightPressed = true;
    }
    else if (e.keyCode === 37) {
        leftPressed = true;
    }
}

function keyUpHandler(e) {
    if (e.keyCode === 39) {
        rightPressed = false;
    }
    else if (e.keyCode === 37) {
        leftPressed = false;
    }
}