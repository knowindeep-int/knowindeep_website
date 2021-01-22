function copyCurrentPageURLToClipBoard(){
    var input = document.createElement("input")
    var url = document.location.href
    input.value = url
    document.body.appendChild(input)
    input.select();
    document.execCommand("copy")
    document.body.removeChild(input)
    toastr.options.timeOut = 200
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
    toastr.options.timeOut = 100
    toastr.success('Copied To ClipBoard');
    var audio = new Audio('/media/copy.mp3');
    audio.volume = 0.2;
    audio.play();
    return

}

var fields = document.getElementsByClassName('field')
if ('{{request.user.is_superuser}}' == 'True') {
    for (var i = 0; i < fields.length; i++) {
        fields[i].addEventListener('mouseover', function(e) {

            if (document.getElementById('sugg_btn') != null && e.target.getAttribute('class') != 'sugg_btn') {
                document.getElementById('sugg_btn').remove()
            }

            if (e.target.getAttribute('class') != 'sugg_btn') {
                var btn = document.createElement('button')
                btn.setAttribute('class', 'sugg_btn')
                btn.innerHTML = 'ADD SUGGESTION'
                btn.setAttribute('id', 'sugg_btn')
                btn.setAttribute('onclick', 'createInputBox(this);')
                e.target.insertBefore(btn, e.target.firstChild.nextSibling);
            }
        })
    }
}

p_tags = document.getElementsByTagName('p')
if ('{{request.user.is_superuser}}' == 'True') {
    for (var i = 0; i < p_tags.length; i++) {
        p_tags[i].addEventListener('mouseover', function(e) {

            if (document.getElementById('sugg_btn') != null && e.target.getAttribute('class') != 'sugg_btn') {
                document.getElementById('sugg_btn').remove()
            }

            if (e.target.getAttribute('class') != 'sugg_btn') {
                var btn = document.createElement('button')
                btn.setAttribute('class', 'sugg_btn')
                btn.innerHTML = 'ADD SUGGESTION'
                btn.setAttribute('id', 'sugg_btn')
                btn.setAttribute('onclick', 'createInputBox(this);')
                e.target.insertBefore(btn, e.target.firstChild.nextSibling);
            }
        })
    }
}
var title = document.getElementsByTagName('h1')
if ('{{request.user.is_superuser}}' == 'True') {
    for (var i = 0; i < title.length; i++) {
        title[i].addEventListener('mouseover', function(e) {

            if (document.getElementById('sugg_btn') != null && e.target.getAttribute('class') != 'sugg_btn') {
                document.getElementById('sugg_btn').remove()
            }

            if (e.target.getAttribute('class') != 'sugg_btn') {
                var btn = document.createElement('button')
                btn.setAttribute('class', 'sugg_btn')
                btn.innerHTML = 'ADD SUGGESTION'
                btn.setAttribute('id', 'sugg_btn')
                btn.setAttribute('onclick', 'createInputBox(this);')
                e.target.insertBefore(btn, e.target.firstChild.nextSibling);
            }
        })
    }
}


function createInputBox(e) {
    if (document.getElementById('sugg_inp') == null) {
        var inp = document.createElement('input')
        inp.id = "sugg_inp"
        e.parentNode.appendChild(inp)

    }

}
document.addEventListener('keyup', function(e) {
    if (e.keyCode == "13") {
        if (document.getElementById('sugg_inp') != null) {
            var value = document.getElementById('sugg_inp').value
            addSuggestion();
        }
        document.getElementById('sugg_inp').remove()
    }
})