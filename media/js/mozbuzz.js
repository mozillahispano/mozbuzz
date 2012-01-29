
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
    $(this)
        .removeClass("followups-show").addClass("followups-hide").text(_("Hide"))
        .parents(".mention").find(".followups").show();

    return false;
}).delegate("a.followups-hide","click",function(){
    $(this)
        .addClass("followups-show").removeClass("followups-hide").text(_("Show"))
        .parents(".mention").find(".followups").hide();
    return false;
});





(function(){

    var slider_values = [0,25,50,100,250,500,1000,2500,5000,10000,25000,50000,100000,250000,500000,1000000,10000000,100000000,1000000000,7000000000];

    function format_quantity(c){
        c = Math.round(c) + "";
        var n = "";
        while(c.length >= 3){
            n = "." + c.substr(-3,3) + n;
            c = c.substr(0,c.length - 3);
        }
        if(c.length){
            return c + n;
        }else{
            return n.substring(1);
        }
    }

    function update_audience(s,e){
        $("#audience-preview").text(_("Between %s and %s", format_quantity(s) , format_quantity(e)));
    }

    var start = parseInt($("#input_audience_audience_gt").val());
    var end = parseInt($("#input_audience_audience_lt").val());

    update_audience(start,end);

    var audienceSlider = $("#slider-audience").slider({
        range: true,
        min: 0,
        max: 19,
        values: [slider_values.indexOf(start), slider_values.indexOf(end)],
        slide: function( event, ui ) {
            var s = slider_values[ui.values[0]], e = slider_values[ui.values[1]];
            update_audience(s,e);
            $("#input_audience_audience_gt").val(s);
            $("#input_audience_audience_lt").val(e);
            $("#audience-update").show();
        }
    });

})();

