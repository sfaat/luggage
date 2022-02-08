
function changeTrip(value)
{   
    var x = document.getElementById("trip_type").value;
    
    if(x =='one-way'){
        document.getElementById("return").style.display="block";
        document.getElementById("inputCheckIn").placeholder = "Arrival";
    }
    else if(x =='return1'){
        document.getElementById("inputCheckIn").placeholder = "Send By Date";
        document.getElementById("return").style.display="none";
    }
    else{
        document.getElementById("return").style.display="none";
        document.getElementById("inputCheckIn").placeholder = "Arrival";
    }


    // if(x=="one-way"){
    //     document.getElementById("return").style.display="none";

    // }
    // else if(x =='return1'){
    //     document.getElementById("return").style.display="none";
    //     document.getElementById("inputCheckIn").placeholder = "Arrival";
    // }
    // else{
    //     document.getElementById("inputCheckIn").placeholder = "Arrival";

    // }
}



