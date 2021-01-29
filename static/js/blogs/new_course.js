// function addChapter(event) {
//     let error = 0;
//     let focus_on = null;
//     // for (var i = 0; i < document.getElementsByClassName("chapter_div").length; i++) {
//     var elem = document.getElementById('chapter_left_button');
//     elem.parentNode.removeChild(elem);
//     var elem = document.getElementById('chapter_right_button');
//     elem.parentNode.removeChild(elem);
//     var elem = document.getElementById('chapter_add_button');
//     elem.parentNode.removeChild(elem);

//     div = document.getElementById("chapter_main_div");
//     new_div = document.createElement('div');
//     new_div.setAttribute("style", "color: black;");
//     new_div.setAttribute("class", "chapter_div");
//     new_div.setAttribute("id", "chapter_div_" + counter)
//     new_div.innerHTML += '<br><br>' + document.getElementsByClassName("chapter_div")[0].innerHTML + '<button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createDifficultyPage()">Next</button><button id="chapter_add_button" type="button" class="btn btn-primary" style="float: right;" onclick="addChapter()">Add</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createDescriptionPage()">Previous</button>';

//     div.appendChild(new_div);
//     document.getElementsByClassName("chapter_h2_heading")[chapter_count - 1].innerHTML = "Chapter " + chapter_count;
//     chapter_innerHTML = div.innerHTML;
//     counter += 1;
//     chapter_count += 1;

// };
// var title = ""
// var description = 
function showhide(id) {
    if (document.getElementById) {
        var divid = document.getElementById(id);
        var divs = document.getElementsByClassName("to_hide");
        for (var i = 0; i < divs.length; i++) {
            divs[i].style.display = "none";
            divs[i].style.visiblity = "hidden";
            if (divs[i] != divid) {
                divs[i].innerHTML = "";
            };
        }
        divid.style.visibility = "visible";
        divid.style.display = "block";
    }
};

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
    c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
    return c.substring(name.length, c.length);
    }
    }
    return "";
}

var languages_add = new Array();
function add_language(){
    
    var new_lang =document.getElementById("search_language").value;
    languages_add.push(new_lang)
    saveDraft("languages",languages_add, isAdded = true)
    // setTimeout(function(){location.reload();},50)
    
}

// var pre_reqs_add = new Array();
// function add_pre_req(){
    
//     var new_pre =document.getElementById("add_pre_req_input").value;
//     pre_reqs_add.push(new_pre)
//     saveDraft("pre_req",pre_reqs_add, isAdded = true)
//     // setTimeout(function(){location.reload();},50)
// }



function createDescriptionPage() {

    // alert("798")
    getLangPrereq();
    
        
    if (document.getElementById("title_input") != null) {

        title = document.getElementById("title_input").value;
        saveDraft("title", title);
        if (title.length == 0) {
            document.getElementById("error_title").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_title").style = "color: red;";
            return;
        }
        else {
            document.getElementById("error_title").innerHTML = "";
        }    
        

        if (document.getElementById("title_input").value == "") {
            document.getElementById("error_title").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_title").style = "color: red;";
            return;
        }
    }
    sessionStorage.setItem("pk", pk);
    // if (document.getElementById("chapter_div") != null) {
    //     for (var i = 0; i < document.getElementsByClassName("chapter_div").length; i++) {
    //         if (document.getElementsByClassName("heading")[i] != null) {
    //             let chapter_add = {};
    //             chapter_add['heading'] = document.getElementsByClassName("heading")[i].value;
    //             chapter_add['description'] = document.getElementsByClassName("description")[i].value;
    //             chapter_add['content'] = document.getElementsByClassName("content")[i].value;
    //             chapter_add['youtube_link'] = document.getElementsByClassName("youtube")[i].value;

    //             chapters[i] = chapter_add;
    //         }
    //     }
    // }
    //window.name = pk
    setTimeout(function(){sessionStorage.setItem('pk',pk);}, 100)

    showhide("2");
    var div_1 = document.getElementById("1");
    div_1.setAttribute("style", "display:none");
    div_1.innerHTML = "";

    var div_3 = document.getElementById("3");
    div_3.setAttribute("style", "display:none");
    div_3.innerHTML = "";

    div_4 = document.getElementById("4");
    div_4.setAttribute("style", "display: none;");
    div_4.innerHTML = "";

    div_6 = document.getElementById("6");
    div_6.setAttribute("style", "display: none;");
    div_6.innerHTML = "";
    
    var div = document.getElementById(2);

    if (div.innerHTML != "") {
        return false
    }
    var content = ""
    content += '<div class="container-fluid container-fluid1"><img src="/media/images/icon.png" class="icon1">' +
    '<h3>How about a working description?</h3>' + 
    "<h6>It's ok if you can't think of a good description now. You can change it later.</h6>" + 
    '<div class="search-bar">'+
    '<input type="text"  class="search-input" placeholder="FOR EXAMPLE" id="description_input" value="' + description + '"> ' 
    content += '<span id="error_description"></span>' +
                '</div>' 
document.getElementById('next_btn').setAttribute('onclick', 'createDifficultyPage();')
document.getElementById('prev_btn').setAttribute('style', 'display:inline;')
document.getElementById('prev_btn').setAttribute('onclick', 'createTitlePage()')
document.getElementById('current').innerHTML = 2
document.getElementsByClassName('progress-bar')[0].style = "width:28%"


    // div.setAttribute("class", "jumbotron text-center");
    content += "<h7>Add Languages</h7>";
    content += '<div style="color: black;">';
    content += '<select id="selectpicker" multiple data-live-search="true" style="display: block;color: black;">';
    var bold = "'bold'"
    var underline = "'underline'"
    var italic = "'italic'"
    var ordered = "'insertOrderedList'"

    


    content += '</select></div>'
    content += '<div class="search-bar">'
    content += '<input type="search" style = "color:black;" id="search_language" class="search-input" placeholder="Type here" onkeyup="getChapterSearches()"></input>'
    content += '<div id ="results_lang" ></div>'
    
    content += '</div>'
    content += '<span id="error_language"></span>';
    
    
    content += "<h8>Add Prerequisites</h8>";
    // content += '<div style="color: black;">';

    // //div.innerHTML += '<select id="selectpicker_prereq" multiple data-live-search="true" style="display: block;color: black;">' +
    // //'{% for pre_req in pre_reqs %}<option>{{pre_req}}</option>{% endfor %}' 
    // content += '<select id="selectpicker_prereq" multiple data-live-search="true" style="display: block;color: black;">'

    // content += '</select></div>'
    content += '<div class="search-bar">'
    content += '<button id="bold" onclick="document.execCommand(' + bold +')">B</button>'
    content += '<button id="underline" onclick="document.execCommand(' + italic +')">I</button>'
    content += '<button id="italic" onclick="document.execCommand(' + underline+')">U</button>'
    content += '<button id="bold" onclick="document.execCommand(' + ordered +')">Ordered</button>'
    content += '<button id="ordered-list" onclick="addLink()">add link</button>'
    content += '<div class="editor" contenteditable="true" spellcheck="false" >'
    content += pre_reqs
    content += '</div>'
    content += '<button onclick = "addPrereqs()">Add Prerequisites</button>'
    // content += '<span id="error_prereq" ></span>'
    content += '</div>'
    // div.setAttribute("class", "jumbotron text-center");
    div.innerHTML = content
    for(var i=0; i< languages_all.length; i++){
        document.getElementById("selectpicker").innerHTML += '<option>' + languages_all[i]['name'] + '</option>';
    }
    // for(var i=0; i< prereqs_all.length; i++){
    //     document.getElementById("selectpicker_prereq").innerHTML += '<option>' + prereqs_all[i]['name'] + '</option>'
    // }
    // document.getElementById('next_btn').setAttribute('onclick', 'createNumberOfHours()')
    // document.getElementById('prev_btn').setAttribute('onclick', 'createTitlePage()')
    // document.getElementById('current').innerHTML = 2
    // div.innerHTML += "<h2 style='color: black;'>DESCRIPTION </h2>";
    // div.innerHTML += '<input id="description_input" type="text" style="color: black"; value="' + description + '"><button type="button" class="btn btn-primary" style="float: left;" onclick="createTitlePage()">Previous</button> <button type="button" class="btn btn-primary" style="float: right;" onclick="createDifficultyPage()">Next</button><span id="error_description"></span>';
    
    if (document.getElementById("selectpicker") != null) {
        for (var i = 0; i < document.getElementById("selectpicker").length; i++) {
            option = document.getElementById("selectpicker").options[i];
            if (languages.includes(option.value) == true) {
                option.selected = true;
            }
        }
    }
    
    // if (document.getElementById("selectpicker_prereq") != null) {
    //     for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
    //         option = document.getElementById("selectpicker_prereq").options[i];
    //         if (pre_reqs.includes(option.value) == true) {
    //             option.selected = true;
    //         }
    //     }
    // }
    
}
document.execCommand('defaultParagraphSeparator', false, 'p');
function addLink(){
    var url = prompt("enter a valid url")
    document.execCommand("CreateLink", false, url);
}

function format(cmd){
    document.execCommand(cmd)
};
function addPrereqs(){
    pre_reqs = document.getElementsByClassName('editor')[0].innerText 
    saveDraft('pre_req', pre_reqs)
}
function addLanguage(e){
    
    
    languages.push(e.innerHTML)
    saveDraft("languages",languages)
}
function createTitlePage() {
    if( document.getElementById("description_input") != null) {
        description = document.getElementById("description_input").value;
    }
    

    var div_2 = document.getElementById("2")
    div_2.innerHTML = "";
    div_2.setAttribute("style", "display: none;")
    showhide("1");

    div_4 = document.getElementById("4");
    div_4.setAttribute("style", "display: none;");
    div_4.innerHTML = "";

    var div = document.getElementById("1");

    div.innerHTML += '<div class="container-fluid container-fluid1"><img src="/media/images/icon.png" class="icon1">' +
    '<h3>How about a working title?</h3>' + 
    "<h6>It's ok if you can't think of a good title now. You can change it later.</h6>" + 
    '<input type="text"  class="example1" placeholder="FOR EXAMPLE" id="title_input" value="' + title + '"> ' +  
    '<br><span id="error_title"></span></div>'
    document.getElementById('next_btn').setAttribute('onclick', 'createDescriptionPage();')
    document.getElementById('prev_btn').setAttribute('style', 'display:none')
    document.getElementById('current').innerHTML = 1
    document.getElementsByClassName('progress-bar')[0].style = "width:14% !important"
    // div.setAttribute("class", "jumbotron text-center") ;
    // div.innerHTML += "<h2 style='color: black;'>TITLE PAGE</h2>" + "<input id='title_input' type='text' style='color: black;' value='" + title +  "'  required>" + '<span id="error_title"></span>' + ' <button type="button" class="btn btn-primary" style="float: right;" onclick="createDescriptionPage();">Next</button>'
    // document.getElementById("title_input").dataset.state = 'invalid';
}


var view_count =0 
// function createChapterPage() {
    
    // if (document.getElementById("description_input") != null) {
    //     description = document.getElementById("description_input").value;
    //     if (document.getElementById("description_input").value == "") {
    //         document.getElementById("error_description").innerHTML = "Cannot Be Empty!";
    //         document.getElementById("error_description").style = "color: red;";
    //         return;
    //     }
    //     else {
    //         document.getElementById("error_description").innerHTML = "";
    //     }
        
    // }
    
    
    
    // if(document.getElementById("selectpicker") != null) {
    //     languages = [];
    //     for (var i=0; i < document.getElementById("selectpicker").length; i++ ) {
    //         if (document.getElementById("selectpicker")[i].selected) {
    //             languages.push(document.getElementById("selectpicker")[i].innerHTML);
    //         }
    //     }
    //     saveDraft("languages",languages)
    //     if (languages.length == 0) {
    //         document.getElementById("error_language").innerHTML = "Cannot Be Empty!";
    //         document.getElementById("error_language").style = "color: red;";
    //         return;
    //     }
    //     else {
    //         document.getElementById("error_language").innerHTML = "";
    //     }
        
    // }

    // if (document.getElementById("selectpicker_prereq") != null) {
    //     pre_reqs = [];
    //     for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
    //         if (document.getElementById("selectpicker_prereq")[i].selected) {
    //             pre_reqs.push(document.getElementById("selectpicker_prereq")[i].innerHTML);
    //         }
    //     }
    //     saveDraft('pre_req',pre_reqs)
    //     if (pre_reqs.length == 0) {
    //         document.getElementById("error_prereq").innerHTML = "Cannot Be Empty!";
    //         document.getElementById("error_prereq").style = "color: red;";
    //         return;
    //     }
    //     else {
    //         document.getElementById("error_prereq").innerHTML = "";
    //     }

    // }
    // saveDraft("description", description);

//     view_count += 1
//     //alert(description)
   
//     //alert(pk)
//     sessionStorage.setItem("pk", pk);
//     //document.cookie = "pk=" + pk;
    
//     showhide("4");
//     div_1 = document.getElementById("1");
//     div_1.setAttribute("style", "display: none;");
//     div_1.innerHTML = "";

//     div_2 = document.getElementById("2");
//     div_2.setAttribute("style", "display: none;");
//     div_2.innerHTML = "";

//     div_3 = document.getElementById("3");
//     div_3.setAttribute("style", "display: none;");
//     div_3.innerHTML = "";

//     div_5 = document.getElementById("5");
//     div_5.setAttribute("style", "display: none;");
//     div_5.innerHTML = "";

//     div_6 = document.getElementById("6");
//     div_6.setAttribute("style", "display: none;");
//     div_6.innerHTML = "";



//     var div = document.getElementById("4");
//     div.setAttribute("class", "jumbotron text-center") ;
//     div.innerHTML +="<h2 style='color: black;'> CHAPTER PAGE</h2>" ;
//     div.innerHTML += '<div id="chapter_main_div" ><div style="color: black;" class="chapter_div" class="current_chapter" id="chapter_div_0">' + 
//             '<h2 class="chapter_h2_heading">Chapter 1</h2><div>' +
//                 '<span>Heading</span>' +
//                 '<input class="heading chapter" id="heading" type="text" required>' +
//                 '<span class="error_heading"></span>' + 
//             '</div>' +
//             '<div>' +
//                 '<span>Description</span>' +
//                 '<input class="description chapter" id="description" type="text" required>' +
//                 '<span class="error_description"></span>' + 
//             '</div>' +
//             '<div>' +
//                 '<span>content</span>' +
//                 '<input class="content chapter" id="content" type="text" required>' +
//                 '<span class="error_content"></span>' + 
//             '</div>' +
//             '<div>' +
//                 '<span>Youtube Link</span>' +
//                 '<input type="url"  id="youtube" class="youtube chapter" required >' + 
//                 '<span class="error_youtube"></span>' +
//             '</div>' ;
//     if (chapter_innerHTML != "") {
//         document.getElementById("chapter_main_div").innerHTML = '<br><br>' + chapter_innerHTML ;   
//     }    
//     else {
//         div.innerHTML += '<button id="chapter_add_button" type="button" class="btn btn-primary" style="float: right;" onclick="addChapter()">Add</button><button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createDifficultyPage()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createDescriptionPage()">Previous</button></div></div>';
//     }

//     // if (document.getElementById('heading') != null) { 
        
//         for (var i=0; i< chapters.length; i++) {
            
//             document.getElementsByClassName("heading")[i].value = chapters[i]['heading'];
//             document.getElementsByClassName("description")[i].value = chapters[i]['description'];
//             document.getElementsByClassName("content")[i].value = chapters[i]['content'];
//             document.getElementsByClassName("youtube")[i].value = chapters[i]['youtube_link'];
//             if( view_count == 1){
//                 if(i < chapters.length-1){addChapter()}
//             }
//         }
//     // }
    
// }

function createOverviewPage() {
    if (document.getElementsByClassName("male") != null) {
        for (var i = 0; i < document.getElementsByClassName("male").length; i++) {
            if (document.getElementsByClassName("male")[i].checked) {
                difficulty_level = document.getElementsByClassName("male")[i].value
            }
        }
    }
    saveDraft('difficulty_level', difficulty_level)
    // if (document.getElementById("selectpicker_prereq") != null) {
    //     pre_reqs = [];
    //     for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
    //         if (document.getElementById("selectpicker_prereq")[i].selected) {
    //             pre_reqs.push(document.getElementById("selectpicker_prereq")[i].innerHTML);
    //         }
    //     }

    // }
    var div_1 = document.getElementById("1")
    div_1.innerHTML = "";
    div_1.setAttribute("style", "display: none;")

    var div_2 = document.getElementById("2")
    div_2.innerHTML = "";
    div_2.setAttribute("style", "display: none;")

    var div_3 = document.getElementById("3")
    div_3.innerHTML = "";
    div_3.setAttribute("style", "display: none;")

    var div_4 = document.getElementById("4")
    div_4.innerHTML = "";
    div_4.setAttribute("style", "display: none;")

    var div_5 = document.getElementById("5")
    div_5.innerHTML = "";
    div_5.setAttribute("style", "display: none;")

    var div_6 = document.getElementById("6")
    div_6.innerHTML = "";
    div_6.setAttribute("style", "display: none;")

    var div_9 = document.getElementById("9")
    div_9.innerHTML = "";
    div_9.setAttribute("style", "display: none;")

    var div_8 = document.getElementById("8")
    div_8.innerHTML = "";
    div_8.setAttribute("style", "display: none;")

    showhide("7");

    var div = document.getElementById("7");
    // div.setAttribute("class", "jumbotron text-center");
    div.innerHTML +='<div class="container-fluid container-fluid1"><img src="/media/images/icon.png" class="icon1">' +
    '<h3>How about a working overview?</h3>' + 
    "<h6>It's ok if you can't think of a good overview now. You can change it later.</h6>" + 
    '<input type="text"  class="example1" placeholder="FOR EXAMPLE" id="overview_input" value="' + overview + '"> ' + 
    '</div>'
    div.innerHTML += " <span id='error_overview'></span>"
    document.getElementById('next_btn').setAttribute('onclick', 'createImagePage();')
    document.getElementById('prev_btn').setAttribute('onclick', 'createDifficultyPage();')
    document.getElementById('current').innerHTML = 4
    document.getElementsByClassName('progress-bar')[0].style = "width:56%"

}



function createImagePage() {
    if (document.getElementById("overview_input") != null) {
        overview = document.getElementById("overview_input").value;
        saveDraft('overview',overview);
        if (document.getElementById("overview_input").value == "") {
            document.getElementById("error_overview").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_overview").style = "color: red;";
            return;
        }
    }

    if (document.getElementsByClassName("male_time") != null) {
        for (var i = 0; i < document.getElementsByClassName("male_time").length; i++) {
            if (document.getElementsByClassName("male_time")[i].checked) {
                no_of_hours = document.getElementsByClassName("male_time")[i].value
            }
        }
    }
        //saveDraft('no_of_hours',parseInt(no_of_hours))
    
    showhide("9")
    div_1 = document.getElementById("1");
    div_1.setAttribute("style", "display: none;");
    div_1.innerHTML = "";

    div_2 = document.getElementById("2");
    div_2.setAttribute("style", "display: none;");
    div_2.innerHTML = "";

    div_3 = document.getElementById("3");
    div_3.setAttribute("style", "display: none;");
    div_3.innerHTML = "";

    div_4 = document.getElementById("4");
    div_4.setAttribute("style", "display: none;");
    div_4.innerHTML = "";

    div_5 = document.getElementById("5");
    div_5.setAttribute("style", "display: none;");
    div_5.innerHTML = "";

    div_6 = document.getElementById("6");
    div_6.setAttribute("style", "display: none;");
    div_6.innerHTML = "";

    div_7 = document.getElementById("7");
    div_7.setAttribute("style", "display: none;");
    div_7.innerHTML = "";

    div_8 = document.getElementById("8");
    div_8.setAttribute("style", "display: none;");
    div_8.innerHTML = "";

    div_10 = document.getElementById("10");
    div_10.setAttribute("style", "display: none;");
    div_10.innerHTML = "";



    div = document.getElementById("9")
    div.setAttribute("class", "jumbotron text-center");

    div.innerHTML += "<h2 style='color: black;'> ADD IMAGE PAGE</h2>";
    div.innerHTML += '<div style="color: black;" id="image_input_div">';
    div.innerHTML += '<input id="image_input" type="file" onchange="checkImage()" style="color: black;" id="image_input">';
    // div.innerHTML += '<button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createNumberOfHours()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createOverviewPage()">Previous</button>';
    document.getElementById('next_btn').setAttribute('onclick', 'createNumberOfHours();')
    document.getElementById('prev_btn').setAttribute('onclick', 'createOverviewPage();')
    document.getElementById('current').innerHTML = 5
    document.getElementsByClassName('progress-bar')[0].style = "width:70%"
    if(image != "None"){
        // alert(image)
        div.innerHTML += '<img id="project_image">';
        document.getElementById('project_image').src =image
    }

}
// if(document.getElementById('project_image')){
//     alert('h')
// }

function checkImage(){
    if(document.getElementsByClassName('image').length>0){
        // alert(document.getElementsByClassName('image').length)
        deleteImage(document.getElementById('image_input'))
    }
    addLocalImage(document.getElementById('image_input'))
}
function createNumberOfHours() {
    saveImageDraft()
    showhide("10");
    div_1 = document.getElementById("1");
    div_1.setAttribute("style", "display: none;");
    div_1.innerHTML = "";

    div_2 = document.getElementById("2");
    div_2.setAttribute("style", "display: none;");
    div_2.innerHTML = "";

    div_3 = document.getElementById("3");
    div_3.setAttribute("style", "display: none;");
    div_3.innerHTML = "";

    div_4 = document.getElementById("4");
    div_4.setAttribute("style", "display: none;");
    div_4.innerHTML = "";

    div_5 = document.getElementById("5");
    div_5.setAttribute("style", "display: none;");
    div_5.innerHTML = "";

    div_7 = document.getElementById("7");
    div_7.setAttribute("style", "display: none;");
    div_7.innerHTML = "";

    div_8 = document.getElementById("8");
    div_8.setAttribute("style", "display: none;");
    div_8.innerHTML = "";

    div_9 = document.getElementById("9");
    div_9.setAttribute("style", "display: none;");
    div_9.innerHTML = "";

    div = document.getElementById("10");
    var content = ""
    content += "<div class='container-fluid container-fluid1'><img src='/media/images/no_of_hours.png' class='icon1'>"
    content += "<h3> ADD HOURS REQUIRED FOR THE PROJECT</h3>";
    content += '<div style="color: black;">'  ;
    content += '<div class="dot><input class="male_time" type="radio" id="0-2" name="" value="0.2" style="opacity: 1;">' +
        '<label for="0--2">0--2 HOURS</label>' +
        '<input class="male_time" type="radio" id="2-4" name="" value="2.4"  style="opacity: 1;">' +
        '<label for="2-4">2-4 HOURS</label>' +
        '<input class="male_time" type="radio" id=">4" name="" value=".4" style="opacity: 1;">' +
        '<label for=">4">MORE THAN 4 HOURS</label></div></div>';
    // div.innerHTML += '<button id="difficulty_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createProject();">Create</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createImagePage()">Previous</button>' +
    //     '</div>';
    div.innerHTML = content
    if(no_of_hours == "0.2"){
        document.getElementById('0-2').checked = true;
    }
    else if(no_of_hours == "2.4"){
        console.log(80)
        document.getElementById('2-4').checked = true;
    }
    else if(no_of_hours == "0.4"){
        document.getElementById('>4').checked = true;
    }
    document.getElementById('next_btn').setAttribute('onclick', 'createChapterPage()')
    document.getElementById('prev_btn').setAttribute('onclick', 'createImagePage();')
    document.getElementById('current').innerHTML = 6;
    document.getElementsByClassName('progress-bar')[0].style = "width:84%"

}


function createDifficultyPage() {

        if (document.getElementById("description_input") != null) {
        description = document.getElementById("description_input").value;
        if (document.getElementById("description_input").value == "") {
            document.getElementById("error_description").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_description").style = "color: red;";
            return;
        }
        else {
            document.getElementById("error_description").innerHTML = "";
        }
        
    }
    // alert(description)
    saveDraft("description", description);
    if(document.getElementById("selectpicker") != null) {
        languages = [];
        for (var i=0; i < document.getElementById("selectpicker").length; i++ ) {
            if (document.getElementById("selectpicker")[i].selected) {
                languages.push(document.getElementById("selectpicker")[i].innerHTML);
            }
        }
        saveDraft("languages",languages)
        if (languages.length == 0) {
            document.getElementById("error_language").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_language").style = "color: red;";
            return;
        }
        else {
            document.getElementById("error_language").innerHTML = "";
        }
        
    }
    saveDraft('pre_req',pre_reqs)
    // if (document.getElementById("selectpicker_prereq") != null) {
    //     pre_reqs = [];
    //     for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
    //         if (document.getElementById("selectpicker_prereq")[i].selected) {
    //             pre_reqs.push(document.getElementById("selectpicker_prereq")[i].innerHTML);
    //         }
    //     }
    //     
    //     if (pre_reqs.length == 0) {
    //         document.getElementById("error_prereq").innerHTML = "Cannot Be Empty!";
    //         document.getElementById("error_prereq").style = "color: red;";
    //         return;
    //     }
    //     else {
    //         document.getElementById("error_prereq").innerHTML = "";
    //     }
       
    // }
    // saveDraft("description", description);

    // let error = 0;
    // let focus_on = null;
    // for (var i = 0; i < document.getElementsByClassName("chapter_div").length; i++) {
    //     if (document.getElementById('heading') != null) {
    //         var chapter_add = {};
    //         let chapter = new Chapter(document.getElementsByClassName("heading")[i].value, document.getElementsByClassName("description")[i].value, document.getElementsByClassName("content")[i].value, document.getElementsByClassName("youtube")[i].value, pk)
    //         chapter_add['heading'] = document.getElementsByClassName("heading")[i].value;
    //         chapter_add['description'] = document.getElementsByClassName("description")[i].value;
    //         chapter_add['content'] = document.getElementsByClassName("content")[i].value; 
    //         chapter_add['youtube_link'] = document.getElementsByClassName("youtube")[i].value;
    //         chapter_add['author'] = author
    //         chapter_add['link_to'] = pk
            
    //         chapters[i] = chapter_add;
    //         if (document.getElementsByClassName("heading")[i].checkValidity() == false) {
    //             document.getElementsByClassName("error_heading")[i].innerHTML = "Not Valid!" 
    //             document.getElementsByClassName("error_heading")[i].style = "color: red;";
    //             error = 1;
    //             if (focus_on == null) {
    //                 document.getElementsByClassName("heading")[i].scrollIntoView({ block: "center" });
    //                 focus_on = "heading";
    //             }
    //         }
    //         else {
    //             document.getElementsByClassName("error_heading")[i].innerHTML = "" 
    //         }
    //         if (document.getElementsByClassName("description")[i].checkValidity() == false) {
    //             document.getElementsByClassName("error_description")[i].innerHTML = "Not Valid!" 
    //             document.getElementsByClassName("error_description")[i].style = "color: red;";
    //             if (focus_on == null) {
    //                 document.getElementsByClassName("description")[i].scrollIntoView({ block: "center" });
    //                 focus_on = "description";
    //             }
    //         }
    //         else {
    //             document.getElementsByClassName("error_description")[i].innerHTML = ""
    //         }
    //         if (document.getElementsByClassName("content")[i].checkValidity() == false) {
    //             document.getElementsByClassName("error_content")[i].innerHTML = "Not Valid!" 
    //             document.getElementsByClassName("error_content")[i].style = "color: red;";
    //             error = 1;
    //             if (focus_on == null) {
    //                 document.getElementsByClassName("content")[i].scrollIntoView({ block: "center" });
    //                 focus_on = "content";
    //             }
    //         }
    //         else {
    //             document.getElementsByClassName("error_content")[i].innerHTML = ""
    //         }
    //         if (document.getElementsByClassName("youtube")[i].checkValidity() == false) {
    //             document.getElementsByClassName("error_youtube")[i].innerHTML = "Not Valid!" 
    //             document.getElementsByClassName("error_youtube")[i].style = "color: red;";
    //             error = 1;
    //             if (focus_on == null) {
    //                 document.getElementsByClassName("youtube")[i].scrollIntoView({ block: "center" });
    //                 focus_on = "youtube";
    //             }
    //         }
    //         else {
    //             document.getElementsByClassName("error_youtube")[i].innerHTML = "" 
    //         }
            
    //         //chapters.push(chapter)            
    //     }
    // }

    // if (error == "1") {
    //     return;
    // }

    // saveChapterDraft();
    
    if (document.getElementById("selectpicker") != null) {
        languages = [];
        for (var i = 0; i < document.getElementById("selectpicker").length; i++) {
            if (document.getElementById("selectpicker")[i].selected) {
                languages.push(document.getElementById("selectpicker")[i].innerHTML);
            }
        }
        if (languages.length == 0) {
            document.getElementById("error_language").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_language").style = "color: red;";
            return;
        }
        else {
            document.getElementById("error_language").innerHTML = "";
        }
    }

    if (document.getElementById("overview_input") != null) {
        overview = document.getElementById("overview_input").value;

    }


    showhide("6");
    div_1 = document.getElementById("1");
    div_1.setAttribute("style", "display: none;");
    div_1.innerHTML = "";

    div_2 = document.getElementById("2");
    div_2.setAttribute("style", "display: none;");
    div_2.innerHTML = "";

    div_3 = document.getElementById("3");
    div_3.setAttribute("style", "display: none;");
    div_3.innerHTML = "";

    div_4 = document.getElementById("4");
    div_4.setAttribute("style", "display: none;");
    div_4.innerHTML = "";

    div_5 = document.getElementById("5");
    div_5.setAttribute("style", "display: none;");
    div_5.innerHTML = "";

    div_7 = document.getElementById("7");
    div_7.setAttribute("style", "display: none;");
    div_7.innerHTML = "";

    div_8 = document.getElementById("8");
    div_8.setAttribute("style", "display: none;");
    div_8.innerHTML = "";

    div_9 = document.getElementById("9");
    div_9.setAttribute("style", "display: none;");
    div_9.innerHTML = "";

    div_10 = document.getElementById("10");
    div_10.setAttribute("style", "display: none;");
    div_10.innerHTML = "";

    div = document.getElementById("6");
    var content = ""
    // div.setAttribute("class", "jumbotron text-center");
    content += "<div class='container-fluid container-fluid1'><img src='/media/images/no_of_hours.png' class='icon1'>"
    content += " <h3>Add difficulty level for the project</h3>";
    content += '<div style="color: black;">';
    content += '<div class="dot">'+
                    '<input class="male" type="radio" id="easy"   name="diff" value="EASY"   style="opacity: 1;">' +
                    '<label style="font-size:18px;" for="easy">EASY</label>' +           
                     '<input class="male" type="radio" id="medium" name="diff" value="MEDIUM" style="opacity: 1;">' +
                     '<label style="font-size:18px;" for="medium">MEDIUM</label>' +
                     '<input class="male" type="radio" id="hard"   name="diff" value="HARD"   style="opacity: 1;">' +
                     '<label style="font-size:18px;" for="hard">HARD</label>' +'</div></div>';
    // div.innerHTML += '<button id="difficulty_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createOverviewPage()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createDescriptionPage()">Previous</button>' +
    //     '</div>';
    div.innerHTML = content
    if(difficulty_level == "EASY"){
        document.getElementById('easy').checked = true;
    }
    else if(difficulty_level == "MEDIUM"){
        console.log(80)
        document.getElementById('medium').checked = true;
    }
    else if(difficulty_level == "HARD"){
        document.getElementById('hard').checked = true;
    }

    document.getElementById('next_btn').setAttribute('onclick', 'createOverviewPage();')
    document.getElementById('prev_btn').setAttribute('onclick', 'createDescriptionPage();')
    document.getElementById('current').innerHTML = 3;
    document.getElementsByClassName('progress-bar')[0].style = "width:42%"

}

function assignParam(
    title = null,
    description = null,
    difficulty_level = null,
    no_of_hours = null,
    languages = null,
    overview = null,
    pre_reqs = null,
    pk = null,
    counter = null,
    chapter_innerHTML = null,
    chapter_count = null,
    image = null,
    author = null

    ){
        var title = title;
        var description = description;
        var difficulty_level = difficulty_level;
        var no_of_hours = no_of_hours;
        var languages = languages;
        var overview = overview;
        var pre_reqs = pre_reqs;
        var pk = pk;
        var counter = counter;
        var chapter_innerHTML = chapter_innerHTML;
        var chapter_count = chapter_count;
        var image = image;
        var author = author
    };




