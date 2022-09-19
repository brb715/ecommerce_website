// Slider
// const swiper = new swiper('.swiper', {
//     slidesPerView: 4,
//     speed: 100,
//     spaceBetween: 40,
//     slidesPerGroup: 4,
//     direction: 'horizontal',
//     loop: true,
//     loopFillGroupWithBlank: true,

//     pagination: {
//         el: '.swiper-pagination',
//         clickable: true,
//     },

//     navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     }
// });
// const swipe = document.querySelector('.swiper').swiper;
// swipe.slideNext();
// Slider

// Cart
updatecart = function (cart) {
    for (let item in cart) {
        document.getElementById('after_add').innerHTML = "<button type='button' class='btn btn-primary minus p-2' id='minus" + item + "'>-</button> <span class='p-2' id='pr" + item + "'>" + cart[item] + "</span> <button type='button' class='btn btn-primary plus p-2' id='plus" + item + "'>+</button>";
    }
}

// document.querySelector('.minus').addEventListener('click', function(){
//     id=this.id.slice(6,);
//     document.getElementById('pr'+id).innerText= max(0,cart[id]-1);
//     console.log('yes');
// })

// document.querySelector('.plus').addEventListener('click',function(){
//     id=this.id.slice(5,);
//     document.getElementById('plus'+id).innerText=cart[id]+1;
//     console.log('yes');
// });

if (localStorage.getItem('cart') == undefined)
    cart = {};
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('total_items').innerText = Object.keys(cart).length;
}

all = document.querySelectorAll('.cart');
for (let i = 0; i < all.length; i++) {
    all[i].addEventListener('click', function () {
        id = this.id.toString();
        if (cart[id] != undefined)
            cart[id] += 1;
        else
            cart[id] = 1;
        localStorage.setItem('cart', JSON.stringify(cart));
        // updatecart(cart);
    });
}
// Cart

