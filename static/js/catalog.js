$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-contact .modal-content").html("");
                $("#modal-contact").modal("show");
            },
            success: function (data) {
                $("#modal-contact .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this).closest('form');
        debugger
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',

            success: function (data) {
                debugger
                if (data.form_is_valid) {
                    $("#modal-contact .modal-content").html(data.html_form);
                } else {
                    $("#modal-contact .modal-content").html(data.html_form);
                }
            },
            error: function(err) {
                debugger
            }
        })
        ;
        return false;
    };


    /* Binding */

    // Create contact
    $(".js-contact").click(loadForm);
    debugger
    $("#modal-contact").on("click", "#saveButton", saveForm);
});