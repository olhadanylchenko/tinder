function onChange() {
    var gender = document.getElementById("gender").value;

    switch (gender) {
        case "female":
            document.body.className = "female"
            break;
        case "male":
            document.body.className = "male"
            break;
        default:
            document.body.className = '';
            break;

    }
}