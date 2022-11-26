// $(document).ready(function(){
//     $(".list-group-item").click(function () {
//         function getCookie(name) {
//             let cookieValue = null;
//             if (document.cookie && document.cookie !== '') {
//                 const cookies = document.cookie.split(';');
//                 for (let i = 0; i < cookies.length; i++) {
//                     const cookie = cookies[i].trim();
//                     // Does this cookie string begin with the name we want?
//                     if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                         break;
//                     }
//                 }
//             }
//             return cookieValue;
//         }
//          const csrftoken = getCookie('csrftoken');
//         $.ajax({
//             url: '4/',
//             method: "POST",
//             headers: {'X-CSRFToken': csrftoken},
//             mode: 'same-origin',
//             data: 4,
//
//             success: function (data){
//                 alert("Success")
//             }
//
//         })
//     })
// })