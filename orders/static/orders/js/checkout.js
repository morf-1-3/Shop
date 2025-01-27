const searchCity = document.querySelector('#city_search')
// searchCity.focus();
function openScroll(event){
    event.stopPropagation();
    const scroll = document.querySelector('.scroll-element')
    scroll.classList.add('active')
    scroll.addEventListener('click', openScroll)
    if(searchCity.value.length>0){
        search_set = searchCity.value + "/"
    }
    else{
        search_set = ""
    }
    
    // if(searchCity.value.length>0){
        $.ajax({
            url: `/order/nova-posta/${search_set}`,         
            method: 'GET', 
            // headers: {'X-CSRFTOKEN': csrf},               
            success: function(data){   
                // alert(data.html)
                const scroll = document.querySelector('.scroll-element')
                scroll.innerHTML = data.html
            }
        });
}

searchCity.addEventListener('click', openScroll)


// function fillCity(event){
//     alert("ss")
//     const target = event.target
//     alert("click")
//     const id = target.id
//     searchCity.value = target.textContent
//     // const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
// }
// const searchLi = document.querySelectorAll('.scroll-element li')

// searchLi.forEach((item)=>{
//     item.addEventListener('click', fillCity)
// })
document.addEventListener('DOMContentLoaded', function() {
    const cityList = document.querySelector('.scroll-element');
    
    function fillCity(event) {
        const target = event.target;
        if (target.tagName.toLowerCase() === 'li') {
            
            searchCity.value = target.textContent;
            const inputWarehouse = document.querySelector('.warehouse_cearch')
            
            if(inputWarehouse){
                inputWarehouse.removeAttribute('disabled')
                inputWarehouse.id = target.id
                     
                
            }
            else{
                alert("error")
            }
            

        }
    }

    cityList.addEventListener('click', fillCity);
});


function closeScroll(event){
    event.stopPropagation();
    const scroll = document.querySelector('.scroll-element')
    scroll.classList.remove('active')
}
document.addEventListener('click',closeScroll)

scrollLiElements = document.querySelectorAll(".scroll-element li")
scrollLiElements.forEach((item) =>{
    item.addEventListener('click',closeScroll)
})
let lastValue = '';
let timeoutId = null;
let preventTyping = false;
function keyInputCity(event){
    const inputKeyValue = event.key;
    const allowedKey = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', 
        'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я',
        " "];
    const specialKeys = ['Backspace', 'Tab', 'Enter', 'Shift', 'Control', 'Alt', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'];
    // const specialKeys = [" "];

    if(!allowedKey.includes(inputKeyValue) && !specialKeys.includes(inputKeyValue)){
        event.preventDefault();
        if (preventTyping) return; 
        const current_value = searchCity.value;
        searchCity.value = current_value + inputKeyValue
        if (timeoutId) {
            clearTimeout(timeoutId); 
        }
        timeoutId = setTimeout(()=>{
            searchCity.value = lastValue
            preventTyping = false
            },50
        )
        preventTyping = true
    }
    else if (specialKeys.includes(inputKeyValue)) {
        // Если это специальная клавиша — ничего не делаем
        return;
    }
    else{
        
        // searchCity.value = lastValue + inputKeyValue
        lastValue = searchCity.value
    }
}
searchCity.addEventListener('keydown',keyInputCity)

function getListSettlements(event){
    // const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    if(searchCity.value.length>0){
        search_set = searchCity.value + "/"
    }
    else{
        search_set = ""
    }
    
    // if(searchCity.value.length>0){
        $.ajax({
            url: `/order/nova-posta/${search_set}`,         
            method: 'GET', 
            // headers: {'X-CSRFTOKEN': csrf},               
            success: function(data){   
                // alert(data.html)
                const scroll = document.querySelector('.scroll-element')
                scroll.innerHTML = data.html
            }
        });
    // }
    
}
searchCity.addEventListener('input',getListSettlements)
searchCity.addEventListener('input',openScroll)

/////////////////////////////////////////////////////////
const searchWarehouse = document.querySelector('#warehouse_cearch')
// searchCity.focus();
function openScrollWarehouse(event){
    event.stopPropagation();
    const scroll = document.querySelector('.warehouse-scroll-element')
    scroll.classList.add('active')
    scroll.addEventListener('click', openScrollWarehouse)
    if(searchWarehouse.value.length>0){
        search_set = searchWarehouse.value + "/"
    }
    else{
        search_set = ""
    }
    // alert(event.target.id)
    // if(searchCity.value.length>0){
        $.ajax({
            url: `/order/nova-posta/warehouse/${event.target.id}/${search_set}`,      
            method: 'GET', 
            // headers: {'X-CSRFTOKEN': csrf}, 
            // alert(url); 
            // alert()           
            success: function(data){   
                // alert(url)
                // const scroll = document.querySelector('.scroll-element')
                scroll.innerHTML = data.html
            }
        });
}

searchWarehouse.addEventListener('click', closeScroll)
searchWarehouse.addEventListener('click', openScrollWarehouse)
searchWarehouse.addEventListener('input', openScrollWarehouse)
searchCity.addEventListener('click',closeScrollWarehouses)

function closeScrollWarehouses(event){
    event.stopPropagation();
    const scroll = document.querySelector('.warehouse-scroll-element')
    scroll.classList.remove('active')
}
document.addEventListener('click',closeScrollWarehouses)



document.addEventListener('DOMContentLoaded', function() {
    const cityWarehouse = document.querySelector('.warehouse-scroll-element');
    
    function fillWarehouse(event) {
        const target = event.target;
        
        if (target.tagName.toLowerCase() === 'li') {
            
            const searchWarehouse = document.querySelector('.warehouse_cearch')
            searchWarehouse.value = target.textContent;
            const warehouse_id = document.querySelector('#id-warehouse')
            warehouse_id.value = target.id
            // alert(target.id)

        }
    }

    cityWarehouse.addEventListener('click', fillWarehouse);
});

let errorList = document.querySelector(".error")

if ((errorList.textContent.length) > 0){
    errorList.classList.add("active")
    
    
}
