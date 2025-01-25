
function plusCountProduct(event){
    const target = event.target
    const id = target.id.split('_')[2]
    const countInput = document.querySelector(`#count_${id}`)
    if (Number(countInput.value) < 9){
        countInput.value = Number(countInput.value) + 1
        const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        $.ajax({
            url: `/cart/plus_count_product/${id}/`,         
            method: 'POST', 
            headers: {'X-CSRFTOKEN': csrf},               
            success: function(data){
                const productsPrice = document.querySelector(`#products_price_${id}`)
                const totalPriceStr = document.querySelector('.total-price');
                const totalPrice = totalPriceStr.textContent.trimStart().split(' ')[3]
                const productPrice = document.querySelector(`#product_price_${id}`)

                totalPriceStr.textContent = "Загальна сумма : "+(parseFloat(productPrice.textContent) + parseFloat(totalPrice))+',00'
                productsPrice.textContent = parseFloat(productsPrice.textContent) + parseFloat(productPrice.textContent)+',00'
                
            }
        });
    }
}


function minusCountProduct(event){
    const target = event.target
    const id = target.id.split('_')[2]
    const countInput = document.querySelector(`#count_${id}`)
    if (Number(countInput.value) >1 ){
        countInput.value = Number(countInput.value) - 1
        const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        $.ajax({
            url: `/cart/minus_count_product/${id}/`,         
            method: 'POST', 
            headers: {'X-CSRFTOKEN': csrf},  
            success: function(data){
                const productsPrice = document.querySelector(`#products_price_${id}`)
                const totalPriceStr = document.querySelector('.total-price');
                const totalPrice = totalPriceStr.textContent.trimStart().split(' ')[3]
                const productPrice = document.querySelector(`#product_price_${id}`)

                totalPriceStr.textContent = "Загальна сумма : "+(parseFloat(totalPrice)-parseFloat(productPrice.textContent))+',00'
                productsPrice.textContent = parseFloat(productsPrice.textContent) - parseFloat(productPrice.textContent)+',00'
                
            }             

        });
    }
}

function removeProduct(event){
    const target = event.target
    const id = target.id.split('_')[3]
    const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value

    
    $.ajax({
        url: `/cart/remove_product/${id}/`,         
        method: 'POST', 
        headers: {'X-CSRFTOKEN': csrf},               
        success: function(data){
            
            const productsPrice = document.querySelector(`#products_price_${id}`)
            const totalPriceStr = document.querySelector('.total-price');
            const totalPrice = totalPriceStr.textContent.trimStart().split(' ')[3]
            totalPriceStr.textContent = "Загальна сумма : "+(parseFloat(totalPrice)-parseFloat(productsPrice.textContent))+',00'
            
            const block = document.querySelector(`#products-in-cart-${id}`)
            block.remove()


        }
    });
    
}

function openCart(){
    const bg = document.querySelector('.background')
    bg.classList.add('active')
    $.ajax({
        url: '/cart/get_cart/',         
        method: 'get',                
        success: function(data){   
             const cart = document.querySelector(".cart .body")
             cart.innerHTML = data
             const minusButtons = document.querySelectorAll(".minus_count")
             const plusButtons = document.querySelectorAll(".plus_count")
            const removeButtons = document.querySelectorAll(".remove_product_in_cart")
             minusButtons.forEach((item) => {
                item.addEventListener('click', minusCountProduct)
             })
             plusButtons.forEach((item) => {
                item.addEventListener('click', plusCountProduct)
             })
             removeButtons.forEach((item)=>{
                item.addEventListener('click', removeProduct)
             })
        }
    });
}
const cartLi = document.querySelector('#opencart')
cartLi.addEventListener('click', openCart)

function closeCart(){
    const bg = document.querySelector('.background')
    bg.classList.remove('active')

}
const closecart = document.querySelector('#close_cart')
closecart.addEventListener("click",closeCart)

const addButtons = document.querySelectorAll('.add_to_cart')

function add_product_to_cart(event){
    const target = event.target
    const id = target.id.split('_')[3]
    const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    $.ajax({
        url: `/cart/get_cart/${id}/`,         
        method: 'POST', 
        headers: {'X-CSRFTOKEN': csrf},               
        success: function(data){   
            openCart()
        }
    });

}
addButtons.forEach((item) => {
    item.addEventListener('click',add_product_to_cart)
})


