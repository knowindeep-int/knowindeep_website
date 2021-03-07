window.onload = function(){
    disableEdit();
};

const FIELDS = {
    FIRSTNAME: "first_name",
    DESCRIPTION: "description",
    DP: "dp",
    PHONENUMBER: "phone_number"
}
function makeEditable(is_verified) {
    $(this).attr('disabled', false);
}

function disableEdit(is_verified) {
    //event.preventDefault();
    edit_buttons = document.getElementsByClassName("can_hide")
    
    if (is_verified == "False") {
        for (var i = 0; i < edit_buttons.length; i++) {
            edit_buttons[i].style.display = "none";
        }
    }
}

function editProfile(field) {
    let value = document.getElementById(field).value

    updateProfile(field, value)
}

