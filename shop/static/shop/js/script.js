const swiper = new Swiper('.swiper', {
    slidesPerView: 4,
    speed: 100,
    spaceBetween: 40,
    slidesPerGroup: 4,
    direction: 'horizontal',
    loop: true,
    loopFillGroupWithBlank: true,

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    }
});
const swipe = document.querySelector('.swiper').Swiper;
swipe.slideNext();