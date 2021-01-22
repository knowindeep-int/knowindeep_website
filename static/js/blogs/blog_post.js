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
function copyCurrentPageURLToClipBoard(){
    var input = document.createElement("input")
    var url = document.location.href
    input.value = url
    document.body.appendChild(input)
    input.select();
    document.execCommand("copy")
    toastr.options.timeOut = 200
    toastr.success('Copied To ClipBoard');
    var audio = new Audio('/media/copy.mp3');
    audio.volume = 0.2;
    audio.play();
    document.body.removeChild(input)

}

function previous(){
    for(var i = 0;i<ch_list.length;i++)
    {
        // console.log('{{chapter_content.slug}}')
        if (ch_list[i] == '{{chapter_content.slug}}'&& i >0)
        {
            document.location.href = '/'+ '{{slug}}/' + ch_list[i-1] ;
            
        }
    }
}
function next(){
    for(var i = 0;i<ch_list.length;i++)
    {
        // console.log('{{chapter_content.slug}}')
        if (ch_list[i] == '{{chapter_content.slug}}'&& i<ch_list.length-1)
        {
            document.location.href = '/'+ '{{slug}}/' + ch_list[i+1] ;
           
        }
    }
}
var codes = document.getElementsByClassName('code')
    // alert(codes.length)

    if( '{{request.user.is_superuser}}' == 'True'){
        for(var i = 0; i< codes.length; i++ ){
            codes[i].addEventListener('mouseover', function(e){
                
                // alert(e.target.getAttribute('class'))
                if(document.getElementById('sugg_btn') != null &&  e.target.getAttribute('class') != 'sugg_btn'){
                    document.getElementById('sugg_btn').remove()
                }

                if(e.target.getAttribute('class') != 'sugg_btn' ){
                    var btn = document.createElement('button')
                    btn.setAttribute('class', 'sugg_btn')
                    btn.innerHTML = 'ADD SUGGESTION'
                    btn.setAttribute('id', 'sugg_btn')
                    btn.setAttribute('onclick', 'createInputBox(this);')
                    // e.target.appendChild(btn)
                    e.target.insertBefore(btn, e.target.firstChild.nextSibling);
                }
            })
        }
    }

    p_tags = document.getElementsByTagName('p')
    if( '{{request.user.is_superuser}}' == 'True'){
    for(var i = 0; i< p_tags.length; i++ ){
        p_tags[i].addEventListener('mouseover', function(e){
            
            // alert(e.target.getAttribute('class'))
            if(document.getElementById('sugg_btn') != null &&  e.target.getAttribute('class') != 'sugg_btn'){
                document.getElementById('sugg_btn').remove()
            }

            if(e.target.getAttribute('class') != 'sugg_btn' ){
                var btn = document.createElement('button')
                btn.setAttribute('class', 'sugg_btn')
                btn.innerHTML = 'ADD SUGGESTION'
                btn.setAttribute('id', 'sugg_btn')
                btn.setAttribute('onclick', 'createInputBox(this);')
                // e.target.appendChild(btn)
                e.target.insertBefore(btn, e.target.firstChild.nextSibling);
            }
        })
    }
}

    var title = document.getElementsByTagName('h1')
    if( '{{request.user.is_superuser}}' == 'True'){
    for(var i = 0; i< title.length; i++ ){
        title[i].addEventListener('mouseover', function(e){
            
            // alert(e.target.getAttribute('class'))
            if(document.getElementById('sugg_btn') != null &&  e.target.getAttribute('class') != 'sugg_btn'){
                document.getElementById('sugg_btn').remove()
            }

            if(e.target.getAttribute('class') != 'sugg_btn' ){
                var btn = document.createElement('button')
                btn.setAttribute('class', 'sugg_btn')
                btn.innerHTML = 'ADD SUGGESTION'
                btn.setAttribute('id', 'sugg_btn')
                btn.setAttribute('onclick', 'createInputBox(this);')
                // e.target.appendChild(btn)
                e.target.insertBefore(btn, e.target.firstChild.nextSibling);
            }
        })
    }
}




    function createInputBox(e){
        // alert('8')
        if(document.getElementById('sugg_inp') == null){
        var inp = document.createElement('input')
        inp.id = "sugg_inp"
        // alert(e.parentNode)
        // document.getElementById('sugg_btn').remove()
        e.parentNode.appendChild(inp)
        
        }
    }

    document.addEventListener('keyup', function(e){
        // alert(e.keyCode)
        if (e.keyCode == "13"){
            // alert("6")
            if(document.getElementById('sugg_inp') != null){
                var value = document.getElementById('sugg_inp').value
                addSuggestion();
                // alert(value)   
            }
            document.getElementById('sugg_inp').remove()
        }
    })
