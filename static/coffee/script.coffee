(->
  $ = null
  scriptName = "embed.js" #name of this script, used to get reference to own tag
  jqueryPath = "http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"
  jqueryVersion = "1.8.3"

  # Get reference to self (scriptTag)
  allScripts = document.getElementsByTagName('script')
  targetScripts = []
  for script, i in allScripts
    name = allScripts[i].src
    if(name && name.indexOf(scriptName) > 0)
      targetScripts.push(allScripts[i])

  scriptTag = targetScripts[targetScripts.length - 1];

  # helper function to load external scripts
  loadScript = (src, onLoad) ->
    script_tag = document.createElement('script')
    script_tag.setAttribute("type", "text/javascript")
    script_tag.setAttribute("src", src)

    if script_tag.readyState
      script_tag.onreadystatechange = ->
        if this.readyState == 'complete' || this.readyState == 'loaded'
          onLoad()
    else
      script_tag.onload = script_tag.onreadystatechange = onLoad

    (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);

  # helper function to load external css
  loadCss = (href) ->
    link_tag = document.createElement('link')
    link_tag.setAttribute("type", "text/css")
    link_tag.setAttribute("rel", "stylesheet")
    link_tag.setAttribute("href", href)
    (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(link_tag)

  # load jquery into 'jQuery' variable then call main
  if window.jQuery is undefined or window.jQuery.fn.jquery isnt jqueryVersion
    loadScript(jqueryPath, initjQuery)
  else
    initjQuery()

  window.addEventListener 'load', ->
    console.log('loaded')
    initjQuery()

  initjQuery = ->
    $ = jQuery = window.jQuery.noConflict(true)
    main()

  # starting point for your widget 
  main = ->
    loadCss "../static/css/style.css"
    buildWidget()

  buildWidget = ->
    container = $('<div>', { id: "git-satisfaction-modal"})
    container.append $('<div>', {id: "git-satisfaction-modal-body"})

    $('body').append container
      
    # //example jsonp call
    # //var jsonp_url = "www.example.com/jsonpscript.js?callback=?";
    # //jQuery.getJSON(jsonp_url, function(result) {
    # //  alert("win");
    # //});
    
    # //example load css
    # //loadCss("http://example.com/widget.css");
    
    # //example script load
    # //loadScript("http://example.com/anotherscript.js", function() { /* loaded */ });
)()