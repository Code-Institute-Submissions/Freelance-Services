// If alert message is displayed then remove it after 3 seconds 
if($('.alert')){
    setTimeout(function(){
        $('.alert').hide();
    }, 3000)
}

// Checks whether the input field is empty and highlights whether red if empty green if not.
function checkInput() {
    var target = $( event.target )
    if (target.val() === "") {
        target.css("border", "2px solid red");
        return false;
    } else {
        target.css("border", "2px solid green");
        return true;
    }
}

// Waits for change then calls check input function
$('input').on("change focusout", () => {
    checkInput();
});