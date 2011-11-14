

$(document.body).delegate("a[data-althref]","click",function(e){
    if(e.shiftKey){
        location.href=this.getAttribute("data-althref");
        return false;
    }
});
