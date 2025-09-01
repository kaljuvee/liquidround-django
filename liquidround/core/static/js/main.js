$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

$(document).ready(function(){
   $('.carousel').carousel({
       interval: 5000
   });


  $('#companies').autocomplete({
      serviceUrl: '/company/search/',
      minChars: 2,
      onSearchComplete: function(query, suggestions){
        if(suggestions.length == 0) {
            $('#company_id').val('');
            $('#industry, #website, #specificrole').val('').prop('readonly',false);
        }
      },
      onSelect: function (suggestion) {
          //alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
          check_company(suggestion.data);
          $('#company_id').val(suggestion.data);
      }
  });
  $('#companies').on('keyup', function(){
    if($(this).val() == '') {
        $('#industry, #website, #specificrole').val('').prop('readonly',false).trigger('change');
        $('#company_id').val('').trigger('change');
    }
  });

  $('body').on('click','a.approve', function(e){
    e.preventDefault();
    var id = $(this).data('id');
    var this2 = this;
    $.ajax({
      url: '/admindeck/approve/',
      type: 'post',
      data: { id: id}
    })
    .done(function(data){
      if(data.success) {
        $(this2).parents('.company').remove();
      }
    })
  });

  $('body').on('click','a.delete', function(e){
    e.preventDefault();
    var id = $(this).data('id')
    var this2 = this;
    if(confirm('Are you sure you want to delete this listing?')){
      $.ajax({
        url: '/listing/delete/',
        type: 'post',
        data: { id: id }
      })
      .done(function(data){
        if(data.success){
          $(this2).parents('tr').remove();
          $(this2).parents('.company').remove();
        }
      });
    } else return false;
  });

  $('body').on('click','a.sold', function(e){
    e.preventDefault();
    var id = $(this).data('id')
    var this2 = this;
    var type = $(this).data('type');
    if(type == 'offer'){
      var word = 'bought';
    } else {
      var word = 'sold';
    }
    if(confirm('Are you sure you want to mark this listing as '+ word +'?')){
      $.ajax({
        url: '/listing/sold/',
        type: 'post',
        data: { id: id }
      })
      .done(function(data){
        if(data.success){
          $(this2).parents('tr').remove();
          var template = $('<tr><td>'+ data.listing.business +'</td><td><span>'+ data.listing.shares +'</span> shares</td><td>£<span>'+ data.listing.price +'</span></td><td>'+ data.listing.date +'</td></tr>');

          if(data.listing.listing_type == 'equity'){
            $('#SellHistory table tbody').append(template);
          } else {
            $('#BuyHistory table tbody').append(template);
          }
        }
      });
    } else return false;
  });

  $('body').on('click','a.remove_image', function(e){
    e.preventDefault();
    var id = $(this).data('id');
    var this2 = this;
    if(confirm('Are you sure you want to delete this picture?')){
      $.ajax({
        url: '/admindeck/remove_image/',
        type: 'post',
        data: { id: id }
      })
      .done(function(data){
        if(data.success){
          $(this2).parents('.image').remove();
        }
      });
    } else return false;
  });

  $('body').on('click','a.remove_doc', function(e){
    e.preventDefault();
    var id = $(this).data('id');
    var this2 = this;
    if(confirm('Are you sure you want to delete this document?')){
      $.ajax({
        url: '/admindeck/remove_doc/',
        type: 'post',
        data: { id: id }
      })
      .done(function(data){
        if(data.success){
          $(this2).parents('li').remove();
        }
      });
    } else return false;
  });

  $('body').on('change', '[name="is_main"]', function(){
    var id = $('[name="is_main"]:checked').val();
    $.ajax({
      url: '/admindeck/change_main_image/',
      type: 'post',
      data: { id: id }
    })
    .done(function(data){
      if(data.success != true){
        alert('Error while setting this picture as main');
      }
    });
  });

  $('body').on('click', 'a.add_doc', function(e){
    e.preventDefault();
    console.log('add_doc')
    var template = $('<div class="form-group"><label class="col-md-3">Document:</label><div class="col-md-6"><input type="text" class="form-control" name="title[]" placeholder="Document title"></div><div class="col-md-3"><label class="btn btn-default">Choose file<input type="file" id="documents" name="docs[]" class="form-control"></label></div></div>');
    $(template).insertBefore($(this).parent());
  });

  $('body').on('click', 'a[data-target="#request"]', function(){
    var lid = $(this).data('id');
    $('#listing_id').val(lid);
  });

  $('body').on('click','#request_contacts', function(){
    var lid = $('#listing_id').val()
    $.ajax({
      url: '/messages/request_contacts/',
      type: 'post',
      data: {id: lid}
    })
    .done(function(data){
      if(data.success){
        $('#request').modal('hide');
        $('#agree').prop('checked', false);
        $('#request_contacts').prop('disabled', true);
        $('a[data-target="#request"][data-id="'+ lid +'"]').parent().html('<small>Requested</small>');
      }
    });
  });

  $('body').on('change', '#agree', function(){
    if($(this).prop('checked') == true){
      $('#request_contacts').prop('disabled',false);
    } else {
      $('#request_contacts').prop('disabled',true);
    }
  });

  $('body').on('click', '.watch', function(e){
    e.preventDefault();
    var cid = $(this).data('id');
    var this2 = this;
    $.ajax({
      url: '/company/watch/',
      type: 'post',
      data: { id: cid }
    })
    .done(function(data){
      if(data.success){
        if(data.status == 'watched'){
          $(this2).html('Remove from watch list');
        } else {
          $(this2).html('Add to watch list');
        }
      }
    });
  });

    $('body').on('submit', '#filter-form', function(e){
        e.preventDefault();
        console.log($(this).serialize());
        $.ajax({
                url: '/company/all/?' + $(this).serialize(),
                type: 'get',
                data: {}
            })
            .done(function(data){
                $('.scroll').html(data);

                $('.scroll').removeData('jscroll');
                $('.scroll').jscroll({
                    loadingHtml: '<img src="loading.gif" alt="Loading" /> Loading...',
                    //padding: 20,
                    nextSelector: 'a.js-next-page',
                    //contentSelector: 'li'
                });

            });

    });

    $('body').on('submit', '#js-company-request', function(e){
        e.preventDefault();
        var formdata = $(this).serializeArray();
        if(validateURL(formdata[0].value)||validateURL('http://' + formdata[0].value)) {
            $.ajax({
                    url: '/company/request/',
                    type: 'post',
                    data: formdata
                })
                .done(function (result) {
                    if (result.success) {
                        var success = templates.request_listing_success.render();
                        $('#request').find('.modal-body').html($(success));
                    }
                });
        } else {
            $('#request').find('.text-danger').removeClass('hidden');
        }
    });

    $('body').on('hidden.bs.modal', '#request', function(){
       var form = templates.request_listing_form.render();
        $(this).find('.modal-body').html($(form));
    });

    $('body').on('click','.js-mark-as-proccessed', function(e){
        e.preventDefault();
        var id = $(this).data('id')
        var this2 = this;
        $.ajax({
            url: '/admindeck/proccessed/',
            type: 'post',
            data: {id: id}
        })
            .done(function(data){
                if(data.success){
                    var e = $(this2).parents('tr').find('td.status');
                    e.html('Proccessed');
                    console.log(e);
                    $(this2).remove();
                }
            });
    });
});


function check_company(id){
  $.ajax({
    type: "POST",
    url: "/company/get/",
    data: { id: id }
  })
  .done(function(data){
    if(data.success){
        $('#industry').val(data.company.industry).prop('readonly',true).trigger('change');
        $('#website').val(data.company.website).prop('readonly',true).trigger('change');
        $('#specificrole').val(data.company.specificrole).prop('readonly',true).trigger('change');
        
        for(var i = 0; i < data.company.photos.length; i++){
          $('.images').append($('<div class="image text-right"><img src="'+ data.company.photos[i].url +'" /><label><input type="radio" name="is_main" '+ data.company.photos[i].is_main +' value="'+ data.company.photos[i].id +'" /> Is main picture</label> <a href="#" class="remove_image" data-id="'+ data.company.photos[i].id +'">Remove photo?</a></div>'));
        }
    } else {
        $('#industry, #website, #specificrole').val('').prop('readonly',false).trigger('change');
        $('#company_id').val('').trigger('change');
    }
  });
}

function validateURL(textval) {
    var urlregex = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+(:[a-zA-Z0-9.&%$-]+)*@)*((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(:[0-9]+)*(\/($|[a-zA-Z0-9.,?'\\+&%$#=~_-]+))*$/;
    return urlregex.test(textval);
}