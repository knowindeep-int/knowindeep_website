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
      }
    }
    divid.style.visibility = "visible";
    divid.style.display = "block";
  }
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

var languages_add = new Array();
function add_language() {
  var new_lang = document.getElementById("search_language").value;
  languages_add.push(new_lang);
  saveDraft("languages", languages_add, (isAdded = true));
  // setTimeout(function(){location.reload();},50)
}

// var pre_reqs_add = new Array();
// function add_pre_req(){

//     var new_pre =document.getElementById("add_pre_req_input").value;
//     pre_reqs_add.push(new_pre)
//     saveDraft("pre_req",pre_reqs_add, isAdded = true)
//     // setTimeout(function(){location.reload();},50)
// }

function createDescriptionPage(e) {
  // alert(document.getElementById("title_input").innerText.replace(/\s/g, ''))
  if (document.getElementById("title_input")) {
    // alert("success")

    title = document.getElementById("title_input").value;

    if (title.length == 0) {
      document.getElementById("error_title").innerHTML = "Cannot Be Empty!";
      document.getElementById("error_title").style = "color: red;";
      return;
    } else {
      saveDraft("title", title);
      document.getElementById("error_title").innerHTML = "";
    }

    if (document.getElementById("title_input").value == "") {
      document.getElementById("error_title").innerHTML = "Cannot Be Empty!";
      document.getElementById("error_title").style = "color: red;";
      return;
    }
  }

  sessionStorage.setItem("pk", pk);
  if (e && e.id == "save_btn") {
    toastr.options.timeOut = 1000;
    toastr.success("Saved successfully!");
    var audio = new Audio("/media/copy.mp3");
    audio.volume = 0.5;
    audio.play();
    return;
  }
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
  setTimeout(function () {
    sessionStorage.setItem("pk", pk);
  }, 100);

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
    return false;
  }
  var content = "";
  content +=
    '<div class="container container-fluid container-fluid1"><img src="/media/images/icon.png" class="icon1">' +
    "<h3>How about a working description?</h3>" +
    // "<h6>It's ok if you can't think of a good description now. You can change it later.</h6>" +
    '<div class="search-bar">' +
    '<input type="text"  class="search-input" placeholder="Ex: App which lets you make notes" id="description_input" value="' +
    description +
    '"> ';
  content += '<span id="error_description"></span>' + "</div>";

  document
    .getElementById("save_btn")
    .setAttribute("onclick", "addPrereqs();createDifficultyPage(this);");
  document
    .getElementById("next_btn")
    .setAttribute("onclick", "addPrereqs();createDifficultyPage(this);");
  document.getElementById("prev_btn").setAttribute("style", "display:inline;");
  document
    .getElementById("prev_btn")
    .setAttribute("onclick", "createTitlePage()");
  document.getElementById("current").innerHTML = 2;
  document.getElementsByClassName("w3-amber")[0].style = "width:28%";

  // div.setAttribute("class", "jumbotron text-center");
  content += "<h7>Add Languages</h7>";
  content += `<div id="langs" style="width: 68%;padding-bottom: 0; margin:10px auto; background-color:white ;text-align:left; border: 1px solid #dcdcdc; box-shadow: inset 1px 2px 8px rgb(0 0 0 / 7%);">
    <input type="search" class="pret" id="search_language" name="Languages"  placeholder="Type here" onkeyup="getChapterSearches()"> 
    </div>`;
  // content += '<div style="color: black;">';
  // content += '<select id="selectpicker" multiple data-live-search="true" style="display: block;color: black;">';
  // <span class="xyz mm">javascript1 <i id="1" class="fa fa-times" aria-hidden="true" onClick="die(event)"></i></span>
  // <span class="xyz">javascript2 <i id="2" class="fa fa-times" aria-hidden="true" onClick="die(event)"></i></span>
  // <span class="xyz">javascript3 <i id="3" class="fa fa-times" aria-hidden="true" onClick="die(event)"></i></span>
  var bold = "'bold'";
  var underline = "'underline'";
  var italic = "'italic'";
  var ordered = "'insertOrderedList'";
  console.log("heygdfg");
  setTimeout(() => {
    getLangPrereq();
  }, 10);

  //content += '</select></div>'
  content += '<div class="search-bar">';
  //content += '<input type="search" style = "color:black;" id="search_language" class="search-input" placeholder="Type here" onkeyup="getChapterSearches()"> <i id="1" class="fa fa-times" aria-hidden="true" onClick="die(event)"></i></input>'
  content += '<div id ="results_lang" ></div>';

  content += "</div>";
  content += '<div id="error_language"></div>';

  content += "<h8>Add Prerequisites</h8>";
  // content += '<div style="color: black;">';

  // //div.innerHTML += '<select id="selectpicker_prereq" multiple data-live-search="true" style="display: block;color: black;">' +
  // //'{% for pre_req in pre_reqs %}<option>{{pre_req}}</option>{% endfor %}'
  // content += '<select id="selectpicker_prereq" multiple data-live-search="true" style="display: block;color: black;">'

  // content += '</select></div>'
  content += '<div class="search-bar">';
  content += '<div class="top-bar12">';
  content +=
    '<button id="bold" onclick="document.execCommand(' +
    bold +
    ')"><i class="fas fa-bold"></i></button>';
  content +=
    '<button id="underline" onclick="document.execCommand(' +
    italic +
    ')"><i class="fas fa-italic"></i></button>';
  content +=
    '<button id="italic" onclick="document.execCommand(' +
    underline +
    ')"><i class="fas fa-underline" style="font-size: 17px;"></i></button>';
  content += '<span class="slash">|</span>';
  content +=
    '<button id="bold" onclick="document.execCommand(' +
    ordered +
    ')"><i class="fas fa-list-ol"></i></button>';
  content += '<span class="slash">|</span>';
  content +=
    '<button id="ordered-list" onclick="addLink()"><svg class="svg1" id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 531.8 534.09"><defs><style>.cls-1{fill:none;stroke:#000;stroke-miterlimit:10;stroke-width:30px;}</style></defs><path class="cls-1" d="M451.41,436,327.12,560.3c-37.9,37.9-42.61,94.64-10.51,126.74s88.84,27.39,126.74-10.51l44.86-41.59" transform="translate(-280.31 -224.63)"/><path class="cls-1" d="M488.21,399.21,616,271.45c37.9-37.91,94.64-42.61,126.74-10.52s27.39,88.84-10.52,126.74L688,431.88" transform="translate(-280.31 -224.63)"/><line class="cls-1" x1="348.12" y1="167.77" x2="165.47" y2="350.42"/><circle class="cls-1" cx="386.8" cy="389.09" r="130"/><line class="cls-1" x1="327.3" y1="389.09" x2="446.3" y2="389.09"/><line class="cls-1" x1="386.8" y1="448.59" x2="386.8" y2="329.59"/></svg></button>';
  content += "</div>";
  content += '<div class="editor" contenteditable="true" spellcheck="false" >';
  content += pre_reqs;
  content += "</div>";
  // content += '<button onclick = "addPrereqs()">Add Prerequisites</button>'
  content += '<div id="error_prereq" ></div>';
  content += "</div>";
  // div.setAttribute("class", "jumbotron text-center");
  div.innerHTML = content;
  // for(var i=0; i< languages_all.length; i++){
  //     document.getElementById("selectpicker").innerHTML += '<option>' + languages_all[i]['name'] + '</option>';
  // }
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
document.execCommand("defaultParagraphSeparator", false, "p");
function addLink() {
  var url = prompt("enter a valid url");
  document.execCommand("CreateLink", false, url);
}

function format(cmd) {
  document.execCommand(cmd);
}
function addPrereqs() {
  pre_reqs = document.getElementsByClassName("editor")[0].innerHTML;
  saveDraft("pre_req", pre_reqs);
}
function addLanguage(e) {
  languages.push(e.innerHTML);
  saveDraft("languages", languages);
  var num = document.getElementById("langs").childNodes.length;
  var d1 = document.getElementsByClassName("xyz")[num];
  d1.insertAdjacentHTML(
    "afterend",
    '<span class="xyz">' +
      e.innerHTML +
      '<i id="' +
      num +
      '" class="fa fa-times" aria-hidden="true" onClick="die(event)"></i></span>'
  );
}
function createTitlePage() {
  if (document.getElementById("description_input") != null) {
    description = document.getElementById("description_input").value;
  }

  var div_2 = document.getElementById("2");
  div_2.innerHTML = "";
  div_2.setAttribute("style", "display: none;");
  showhide("1");

  div_4 = document.getElementById("4");
  div_4.setAttribute("style", "display: none;");
  div_4.innerHTML = "";

  var div = document.getElementById("1");

  div.innerHTML +=
    '<div class="container container-fluid container-fluid1"><img src="/media/images/icon.png" class="icon1">' +
    "<h3>How about a working title?</h3>" +
    "<h6>It's ok if you can't think of a good title now. You can change it later.</h6>" +
    '<input type="text"  class="example1" placeholder="Ex: Notes App" id="title_input" value="' +
    title +
    '"> ' +
    '<br><span id="error_title"></span></div>';
  document
    .getElementById("save_btn")
    .setAttribute("onclick", "createDescriptionPage(this);");
  document
    .getElementById("next_btn")
    .setAttribute("onclick", "createDescriptionPage(this);");
  document.getElementById("prev_btn").setAttribute("style", "display:none");
  document.getElementById("prev_btn").setAttribute("style", "display:inline;");
  document
    .getElementById("prev_btn")
    .setAttribute("onclick", 'document.location.href = "/teach"');
  document.getElementById("current").innerHTML = 1;
  document.getElementsByClassName("w3-amber")[0].style = "width:14% !important";
  // div.setAttribute("class", "jumbotron text-center") ;
  // div.innerHTML += "<h2 style='color: black;'>TITLE PAGE</h2>" + "<input id='title_input' type='text' style='color: black;' value='" + title +  "'  required>" + '<span id="error_title"></span>' + ' <button type="button" class="btn btn-primary" style="float: right;" onclick="createDescriptionPage();">Next</button>'
  // document.getElementById("title_input").dataset.state = 'invalid';
}

var view_count = 0;
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

function createOverviewPage(e) {
  if (document.getElementsByClassName("male") != null) {
    for (var i = 0; i < document.getElementsByClassName("male").length; i++) {
      if (document.getElementsByClassName("male")[i].checked) {
        difficulty_level = document.getElementsByClassName("male")[i].value;
      }
    }
  }
  // if ($('input:checked').length == 0){
  //     document.getElementById("error_diff").innerHTML = "Cannot Be Empty!";
  //     document.getElementById("error_diff").style = "color: red;";
  //     return;
  // }
  saveDraft("difficulty_level", difficulty_level);
  // if (document.getElementById("selectpicker_prereq") != null) {
  //     pre_reqs = [];
  //     for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
  //         if (document.getElementById("selectpicker_prereq")[i].selected) {
  //             pre_reqs.push(document.getElementById("selectpicker_prereq")[i].innerHTML);
  //         }
  //     }

  // }
  if (e && e.id == "save_btn") {
    toastr.options.timeOut = 1000;
    toastr.success("Saved successfully!");
    var audio = new Audio("/media/copy.mp3");
    audio.volume = 0.5;
    audio.play();
    return;
  }
  var div_1 = document.getElementById("1");
  div_1.innerHTML = "";
  div_1.setAttribute("style", "display: none;");

  var div_2 = document.getElementById("2");
  div_2.innerHTML = "";
  div_2.setAttribute("style", "display: none;");

  var div_3 = document.getElementById("3");
  div_3.innerHTML = "";
  div_3.setAttribute("style", "display: none;");

  var div_4 = document.getElementById("4");
  div_4.innerHTML = "";
  div_4.setAttribute("style", "display: none;");

  var div_5 = document.getElementById("5");
  div_5.innerHTML = "";
  div_5.setAttribute("style", "display: none;");

  var div_6 = document.getElementById("6");
  div_6.innerHTML = "";
  div_6.setAttribute("style", "display: none;");

  var div_9 = document.getElementById("9");
  div_9.innerHTML = "";
  div_9.setAttribute("style", "display: none;");

  var div_8 = document.getElementById("8");
  div_8.innerHTML = "";
  div_8.setAttribute("style", "display: none;");

  showhide("7");

  var div = document.getElementById("7");
  // div.setAttribute("class", "jumbotron text-center");
  div.innerHTML +=
    '<div class=" container container-fluid container-fluid1"><img src="/media/images/icon.png" class="icon1">' +
    "<h3>How about a working overview?</h3>" +
    "<h6>It's ok if you can't think of a good overview now. You can change it later.</h6>" +
    '<input type="text"  class="example1" placeholder="Ex: App which lets you make notes" id="overview_input" value="' +
    overview +
    '"> ' +
    "</div>";
  div.innerHTML += " <div id='error_overview'></div>";
  document
    .getElementById("save_btn")
    .setAttribute("onclick", "createImagePage(this);");
  document
    .getElementById("next_btn")
    .setAttribute("onclick", "createImagePage(this);");
  document
    .getElementById("prev_btn")
    .setAttribute("onclick", "createDifficultyPage(this);");
  document.getElementById("current").innerHTML = 4;
  document.getElementsByClassName("w3-amber")[0].style = "width:56%";
}

function createImagePage(e) {
  if (document.getElementById("overview_input") != null) {
    overview = document.getElementById("overview_input").value;
    // saveDraft('overview',overview);
    if (document.getElementById("overview_input").value == "") {
      document.getElementById("error_overview").innerHTML = "Cannot Be Empty!";
      document.getElementById("error_overview").style = "color: red;";
      return;
    } else {
      saveDraft("overview", overview);
    }
  }
  if (e && e.id == "save_btn") {
    toastr.options.timeOut = 1000;
    toastr.success("Saved successfully!");
    var audio = new Audio("/media/copy.mp3");
    audio.volume = 0.5;
    audio.play();
    return;
  }

  showhide("9");
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

  div = document.getElementById("9");
  // div.setAttribute("class", "jumbotron text-center k");
  //     `
  //     <img src="icon.png" class="icon1">

  // <br>
  // <div >
  //   <img class="imgusr" src="imgg.jpg" >
  // </div>

  // <div class="xyz">xyz.jpg</div>
  // <br>
  //   <span class="button-img">
  //     <button class="button-size" type="button" onclick="alert('Hello world!')">Choose image</button>
  //   </span>
  //   <span class="button-img">
  //     <button class="button-size" type="button" onclick="alert('Hello world!')">Remove</button>
  //   </span>
  // </div>`
  div.innerHTML += `<div class="container-fluid container-fluid1 container"><img src='/media/images/no_of_hours.png' class='icon1'>
                        <h3>Add image for your page</h3>
                        <div style="color: black;" id="image_input_div">
                        <input id="image_input" type="file" onchange="checkImage()" style="color: black;right: -50px;" ><div id="error_image" ></div></div>`;
  // div.innerHTML += '<button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createNumberOfHours()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createOverviewPage()">Previous</button>';
  // document.getElementById('save_btn').setAttribute('onclick', 'createChapterPage(this);')
  document
  .getElementById("save_btn")
  .setAttribute("onclick", "createChapterPage(this);");
  document
    .getElementById("next_btn")
    .setAttribute("onclick", "createChapterPage(this);");
  document
    .getElementById("prev_btn")
    .setAttribute("onclick", "createOverviewPage(this);");
  document.getElementById("current").innerHTML = 5;
  // document.getElementsByClassName("w3-amber")[0].style = "width:70%";
  if (image != "None") {
    // document.getElementsByClassName('container')[2].innerHTML += '<img id="project_image">';
    document
      .getElementById("image_input")
      .insertAdjacentHTML("beforebegin", '<img id="project_image"><br>');
    document.getElementById("project_image").src = image;
  }
}
// if(document.getElementById('project_image')){
// }

function checkImage() {
  document.getElementById("error_image").style = "display:none;";
  if (document.getElementsByClassName("imgusr").length > 0) {
    deleteImage(document.getElementById("image_input"));
  }
  addLocalImage(document.getElementById("image_input"));
}

function createDifficultyPage(e) {
  if (document.getElementById("description_input") != null) {
    description = document.getElementById("description_input").value;
    if (document.getElementById("description_input").value == "") {
      document.getElementById("error_description").innerHTML =
        "Cannot Be Empty!";
      document.getElementById("error_description").style = "color: red;";
      return;
    } else {
      document.getElementById("error_description").innerHTML = "";
    }
  }
  saveDraft("description", description);
  if (document.getElementById("selectpicker") != null) {
    languages = [];
    for (var i = 0; i < document.getElementById("selectpicker").length; i++) {
      if (document.getElementById("selectpicker")[i].selected) {
        languages.push(document.getElementById("selectpicker")[i].innerHTML);
      }
    }
    saveDraft("languages", languages);
    if (languages.length == 0) {
      document.getElementById("error_language").innerHTML = "Cannot Be Empty!";
      document.getElementById("error_language").style = "color: red;";
      return;
    } else {
      document.getElementById("error_language").innerHTML = "";
    }
  }

  if (pre_reqs == "") {
    document.getElementById("error_prereq").innerHTML = "Cannot Be Empty!";
    document.getElementById("error_prereq").style = "color: red;";
    return;
  }
  saveDraft("pre_req", pre_reqs);
  if (e && e.id == "save_btn") {
    toastr.options.timeOut = 1000;
    toastr.success("Saved successfully!");
    var audio = new Audio("/media/copy.mp3");
    audio.volume = 0.5;
    audio.play();
    return;
  }

  // else {
  //     document.getElementById("error_prereq").innerHTML = "";
  // }

  // if (document.getElementById("selectpicker_prereq") != null) {
  //     pre_reqs = [];
  //     for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
  //         if (document.getElementById("selectpicker_prereq")[i].selected) {
  //             pre_reqs.push(document.getElementById("selectpicker_prereq")[i].innerHTML);
  //         }
  //     }
  //
  //     if (pre_reqs.length == 0) {
  //     document.getElementById("error_prereq").innerHTML = "Cannot Be Empty!";
  //     document.getElementById("error_prereq").style = "color: red;";
  //     return;
  // }
  // else {
  //     document.getElementById("error_prereq").innerHTML = "";
  // }

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
    } else {
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
  var content = "";
  // div.setAttribute("class", "jumbotron text-center");
  content +=
    "<div class='container-fluid container-fluid1 container'><img src='/media/images/no_of_hours.png' class='icon1'>";
  content += " <h3>Add difficulty level for the project</h3><br>";
  // content += '<div style="color: black;">';
  content +=
    '<div class="dot">' +
    ' <span class="dot-bar"><input class="male" type="radio" id="easy"   name="diff" value="EASY"  >' +
    '<label  for="easy">EASY</label></span>' +
    '<span class="dot-bar"><input class="male" type="radio" id="medium" name="diff" value="MEDIUM" >' +
    '<label  for="medium">MEDIUM</label></span>' +
    '<span class="dot-bar"><input class="male" type="radio" id="hard"   name="diff" value="HARD" >' +
    '<label  for="hard">HARD</label></span><div id="error_diff" ></div>' +
    "</div><br><br><br>";
  // div.innerHTML += '<button id="difficulty_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createOverviewPage()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createDescriptionPage()">Previous</button>' +
  //     '</div>';
  div.innerHTML = content;
  if (difficulty_level == "EASY") {
    document.getElementById("easy").checked = true;
  } else if (difficulty_level == "MEDIUM") {
    console.log(80);
    document.getElementById("medium").checked = true;
  } else if (difficulty_level == "HARD") {
    document.getElementById("hard").checked = true;
  }
  document
    .getElementById("save_btn")
    .setAttribute("onclick", ";createOverviewPage(this)");
  document
    .getElementById("next_btn")
    .setAttribute("onclick", ";createOverviewPage(this)");
  document
    .getElementById("prev_btn")
    .setAttribute("onclick", "createDescriptionPage(this);");
  document.getElementById("current").innerHTML = 3;
  document.getElementsByClassName("w3-amber")[0].style = "width:42%";
}

function assignParam(
  title = null,
  description = null,
  difficulty_level = null,
  languages = null,
  overview = null,
  pre_reqs = null,
  pk = null,
  counter = null,
  chapter_innerHTML = null,
  chapter_count = null,
  image = null,
  author = null
) {
  var title = title;
  var description = description;
  var difficulty_level = difficulty_level;
  var languages = languages;
  var overview = overview;
  var pre_reqs = pre_reqs;
  var pk = pk;
  var counter = counter;
  var chapter_innerHTML = chapter_innerHTML;
  var chapter_count = chapter_count;
  var image = image;
  var author = author;
}
