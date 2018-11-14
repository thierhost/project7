
//to clear the page when reload
document.getElementById("dialogue").value = ""
document.getElementById("msg").value = ""

var dialogues = []
//intro from GrandPy
var grandpy = ["Tiens savais-tu que ","A propos il faut que tu saches que ", "Pour ton info, "]




function enter_address() {

    //document.getElementById("dialogue").textContent  = "";

    var dialogues2 = ""


    var xhr = new XMLHttpRequest();

    xhr.open("POST", "/GrandPy", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    //replace below to remove /n from textarea
    entry_user = document.getElementById("msg").value.replace(/\n/g, "")
    entry_user = entry_user.trim()//remove blank if needed
    entry_grandpy = grandpy[Math.floor(Math.random() * 3)]//pick up 1 random intro from grandpy
    //console.log(entry_grandpy);
    xhr.send("msg=" + entry_user)




    xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 0)) {


                    reponse = JSON.parse(xhr.responseText);

                    //remove id=plan to clear any existing map
                    document.getElementById("google").removeChild(document.getElementById("plan"));

                    var img = document.createElement("img");
                    img.id = 'plan'


                    img.src = reponse["google"];
                    var src = document.getElementById("google");
                    src.appendChild(img);
                    //console.log(img.src);

                    var wiki_string = reponse["wiki"];

                    //add in the list entries
                    dialogues.unshift(wiki_string)
                    dialogues.unshift(entry_grandpy)
                    dialogues.unshift(entry_user + "\n")
                    dialogues.unshift('\n*-*-*-*\n\n')


                    //console.log(wiki_string);


                    //this fct added to remove comma
                    dialogues2 = copy_dialog(dialogues2);

                    document.getElementById("dialogue").value = dialogues2  ;





            }
    };


    ;

}



//listener on msg textarea to trigger Ajax when press enter
document.getElementById("msg").addEventListener("keyup", function (e) {

if (e.keyCode == 13) {
   enter_address();
    e.preventDefault();}

});


//fct to read array and write into textarea

function copy_dialog(dialogues2) {
    dialogues.forEach(function(element) {
    dialogues2 += element;
    //dialogues2 += element + "\n";
    });
    return dialogues2
}


