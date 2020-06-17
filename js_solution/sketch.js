// Game of the life in Javascrip with P5.js
// by : @jadry 92


let nx = 50
let ny = 50
let compute = true
let fr = 5

let gameState = new Array(ny*nx)
for (let i = 0; i < ny*nx; i++) {
  gameState[i] = 0
}
// index  ix + iy * nx
gameState[5 + 3*nx] = 1
gameState[5 + 4*nx] = 1
gameState[5 + 5*nx] = 1

let newGameState = gameState.slice()

function setup() {
  createCanvas(500, 500);
  frameRate(fr)
}

function mousePressed(event) {
  if (mouseButton === LEFT) {
    if (mouseX < width && mouseY < height && mouseX >= 0 && mouseY >= 0){
      ix = floor((nx*mouseX)/width)
      iy = floor((ny*mouseY)/height)
      newGameState[ix + iy*nx] = 1
    }
  } else {
    if (mouseX < width && mouseY < height && mouseX >= 0 && mouseY >= 0){
      ix = floor((nx*mouseX)/width)
      iy = floor((ny*mouseY)/height)
      newGameState[ix + iy*nx] = 0
    }
  }
}

function keyTyped() {
  if (key === ' '){
    compute = !compute
  }
}


function draw() {
  for (let y = 0; y < ny; y++) {
    for (let x = 0; x < nx; x++) {
      if (compute){
        let totalNear = 0
        // add the values
        for (let i = 0; i < 9; i++) {
          if (i != 4) {
            const ix = (i % 3) - 1
            const iy = floor((i-ix) / 3) - 1
            totalNear += gameState[(x + ix) + (y + iy)*nx];
          }
        }


        // Rule #1: if the cell is dead and there are 3 cells alife close, will be revivie
        if (gameState[x + y*nx] === 0 && totalNear == 3) {
          newGameState[x + y*nx] = 1
        }
        else if (gameState[x + y*nx] === 1 && (totalNear < 2 || totalNear > 3)) {
          // Rule #2: if the cell is alive and there are less than two or more tha three cells alive, will be died
          newGameState[x + y*nx] = 0
        }
      }
      // Draw the base

      if (newGameState[x + y*nx] === 1) {
        fill(255,0,0)
        //noStroke()
        square((x*width/nx), (y*height/ny), width/nx);
      } else {
        fill(255,255,255)
        square((x*width/nx), (y*height/ny), width/nx);
      }
    }
  }
  gameState = newGameState.slice()
}
