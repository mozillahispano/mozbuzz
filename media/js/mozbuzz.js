$(document.body).delegate("a[data-althref]","click",function(e){
    if(e.shiftKey){
        location.href=this.getAttribute("data-althref");
        return false;
    }
});


function toggle_followups(mention_id){
	$('#followups_' + mention_id).toggle()
}