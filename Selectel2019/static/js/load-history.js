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
                if (data["data"]){
                    $('#error-message').css("display", "none");
                    var content = '';
                    var commits = data["data"];
                    if (commits.length == 0) {
                        content += '<tr>';
                        content += '<td class="col-xs-12 td-white" colspan="4">No commits were made during this period</td>';
                        content += '</tr>';
                    }
                    for (var i = 0; i < commits.length; i++) {
                        content += '<tr>';
                        if (i % 2 == 0) {
                            content += '<td class="col-xs-3 td-white">' + (i + 1).toString() + '</td>';
                            content += '<td class="col-xs-3 td-white">' + commits[i][0] + '</td>';
                            content += '<td class="col-xs-3 td-white">' + commits[i][1][0]["author"] + '</td>';
                            content += '<td class="col-xs-3 td-white">' + commits[i][1][0]["message"] + '</td>';
                        } else {
                            content += '<td class="col-xs-3 td-gray">' + (i + 1).toString() + '</td>';
                            content += '<td class="col-xs-3 td-gray">' + commits[i][0] + '</td>';
                            content += '<td class="col-xs-3 td-gray">' + commits[i][1][0]["author"] + '</td>';
                            content += '<td class="col-xs-3 td-gray">' + commits[i][1][0]["message"] + '</td>';
                        }
                        content += '</tr>';
                    }
                    $('#history').find('tbody').html(content);
                } else {
                    var content = '';
                    content += '<tr>';
                    content += '<td class="col-xs-12 td-white" colspan="4">No commits were made during this period</td>';
                    content += '</tr>';
                    $('#history').find('tbody').html(content);

                    $('#error-message').css("display","inline");
                }                                
            });
        event.preventDefault();
    });
});