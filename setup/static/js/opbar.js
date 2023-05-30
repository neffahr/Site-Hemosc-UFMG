var opicon = document.querySelector(".icons-options");
var opbar = document.querySelector(".options-bar-hidden");

opicon.addEventListener("click", () => {
    opicon.classList.toggle("active");
    opbar.classList.toggle("active");
})

document.querySelectorAll(".op-div").forEach(n => n.addEventListener("click", () => {
    opicon.classList.toggle("active");
    opbar.classList.toggle("active");
}))