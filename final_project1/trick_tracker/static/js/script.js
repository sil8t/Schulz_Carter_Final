function toggleNotes(notesId) {
    var notesElement = document.getElementById(notesId);
    if (notesElement.style.display === 'none' || !notesElement.style.display) {
        notesElement.style.display = 'block';
    } else {
        notesElement.style.display = 'none';
    }
}

function rollDice() {
    const stances = ['Regular', 'Switch', 'Nollie', 'Fakie'];
    const tricks = ['Ollie', 'Kickflip', 'Heelflip', 'Shuvit', '360 Flip'];
    const obstacles = ['Flatground', 'Ledge', 'Rail', 'Stairs'];

    const stance = stances[Math.floor(Math.random() * stances.length)];
    const trick = tricks[Math.floor(Math.random() * tricks.length)];
    const obstacle = obstacles[Math.floor(Math.random() * obstacles.length)];

    document.getElementById('diceResult').innerHTML = `<strong>Stance:</strong> ${stance}, <strong>Trick:</strong> ${trick}, <strong>Obstacle:</strong> ${obstacle}`;
}
