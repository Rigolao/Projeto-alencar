$(document).ready(function() {

    var baseUrl   = 'http://localhost:8000/doc/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter    = $('#filter');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar este conteúdo?');

        if(result) {
            window.location.href = delLink;
        }

    });
    
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(filter).change(function() {
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });

});

/* drop */

function dropHandler(ev) {
    console.log('File(s) dropped');
  
    // Impedir o comportamento padrão (impedir que o arquivo seja aberto)
    ev.preventDefault();
  
    if (ev.dataTransfer.items) {
      // Use a interface DataTransferItemList para acessar o (s) arquivo (s)
      for (var i = 0; i < ev.dataTransfer.items.length; i++) {
        // Se os itens soltos não forem arquivos, rejeite-os
        if (ev.dataTransfer.items[i].kind === 'file') {
          var file = ev.dataTransfer.items[i].getAsFile();
          console.log('... file[' + i + '].name = ' + file.name);
        }
      }
    } else {
      // Use a interface DataTransfer para acessar o (s) arquivo (s)
      for (var i = 0; i < ev.dataTransfer.files.length; i++) {
        console.log('... file[' + i + '].name = ' + ev.dataTransfer.files[i].name);
      }
    }
}

function dragOverHandler(ev) {
  console.log('File(s) in drop zone');

  // Impedir o comportamento padrão (impedir que o arquivo seja aberto)
  ev.preventDefault();
}

