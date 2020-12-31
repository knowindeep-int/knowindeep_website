window.onload = function(){
    disableEdit();
};

const FIELDS = {
    FIRSTNAME: "first_name",
    DESCRIPTION: "description",
    DP: "dp",
    PHONENUMBER: "phone_number"
}




function editProfile(field) {
    let value = document.getElementById(field).value

    updateProfile(field, value)
}

