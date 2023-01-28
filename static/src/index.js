let in_name = document.getElementById('in_name');
let btn_join = document.getElementById('btn_join');

in_name.addEventListener("input", function () {
    btn_join.disabled = !this.value.trim();
})
in_name.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        btn_join.click();
    }
});

const registerUser = async (userid) => {
    await fetch("/register", {
        method: "POST",
        body: JSON.stringify({
            "id": userid,
            "name": in_name.value.trim()
        }),
        headers: {
            "Content-Type": "application/json"
        }
    });
    window.location.href = "/profile/" + userid;
}

let profile = localStorage.getItem("profile");

if (profile !== null) {
    window.location.href = profile
}
