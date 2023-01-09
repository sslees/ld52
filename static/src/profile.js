const end = new Date("2023-01-27T20:00:00Z");

let cd_days = document.getElementById("cd_days");
let cd_hrs = document.getElementById("cd_hrs");
let cd_min = document.getElementById("cd_min");
let cd_sec = document.getElementById("cd_sec");

function tick() {
    seconds = Math.round((end.valueOf() - new Date().valueOf()) / 1000);

    cd_sec.style.setProperty("--value", seconds % 60)
    cd_min.style.setProperty("--value", Math.floor(seconds / 60) % 60)
    cd_hrs.style.setProperty("--value", Math.floor(seconds / 3600) % 24)
    cd_days.style.setProperty("--value", Math.floor(seconds / 86400))
}

window.localStorage.setItem("profile", window.location.href);
tick()
setInterval(tick, 1000)
