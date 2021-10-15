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

        // let url = $("#urldesk").val()
        // if (url && !/\s/.test(url)){
        //     $.get("./get_auto_icon.sh.py", url,function(resp){
        //         if (resp) {
        //             $("#icondeskhidden").val(resp);
        //             $("#icondesk").val(resp.replace(/.*\//, ""));
        //             $("#preview").attr("src", resp);
        //         } else {
        //             return;
        //         }
        //     });
        // }
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
            $("#btn-icon").hide();
            $("#btn-icon-go").show();
            $.get("./get_favicon.sh.py", url, function(data){
                if (data){
                    if (/.*tmp.*/.test(data)){
                      $("#icondeskhidden").val(data);
                      $("#icondesk").val(data.replace(/.*\//, ""));
                      $("#preview").attr("src", data);
                    } else {
                      $("#modal-body").html(data);
                      $(".modal").modal("show");
                      $("img#input_img").each(function(){
                        $(this).click(function(){
                          $(".modal").modal("hide");
                          let url = $(this).attr("src");
                          $.get('./save_favicon.sh.py', url,function(img){
                            $("#icondeskhidden").val(img);
                            $("#icondesk").val(img.replace(/.*\//, ""));
                            $("#preview").attr("src", '');
                            $("#preview").attr("src", img);
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
        let nome = $("#namedesk").val();
        let url = $("#urldesk").val();

        if (!nome) {
            e.preventDefault();
            $("#alert-name").fadeIn();
            $("#namedesk").focus();
            setTimeout(function(){
                $("#alert-name").fadeOut();
            }, 3000);
        } else if (url == "https://" || !url) {
            e.preventDefault();
            $("#alert-url").fadeIn();
            $("#urldesk").focus();
            setTimeout(function(){
                $("#alert-url").fadeOut();
            }, 3000);
        } else {
            $("#install").submit();
        }
    });

    function isValidURL(string) {
      var res = string.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi);
      return (res !== null)
    };
});
