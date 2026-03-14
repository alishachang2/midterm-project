$(document).ready(function() {

  $('#submit-btn').on('click', function() {
    $('.form-control').removeClass('is-invalid');

    var showObject = {
      title:     $('#title').val(),
      network:   $('#network').val(),
      host:      $('#host').val(),
      season:    $('#season').val(),
      year:      $('#year').val(),
      rating:    $('#rating').val(),
      genre:     $('#genre').val(),
      summary:   $('#summary').val(),
      image_url: $('#image_url').val()
    };

    $.ajax({
      type: 'POST',
      url: '/edit_show/' + showId,
      data: JSON.stringify(showObject),
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      success: function(result) {
        window.location.href = '/show/' + showId;
      },
      error: function(request, status, error) {
        var errors = request.responseJSON.errors;
        Object.keys(errors).forEach(function(field) {
          $('#' + field).addClass('is-invalid');
          $('#' + field + '-error').text(errors[field]);
        });
      }
    });
  });

  $('#discard-btn').on('click', function() {
    if (confirm('Are you sure you want to discard your changes?')) {
      window.location.href = '/show/' + showId;
    }
  });

});