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
function createInputBox(e) {
    if (document.getElementById('sugg_inp') == null) {
        var inp = document.createElement('input')
        inp.id = "sugg_inp"
            // alert(e.parentNode)
            // document.getElementById('sugg_btn').remove()
        e.parentNode.appendChild(inp)

    }

    // alert('y')

}
document.addEventListener('keyup', function(e) {
    // alert(e.keyCode)
    if (e.key == "13") {
        // alert("6")
        if (document.getElementById('sugg_inp') != null) {
            var value = document.getElementById('sugg_inp').value
            addSuggestion();
            // alert(value)   
        }
        document.getElementById('sugg_inp').remove()
    }
})