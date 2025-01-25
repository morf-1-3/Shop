let categoriesBut = document.querySelector('#dropdown-button')
function categoriesOpen(event){
    event.stopPropagation();
    const backgroundMenu = document.querySelector(".background-menu")
    backgroundMenu.classList.add("active")
    const caregoriesMenu = document.querySelector('.categories-menu')
    caregoriesMenu.addEventListener('click', categoriesOpen)
    
}   
categoriesBut.addEventListener('click', categoriesOpen)


function categoriesClose(event){
    event.stopPropagation();
    const backgroundMenu = document.querySelector(".background-menu")

    // categoriesBut.addEventListener('click', categoriesOpen)
    backgroundMenu.classList.remove('active')
    

}
document.addEventListener('click',categoriesClose)
// let categoriesBut = document.querySelector('#dropdown-button')
// function categoriesOpen(event){
//     event.stopPropagation();
//     const caregoriesMenu = document.querySelector(".categories-menu")
//     caregoriesMenu.classList.add("active")
//     caregoriesMenu.addEventListener('click', categoriesOpen)
    
// }   
// categoriesBut.addEventListener('click', categoriesOpen)


// function categoriesClose(event){
//     event.stopPropagation();
//     const caregoriesMenu = document.querySelector(".categories-menu")

//     // categoriesBut.addEventListener('click', categoriesOpen)
//     caregoriesMenu.classList.remove('active')
    

// }
// document.addEventListener('click',categoriesClose)
