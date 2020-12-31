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