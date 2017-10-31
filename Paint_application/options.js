    var canvas = document.getElementById("drawArea");
    var context = canvas.getContext("2d");
    var nowx = 0 ,nowy= 0,thenx = 0 ,theny= 0;
    var flag = false;
    var color = "black";
    var thick = 2;
    var drawing = false;
    dot_flag = false;
    context.strokeStyle = 'red'


canvas.addEventListener("mousedown",function(e){
    plotxy('mousedown',e)
},false);
canvas.addEventListener("mousemove", function (e) {
    plotxy('mousemove', e)
}, true);
canvas.addEventListener("mouseup", function (e) {
    plotxy('mouseup', e)
}, false);
canvas.addEventListener("mouseout", function (e) {
    plotxy('mouseout', e)
}, false);

var rect = canvas.getBoundingClientRect();

function outlineColor(selectedcolor) {
    switch (selectedcolor.id){
        case "green": color = "green"; break;
        case "blue": color = "blue"; break;
        case "red": color = "red"; break;
        case "white": color = "white"; break;
        case "lightblue": color = "blue"; break;
        case "yellow": color = "yellow"; break;
    }
    if (color == "white") { thick = 14 }
    else { thich = 2 }
    return color
}

function plotxy(fun,e){
    if(fun == 'mousedown'){
        thenx = nowx;
        theny = nowy;
        
        nowx = e.clientX - rect.left;
        nowy = e.clientY - rect.top;
        flag = true;
    }
    if (fun == 'mouseout' || fun == 'mouseup') {
flag = false;
    }
    if (fun=='mousemove'){
        if(flag == true){
            thenx = nowx;
            theny = nowy;
            nowx = e.clientX - rect.left;
            nowy = e.clientY - rect.top;
            draw();
        }
    }
}

function draw(){
    context.beginPath();
    context.lineJoin = "round";
    context.strokeStyle = "red";
    context.moveTo(thenx,theny);
    context.lineTo(nowx,nowy);
    context.closePath();
    context.stroke();

}
