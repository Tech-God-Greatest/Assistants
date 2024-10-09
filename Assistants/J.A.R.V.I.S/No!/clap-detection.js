const startButton = document.getElementById('start');
const statusText = document.getElementById('status');
let audioContext, microphone, analyser, dataArray, bufferLength;
let clapLastDetectedAt = 0;
const CLAP_THRESHOLD = 250; // Adjust for sensitivity
const CLAP_DELAY = 550; // Minimum time between claps (in ms)

startButton.addEventListener('click', () => {
    startClapDetection();
});

function startClapDetection() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            audioContext = new (window.AudioContext || window.webkitAudioContext)();
            microphone = audioContext.createMediaStreamSource(stream);
            analyser = audioContext.createAnalyser();
            analyser.fftSize = 2048;
            bufferLength = analyser.frequencyBinCount;
            dataArray = new Uint8Array(bufferLength);
            microphone.connect(analyser);
            detectClap();
            statusText.innerHTML = "Listening for claps...";
        })
        .catch(err => {
            console.error('Microphone access denied:', err);
            statusText.innerHTML = "Microphone access denied!";
        });
}

function detectClap() {
    analyser.getByteTimeDomainData(dataArray);
    let maxAmplitude = Math.max(...dataArray);

    let now = Date.now();

    // Check for a strong enough amplitude spike (possible clap)
    if (maxAmplitude > CLAP_THRESHOLD && (now - clapLastDetectedAt) > CLAP_DELAY) {
        clapLastDetectedAt = now;
        clapDetected();
    }

    requestAnimationFrame(detectClap); // Keep checking
}

function clapDetected() {
    statusText.innerHTML = "Clap detected!";
    console.log("Clap detected at", new Date());
    
    // Reset status after 1 second
    setTimeout(() => {
        statusText.innerHTML = "Listening for claps...";
    }, 1000);
}