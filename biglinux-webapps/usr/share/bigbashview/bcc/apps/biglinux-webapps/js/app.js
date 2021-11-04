$(function(){

    $(".alert, #modetv, #open_change, #btn-spin, #btn-title-go, #btn-icon-go").hide();

    $("#btn-enable-0").click(function(){
        $("#btn-spin").show();
    });

    var iconSelected = $("select").val();
    $("#browsericon").attr("src", "icons/" + iconSelected + ".png");
    if (iconSelected == "firefox") {
        $("#perfil").hide();
    } else {
        $("#perfil").show();
    }

    $("select").on("change", function(){
        $("#browsericon").attr("src", "icons/" + this.value + ".png");

        if (this.value == "firefox") {
            $("#perfil").hide();
        } else {
            $("#perfil").show();
        }
    });

    $("#btn").click(function(e){
        e.preventDefault();

        $.get("./get_dialog_icon.sh.py", function(dados){
            if (dados){
                $("#open_folder").hide()
                $("#open_change").show();
                $("#icondesk").focus();
                $("#icondeskhidden").val(dados);
                $("#icondesk").val(dados.replace(/.*\//, ""));
                $("#preview").attr("src", dados);
            } else {
                $("#btn").blur();
                return;
            }
        });
    });

    $("#urldesk").keyup(function(){

        if($(this).val().match(/youtu/gi)){
            $("#modetv").show();
            $("#modetv_empty").hide();
        } else {
            $("#modetv").hide();
            $("#modetv_empty").show();
        }
    });

    $("#gettitle").click(function(e){
        e.preventDefault();

        let url = $("#urldesk").val();

        if (!isValidURL(url) || !url || /\s/.test(url)){
            $("#alert-url").fadeIn();
            $("#urldesk").focus();
            setTimeout(function () {
                $("#alert-url").fadeOut();
            },3000);
        } else {
            $("#gettitle").tooltip("hide");
            $("#btn-title").hide();
            $("#btn-title-go").show();
            $.get("./get_title.sh.py", url, function(title){
                if (title){
                    $("#namedesk").focus();
                    $("#namedesk").val(title);
                    $("#btn-title-go").hide();
                    $("#btn-title").show();
                } else {
                    $("#alert-title").fadeIn();
                    setTimeout(function(){
                        $("#alert-title").fadeOut();
                        $("#urldesk").focus();
                        $("#btn-title-go").hide();
                        $("#btn-title").show();
                    }, 3000);
                }
            });
        }
    });

    $("#favicon").click(function(e){
        e.preventDefault();

        let url = $("#urldesk").val();

        if (!isValidURL(url) || !url || /\s/.test(url)){
            $("#alert-url").fadeIn();
            $("#urldesk").focus();
            setTimeout(function () {
                $("#alert-url").fadeOut();
            },3000);
        } else {
            $("#favicon").tooltip("hide");
            $("#btn-icon").hide();
            $("#btn-icon-go").show();
            $.get("./get_favicon.sh.py", url, function(data){
                if (data){
                    if (/\/tmp\/.*/.test(data)){
                      $("#icondeskhidden").val(data);
                      $("#icondesk").val(data.replace(/.*\//, ""));
                      $("#preview").attr("src", data);
                    } else {
                        $("#modal-body").html(data);
                        $(".modal#modal-favicon").modal("show");
                        $("div#input_img").each(function(){
                            $("span#btn-spin").hide();
                            $(this).click(function(){
                                $(this).children("span#btn-spin").show();
                                let url = $(this).children("img").attr("src");
                                $.get('./save_favicon.sh.py', url,function(img){
                                    $("#icondeskhidden").val(img);
                                    $("#icondesk").val(img.replace(/.*\//, ""));
                                    $("#preview").attr("src", img);
                                    $(".modal#modal-favicon").modal("hide");
                                });
                            });
                        });
                    }
                    $("#btn-icon-go").hide();
                    $("#btn-icon").show();
                    $("#open_folder").hide()
                    $("#open_change").show();
                } else {
                    $("#alert-favicon").fadeIn();
                    setTimeout(function(){
                        $("#alert-favicon").fadeOut();
                        $("#btn-icon-go").hide();
                        $("#btn-icon").show();
                    }, 3000);
                    return;
                }
            });
        }
    });

    $("#install").click(function (e) {
        e.preventDefault();
        let nome = $("#namedesk").val();
        let url = $("#urldesk").val();

        if (!nome) {
            $("#alert-name").fadeIn();
            $("#namedesk").focus();
            setTimeout(function(){
                $("#alert-name").fadeOut();
            }, 3000);
        } else if (!isValidURL(url) || !url || /\s/.test(url)) {
            $("#alert-url").fadeIn();
            $("#urldesk").focus();
            setTimeout(function(){
                $("#alert-url").fadeOut();
            }, 3000);
        } else {
            let formUrl = $("#form-install").attr("action");
            let formData = $("#form-install").serialize();

            $.get(formUrl, formData, function(){
                $("#form-install").trigger("reset");
                $("#alert-install").fadeIn();
                $("#install").blur();
            });

            setTimeout(function(){
                $("#alert-install").fadeOut();
                $("#namedesk").focus();
            }, 3000);
        }
    });

    $("#install-edit").click(function (e) {
        e.preventDefault();
        let nome = $("#namedesk").val();
        let url = $("#urldesk").val();

        if (!nome) {
            $("#alert-name").fadeIn();
            $("#namedesk").focus();
            setTimeout(function(){
                $("#alert-name").fadeOut();
            }, 3000);
        } else if (!isValidURL(url) || !url || /\s/.test(url)) {
            $("#alert-url").fadeIn();
            $("#urldesk").focus();
            setTimeout(function(){
                $("#alert-url").fadeOut();
            }, 3000);
        } else {
            let formUrl = $("#form-edit").attr("action");
            let formData = $("#form-edit").serialize();

            $.get(formUrl, formData, function(){
                $("#form-edit").trigger("reset");
                $("#alert-edit").fadeIn();
                $("#install").blur();
            });

            setTimeout(function(){
                $("#alert-edit").fadeOut();
                $("#namedesk").focus();
            }, 3000);
        }
    });

    function isValidURL(string) {
      var res = string.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi);
      return (res !== null)
    };
});
