document.querySelectorAll('.dropdown').forEach(element => {
    console.log("hehe")
    dropDownBtn = element.querySelector('.dropdown_button');

    dropDownBtn.addEventListener('click', function () {
        const dropdownlists = element.querySelectorAll('.dropdown_list')
        dropdownlists.forEach(element => {
            element.classList.toggle('dropdownListVisible');
        });
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Tab' || e.key === 'Escape') {
            const dropdownlists = element.querySelectorAll('.dropdown_list')
            dropdownlists.forEach(element => {
                element.classList.remove('dropdownListVisible');
            });

        }
    });


    // element.querySelector('.dropdown_list').querySelectorAll('.dropdown-list-item').forEach(element => {
    //     if (element.id === "1") {
    //         element.addEventListener('click', function () {
    //             console.log(element.textContent || element.innerText);
    //             deleteTask.classList.add('deleteVisible')

    //         })
    //     }
    // })

});

// dropDownBtn = document.querySelector('.dropdown-button')
// dropDownList = document.querySelector('.dropdown-list')
// dropDownListItem = dropDownList.querySelectorAll('.dropdown-list-item')

// dropDownBtn.addEventListener('click', function () {
//     dropDownList.classList.toggle('dropdown-list--visible');
// });

// dropDownListItem.forEach(function (listItem) {
//     listItem.addEventListener('click', function (e) {
//         e.stopPropagation();
//     })
// })

// document.addEventListener('click', function (e) {
//     console.log('Document click');
//     if (e.target !== dropDownBtn) {
//         dropDownList.classList.remove('dropdown-list--visible');
//     }
// });

// document.addEventListener('keydown', function (e) {
//     if (e.key === 'Tab' || e.key === 'Escape') {
//         dropDownList.classList.remove('dropdown-list--visible');
//     }
// }); 