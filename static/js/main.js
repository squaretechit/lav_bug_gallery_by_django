document.addEventListener('DOMContentLoaded', function () {
    // Mobile Menu
    let menu_icon = document.querySelector('.mobile_menu_bar'),
        menu_item = document.querySelector('.menu-list');

    menu_icon.addEventListener('click', function(){
        if (menu_item.style.display == 'block'){
            menu_item.style.display = 'none';
        }else {
            menu_item.style.display = 'block';
        }
    })
})