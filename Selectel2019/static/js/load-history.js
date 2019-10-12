$(document).ready(function () {
    $('form').on('submit', function (event) {
        $.ajax({
                data: {
                    start_time: $('#start-time').val(),
                    end_time: $('#end_time').val(),
                    repo_link: $('#repo_link').val()
                },
                type: 'POST',
                url: '/get_history'
            })
            .done(function (data) {
                // create table
            });
        event.preventDefault();
    });
});