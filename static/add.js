$(document).ready(function() {

  $('#submit-btn').on('click', function() {

    $('.form-control').removeClass('is-invalid');
    $('#success-msg').addClass('d-none');

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

    // validate rating is 1-5
    var rating = parseInt(showObject.rating);
    if (isNaN(rating) || rating < 1 || rating > 5) {
      $('#rating').addClass('is-invalid');
      $('#rating-error').text('Rating must be a number between 1 and 5');
      return;
    }

    $.ajax({
      type: 'POST',
      url: '/add_show',
      data: JSON.stringify(showObject),
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      success: function(result) {
        $('#see-it-link').attr('href', '/show/' + result.id);
        $('#success-msg').removeClass('d-none');
        $('#add-form')[0].reset();
        $('#title').focus();
        window.scrollTo(0, 0);
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

});