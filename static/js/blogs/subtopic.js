function copyCurrentPageURLToClipBoard(){
    var input = document.createElement("input")
    var url = document.location.href
    input.value = url
    document.body.appendChild(input)
    input.select();
    document.execCommand("copy")
    document.body.removeChild(input)
    toastr.options.timeOut = 1000
    toastr.success('Copied To ClipBoard');
    var audio = new Audio('/media/copy.mp3');
    audio.play();
    return 

}
function copyChapterPageURL(e) {

    var input = document.createElement('input');
    input.value = e.getAttribute('data-href');
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
    toastr.options.timeOut = 1000
    toastr.success('Copied To ClipBoard');
    var audio = new Audio('/media/copy.mp3');
    audio.volume = 0.2;
    audio.play();
    return

}
function createInputBox(e) {
    if (document.getElementById('sugg_inp') == null) {
        var inp = document.createElement('input')
        inp.id = "sugg_inp"
            // document.getElementById('sugg_btn').remove()
        e.parentNode.appendChild(inp)

    }


}
document.addEventListener('keyup', function(e) {
    if (e.key == "13") {
        if (document.getElementById('sugg_inp') != null) {
            var value = document.getElementById('sugg_inp').value
            addSuggestion();
        }
        document.getElementById('sugg_inp').remove()
    }
})

function stoppedTyping(value) {
    if (value.length > 0) {
        document.getElementById('comment-btn').disabled = false;
    } else {
        document.getElementById('comment-btn').disabled = true;
    }
}

function updateLikes(likes, success) {
    if (success) {
        $('#like-btn').addClass('liked');
        document.getElementById('likeImg').src = "/static/images/heart_active.svg";
    } else {
        $('#like-btn').removeClass('liked');
        document.getElementById('likeImg').src = "/static/images/heart.svg";
    }
    $('#likes').text(likes)
}

function showLoader() {
    var loader = document.getElementById('comment_loader')
    loader.style.display = 'block'
}

function hideLoader() {
    var loader = document.getElementById('comment_loader')
    loader.style.display = 'none'
}



if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}



document.getElementById('googleLoginCmt').onclick = function () {
    var url = this.getAttribute('google-href-cmt')
    window.open(url, "_self")
};

document.getElementById('githubLoginCmt').onclick = function () {
    var url = this.getAttribute('github-href-cmt')
    window.open(url, "_self")
};