$(document).ready(function(){
   $('[data-toggle="offcanvas"]').click(function(){
       $("#navigation").toggleClass("hidden-xs");
   });
});

function user_logout(){
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: "/user_logout",
        method: "POST",
        'dataType': 'json',

        beforeSend: function (xhr) {
           xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function () {
            window.location.href = '/login';
        },
        error: function () {
            alert("Error")

        }

    });
}
