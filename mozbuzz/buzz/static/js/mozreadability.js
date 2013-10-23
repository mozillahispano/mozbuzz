function getURLContents(url, cb){
    var xhr = new XMLHttpRequest();
    xhr.onload = function(){
        if(xhr.status != 200){
            alert("Invalid response code " + xhr.status);
            guessCallFinished();
            return;
        }
        var doc = xhr.responseXML, articleContent, articleTitle;
        if(!doc){
            alert("Malformed document, or browser doesn't support XHR HTML parsing (try Firefox 11+)");
            guessCallFinished();
            return;
        }
        try{
            readability.removeScripts(doc);
            readability.prepDocument(doc);
            articleContent = readability.grabArticle(doc.body);
            articleTitle = readability.getArticleTitle(doc);
        }catch(e){
            alert(e);
            guessCallFinished();
            return;
        }
        if(articleContent){
            if(articleTitle && articleContent.firstChild){
                articleContent.insertBefore(articleTitle, articleContent.firstChild);
            }
            cb(articleContent);
        }else{
            guessCallFinished();
        }
    };
    xhr.open("GET", URL_ROOT + "proxy?url=" + encodeURIComponent(url) + "&_=" + new Date());
    xhr.responseType = "document";
    xhr.send();
}


function markdownEscape(text){
    return text?text.replace(/\s+/g," ").replace(/[\\\-*_>#]/g,"\\$&"):"";
}

function repeat(str,times){
    return (new Array(times+1)).join(str);
}

function childsToMarkdown(tree,mode){
    var res = "";
    for(var i=0, l=tree.childNodes.length; i<l; ++i){
        res += nodeToMarkdown(tree.childNodes[i], mode);
    }
    return res;
}

function nodeToMarkdown(tree,mode){
    var nl = "\n\n";
    if(tree.nodeType == 3){ // Text node
        return markdownEscape(tree.nodeValue);
    }else if(tree.nodeType == 1){
        if(mode == "block"){
            switch(tree.tagName.toLowerCase()){
                case "br":
                    return nl;
                case "hr":
                    return nl + "---" + nl;
                // Block container elements
                case "p":
                case "div":
                case "section":
                case "address":
                case "center":
                    return nl + childsToMarkdown(tree, "block") + nl;
                case "ul":
                    return nl + childsToMarkdown(tree, "u") + nl;
                case "ol":
                    return nl + childsToMarkdown(tree, "o") + nl;
                case "pre":
                    return nl + "    " + childsToMarkdown(tree, "inline") + nl;
                case "code":
                    if(tree.childNodes.length == 1){
                        break; // use the inline format
                    }
                    return nl + "    " + childsToMarkdown(tree, "inline") + nl;
                case "h1": case "h2": case "h3": case "h4": case "h5": case "h6": case "h7":
                    return nl + repeat("#", +tree.tagName[1]) + "  " + childsToMarkdown(tree, "inline") + nl;
                case "blockquote":
                    return nl + "> " + childsToMarkdown(tree, "inline") + nl;
            }
        }
        if(/^[ou]+$/.test(mode)){
            if(tree.tagName == "LI"){
                return "\n" + repeat("  ", mode.length - 1) + (mode[mode.length-1]=="o"?"1. ":"- ") + childsToMarkdown(tree, mode+"l");
            }else{
                console.log("[toMarkdown] - invalid element at this point " + mode.tagName);
                return childsToMarkdown(tree, "inline");
            }
        }else if(/^[ou]+l$/.test(mode)){
            if(tree.tagName == "UL"){
                return childsToMarkdown(tree,mode.substr(0,mode.length-1)+"u");
            }else if(tree.tagName == "OL"){
                return childsToMarkdown(tree,mode.substr(0,mode.length-1)+"o");
            }
        }

        // Inline tags
        switch(tree.tagName.toLowerCase()){
            case "strong":
            case "b":
                return "**" + childsToMarkdown(tree,"inline") + "**";
            case "em":
            case "i":
                return "_" + childsToMarkdown(tree,"inline") + "_";
            case "code": // Inline version of code
                return "`" + childsToMarkdown(tree,"inline") + "`";
            case "a":
                return "[" + childsToMarkdown(tree,"inline") + "](" + tree.getAttribute("href") + ")";
            case "img":
                return nl + "[_Image_: " + markdownEscape(tree.getAttribute("alt")) + "](" + tree.getAttribute("src") + ")" + nl;
            case "script":
            case "style":
            case "meta":
                return "";
            default:
                console.log("[toMarkdown] - undefined element " + tree.tagName);
                return childsToMarkdown(tree,mode);
        }

    }
}

function toMarkdown(node){
    try{
        return nodeToMarkdown(node,"block").replace(/[\n]{2,}/g,"\n\n").replace(/^[\n]+/,"").replace(/[\n]+$/,"");
    }catch(e){
        alert("[toMarkdown]" + e);
        guessCallFinished();
        throw e;
    }
}

var finishedCallsCnt = 0;
function guessCallFinished(){
    if(++finishedCallsCnt == 2){
        $("#mention_form_otherfields_cnt").show();
        $("#mention_guess_prompt").hide();
    }
}

function parseUri (str) {
	var	parser = /^(?:(?![^:@]+:[^:@\/]*@)([^:\/?#.]+):)?(?:\/\/)?((?:(([^:@]*)(?::([^:@]*))?)?@)?([^:\/?#]*)(?::(\d*))?)(((\/(?:[^?#](?![^?#\/]*\.[^?#\/.]+(?:[?#]|$)))*\/?)?([^?#\/]*))(?:\?([^#]*))?(?:#(.*))?)/;
    var m   = parser.exec(str);
    if(!m){
        return false;
    }
    var key = ["source","protocol","authority","userInfo","user","password","host","port","relative","path","directory","file","query","anchor"];
    var uri = {};
	for(var i=0; i<14; ++i){
        uri[key[i]] = m[i] || "";
    }
	return uri;
}

function findDuplicates(url, objs){
    objs.forEach(function(obj){
        if(obj.link.toLowerCase() == url.toLowerCase()){
            $("#duplicates").show();
            $("#duplicates-list").append(
                $("<li/>").append(
                    $("<a/>").text(obj.link +" Created On "+ obj.creation_date)
                             .attr("href", URL_ROOT + "mention/" + obj.pk)
                )
            );
        }
    });
}

function guessInformation(){
    var spec = $("#id_link").val();

    // Stupid tracking
    if(/http:\/\/news\.google\.com\/news\/url?.*url=([^&]+)/.test(spec)){
        spec = decodeURIComponent(RegExp.$1);
        $("#id_link").val(spec);
    }
    var url = parseUri(spec);

    if(!url || url.protocol.indexOf("http") !== 0){
        alert("Please, write a valid url");
        return false;
    }

    $("#mention_guess_prompt").html("guessing information...");

    getURLContents(spec,function(node){
        $("#id_text").val(toMarkdown(node));
        $("#field_text_result").html("Extracted from the provided page").parent().addClass("guess-ok");
        guessCallFinished();
    });

    var source = url.host.replace(/^www\./,"");

    $("#id_source_name").val(source);
    $("#field_source_name_result").html("Guessed from the url").parent().addClass("guess-ok");


    $.getJSON(URL_ROOT + "source/" + source + ".json?_="+new Date(), function(res){
        if(res.status != 200){
            alert("Server error: " + res.status + " " + res.message);
        }else{
            res = res.response;
            var cnt=res.length;

            findDuplicates(spec, res);

            var fields = ["origin","type",
                "author_expertise","country","product","feedback",
                "previous_product_comments","estimated_audience",
                "relevant_audience","update_rate"];

            fields.forEach(function(field){
                var hist = {};
                res.forEach(function(o){
                    hist[o[field]] = (hist[o[field]]||0)+1;
                });
                var hist_ordered = [];
                for(var k in hist){
                    hist_ordered.push([k,hist[k]]);
                }
                hist_ordered.sort(function(a,b){
                    return b[1] - a[1];
                });
                if(hist_ordered.length){
                    if(field == "relevant_audience"){
                        $("#id_relevant_audience")[0].checked = hist_ordered[0][0] == "true";
                    }else{
                        $("#id_"+field).val(hist_ordered[0][0]);
                    }
                    $("#field_" + field + "_result")
                        .html(hist_ordered[0][1] + " (" + Math.round(hist_ordered[0][1]*100/cnt) + "%) of the mentions from " + source + " have this value")
                        .parent().addClass("guess-ok");
                }else{
                    $("#field_"+field+"_cnt").addClass("guess-fail");
                }
            });
            guessCallFinished();
        }
    }).error(function(){
        alert("Error guessing data :(");
        guessCancell();
    });

    return false;
}

function guessCancell(){
    $("#mention_form_otherfields_cnt").show();
    $("#mention_guess_prompt").hide();
    return false;
}
