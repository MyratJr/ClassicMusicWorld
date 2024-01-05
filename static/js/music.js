const playButton = document.querySelector(".play");
const pauseButton = document.querySelector(".pause");
const previousButton = document.querySelector(".previous");
const containerAudio = document.querySelector(".bashla");

playButton.addEventListener("click", () => {
    const audio = document.getElementById(`myAudio`);
    audio.play();
    playButton.style.display = "none";
    pauseButton.style.display = "block";
    containerAudio.style.display = "block";
    containerAudio.classList.add("animate-in");
});

previousButton.addEventListener("click", () => {
    let audio = document.getElementById(`myAudio`);
    audio.currentTime = 0;
    audio.play();
    playButton.style.display = "none";
    pauseButton.style.display = "block";
    containerAudio.style.display = "block";
    containerAudio.classList.add("animate-in");
});
pauseButton.addEventListener("click", () => {
    let audio = document.getElementById(`myAudio`);
    audio.pause();
    playButton.style.display = "block";
    pauseButton.style.display = "none";
    containerAudio.style.display = "none";
});