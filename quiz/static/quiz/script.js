/*
    JavaScript for OdeToJS
    Copyright (C) 2015  Rik de Graaff

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
3/

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