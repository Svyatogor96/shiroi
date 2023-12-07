document.querySelectorAll('.go_btn').forEach(element => {
    element.addEventListener('click', function () {
        var title = element.querySelector('.invisible').textContent
        $.ajax({
            url: '/go',
            method: 'get',
            dataType: 'json',
            data: { 'paty': title },
            success: function (data) {

            }
        });
    });
})