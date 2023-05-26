var button1 = document.querySelector(".search-icon");
var button2 = document.querySelector(".search-icon-hidden");
var search = document.querySelector(".search-form");
var input = document.querySelector(".search-input");
var cancel = document.querySelector(".cancel-icon");
var login_btn = document.querySelector(".page-login");

// Add event listener
button1.addEventListener("click", ()=>{
    // Checks if element has search bar enabled
    let enabledSearchBar = search.classList.contains("active");
    // If not, adds class and remove hidden status, else removes it and add hidden status.
    if(!enabledSearchBar){
        button2.removeAttribute("hidden");
        button1.setAttribute("hidden", "hidden");
        input.removeAttribute("hidden");
        cancel.removeAttribute("hidden");
        login_btn.setAttribute("hidden", "hidden");
    }else{
        button1.removeAttribute("hidden");
        button2.setAttribute("hidden", "hidden");
        input.setAttribute("hidden", "hidden");
        cancel.setAttribute("hidden", "hidden");
        login_btn.removeAttribute("hidden");
    }
    search.classList.toggle('active');
})

cancel.addEventListener("click", ()=>{
    search.classList.toggle('active');
    button1.removeAttribute("hidden");
    button2.setAttribute("hidden", "hidden");
    input.setAttribute("hidden", "hidden");
    cancel.setAttribute("hidden", "hidden");
    login_btn.removeAttribute("hidden");
})