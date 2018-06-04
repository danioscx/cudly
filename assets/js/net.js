
$(document).ready(function () {
    function UrlImg(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {  
                $("#dis").attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
      }
      $("#files").change(
          function () { 
              UrlImg(this);
           }
      )
    $("#data").keyup(function (str) {
        if (str != '') {
            $.ajax({
                type: "GET",
                url: "/json_search",
                data: {q: $("#data").val()},
                dataType: "json",
                success: function (ev) {
                },
                error: function (ev) {
                }
            }).done(function (x) {
            });
        }
    });
    $("#add").click(function () {
    $("#x").show();
    $("#add").hide();
});
  });