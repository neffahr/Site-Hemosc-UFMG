var bag_info = document.querySelectorAll("div[class*='bag-moreinfo-']");
var bags = document.querySelectorAll(".hc-img");

for (let i=0; i<bags.length; i++) {
    bags[i].addEventListener("click", () => {
        let info_on = bag_info[i].classList.contains("active");

        for (let other of bag_info) {
            console.log(other);
            if(other.classList.contains("active")) {
                other.classList.remove('active');
            }
        }

        if(!info_on){
            bag_info[i].classList.add('active');
        }else{
            bag_info[i].classList.remove('active');
        }
    })

    bag_info[i].addEventListener("click", () => {
        bag_info[i].classList.remove('active');
    })
}