function copyProjectPageURLToClipBoard(e) {
    var input = document.createElement('input');
    // document.getElementById("clipboard").setAttribute("data-href",  getProjectAbsoluteUrl(project_slug) )
    // input.value = document.getElementById("clipboard").getAttribute('data-href');
    // alert(e.getAttribute("class"))
    //e.setAttribute("data-href",  getProjectAbsoluteUrl(project_slug) )
    input.value = e.getAttribute('data-href');
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
    toastr.options.timeOut = 200
    toastr.success('Copied To ClipBoard');
    var audio = new Audio('/media/copy.mp3');
    audio.volume = 0.2;
    audio.play();


    // FB.ui({
    //     display: 'popup',
    //     method: 'share',
    //     href: 'https://developers.facebook.com/docs/',
    // }, function(response) {});
}
