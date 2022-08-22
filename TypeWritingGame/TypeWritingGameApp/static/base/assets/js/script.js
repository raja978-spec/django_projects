const timeEl = document.getElementById('time');
const difficultySelect = document.getElementById('difficulty');
const endgameEl = document.getElementById('end-game-container');
const settingsForm = document.getElementById('settings-form');
const stopper=document.getAnimations('Stop')
// Init time
let time = 0;

// Set difficulty to value in ls or medium
let difficulty =
  localStorage.getItem('difficulty') !== null
    ? localStorage.getItem('difficulty')
    : 'medium';

// Set difficulty select value
difficultySelect.value =
  localStorage.getItem('difficulty') !== null
    ? localStorage.getItem('difficulty')
    : 'medium';

// Focus on text on start
//text.focus();

// Start counting down
const timeInterval = setInterval(updateTime, 1000);

// Update time
function updateTime() {
  time--;
  timeEl.innerHTML = time + 's';

  if (time === 0) {
    clearInterval(timeInterval);
    // end game
    gameOver();
  }
}

// Game over, show end screen
function gameOver() {
  endgameEl.innerHTML = `
    <h1>Time ran out</h1>
  `;
  stopper.addEventListener('on')

}

if (difficulty === 'hard') {
  time += 60;
} else if (difficulty === 'medium') {
  time += 120;
} else {
  time += 240;
}
updateTime();

// Settings select
settingsForm.addEventListener('change', e => {
  difficulty = e.target.value;
  localStorage.setItem('difficulty', difficulty);
});
