(->
  $ = null
  scriptName = "embed.js" #name of this script, used to get reference to own tag
  jqueryPath = "http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"
  jqueryVersion = "1.8.3"
  dict = {}

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
      script_tag.onload = onLoad

    (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);

  # helper function to load external css
  loadCss = (href) ->
    link_tag = document.createElement('link')
    link_tag.setAttribute("type", "text/css")
    link_tag.setAttribute("rel", "stylesheet")
    link_tag.setAttribute("href", href)
    (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(link_tag)

  initjQuery = ->
    $ = jQuery = window.jQuery.noConflict(true)
    main()

  # load jquery into 'jQuery' variable then call main
  if window.jQuery is undefined or window.jQuery.fn.jquery isnt jqueryVersion
    loadScript(jqueryPath, initjQuery)
  else
    initjQuery()

  # starting point for your widget 
  main = ->
    loadCss "../static/css/style.css"
    buildWidget()
    loadIssues()
    renderForm()

  loadIssues = ->
    $.ajax
      url: "/issues"
      success: (data) =>
        renderIssues data
      dataType: "json"

  postIssue = (issue) ->
    $.ajax
      type: "POST"
      url: "/issues"
      dataType: "json"
      data: JSON.stringify issue
      success: (data) =>
        expandIssue(data.id)

  buildWidget = ->
    container = $('<div>', { id: "git-satisfaction-modal"})
    container.append $('<div>', { id: "git-satisfaction-modal-background" })    
    
    modal_body = $('<div>', {id: "git-satisfaction-modal-body"})

    left_pane = $('<div>', { id: "git-satisfaction-left-pane" })
    left_pane.append $('<div>', { id: "git-satisfaction-pane-heading", text: "Existing issues:" })
    left_pane.append $('<ul>', { id: "git-satisfaction-issue-list" })
    
    right_pane = $('<div>', { id: "git-satisfaction-right-pane" })

    modal_body.append left_pane
    modal_body.append right_pane

    container.append modal_body

    $('body').append container

  renderIssues = (issues) ->
    issue_list = $('#git-satisfaction-issue-list')
    # render each issue as an li
    for issue in issues
      dict[issue.id] = issue
      issue_list.append $("<li>", { text: "#{issue.title} (#{issue.num_subscribers})", id: issue.id, class: "git-satisfaction-issue-li" })
    
    # enlarge issue when user clicks on it
    $('.git-satisfaction-issue-li').on 'click', (e) ->
      expandIssue $(e.currentTarget).attr('id')

  renderForm = ->
    # build and replace right pane html with form
    right_pane = $('#git-satisfaction-right-pane')
    form = $('<form>', {id: "git-satisfaction-submit-form", text: "Create a new issue:"})
    form.append $('<input>', {id: "git-satisfaction-form-title", placeholder: "Enter your title here", name: "title"})
    form.append $('<textarea>', {id: "git-satisfaction-form-body", placeholder: "Enter a new issue here", name: "body"})
    form.append $('<button>', {id: "git-satisfaction-form-submit", text: "Submit", type: "submit"})
    right_pane.html form

    # add listener
    form.on 'submit', (e) =>
      e.preventDefault()
      inputs = {}
      inputs.title = $('#git-satisfaction-form-title').val()
      inputs.body = $('#git-satisfaction-form-body').val()
      postIssue inputs

  expandIssue = (id) ->
    # get correct issue object by id
    issue = dict[id]

    right_pane = $('#git-satisfaction-right-pane')
    issue_holder = $('<div>', { id: "git-satisfaction-enlarged-issue" })
    issue_holder.append $('<p>', { class: 'git-satisfaction-issue-title', text: issue.title })
    issue_holder.append $('<p>', { class: 'git-satisfaction-issue-num-voters', text: "#{issue.num_subscribers} voters" })
    issue_holder.append $('<p>', { class: 'git-satisfaction-issue-body', text: issue.body })
    right_pane.html issue_holder

  removeListeners = ->
    $('#git-satisfaction-submit-form').off()

)()
