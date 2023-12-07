dropDownBtn = document.querySelector('.user-dropdown')
dropDownList = document.querySelector('.user_box')
dropDownListItem = dropDownList.querySelectorAll('.dropdown-list-item')

dropDownBtn.addEventListener('click', function () {
    dropDownList.classList.toggle('dropdownListVisible');
});

dropDownListItem.forEach(function (listItem) {
    listItem.addEventListener('click', function (e) {
        e.stopPropagation();
    })
})

document.addEventListener('click', function (e) {
    console.log('Document click');
    if (e.target !== dropDownBtn) {
        dropDownList.classList.remove('dropdownListVisible');
    }
});

document.addEventListener('keydown', function (e) {
    if (e.key === 'Tab' || e.key === 'Escape') {
        dropDownList.classList.remove('dropdownListVisible');
    }
}); 