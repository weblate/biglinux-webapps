$(function(){

    $(".alert, #modetv, #open_change, #btn-spin, #btn-title-go, #btn-icon-go").hide();

    $("#btn-enable-0").click(function(){
        $("#btn-spin").show();
    });

    var iconSelected = $("select").val();
    if(iconSelected){
      $("#browsericon").attr("src", "icons/" + iconSelected + ".png");
      if(iconSelected.match(/firefox/gi)){
          $("#perfil").hide();
      }
    }

    $("select").on("change", function(){
        $("#browsericon").attr("src", "icons/" + this.value + ".png");

        switch(this.value){
        case "firefox":
            $("#perfil").hide();
            break;

        case "firefox-developer-edition":
            $("#perfil").hide();
            break;

        case "firefox-nightly":
            $("#perfil").hide();
            break;

        default:
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

    var modetv = $("#urldesk").val()
    if(modetv){
        if(modetv.match(/youtu/gi)){
            $("#modetv").show();
            $("#modetv_empty").hide();
        }
    }

    $("#urldesk").keyup(function(){

        if($(this).val().match(/.*youtu.*watch.*/gi)){
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

            $.get(formUrl, formData, function(feed){
                if (feed == 0){
                    $("#install").blur();
                    $("#alert-install").fadeIn();
                    setTimeout(function(){
                        $("#alert-install").fadeOut();
                        $("#form-install").trigger("reset");
                        $("#preview").attr("src", "img/default.png");
                        $("select").trigger("change");
                        $("#modetv").hide();
                        $("#modetv_empty").show();
                        $("#namedesk").focus();
                    }, 3000);
                } else {
                    $("#install").blur();
                    $("#alert-install-error").fadeIn();
                    setTimeout(function(){
                        $("#alert-install-error").fadeOut();
                        $("#form-install").trigger("reset");
                        $("#preview").attr("src", "img/default.png");
                        $("select").trigger("change");
                        $("#modetv").hide();
                        $("#modetv_empty").show();
                        $("#namedesk").focus();
                    }, 3000);
                }
            });
        }
    });

    $("#install-edit").click(function (e) {
        e.preventDefault();
        let nome = $("#namedesk").val();

        if (!nome) {
            $("#alert-name").fadeIn();
            $("#namedesk").focus();
            setTimeout(function(){
                $("#alert-name").fadeOut();
            }, 3000);
        } else {
            let namedesk = $("#namedesk").val();
            $("#namedesk").val(namedesk);

            let icondesk = $("#icondesk").val();
            $("#icondesk").val(icondesk);

            let browser = $("#browser").val();
            $("#browser").val(browser);

            let formUrl = $("#form-edit").attr("action");
            let formData = $("#form-edit").serialize();

            $.get(formUrl, formData, function(resp){
                //alert(resp);
                if(resp==0){
                    $("#alert-edit").fadeIn();
                    $("#install").blur();
                    setTimeout(function(){
                        $("#alert-edit").fadeOut();
                        location.replace("index-edit.sh.htm");
                    }, 3000);
                } else {
                    $("#alert-edit-error").fadeIn();
                    $("#install").blur();
                    setTimeout(function(){
                        $("#alert-edit-error").fadeOut();
                    }, 3000);
                }
            });

        }
    });

    function isValidURL(string) {
      var res = string.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi);
      return (res !== null)
    };

    $("#filter-edit").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#table-filter-edit tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("#filter").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#table-filter-del tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

function openModal(elem, n){
    $(".modal#modal"+n).modal("show");
    $(elem).tooltip("hide");
}

function closeModal(i){
    $(".modal#modal"+i).modal("hide");
    let valueFiledesk = $("#filedesk"+i).val();
    startRemove(valueFiledesk);
}

function startRemove(file){
    fetch("./webapp-remove.sh?filedesk="+file)
    .then(data => {
        return data.text();
    })
    .then(resp => {
        if(resp==0){
            $(".modal#modal-success").modal("show");
            $(".modal#modal-success").on("hide.bs.modal", function(){
                location.reload(true);
            });
        } else {
            $(".modal#modal-error").modal("show");
        }
    });
}
