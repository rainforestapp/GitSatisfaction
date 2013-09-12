// Generated by CoffeeScript 1.3.3
(function() {

  (function() {
    var $, allScripts, buildWidget, i, initjQuery, jqueryPath, jqueryVersion, loadCss, loadScript, main, name, script, scriptName, scriptTag, targetScripts, _i, _len;
    $ = null;
    scriptName = "embed.js";
    jqueryPath = "http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js";
    jqueryVersion = "1.8.3";
    allScripts = document.getElementsByTagName('script');
    targetScripts = [];
    for (i = _i = 0, _len = allScripts.length; _i < _len; i = ++_i) {
      script = allScripts[i];
      name = allScripts[i].src;
      if (name && name.indexOf(scriptName) > 0) {
        targetScripts.push(allScripts[i]);
      }
    }
    scriptTag = targetScripts[targetScripts.length - 1];
    loadScript = function(src, onLoad) {
      var script_tag;
      script_tag = document.createElement('script');
      script_tag.setAttribute("type", "text/javascript");
      script_tag.setAttribute("src", src);
      if (script_tag.readyState) {
        script_tag.onreadystatechange = function() {
          if (this.readyState === 'complete' || this.readyState === 'loaded') {
            return onLoad();
          }
        };
      } else {
        script_tag.onload = script_tag.onreadystatechange = onLoad;
      }
      return (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);
    };
    loadCss = function(href) {
      var link_tag;
      link_tag = document.createElement('link');
      link_tag.setAttribute("type", "text/css");
      link_tag.setAttribute("rel", "stylesheet");
      link_tag.setAttribute("href", href);
      return (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(link_tag);
    };
    if (window.jQuery === void 0 || window.jQuery.fn.jquery !== jqueryVersion) {
      loadScript(jqueryPath, initjQuery);
    } else {
      initjQuery();
    }
    window.addEventListener('load', function() {
      console.log('loaded');
      return initjQuery();
    });
    initjQuery = function() {
      var jQuery;
      $ = jQuery = window.jQuery.noConflict(true);
      return main();
    };
    main = function() {
      loadCss("../static/css/style.css");
      return buildWidget();
    };
    return buildWidget = function() {
      var container;
      container = $('<div>', {
        id: "git-satisfaction-modal"
      });
      container.append($('<div>', {
        id: "git-satisfaction-modal-body"
      }));
      return $('body').append(container);
    };
  })();

}).call(this);
