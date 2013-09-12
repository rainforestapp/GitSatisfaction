// Generated by CoffeeScript 1.6.2
(function() {
  (function() {
<<<<<<< HEAD
    var $, allScripts, buildWidget, i, initjQuery, jqueryPath, jqueryVersion, loadCss, loadScript, main, name, renderForm, renderIssue, renderIssues, script, scriptName, scriptTag, targetScripts, _i, _len;
=======
    var $, allScripts, buildWidget, i, initjQuery, jqueryPath, jqueryVersion, loadCss, loadScript, main, name, script, scriptName, scriptTag, targetScripts, _i, _len;

>>>>>>> 6e040e06420fcff51b20c488dbc6d13382c1702d
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
        script_tag.onload = onLoad;
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
    initjQuery = function() {
      var jQuery;

      $ = jQuery = window.jQuery.noConflict(true);
      return main();
    };
    if (window.jQuery === void 0 || window.jQuery.fn.jquery !== jqueryVersion) {
      loadScript(jqueryPath, initjQuery);
    } else {
      initjQuery();
    }
    main = function() {
      loadCss("../static/css/style.css");
      buildWidget();
      renderIssues(['thing', 'next', 'lol', 'biz']);
      return renderForm();
    };
<<<<<<< HEAD
    buildWidget = function() {
      var container, left_pane, modal_body, right_pane;
=======
    return buildWidget = function() {
      var container;

>>>>>>> 6e040e06420fcff51b20c488dbc6d13382c1702d
      container = $('<div>', {
        id: "git-satisfaction-modal"
      });
      container.append($('<div>', {
        id: "git-satisfaction-modal-background"
      }));
      modal_body = $('<div>', {
        id: "git-satisfaction-modal-body"
      });
      left_pane = $('<div>', {
        id: "git-satisfaction-left-pane"
      });
      left_pane.append($('<div>', {
        id: "git-satisfaction-pane-heading",
        text: "Existing issues:"
      }));
      left_pane.append($('<ul>', {
        id: "git-satisfaction-issue-list"
      }));
      right_pane = $('<div>', {
        id: "git-satisfaction-right-pane"
      });
      modal_body.append(left_pane);
      modal_body.append(right_pane);
      container.append(modal_body);
      return $('body').append(container);
    };
    renderIssues = function(issues) {
      var issue, issue_list, _j, _len1, _results;
      issue_list = $('#git-satisfaction-issue-list');
      _results = [];
      for (_j = 0, _len1 = issues.length; _j < _len1; _j++) {
        issue = issues[_j];
        _results.push(issue_list.append($("<li>", {
          text: issue
        })));
      }
      return _results;
    };
    renderForm = function() {
      var form, right_pane;
      right_pane = $('#git-satisfaction-right-pane');
      form = $('<form>', {
        id: "git-satisfaction-submit-form",
        text: "Create a new issue:"
      });
      form.append($('<textarea>', {
        id: "git-satisfaction-form-textarea",
        placeholder: "Enter a new issue here",
        name: "new-issue"
      }));
      form.append($('<button>', {
        id: "git-satisfaction-form-submit",
        text: "Submit",
        type: "submit"
      }));
      right_pane.html(form);
      return form.on('submit', function(e) {
        var inputs;
        e.preventDefault();
        inputs = form.serializeArray();
        $('#git-satisfaction-form-textarea').val("");
        return renderIssue();
      });
    };
    return renderIssue = function(issue) {
      var issue_holder, right_pane;
      right_pane = $('#git-satisfaction-right-pane');
      issue_holder = $('<div>', {
        id: "git-satisfaction-enlarged-issue"
      });
      issue_holder.append($('<p>', {
        "class": 'git-satisfaction-p',
        text: "Leberkäse spare ribs beef kielbasa frankfurter, corned beef strip steak jerky. Bacon flank meatball jowl, hamburger boudin jerky sirloin rump venison turkey drumstick tenderloin. Corned beef turkey beef, hamburger capicola spare ribs ham cow chuck pork chop ribeye tenderloin bresaola venison tongue. Ground round pancetta"
      }));
      return right_pane.html(issue_holder);
    };
  })();

}).call(this);
