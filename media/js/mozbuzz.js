
function _(x){
    var args = arguments,i=1;
    return x.replace(/%s/g,function(){
        return args[i++];
    });
}

$(document.body).delegate("a[data-althref]","click",function(e){
    if(e.shiftKey){
        location.href=this.getAttribute("data-althref");
        return false;
    }
}).delegate("a.followups-show","click",function(){
    $(this).parents(".mention").find(".followups").show();
    return false;
});
