
document.getElementById("dialogue").value = ""

var dialogues = []

var grandpy = ["Tiens savais-tu que ","A propos il faut que tu saches que ", "Pour ton info, "]




function enter_address() {

    //document.getElementById("dialogue").textContent  = "";

    var dialogues2 = ""

    var xhr = new XMLHttpRequest();

    xhr.open("POST", "http://127.0.0.1:5000/message", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    //replace below to remove /n from textarea
    entry_user = document.getElementById("msg").value.replace(/\n/g, "")
    entry_grandpy = grandpy[Math.floor(Math.random() * 3)]
    console.log(entry_grandpy);
    xhr.send("msg=" + entry_user)
    dialogues.push(entry_user)
    dialogues.push(entry_grandpy)


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
                    console.log(img.src);

                    var wiki_string = reponse["wiki"];
                    dialogues.push(wiki_string)
                    dialogues.push('*-*-*-*')

                    console.log(wiki_string);

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
    dialogues2 += element + "\n";
    });
    return dialogues2
}


