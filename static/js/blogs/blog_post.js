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

function updateComment(user, comment) {
    var com = document.getElementById('comments-list')
    hideLoader()
    com.innerHTML = '<div class="row"><div class="col-1"><span class="glyphicon glyphicon-user"></span></div><div class="col-11"><h5>{{user.first_name}} {{user.last_name}}</h5><p>' + comment + '</p></div></div>' + com.innerHTML
    document.getElementById('comment').value = ''
}

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

function stoppedTyping(value) {
    if (value.length > 0) {
        document.getElementById('comment-btn').disabled = false;
    } else {
        document.getElementById('comment-btn').disabled = true;
    }
}

document.getElementById('googleLoginCmt').onclick = function () {
    var url = this.getAttribute('google-href-cmt')
    window.open(url, "_self")
};

document.getElementById('githubLoginCmt').onclick = function () {
    var url = this.getAttribute('github-href-cmt')
    window.open(url, "_self")
};
