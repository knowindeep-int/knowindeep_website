
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


