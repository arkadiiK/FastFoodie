function showRestaurantinfo(restaurant) {
    var restaurantName = "";
    var restaurantDescription = "";
    switch (restaurant) {
        case 'restaurant1':
            restaurantName = "Ресторан 1";
            restaurantDescription = "Це перший ресторан. Він славиться своєю кухнею та атмосферою.";
            break;
        case 'restaurant2':
            restaurantName = "Ресторан 2";
            restaurantDescription = "Це другий ресторан. Тут ви зможете скуштувати найсмачніші страви.";
            break;
        case 'restaurant3':
            restaurantName = "Ресторан 3";
            restaurantDescription = "Це третій ресторан. Його головна особливість - це дивовижна атмосфера та видовищний інтер'єр.";
            break;
        default:
            break;
    }

    document.getElementById("restaurantName").innerText = restaurantName;
    document.getElementById("restaurantDescription").innerText = restaurantDescription;
    document.getElementById("restaurantInfo").style.display = "block";
}