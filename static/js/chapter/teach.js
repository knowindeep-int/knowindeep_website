var isSaved = true
window.addEventListener("beforeunload", function (e) {
    
    if(!isSaved){
        e.preventDefault(); 
        e.returnValue = ''; 
    }

        }); 

        function inputvar(e){
            var inp = document.createElement('span');
            // inp.setAttribute('contenteditable', 'false')
            // inp.className = 'input'
            // inp.id = "unsplash_input"
            // inp.type = "text"
            if(e.id == "pe"){
                inp.className = 'input_pexels'
                inp.id = "inptext_pexels"
            fx().appendChild(inp)
            }
            else{
                inp.className = 'input'
                inp.id = "inptext"
            fx().appendChild(inp)
            }
           
        }

        function getEmbedLink(link){
            if ( link.indexOf('watch?v=') == -1) {
                return link
            }
            else{
                link = link.replace('watch?v=', 'embed/')
                return link
            }
        }

        // document.addEventListener("keyup", function(e){
        //     // if(document.getElementById('menu_div') != null){
        //     //     // document.getElementById('menu_div').remove();
        //     //     return;
        //     // }
        //     // if(e.keyCode != "13"){
        //         isSaved = false;
        //         if( document.getElementById('menu_div') != null){
        //             document.getElementById('menu_div').remove();
        //             // for(var i=0; i< document.getElementsByClassName('menu').length; i++){
        //             //     document.getElementsByClassName('menu')[i].remove();
        //             // }
        
        //         }
        
        //     // if(e.keyCode == '13'){
        //         var menu_div = document.createElement("span")
        //         menu_div.setAttribute("contenteditable",'false')
        //         menu_div.id = "menu_div"
        //         var plus = document.createElement('button')
        //         plus.className = "btn"
        //         plus.id = "plus_btn"
        //         var plus_i = document.createElement("i")
        //         plus_i.classList = "fa fa-plus"
        //         plus.appendChild(plus_i)
        //         var close = document.createElement('button')
        //         close.classList = "btn menu"
        //         close.id = "close_btn"
        //         var close_i = document.createElement("i")
        //         close_i.classList = "fa fa-close"
        //         close.appendChild(close_i)
        //         var image = document.createElement('button')
        //         image.classList = "btn menu"
        //         var image_i = document.createElement("i")
        //         image_i.classList = "fa fa-camera"
        //         var input = document.createElement('input')
        //         input.setAttribute('type', 'file')
        //         input.setAttribute('id','inpfile_input')
        //         input.setAttribute('onchange', 'addLocalImage(this)')
        //         image_i.appendChild(input)
        //         // <input type='file' id='inpfile' accept="image/jpeg, image/png, image/gif">
        //         // image_i.appendChild()
        //         image.appendChild(image_i)
        //         var un = document.createElement('button')
        //         un.classList = "btn menu "
        //         un.id = "un"
        //         un.setAttribute("onclick","inputvar(this)")
        //         var un_i = document.createElement("i")
        //         un_i.classList = "fa fa-search"
        //         un.appendChild(un_i)
        //         var pe = document.createElement('button')
        //         pe.classList = "btn menu "
        //         pe.id = "pe"
        //         pe.setAttribute("onclick","inputvar(this)")
        //         var pe_i = document.createElement("i")
        //         pe_i.classList = "fa fa-search"
        //         pe.appendChild(pe_i)
        //         menu_div.appendChild(plus)
        //         menu_div.appendChild(close)
        //         menu_div.appendChild(image)
        //         menu_div.appendChild(un)
        //         menu_div.appendChild(pe)
                
        //         if(fx().innerHTML == "<br>" || fx().innerHTML == "&nbsp;" || fx().innerHTML == '<br>' +  menu_div.innerHTML){
        //         if( document.getElementById('plus_btn') != null){
        //             document.getElementById('plus_btn').remove();
        //         }
        //         fx().innerHTML = ""
            
        //         fx().appendChild(menu_div)
        //         fx().innerHTML += "&nbsp;"
        //         var el = document.getElementById("editable")
        //         var range = document.createRange()
        //         var sel = window.getSelection()
        //         range.setStart(fx(), 2)
        //         range.collapse(true)
                
        //         sel.removeAllRanges()
        //         sel.addRange(range)
                
        //         document.getElementById('plus_btn').addEventListener('click', function(){
        //                 this.style.display = 'none'
        //                 var menu = document.getElementsByClassName('menu')
        //                 for(var i=0; i< menu.length; i++){
        //                     menu[i].style.display = 'inline'
        //                 }
                        
        //             })
                
        //             document.getElementById('close_btn').addEventListener('click', function(){
        //                 document.getElementById('plus_btn').style.display = 'inline'
        //                 var menu = document.getElementsByClassName('menu')
        //                 for(var i=0; i< menu.length; i++){
        //                     menu[i].style.display = 'none'
        //                 }
                        
        //             })
        //     }
        //     // <div id="menu_div" style="display: none;">
        //     //         <button class="btn" id="plus_btn" title="Add menu"><i class="fa fa-plus"></i></button>
        //     //         <button class="btn menu" id="close_btn" title="Close menu"><i class="fa fa-close"></i></button>
        //     //         <button class="btn menu" title="Add a image"><i class="fa fa-camera"></i></button>
        //     //         <button class="btn menu" title="Sarch Unsplash"><i class="fa fa-search"></i></button>
        //     //         <button class="btn menu" title="Search Pexels"><i class="fa fa-search"></i></button>
        //     //     </div>
        //     }
        // }
        //)

        var span_text
            document.addEventListener("keypress", function(e){

                // x = getCaretCoordinates()[0]
                // y = getCaretCoordinates()[1]
                if(e.keyCode == '13'){
                //     if(fx().className == "input" && document.getElementsByClassName('input') != null){
                //     implementUnsplashSearch(query = fx().innerHTML)
                //     return; 
                    
                // }
            if( document.getElementById('input_iframe')){
                var embed_link = getEmbedLink(document.getElementById('input_iframe').value)
                var pre = document.createElement('iframe')
                pre.id = "iframe_video"
                pre.setAttribute('src', embed_link)
                fx().appendChild(pre)
                document.getElementById('input_iframe').remove();
            }
                

               

                if(fx().className == 'fig-caption' && document.getElementsByClassName('fig-caption') != null && document.getElementsByClassName('fig-caption').length >= document.getElementsByClassName('fig').length){
                    // e.preventDefault()
                    
                    var p =document.createElement('p')
                    p.innerHTML = "&nbsp;"
                    // p.style.display = "none"
                    fx().parentNode.parentNode.append(p)
                    var el = document.getElementById("editable")
                    var range = document.createRange()
                    var sel = window.getSelection()
                    e.preventDefault();
                    range.setStart(fx().parentNode.nextSibling, 0)
                    range.collapse(true)
                    
                    sel.removeAllRanges()
                    sel.addRange(range)
                    //
                    
                }
            }
            });

function fx(){

  var target=null;
  if(window.getSelection)
  {
    target=window.getSelection().getRangeAt(0).commonAncestorContainer;
    return((target.nodeType===1)?target:target.parentNode);
  }
//   else if(document.selection)
//   {
//     var target=document.selection.createRange().parentElement();
//   }
  return target;
}
           
            document.execCommand('defaultParagraphSeparator', false, 'p');

            function setImgurHeader(xhr) {  
                        // xhr.setRequestHeader('Cache-Control', null) 
                        // xhr.setRequestHeader("Origin, X-Requested-With, Content-Type, Accept, Authorization, Token");
                        // xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
                        // xhr.setRequestHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH');
                        // xhr.setRequestHeader('Origin, X-Requested-With, Content-Type, Accept, Authorization, Authentication');
                        // xhr.setRequestAhorization
                        xhr.setRequestHeader('Authorization', 'Client-ID {{IMGUR_CLIENT_ID_DEBUG}}') 
                        xhr.setRequestHeader('Authorization','Bearer {{IMGUR_BEARER_DEBUG}}');
                        // xhr.setRequestHeader('Authorization')
                        // xhr.setRequestHeader('Authorization', 'Bearer 7cd876bf6ab3405bad138d3a1886a3048fe9a0f0')
                        }

                        $( document ).ready(function(){
                            $('#inpfile').on('change', function(){
                                    var targetDiv=document.getElementsByClassName("editor")[0];
                                    var file = $(this).prop('files')[0];
                                    var img=document.createElement("img");
                                    img.className="image"
                                    var reader  = new FileReader();
                                    var fig = document.createElement('figure')
                                    var fig_caption = document.createElement('figcaption')
                                    fig_caption.className = "fig-caption"
                                    // fig_caption.setAttribute("contenteditable", "true")
                                    fig_caption.innerHTML =  "Write your caption here!"
                                    // var span = document.createElement('span')
                                    // span.innerHTML = "h"
                                    // fig_caption.appendChild(span)
                                    fig.className = "fig"
                                    fig.setAttribute('contenteditable','true')
                                    
                                    // fig_caption.setAttribute("onclick",'this.innerHTML=""')
                                    fig.appendChild(img);
                                    fig.appendChild(fig_caption)
                                    if(fx().className == 'editor' ||  document.body === fx()){
                                        // console.log('2')
                                        fx().insertBefore(fig, fx().childNodes[1]);
                                        // targetDiv.appendChild(fig)
                                        // fx().insertBefore(fig, fx().nextSibling);
                                    }
                                    else{
                                        console.log('1')
                                        fx().parentNode.insertBefore(fig, fx().nextSibling);
                                    }
            
                                    
                                    // targetDiv.append(fig);
                                    // $(fig).insertAfter(fx());
                                    // targetDiv.insertBefore(fig, fig.nextSibling);
                                    
                                    // var p =document.createElement('p')
                                    // // p.setAttribute("onclick",'this.style.display = "none"')
                                    // p.innerHTML = "&nbsp;"
                                    // targetDiv.append(p)
                        //             fig_captio.addEventListener('keydown', event => {
                        // if (event.key === 'Enter') {
                        // document.execCommand('insertLineBreak')
                        // event.preventDefault()
                        // }
                        // })
                                    reader.addEventListener("load", function () {
                                        img.src=reader.result;
                                       
                                        // var image = document.createElement('img')
                                        
                                        // fig_caption.appendChild(a)
                                        // fig_caption.innerHTML += "on Unsplash"
                                    }); 
                                    if (file)
                                        reader.readAsDataURL(file);
                                    document.getElementById('inpfile').value = "";
                            });
                        });

                        function addImage(e, url, name){
                            // console.log("click")
                            var fig = document.createElement('figure')
                            var image = document.createElement('img')
                            var fig_caption = document.createElement('figcaption')
                            fig_caption.className = "fig-caption"
                            fig.className = "fig"
                            fig_caption.innerHTML = "Photo by " 
                            var a = document.createElement('a')
                            a.setAttribute("contenteditable", "false")
                            a.setAttribute("target", "_blank")
                            a.href = url    
                            a.innerHTML = name
                            fig_caption.appendChild(a)
                            fig_caption.innerHTML += " on " 
            
                            var unsplash_a = document.createElement('a')
                            unsplash_a.setAttribute("contenteditable", "false")
                            unsplash_a.setAttribute("target", "_blank")
                            if(url.indexOf('pexels.com') !=-1){
                                unsplash_a.href = "https://www.pexels.com/"
                                unsplash_a.innerHTML = "Pexels"
                            }
                            else{
                                unsplash_a.href = "https://unsplash.com/"
                                unsplash_a.innerHTML = "Unsplash"
                            }
                            
                            fig_caption.appendChild(unsplash_a)
            
            
             
                            image.src = e.src
                            image.className = "image"
                            fig.appendChild(image)
                            fig.appendChild(fig_caption)
                            if(fx().className == 'editor' ||  document.body === fx()){
                                        console.log('2')
                                        fx().insertBefore(fig, fx().childNodes[0]);
                                        // targetDiv.appendChild(fig)
                                        // fx().insertBefore(fig, fx().nextSibling);
                                    }
                                    else{
                                        console.log('1')
                                        fx().parentNode.insertBefore(fig, fx().nextSibling);
                                    }
                            
                            document.getElementsByClassName('editor')[0].appendChild(fig)
            
                            document.getElementsByClassName('grid')[0].remove()
                            document.getElementsByClassName('buttons')[0].remove()
                            // document.execCommand('insertImage', false, e.src)
                            
                            
                        }