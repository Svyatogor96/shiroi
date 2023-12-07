
//var obj = {
//    hello: function (name) {
//        alert("Hello " + name);
//    }
//};
//// создаём объект Deferred
//defer = $.Deferred();
//// передаём свойства объекта Deferred нашему объекту
//defer.promise(obj);
//// выставляем состояние resolve
//defer.resolve("John");
//// используем наш объект, как заместитель объекта Deferred
//obj.done(function (name) {
//    obj.hello(name); // выводит "Hello John"
//}).hello("Karl"); // выводит "Hello Karl"

function init() {
    let map = new ymaps.Map('map', {
        center: [56.00899172891002, 92.86888253291062],
        zoom: 13,
    });
    $.ajax({
        url: '/jsonParty.json',
        method: 'get',
        dataType: 'json',
        success: function (data) {
            for (var i = 0; i < data['partys'].length; i++) {
                element = data['partys'][i];
                console.log(element)
                let placeMark = new ymaps.Placemark([element[5], element[4]], {
                    balloonContentHeader: element[0],
                    // balloonContentBody: element[6],
                }, {
                    iconLayout: 'default#image',
                    iconImageHref: 'https://cdn-icons-png.flaticon.com/512/9131/9131546.png',
                    iconImageSize: [30, 30],
                    iconImageOffset: [-10, -15],
                    title: 'hellow rold',
                });
                map.geoObjects.add(placeMark);

                placeMark.events.add('click', function () {
                    $.ajax({
                        url: '/getParty.json',
                        method: 'post',
                        dataType: 'json',
                        data: {},
                        success: function (data) {
                        }
                    })
                });
            }
        }
    });

    map.controls.remove('geolocationControl'); // удаляем геолокацию
    map.controls.remove('searchControl'); // удаляем поиск
    map.controls.remove('trafficControl'); // удаляем контроль трафика
    map.controls.remove('typeSelector'); // удаляем тип
    map.controls.remove('fullscreenControl'); // удаляем кнопку перехода в полноэкранный режим
    map.controls.remove('zoomControl'); // удаляем контрол зуммирования
    map.controls.remove('rulerControl'); // удаляем контрол правил

    // placeMark.
}
ymaps.ready(init);




