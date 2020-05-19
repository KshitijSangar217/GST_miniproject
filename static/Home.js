input_excel = document.getElementById("excelfile");
var ret = document.querySelector("#excelfile").value

eel.expose(submit_button);
function submit_button()
{
   eel.RunBackend();
}

eel.expose(browsefile);
function browsefile()
{
    eel.browsefile()(function(ret){
    console.log(ret);
    });
}

eel.expose(browsefolder);
function browsefolder()
{
    eel.browsefolder()(function(ret){
    console.log(ret);
    });
}


