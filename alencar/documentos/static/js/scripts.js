$(document).ready(function() {

    var deleteBtn = $('.detete-btn');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar este documento?');

        if(result ) {
            window.location.href = delLink;
        }

    });

})