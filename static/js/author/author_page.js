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
    // alert('hello')
    alert(is_verified);
    $(this).attr('disabled', false);
}

function disableEdit(is_verified) {
    //event.preventDefault();
    // alert('hello')
    edit_buttons = document.getElementsByClassName("can_hide")
    alert(is_verified)
        //alert('HELLO WORLD!')
    
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

