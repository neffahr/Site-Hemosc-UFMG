var button1 = document.querySelector(".search-icon");
var button2 = document.querySelector(".search-icon-hidden");
var search = document.querySelector(".search-form");
var input = document.querySelector(".search-input");
var login_btn = document.querySelector(".page-login");

// Add event listener
button1.addEventListener("click", ()=>{
    // Checks if element has search bar enabled
    let enabledSearchBar = search.classList.contains("search-active");
    // If not, adds class and remove hidden status, else removes it and add hidden status.
    if(!enabledSearchBar){
        input.removeAttribute("hidden");
        button2.removeAttribute("hidden");
        button1.setAttribute("hidden", "hidden");
        login_btn.setAttribute("hidden", "hidden");
        search.classList.add("search-active");
    }else{
        input.setAttribute("hidden", "hidden");
        button1.removeAttribute("hidden");
        button2.setAttribute("hidden", "hidden");
        button1.removeAttribute("hidden");
        search.classList.remove("search-active");
    }
})