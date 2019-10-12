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
                var content = '';
                var commits = data["data"];
                if (commits.length == 0){
                    content += '<tr>';
                    content += '<td class="col-xs-12" colspan="4">No commits were made during this period</td>';
                    content += '</tr>';
                }
                for (var i = 0; i < commits.length; i++) {
                    content += '<tr>';
                    content += '<td class="col-xs-3">' + (i + 1).toString() + '</td>';
                    content += '<td class="col-xs-3">' + commits[i][0] + '</td>';
                    content += '<td class="col-xs-3">' + commits[i][1][0]["author"] + '</td>';
                    content += '<td class="col-xs-3">' + commits[i][1][0]["message"] + '</td>';
                    content += '</tr>';
                }
                
                $('#history').find('tbody').html(content);
                                
            });
        event.preventDefault();
    });
});