$(document).ready(function () {
    $('form').on('submit', function (event) {
        $.ajax({
                data: {
                    start_time: $('#startTime').val(),
                    end_time: $('#endTime').val(),
                    repo_link: $('#repoLink').val()
                },
                type: 'POST',
                url: '/get_history'
            })
            .done(function (data) {
                var table = document.getElementById("history");
                alert(data);
                table.innerHTML = "Hello World!";
            });
        event.preventDefault();
    });
});