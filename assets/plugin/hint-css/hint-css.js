!function(t){function i(t,i){return"function"==typeof t?t.call(i):t}function e(i,e){this.$element=t(i),this.options=e,this.enabled=!0,this.fixTitle()}e.prototype={show:function(){t(".hint-css").remove();var e=this.getTitle();if(e&&this.enabled){var s=this.tip();s.find(".hint-css-inner")[this.options.html?"html":"text"](e)[this.options.html?"addClass":"removeClass"]("hint-css-inner-html").css({"text-align":this.options.textAlign,"max-width":this.options.maxWidth?this.options.maxWidth:""}),s[0].className="hint-css",s.remove().css({top:0,left:0,visibility:"hidden",display:"block"}).prependTo(document.body),this.options.className&&s.addClass(i(this.options.className,this.$element[0])),this.options.fade?s.stop().css({opacity:0,display:"block",visibility:"visible"}).animate({opacity:this.options.opacity}):s.css({visibility:"visible",opacity:this.options.opacity}),this.calculatePosition(),this._checkStatus()}},update:function(t){var i=this.tip();i&&t&&this.enabled&&i.find(".hint-css-inner")[this.options.html?"html":"text"](t)},calculatePosition:function(){var e,s=this.tip(),n=t.extend({},this.$element.offset(),{width:this.$element[0].offsetWidth,height:this.$element[0].offsetHeight}),a=s[0].offsetWidth,h=s[0].offsetHeight,o=i(this.options.gravity,this.$element[0]);switch(o.charAt(0)){case"n":e={top:n.top+n.height+this.options.offset,left:n.left+n.width/2-a/2};break;case"s":e={top:n.top-h-this.options.offset,left:n.left+n.width/2-a/2};break;case"e":e={top:n.top+n.height/2-h/2,left:n.left-a-this.options.offset};break;case"w":e={top:n.top+n.height/2-h/2,left:n.left+n.width+this.options.offset}}2==o.length&&("w"==o.charAt(1)?e.left=n.left+n.width/2-15:e.left=n.left+n.width/2-a+15),"n"===o&&e.top+h>t(window).height()&&(o="s",e.top=n.top-h-this.options.offset),(e.left<0||e.top<0)&&(e.left=-1e3,e.top=-1e3),s.css(e),s.addClass("hint-css-"+o),s.find(".hint-css-arrow")[0].className="hint-css-arrow hint-css-arrow-"+o.charAt(0)},hide:function(){this.options.fade?this.tip().stop().fadeOut(function(){t(this).remove()}):this.tip().remove(),window.clearInterval(this._checkingInterval)},fixTitle:function(){var t=this.$element;t.attr("title")&&!t.attr("data-hint")&&t.attr("data-hint",t.attr("title")||"").removeAttr("title")},getTitle:function(){var t,i=this.$element,e=this.options;return this.fixTitle(),"string"==typeof e.title?t=i.attr("title"==e.title?"data-hint":e.title):"function"==typeof e.title&&(t=e.title.call(i[0])),(t=(""+t).replace(/(^\s*|\s*$)/,""))||e.fallback},tip:function(){return this.$tip||(this.$tip=t('<div class="hint-css"></div>').html('<div class="hint-css-arrow"></div><div class="hint-css-inner"></div>'),this.$tip.data("hint-pointee",this.$element[0])),this.$tip},_checkStatus:function(){this._checkingInterval&&window.clearInterval(this._checkingInterval);var t=this;this._checkingInterval=window.setInterval(function(){(!t.$element||t.$element.is(":hidden"))&&t.hide()},300)}},t.hint=function(){var i=function(i,s){var n=i.data("hint-css"),a=i.data("hint-object");return s.html=!!i.data("hint-html"),s.textAlign=i.data("hint-align")||t.hint.defaults.textAlign,s.maxWidth=i.data("hint-max-width")||0,n||(n=a&&"object"==typeof a?new e(i,t.extend({},t.hint.defaults,s,{className:"hint-object",html:!0,title:function(){try{a=JSON.parse(i.attr("data-hint-object"))}catch(e){}return t("<div>").append(t.dialog.getKeyAndValTable(a,2)).html()}})):new e(i,t.extend({},t.hint.defaults,s)),i.data("hint-css",n)),n},s=function(t){if(t.data("gravity"))return t.data("gravity");if(t.hasClass("hint--top"))return"s";if(t.hasClass("hint--bottom"));else if(t.hasClass("hint--left"))return"e";else if(t.hasClass("hint--right"))return"w";return"n"},n=0;t(document).on("mouseenter","[data-hint]",function(e){"ignore"!==t(this).data("hint-type")&&(void 0===t(this).attr("hint-auto")||!(t(this)[0].offsetWidth>=t(this)[0].scrollWidth))&&(e.stopPropagation&&e.stopPropagation(),n=setTimeout(function(){var n=t(e.currentTarget),a=i(n,{gravity:s(n)});a.hoverState="in",a.show()},t.hint.defaults.delayIn))}),t(document).on("mouseleave","[data-hint]",function(e){if("ignore"!==t(this).data("hint-type")){clearTimeout(n);var a=t(e.currentTarget),h=i(a,{gravity:s(a)});h.hoverState="out",h.hide()}}),t(document).on("click","[data-hint]",function(t){clearTimeout(n)})},t.fn.hint=function(i,s){var n=t("body").data("hint-css");switch(this.data("hint-type","ignore"),i){case"show":(n=new e(this,t.extend({},t.hint.defaults,{gravity:"n",className:"hint-object",html:!0,title:function(){return t("<div>").append(t.dialog.getKeyAndValTable(s,2)).html()}}))).hoverState="in",n.show(),t("body").data("hint-css",n);break;case"update":n.update(t("<div>").append(t.dialog.getKeyAndValTable(s,2)).html());break;case"hide":n.hoverState="out",n.hide()}},t.hint.defaults={className:null,delayIn:500,fade:!0,fallback:"",gravity:"n",html:!1,live:!1,offset:0,opacity:.8,title:"title",textAlign:"center",maxWidth:0}}(jQuery),$(function(){$.hint()});