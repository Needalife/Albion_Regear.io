document.addEventListener('DOMContentLoaded', () => {
    const modeToggle = document.getElementById('toggle-mode');
    const body = document.body;

    modeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
    });
});
