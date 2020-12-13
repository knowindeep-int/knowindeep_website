var title = "";
let chapters = [];

    var description = "";
    var category = "";
    var difficulty_level = null;
    var no_of_hours = null;
    var languages = [];
    var overview = "";
    var pre_reqs = [];
    var pk = "";
    var counter = 1;
    var chapter_innerHTML = "";
    var chapter_count = 2;
    function addChapter(event) {
        let error = 0;
        let focus_on = null;
        for (var i = 0; i < document.getElementsByClassName("chapter_div").length; i++) {
            if (document.getElementsByClassName("heading")[i] != null) {

                if (document.getElementsByClassName("heading")[i].checkValidity() == false) {
                    document.getElementsByClassName("error_heading")[i].innerHTML = "Not Valid!" 
                    document.getElementsByClassName("error_heading")[i].style = "color: red;";
                    error = 1;
                    if (focus_on == null) {
                        document.getElementsByClassName("heading")[i].scrollIntoView({ block: "center" });
                        focus_on = "heading";
                    }
                }
                else {
                    document.getElementsByClassName("error_heading")[i].innerHTML = "" 
                }
                if (document.getElementsByClassName("description")[i].checkValidity() == false) {
                    document.getElementsByClassName("error_description")[i].innerHTML = "Not Valid!" 
                    document.getElementsByClassName("error_description")[i].style = "color: red;";
                    error = 1;
                    if (focus_on == null) {
                        document.getElementsByClassName("description")[i].scrollIntoView({ block: "center" });
                        focus_on = "description";
                    }
                }
                else {
                    document.getElementsByClassName("error_description")[i].innerHTML = "" 
                }
                if (document.getElementsByClassName("content")[i].checkValidity() == false) {
                    document.getElementsByClassName("error_content")[i].innerHTML = "Not Valid!" 
                    document.getElementsByClassName("error_content")[i].style = "color: red;";
                    error = 1;
                    if (focus_on == null) {
                        document.getElementsByClassName("content")[i].scrollIntoView({ block: "center" });
                        focus_on = "content";
                    }
                }
                else {
                    document.getElementsByClassName("error_content")[i].innerHTML = "" 
                }
                if (document.getElementsByClassName("youtube")[i].checkValidity() == false) {
                    document.getElementsByClassName("error_youtube")[i].innerHTML = "Not Valid!" 
                    document.getElementsByClassName("error_youtube")[i].style = "color: red;";
                    error = 1;
                    if (focus_on == null) {
                        document.getElementsByClassName("youtube")[i].scrollIntoView({ block: "center" });
                        focus_on = "youtube";
                    }
                }
                else {
                    document.getElementsByClassName("error_youtube")[i].innerHTML = "" 
                }

            }

        }
        if (error == "1") {
            return;
        }

        var elem = document.getElementById('chapter_left_button');
        elem.parentNode.removeChild(elem);
        var elem = document.getElementById('chapter_right_button');
        elem.parentNode.removeChild(elem);
        var elem = document.getElementById('chapter_add_button');
        elem.parentNode.removeChild(elem);

        div = document.getElementById("chapter_main_div");
        new_div = document.createElement('div');
        new_div.setAttribute("style", "color: black;");
        new_div.setAttribute("class", "chapter_div");
        new_div.setAttribute("id", "chapter_div_" + counter)
        new_div.innerHTML += '<br><br>' + document.getElementsByClassName("chapter_div")[0].innerHTML + '<button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createLanguagesPage()">Next</button><button id="chapter_add_button" type="button" class="btn btn-primary" style="float: right;" onclick="addChapter()">Add</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createDescriptionPage()">Previous</button>';

        div.appendChild(new_div);
        document.getElementsByClassName("chapter_h2_heading")[chapter_count - 1].innerHTML = "Chapter " + chapter_count;
        chapter_innerHTML = div.innerHTML;
        counter += 1;
        chapter_count += 1;

    };

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
    window.onload = function () {
        createTitlePage();
        createAlert();
    };

    function createDescriptionPage() {
        if (document.getElementById("title_input") != null) {
            title = document.getElementById("title_input").value;
            if (document.getElementById("title_input").value == "") {
                document.getElementById("error_title").innerHTML = "Cannot Be Empty!";
                document.getElementById("error_title").style = "color: red;";
                return;
            }
        }
        for (var i = 0; i < document.getElementsByClassName("chapter_div").length; i++) {
            if (document.getElementsByClassName("heading")[i] != null) {
                let chapter_add = {};
                chapter_add['heading'] = document.getElementsByClassName("heading")[i].value;
                chapter_add['description'] = document.getElementsByClassName("description")[i].value;
                chapter_add['content'] = document.getElementsByClassName("content")[i].value;
                chapter_add['youtube'] = document.getElementsByClassName("youtube")[i].value;

                chapters[i] = chapter_add;
            }
        }
        saveDraft("title", title);
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

        var div = document.getElementById(2);
        if (div.innerHTML != "") {
            return false
        }
        div.setAttribute("class", "jumbotron text-center");
        div.innerHTML += "<h2 style='color: black;'>DESCRIPTION PAGE</h2>";
        div.innerHTML += '<input id="description_input" type="text" style="color: black"; value="' + description + '"><button type="button" class="btn btn-primary" style="float: left;" onclick="createTitlePage()">Previous</button> <button type="button" class="btn btn-primary" style="float: right;" onclick="createChapterPage()">Next</button><span id="error_description"></span>';

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
    div.setAttribute("class", "jumbotron text-center") ;
    div.innerHTML += "<h2 style='color: black;'>TITLE PAGE</h2>" + "<input id='title_input' type='text' style='color: black;' value='" + title +  "'  required>" + '<span id="error_title"></span>' + ' <button type="button" class="btn btn-primary" style="float: right;" onclick="createDescriptionPage();">Next</button>'
    document.getElementById("title_input").dataset.state = 'invalid';
}

function createChapterPage() {
    if (document.getElementById("description_input") != null) {
        description = document.getElementById("description_input").value;
        if (document.getElementById("description_input").value == "") {
            document.getElementById("error_description").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_description").style = "color: red;";
            return;
        }
    }
    
    if(document.getElementById("selectpicker") != null) {
        languages = [];
        for (var i=0; i < document.getElementById("selectpicker").length; i++ ) {
            if (document.getElementById("selectpicker")[i].selected) {
                languages.push(document.getElementById("selectpicker")[i].innerHTML);
            }
        }
        
    }
    saveDraft("description", description);

    showhide("4");
    div_1 = document.getElementById("1");
    div_1.setAttribute("style", "display: none;");
    div_1.innerHTML = "";

    div_2 = document.getElementById("2");
    div_2.setAttribute("style", "display: none;");
    div_2.innerHTML = "";

    div_3 = document.getElementById("3");
    div_3.setAttribute("style", "display: none;");
    div_3.innerHTML = "";

    div_5 = document.getElementById("5");
    div_5.setAttribute("style", "display: none;");
    div_5.innerHTML = "";

    div_6 = document.getElementById("6");
    div_6.setAttribute("style", "display: none;");
    div_6.innerHTML = "";



    var div = document.getElementById("4");
    div.setAttribute("class", "jumbotron text-center") ;
    div.innerHTML +="<h2 style='color: black;'> CHAPTER PAGE</h2>" ;
    div.innerHTML += '<div id="chapter_main_div" ><div style="color: black;" class="chapter_div" class="current_chapter" id="chapter_div_0">' + 
            '<h2 class="chapter_h2_heading">Chapter 1</h2><div>' +
                '<span>Heading</span>' +
                '<input class="heading chapter" id="heading" type="text" required>' +
                '<span class="error_heading"></span>' + 
            '</div>' +
            '<div>' +
                '<span>Description</span>' +
                '<input class="description chapter" id="description" type="text" required>' +
                '<span class="error_description"></span>' + 
            '</div>' +
            '<div>' +
                '<span>content</span>' +
                '<input class="content chapter" id="content" type="text" required>' +
                '<span class="error_content"></span>' + 
            '</div>' +
            '<div>' +
                '<span>Youtube Link</span>' +
                '<input type="url"  id="youtube" class="youtube chapter" required >' + 
                '<span class="error_youtube"></span>' +
            '</div>' ;
    if (chapter_innerHTML != "") {
        document.getElementById("chapter_main_div").innerHTML = '<br><br>' + chapter_innerHTML ;   
    }    
    else {
        div.innerHTML += '<button id="chapter_add_button" type="button" class="btn btn-primary" style="float: right;" onclick="addChapter()">Add</button><button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createLanguagesPage()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createDescriptionPage()">Previous</button></div></div>';
    }
    if (document.getElementById('heading') != null) { 
        for (var i=0; i< document.getElementsByClassName("chapter_div").length; i++) {
            document.getElementsByClassName("heading")[i].value = chapters[i]['heading'];
            document.getElementsByClassName("description")[i].value = chapters[i]['description'];
            document.getElementsByClassName("content")[i].value = chapters[i]['content'];
            document.getElementsByClassName("youtube")[i].value = chapters[i]['youtube'];
        }
    }
    
}

function createLanguagesPage() {

    let error = 0;
    let focus_on = null;
    for (var i = 0; i < document.getElementsByClassName("chapter_div").length; i++) {
        if (document.getElementById('heading') != null) {
            var chapter_add = {};
            chapter_add['heading'] = document.getElementsByClassName("heading")[i].value;
            chapter_add['description'] = document.getElementsByClassName("description")[i].value;
            chapter_add['content'] = document.getElementsByClassName("content")[i].value;
            chapter_add['youtube'] = document.getElementsByClassName("youtube")[i].value;

            if (document.getElementsByClassName("heading")[i].checkValidity() == false) {
                document.getElementsByClassName("error_heading")[i].innerHTML = "Not Valid!" 
                document.getElementsByClassName("error_heading")[i].style = "color: red;";
                error = 1;
                if (focus_on == null) {
                    document.getElementsByClassName("heading")[i].scrollIntoView({ block: "center" });
                    focus_on = "heading";
                }
            }
            else {
                document.getElementsByClassName("error_heading")[i].innerHTML = "" 
            }
            if (document.getElementsByClassName("description")[i].checkValidity() == false) {
                document.getElementsByClassName("error_description")[i].innerHTML = "Not Valid!" 
                document.getElementsByClassName("error_description")[i].style = "color: red;";
                if (focus_on == null) {
                    document.getElementsByClassName("description")[i].scrollIntoView({ block: "center" });
                    focus_on = "description";
                }
            }
            else {
                document.getElementsByClassName("error_description")[i].innerHTML = ""
            }
            if (document.getElementsByClassName("content")[i].checkValidity() == false) {
                document.getElementsByClassName("error_content")[i].innerHTML = "Not Valid!" 
                document.getElementsByClassName("error_content")[i].style = "color: red;";
                error = 1;
                if (focus_on == null) {
                    document.getElementsByClassName("content")[i].scrollIntoView({ block: "center" });
                    focus_on = "content";
                }
            }
            else {
                document.getElementsByClassName("error_content")[i].innerHTML = ""
            }
            if (document.getElementsByClassName("youtube")[i].checkValidity() == false) {
                document.getElementsByClassName("error_youtube")[i].innerHTML = "Not Valid!" 
                document.getElementsByClassName("error_youtube")[i].style = "color: red;";
                error = 1;
                if (focus_on == null) {
                    document.getElementsByClassName("youtube")[i].scrollIntoView({ block: "center" });
                    focus_on = "youtube";
                }
            }
            else {
                document.getElementsByClassName("error_youtube")[i].innerHTML = "" 
            }
            chapters[i] = chapter_add;
        }
    }
    if (error == "1") {
        return;
    }
    showhide("5");
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

    div_6 = document.getElementById("6");
    div_6.setAttribute("style", "display: none;");
    div_6.innerHTML = "";

    div_7 = document.getElementById("7");
    div_7.setAttribute("style", "display: none;");
    div_7.innerHTML = "";


    div = document.getElementById("5")
    div.setAttribute("class", "jumbotron text-center");
    div.innerHTML += "<h2 style='color: black;'> ADD LANGUAGES PAGE</h2>";
    div.innerHTML += '<div style="color: black;">';

    div.innerHTML += '<select id="selectpicker" multiple data-live-search="true" style="display: block;color: black;">' +
        '{% for language in languages %}' +
        '<option>{{language}}</option>{% endfor %}</select>';
    div.innerHTML += '<button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createDifficultyPage()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createChapterPage()">Previous</button>';
    div.innerHTML += '<span id="error_language"></span></div>';
    if (document.getElementById("selectpicker") != null) {
        for (var i = 0; i < document.getElementById("selectpicker").length; i++) {
            option = document.getElementById("selectpicker").options[i];
            if (languages.indexOf(option.value) != -1) {
                option.selected = true;
            }
        }
    }
}

function createDifficultyPage() {
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

    div = document.getElementById("6");
    div.setAttribute("class", "jumbotron text-center");
    div.innerHTML += "<h2 style='color: black;'> ADD DIFFICULTY LEVEL FOR THE PROJECT</h2>";
    div.innerHTML += '<div style="color: black;">';
    div.innerHTML += '<input class="difficulty_radio_input" type="radio" id="easy" name="" value="EASY" checked="checked">' +
        '<label for="easy">EASY</label><br>' +
        '<input class="difficulty_radio_input" type="radio" id="medium" name="" value="MEDIUM">' +
        '<label for="meduim">MEDIUM</label><br>' +
        '<input  class="difficulty_radio_input" type="radio" id="hard" name="" value="HARD">' +
        '<label for="hard">HARD</label>';
    div.innerHTML += '<button id="difficulty_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createOverviewPage()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createLanguagesPage()">Previous</button>' +
        '</div>';


}

function createOverviewPage() {
    if (document.getElementsByClassName("difficulty_radio_input") != null) {
        for (var i = 0; i < document.getElementsByClassName("difficulty_radio_input").length; i++) {
            if (document.getElementsByClassName("difficulty_radio_input")[i].checked) {
                difficulty_level = document.getElementsByClassName("difficulty_radio_input")[i].value
            }
        }
    }

    if (document.getElementById("selectpicker_prereq") != null) {
        pre_reqs = [];
        for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
            if (document.getElementById("selectpicker_prereq")[i].selected) {
                pre_reqs.push(document.getElementById("selectpicker_prereq")[i].innerHTML);
            }
        }

    }
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


    var div_8 = document.getElementById("8")
    div_8.innerHTML = "";
    div_8.setAttribute("style", "display: none;")
    showhide("7");

    var div = document.getElementById("7");
    div.setAttribute("class", "jumbotron text-center");
    div.innerHTML += "<h2 style='color: black;'>OVERVIEW PAGE</h2>" + "<input id='overview_input' type='text' style='color: black;' value='" + overview + "'> " + '<button type="button" class="btn btn-primary" style="float: right;" onclick="createPreReqsPage()">Next</button><button type="button" class="btn btn-primary" style="float: left;" onclick="createDifficultyPage()">Previous</button>'
    div.innerHTML += " <span id='error_overview'></span>"
}


function createPreReqsPage() {
    if (document.getElementById("overview_input") != null) {
        overview = document.getElementById("overview_input").value;
        if (document.getElementById("overview_input").value == "") {
            document.getElementById("error_overview").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_overview").style = "color: red;";
            return;
        }
    }

    showhide("8")
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

    div_9 = document.getElementById("9");
    div_9.setAttribute("style", "display: none;");
    div_9.innerHTML = "";



    div = document.getElementById("8")
    div.setAttribute("class", "jumbotron text-center");
    div.innerHTML += "<h2 style='color: black;'> ADD PRE-REQUISITES PAGE</h2>";
    div.innerHTML += '<div style="color: black;">';

    div.innerHTML += '<select id="selectpicker_prereq" multiple data-live-search="true" style="display: block;color: black;">' +
        '{% for pre_req in pre_reqs %}<option>{{pre_req}}</option>{% endfor %}</select>'

    div.innerHTML += '<button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createImagePage()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createOverviewPage()">Previous</button>';
    div.innerHTML += '<span id="error_prereq" ></span></div>'
    if (document.getElementById("selectpicker_prereq") != null) {
        for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
            option = document.getElementById("selectpicker_prereq").options[i];
            if (pre_reqs.indexOf(option.value) != -1) {
                option.selected = true;
            }
        }
    }
}

function createImagePage() {
    if (document.getElementsByClassName("time_radio_input") != null) {
        for (var i = 0; i < document.getElementsByClassName("time_radio_input").length; i++) {
            if (document.getElementsByClassName("time_radio_input")[i].checked) {
                no_of_hours = document.getElementsByClassName("time_radio_input")[i].value
            }
        }
    }

    if (document.getElementById("selectpicker_prereq") != null) {
        pre_reqs = [];
        for (var i = 0; i < document.getElementById("selectpicker_prereq").length; i++) {
            if (document.getElementById("selectpicker_prereq")[i].selected) {
                pre_reqs.push(document.getElementById("selectpicker_prereq")[i].innerHTML);
            }
        }
        if (pre_reqs.length == 0) {
            document.getElementById("error_prereq").innerHTML = "Cannot Be Empty!";
            document.getElementById("error_prereq").style = "color: red;";
            return;
        }
        else {
            document.getElementById("error_prereq").innerHTML = "";
        }

    }
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
    div.innerHTML += '<div style="color: black;">';
    div.innerHTML += '<input type="file" style="color: black;">';
    div.innerHTML += '<button id="chapter_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="createNumberOfHours()">Next</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createPreReqsPage()">Previous</button>';
}

function createNumberOfHours() {

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
    div.setAttribute("class", "jumbotron text-center");
    div.innerHTML += "<h2 style='color: black;'> ADD HOURS REQUIRED FOR THE PROJECT</h2>";
    div.innerHTML += '<div style="color: black;">';
    div.innerHTML += '<input class="time_radio_input" checked="checked" type="radio" id="0-2" name="" value="0-2" disabled=false>' +
        '<label for="0-2">0-2 HOURS</label><br>' +
        '<input checked="checked" class="time_radio_input" type="radio" id="2-4" name="" value="2-4" style="display: block;visibility: visible">' +
        '<label for="2-4">2-4 HOURS</label><br>' +
        '<input class="time_radio_input" type="radio" id=">4" name="" value=">4">' +
        '<label for=">4">MORE THAN 4 HOURS</label>';
    div.innerHTML += '<button id="difficulty_right_button" type="button" class="btn btn-primary" style="float: right;" onclick="">Create</button><button id="chapter_left_button" type="button" class="btn btn-primary" style="float: left;" onclick="createImagePage()">Previous</button>' +
        '</div>';
}

