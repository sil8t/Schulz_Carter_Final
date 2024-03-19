function toggleNotes(notesId) {
    var notesElement = document.getElementById(notesId);
    if (notesElement.style.display === 'none') {
        notesElement.style.display = 'block';
    } else {
        notesElement.style.display = 'none';
    }
}
