(function ($) {
    "use strict";

    $(".input100").focusin(function () {

        $(this).keydown(function () {
            $("#btnId").attr("disabled", true);
        });
    });


    $('.input100').each(function () {
        $(this).removeClass('has-val');
        $(this).addClass('has-val');
    });


    /*==================================================================
    [ Focus input ]*/
    $('.input100').each(function () {

        $(this).on('blur', function () {
            if ($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        });
    })


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit', function () {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if ($(input).val().trim() == '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

    /*==================================================================
    [ Show pass ]*/
    var showPass = 0;
    $('.btn-show-pass').on('click', function () {
        if (showPass == 0) {
            $(this).next('input').attr('type', 'text');
            $(this).find('i').removeClass('zmdi-eye');
            $(this).find('i').addClass('zmdi-eye-off');
            showPass = 1;
        }
        else {
            $(this).next('input').attr('type', 'password');
            $(this).find('i').addClass('zmdi-eye');
            $(this).find('i').removeClass('zmdi-eye-off');
            showPass = 0;
        }

    });

    $('#password, #confirm_pass').on('keyup', function () {
        if ($('#password').val() == $('#confirm_pass').val()) {
            $('#message').html('<i class="zmdi zmdi-check-circle"></i>').css('color', 'green');
        }
        else
            $('#message').html('<i class="zmdi zmdi-close-circle"></i>').css('color', 'red');
    });

    $('#username').keyup(function () {
        var id = $('#username').val();
        var key = "1300d368c9fa449ab69e2699b5bdfe80";
        if (id.length == 18 || id.length == 16 || id.length == 9) {
            $.ajax({
                url: "https://account.kemenkeu.go.id/Account/GetNamaPegawai?id=" + id + "&key=" + key,
                type: "GET",
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('Content-Type', 'application/json');
                },
            }).done(function (result) {
                var nama = result.Nama;
                var imgUrl = 'https://account.kemenkeu.go.id/manage/Uploads/Thumbnails/' + id + '.jpg';
                if (result.Nama != undefined) {
                    $('.gambar img.profil').attr('src', imgUrl);
                    $('#nama').empty();
                    $('#nama').append(nama);
                } else {
                    $('.gambar img.profil').attr('src', '/v2-assets/assets/imgs/default.jpg');
                    $('#nama').empty();
                }

            }).fail(function () {
                $('.gambar img.profil').attr('src', '/v2-assets/assets/imgs/default.jpg');
            });
        }
    });

    $(window).ready(function () {
        $('#myModal').modal('show');
        $('.modal-backdrop.show').css('opacity', '0.8');
        $('.modal-header').css('height', '50px');
        $('.modal-dialog').addClass('vertical-centered');
    });

    $('.datetime').change(function () {
        $(this).attr('value', $('.datetime').val());
    });

    $(document).ready(function () {
        $('.datetime , .regisTglLahir').datepicker({
            showButtonPanel: true,
            closeText: "Close",
            changeMonth: true,
            changeYear: true,
            yearRange: "-100:+0",
            dateFormat: "yy-mm-dd",
            beforeShow: function (input) {
                setTimeout(function () {
                    $(input).datepicker("widget").find(".ui-datepicker-current").hide();
                }, 1);
            },
            onSelect: function () {
                if ($(this).val().trim() != "") {
                    $(this).addClass('has-val');
                }
                else {
                    $(this).removeClass('has-val');
                }

            }
        });
    });

})(jQuery);