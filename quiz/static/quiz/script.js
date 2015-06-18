function checkEq() {
    var expression = document.getElementById("expression").value;
    var value = document.getElementById("value").value;
    if (value === "expression" || value === expression) {
        document.getElementById("result").innerHTML = "Nice try.";
    } else {
        try {
            var result = eval(expression + " === " + value);        
            document.getElementById("result").innerHTML = result;
            if (result === true) {
                var button = document.getElementById('next');
                button.type = "submit";
            }
        } catch(e) {
            document.getElementById("result").innerHTML = "That didn't even run without errors...";
        }
    }
}

function showAns() {
    var expression = document.getElementById("expression").value;
    var value = eval(expression);
    document.getElementById("value").value = (typeof value === "string")? "'" + value + "'" : String(value);
}