"use strict";StackExchange.mockups=function(){function e(e,t,n,r,i){function a(e,t,n){for(var r=-1,i=-1;;){if(i=t.indexOf(e,i+1),-1==i)break;(0>r||Math.abs(i-n)<Math.abs(i-r))&&(r=i)}return r}return e.replace(new RegExp("<!-- Begin mockup[^>]*? -->\\s*!\\[[^\\]]*\\]\\((http://[^ )]+)[^)]*\\)\\s*<!-- End mockup -->","g"),function(e,o,s){var c={"payload":o.replace(/[^-A-Za-z0-9+&@#\/%?=~_|!:,.;\(\)]/g,""),"pos":a(e,t,s),"len":e.length};return-1===c.pos?e:(i.push(c),e+"\n\n"+n+r+"-"+(i.length-1)+"%")})}function t(){StackExchange.externalEditor.init({"thingName":"mockup","thingFinder":e,"getIframeUrl":function(e){var t="/plugins/mockups/editor";return e&&(t+="?edit="+encodeURIComponent(e)),t},"buttonTooltip":"UI wireframe","buttonImageUrl":"/content/balsamiq/wmd-mockup-button.png?v=4","onShow":function(e){window.addMockupToEditor=e},"onRemove":function(){window.addMockupToEditor=null;try{delete window.addMockupToEditor}catch(e){}}})}return{"init":t}}(),StackExchange.schematics=function(){function e(){if(!window.postMessage)return r;var e=document.createElement("div");e.innerHTML="<svg/>";var t="http://www.w3.org/2000/svg"==(e.firstChild&&e.firstChild.namespaceURI);if(!t)return r;var n=navigator.userAgent;return/Firefox|Chrome/.test(n)?o:/Apple/.test(navigator.vendor)||/Opera/.test(n)?a:i}function t(e,t,n,r,i){function a(e,t,n){for(var r=-1,i=-1;;){if(i=t.indexOf(e,i+1),-1==i)break;(0>r||Math.abs(i-n)<Math.abs(i-r))&&(r=i)}return r}return e.replace(new RegExp("<!-- Begin schematic[^>]*? -->\\s*!\\[[^\\]]*\\]\\((http://[^ )]+)[^)]*\\)\\s*<!-- End schematic -->","g"),function(e,o,s){var c={"payload":o.replace(/[^-A-Za-z0-9+&@#\/%?=~_|!:,.;\(\)]/g,""),"pos":a(e,t,s),"len":e.length};return-1===c.pos?e:(i.push(c),e+"\n\n"+n+r+"-"+(i.length-1)+"%")})}function n(){var n;StackExchange.externalEditor.init({"thingName":"schematic","thingFinder":t,"getIframeUrl":function(e){var t="/plugins/schematics/editor";return e&&(t+="?edit="+encodeURIComponent(e)),t},"buttonTooltip":"Schematic","buttonImageUrl":"/content/electronics/img/wmd-schematic-button.png?v=1","checkSupport":function(){var t=e();switch(t){case o:return!0;case a:return confirm("Your browser is not officially supported by the schematics editor; however it has been reported to work. Launch the editor?");case i:return confirm("Your browser is not officially supported by the schematics editor; it may or may not work. Launch the editor anyway?");case r:return alert("Sorry, your browser does not support all the necessary features for the schematics editor."),!1}},"onShow":function(e){var t=$("<div class='popup' />").css("z-index",1111).text("Loading editor").appendTo("body").show().addSpinner({"marginLeft":5}).center({"dy":-200});$("<div style='text-align:right;margin-top: 10px' />").append($("<button>cancel</button>").click(function(){t.remove(),e()})).appendTo(t),n=function(n){if(n=n.originalEvent,"https://www.circuitlab.com"===n.origin){n.data||e();var r=$.parseJSON(n.data);if(r&&"success"===r.load)return t.remove(),void 0;if(r&&r.edit_url&&r.image_url){r.fkey=StackExchange.options.user.fkey;var i=$("<div class='popup' />").css("z-index",1111).appendTo("body").show(),a=function(){i.text("Storing image").addSpinner({"marginLeft":5}).center(),$.post("/plugins/schematics/save",r).done(function(t){i.remove(),e(t.img)}).fail(function(e){if(409===e.status){var t="Storing aborted";e.responseText.length<200&&(t=e.responseText),i.text(t+", will retry shortly").addSpinner({"marginLeft":5}).center(),setTimeout(a,1e4)}else i.remove(),alert("Failed to upload the schematic image.")})};a()}}},$(window).on("message",n)},"onRemove":function(){$(window).off("message",n)}})}var r=0,i=1,a=2,o=3;return{"init":n}}(),StackExchange.externalEditor=function(){function e(e){function t(e,t){function f(t){function r(){StackExchange.helpers.closePopups(x.add(i)),u()}var i,s=m||g.caret(),c=g[0].value||"",d=t?t.pos:s.start,f=t?t.len:s.end-s.start,p=c.substring(0,d),h=c.substring(d+f);m=null;var v=function(t,i){if(!t)return setTimeout(r,0),g.focus(),void 0;StackExchange.navPrevention.start();var a=void 0===i?n(t):i,o=p.replace(/(?:\r\n|\r|\n){1,2}$/,""),c=o+a+h.replace(/^(?:\r\n|\r|\n){1,2}/,""),l=s.start+a.length-p.length+o.length;setTimeout(function(){e.textOperation(function(){g.val(c).focus().caret(l,l)}),r()},0)},x=null;if(a){var b=a(t?t.payload:null);x=$("<iframe>",{"src":b})}else{var y=o(t?t.payload:null);x=$(y)}x.addClass("esc-remove").css({"position":"fixed","top":"2.5%","left":"2.5%","width":"95%","height":"95%","background":"white","z-index":1001}),$("body").loadPopup({"html":x,"target":$("body"),"lightbox":!0}).done(function(){$(window).resize(),l(v)})}$('<style type="text/css"> .wmd-'+r+"-button span { background-position: 0 0; } .wmd-"+r+"-button:hover span { background-position: 0 -40px; }</style>)").appendTo("head");var p,h,m,v=e.getConverter().hooks,g=$("#wmd-input"+t);v.chain("preConversion",function(e){var t=(e.match(/%/g)||[]).length,n=g[0].value||"";return p=new Array(t+2).join("%"),h=[],i(e,n,p,r,h)}),v.chain("postConversion",function(e){return e.replace(new RegExp(p+r+"-(\\d+)%","g"),function(e,t){return"<sup><a href='#' class='edit-"+r+"' data-id='"+t+"'>edit the above "+r+"</a></sup>"})});var x="The "+r+" editor does not support touch devices.",b=!1;$("#wmd-preview"+t).on("touchend",function(){b=!0}).on("click","a.edit-"+r,function(){return b?(alert(x),b=!1,!1):(b=!1,(!d||d())&&f(h[$(this).attr("data-id")]),!1)}),$("#wmd-input"+t).keyup(function(e){e.shiftKey||e.altKey||e.metaKey||!e.ctrlKey||77!==e.which||(!d||d())&&f()}),setTimeout(function(){var e=($("#wmd-button-bar"+t),$("#wmd-image-button"+t)),n=parseInt(e.css("left"));e.nextAll("li").each(function(){var e=$(this),t=parseInt(e.css("left"));e.css("left",t+25)});var i=$("<li class='wmd-button wmd-"+r+"-button' style='left:"+(n+25)+"px' id='wmd-"+r+"-button"+t+"' title='"+s+" Ctrl-M' />").insertAfter(e),a=!1,o=$("<span />").css({"backgroundImage":"url("+c+")"}).appendTo(i).on("touchend",function(){a=!0}).click(function(){return a?(alert(x),a=!1,void 0):(a=!1,(!d||d())&&f(),void 0)});$.browser.msie&&o.mousedown(function(){m=g.caret()})},0)}function n(e){return('\n\n<!-- Begin {THING}: In order to preserve an editable {THING}, please\n     don\'t edit this section directly.\n     Click the "edit" link below the image in the preview instead. -->\n\n![{THING}]('+e+")\n\n<!-- End {THING} -->\n\n").replace(/{THING}/g,r)}var r=e.thingName,i=e.thingFinder,a=e.getIframeUrl,o=e.getDivContent,s=e.buttonTooltip,c=e.buttonImageUrl,l=e.onShow,u=e.onRemove||function(){},d=e.checkSupport;StackExchange.MarkdownEditor.creationCallbacks.add(t)}return{"init":e}}();