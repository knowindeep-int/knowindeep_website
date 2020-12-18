document.addEventListener('DOMContentLoaded', function() {
    var element = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(element, options);
});

// function myfunc() {
//  {% if request.user.is_authenticated %}
//         window.open("{% url 'site_users:logout' %}", "", "width=700,height=700");
//     {% else %}
//         window.open("{% url 'social:begin' 'google-oauth2' %}?next={{request.path}}", "", "width=700,height=700");
//     {% endif %}
// }
