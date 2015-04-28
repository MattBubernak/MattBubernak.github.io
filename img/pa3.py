


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>NaturalLanguageProcessing/pa3.py at master · MattBubernak/NaturalLanguageProcessing</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="MattBubernak/NaturalLanguageProcessing" name="twitter:title" /><meta content="NaturalLanguageProcessing - Includes implementation of HMM based Viterbi algorithm, for POS tagging and other related things. " name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/3433034?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/3433034?v=3&amp;s=400" property="og:image" /><meta content="MattBubernak/NaturalLanguageProcessing" property="og:title" /><meta content="https://github.com/MattBubernak/NaturalLanguageProcessing" property="og:url" /><meta content="NaturalLanguageProcessing - Includes implementation of HMM based Viterbi algorithm, for POS tagging and other related things. " property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MzQzMzAzNDo4NTQwMzI2YTYzOWI3MmFiMWM0NzI0NjU5NzdjNjJhMDozNTM5ZDdmZDdkYTA3Y2YzYzk0NjJiYTViNWI5MTNlYjNkNTU0NWVlOWMxNGE1ODA0OWMwOGI4ZGQ2ODhjYzNm--b4b82c3568801b9eb62bdfac25d5d447e8c152a0">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="AE10741F:54C7:87C33FF:553AE4AE" name="octolytics-dimension-request_id" /><meta content="3433034" name="octolytics-actor-id" /><meta content="MattBubernak" name="octolytics-actor-login" /><meta content="15753331ba2cfd5d3e860dd50c3b675d77ea29117676a044b39be3da167820f0" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged In">
    <meta class="js-ga-set" name="dimension2" content="Header v3">
    <meta name="is-dotcom" content="true">
    <meta name="hostname" content="github.com">
    <meta name="user-login" content="MattBubernak">

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="r+IaEM6oXSAJYP6JGonCODVuLF/ZuPxwdG8wRPcjpRI4ECreaE4LLIt8vzho4z3maOkJCogBwgtxLfG6wPtulQ==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-99a212f30ce9bafd05712fa4c5c5de4e89c6c27396c34f6458dea3ea2a0b05b0.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-b21c331cc5a9542882fc1f4e2cf08c371d7e52473ffc1017b2b64e3eccc953b8.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="380e0b7c2b581631835a2841991e7107">

      
  <meta name="description" content="NaturalLanguageProcessing - Includes implementation of HMM based Viterbi algorithm, for POS tagging and other related things. ">
  <meta name="go-import" content="github.com/MattBubernak/NaturalLanguageProcessing git https://github.com/MattBubernak/NaturalLanguageProcessing.git">

  <meta content="3433034" name="octolytics-dimension-user_id" /><meta content="MattBubernak" name="octolytics-dimension-user_login" /><meta content="33843244" name="octolytics-dimension-repository_id" /><meta content="MattBubernak/NaturalLanguageProcessing" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="33843244" name="octolytics-dimension-repository_network_root_id" /><meta content="MattBubernak/NaturalLanguageProcessing" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/MattBubernak/NaturalLanguageProcessing/commits/master.atom" rel="alternate" title="Recent Commits to NaturalLanguageProcessing:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/MattBubernak/NaturalLanguageProcessing/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/MattBubernak/NaturalLanguageProcessing/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item explore">
            <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
          </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
            </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
            </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
          </li>
      </ul>

      
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/MattBubernak" data-ga-click="Header, go to profile, text:username">
      <img alt="@MattBubernak" class="avatar" data-user="3433034" height="20" src="https://avatars0.githubusercontent.com/u/3433034?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">MattBubernak</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="/new" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu">
        
<li>
  <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
</li>
<li>
  <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
</li>


  <li class="dropdown-divider"></li>
  <li class="dropdown-header">
    <span title="MattBubernak/NaturalLanguageProcessing">This repository</span>
  </li>
    <li>
      <a href="/MattBubernak/NaturalLanguageProcessing/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
    <li>
      <a href="/MattBubernak/NaturalLanguageProcessing/settings/collaboration" data-ga-click="Header, create new collaborator, icon:person"><span class="octicon octicon-person"></span> New collaborator</a>
    </li>

      </ul>
    </div>
  </li>

  <li class="header-nav-item">
      <span 
        data-channel="notification-changed:MattBubernak"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
          <span class="mail-status unread"></span>
          <span class="octicon octicon-inbox"></span>
</a>  </span>

  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="KdF6hhZ3b9SbuXaax6WJ+GgzJbqYFQxs68WJyvgNBhqueDhMISKu13YbGFn4s2r4XsYlEUIPKSlbDdZsA6a4wA==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>



    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="oeSCzyTesEiBOnWLsp1nMwp1ApZCHb1vkYCpGrSpGCyv+eyjI4PwLj4Nrcpzj4Y/hAfPYhZBLxrzL3utOiaT5Q==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="33843244" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/MattBubernak/NaturalLanguageProcessing/subscription"
          class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Unwatch
          </span>
        </a>
        <a class="social-count js-social-count" href="/MattBubernak/NaturalLanguageProcessing/watchers">
          1
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/MattBubernak/NaturalLanguageProcessing/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="TBmMk59Uk8JwmXX3HIWyizudMh4WPuqYtXOolH0B8HNg3/TC7rp34xakfGnLdv8/iwA7ofkWbgeO916lKgTeAg==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar MattBubernak/NaturalLanguageProcessing"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/MattBubernak/NaturalLanguageProcessing/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/MattBubernak/NaturalLanguageProcessing/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="5hhPSPDUvo0C7WFX+TVu2dvyAg04J4CeJtYDLyxlwyvXKkcXiS+yQ7dyU7b1w6CKwlX6nDl+WbagX82wwXMtAw==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star MattBubernak/NaturalLanguageProcessing"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/MattBubernak/NaturalLanguageProcessing/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of MattBubernak/NaturalLanguageProcessing to your account"
              aria-label="Fork your own copy of MattBubernak/NaturalLanguageProcessing to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/MattBubernak/NaturalLanguageProcessing/network" class="social-count">0</a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/MattBubernak/NaturalLanguageProcessing/fork?fragment=1">
              <img alt="Loading" height="64" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-128-338974454bb5c32803e82f601beb051d373744b024fe8742a76009700fd7e033.gif" width="64" />
            </include-fragment>
          </div>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/MattBubernak" class="url fn" itemprop="url" rel="author"><span itemprop="title">MattBubernak</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/MattBubernak/NaturalLanguageProcessing" class="js-current-repository" data-pjax="#js-repo-pjax-container">NaturalLanguageProcessing</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/MattBubernak/NaturalLanguageProcessing/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/MattBubernak/NaturalLanguageProcessing" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /MattBubernak/NaturalLanguageProcessing">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/MattBubernak/NaturalLanguageProcessing/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /MattBubernak/NaturalLanguageProcessing/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/MattBubernak/NaturalLanguageProcessing/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /MattBubernak/NaturalLanguageProcessing/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/MattBubernak/NaturalLanguageProcessing/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /MattBubernak/NaturalLanguageProcessing/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/MattBubernak/NaturalLanguageProcessing/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /MattBubernak/NaturalLanguageProcessing/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/MattBubernak/NaturalLanguageProcessing/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /MattBubernak/NaturalLanguageProcessing/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Settings">
        <a href="/MattBubernak/NaturalLanguageProcessing/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_settings /MattBubernak/NaturalLanguageProcessing/settings">
          <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
    </ul>
</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/MattBubernak/NaturalLanguageProcessing.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:MattBubernak/NaturalLanguageProcessing.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/MattBubernak/NaturalLanguageProcessing" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/MattBubernak/NaturalLanguageProcessing" class="btn btn-sm sidebar-button" title="Save MattBubernak/NaturalLanguageProcessing to your computer and use it in GitHub Desktop." aria-label="Save MattBubernak/NaturalLanguageProcessing to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/MattBubernak/NaturalLanguageProcessing/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of MattBubernak/NaturalLanguageProcessing as a zip file"
                   title="Download the contents of MattBubernak/NaturalLanguageProcessing as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/MattBubernak/NaturalLanguageProcessing/blob/1b14a499f79923806e793eb31e4f4bdb519ebf19/Assignment3/pa3.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:626b18ba291be4583e78cc6b6bad7b81 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/MattBubernak/NaturalLanguageProcessing/blob/master/Assignment3/pa3.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <form accept-charset="UTF-8" action="/MattBubernak/NaturalLanguageProcessing/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="7W6dYsrzuDgNcHxocg3d+0Oc660bJnXaDvVasXFC9sO7r28XSRVYHRveUjr6tPk8CJPjgxPnUQHBIpGm5yYrkw==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="Assignment3/pa3.py">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/MattBubernak/NaturalLanguageProcessing/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/MattBubernak/NaturalLanguageProcessing" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">NaturalLanguageProcessing</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/MattBubernak/NaturalLanguageProcessing/tree/master/Assignment3" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Assignment3</span></a></span><span class="separator">/</span><strong class="final-path">pa3.py</strong>
  </div>
</div>

<include-fragment class="commit commit-loader file-history-tease" src="/MattBubernak/NaturalLanguageProcessing/contributors/master/Assignment3/pa3.py">
  <div class="file-history-tease-header">
    Fetching contributors&hellip;
  </div>

  <div class="participation">
    <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-EAF2F5-0bdc57d34b85c4a4de9d0d1db10cd70e8a95f33ff4f46c5a8c48b4bf4e5a9abe.gif" width="16" /></p>
    <p class="loader-error">Cannot retrieve contributors at this time</p>
  </div>
</include-fragment>
<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/MattBubernak/NaturalLanguageProcessing/raw/master/Assignment3/pa3.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/MattBubernak/NaturalLanguageProcessing/blame/master/Assignment3/pa3.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/MattBubernak/NaturalLanguageProcessing/commits/master/Assignment3/pa3.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>

        <a class="octicon-btn tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/MattBubernak/NaturalLanguageProcessing?branch=master&amp;filepath=Assignment3%2Fpa3.py"
           aria-label="Open this file in GitHub for Windows">
            <span class="octicon octicon-device-desktop"></span>
        </a>

            <form accept-charset="UTF-8" action="/MattBubernak/NaturalLanguageProcessing/edit/master/Assignment3/pa3.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="tnBJR2muA+uEVSYGhR5Lz0DPko+Fjw1AxR0iqKOap94MFan59fxLFsrA+Av/Qsz+DoCUn+3ylUdwJQ5ZHOxeSA==" /></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Edit this file" data-hotkey="e" data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <form accept-charset="UTF-8" action="/MattBubernak/NaturalLanguageProcessing/delete/master/Assignment3/pa3.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Wbp4p9R2QEMjupyv3Kv5Wk1+qm2gRyEThG1UV7EDbsgO8kXSxY3HYNIMZ78xYJW/prsntYAKW4H8HJp+KO8FBg==" /></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Delete this file" data-disable-with>
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        292 lines (247 sloc)
        <span class="file-info-divider"></span>
      12.222 kb
    </div>
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#!/usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> math</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os, sys</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#emissin_prob: P( word | tag )</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#transition_rrob: P( tag_i | tag_{i-1} )</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#emission_firstCapital_prob: P( the character is capitalized (0 or 1) | tag )</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#emission_allCapital_prob: P( all character are capitalized (0 or 1) | tag )</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">tagList <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>I<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>O<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">tagType <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>I<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">1</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>O<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">2</span>}</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">tagTotalCounts <span class="pl-k">=</span> {<span class="pl-c1">0</span>:<span class="pl-c1">0</span>, <span class="pl-c1">1</span>:<span class="pl-c1">0</span>, <span class="pl-c1">2</span>:<span class="pl-c1">0</span>}</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">emission_cnt <span class="pl-k">=</span> [{} <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">transition_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span> <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">emission_allCapital_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">emission_firstCapital_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">emission_feature3_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">emission_feature4_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">emission_feature5_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">emission_feature6_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">emission_feature7_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">emission_feature8_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">emission_feature9_cnt <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">firstTag_cnt <span class="pl-k">=</span> [<span class="pl-c1">0</span> <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">emission_prob <span class="pl-k">=</span> [{} <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">emission_allCapital_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">emission_firstCapital_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">emission_feature3_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">emission_feature4_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">emission_feature5_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">emission_feature6_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">emission_feature7_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">emission_feature8_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">emission_feature9_prob <span class="pl-k">=</span> [[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">transition_prob <span class="pl-k">=</span> [<span class="pl-c1">None</span> <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">firstTag_prob <span class="pl-k">=</span> [<span class="pl-c1">None</span> <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))]</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># weight for [emission_prob, emission_firstCaptial_prob, emission_allCapital_prob]</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">weights <span class="pl-k">=</span> [<span class="pl-c1">0.9999995</span>, <span class="pl-c1">0.0000000005</span>, <span class="pl-c1">0.000000480</span>,<span class="pl-c1">0.000000045</span>,<span class="pl-c1">0.00000000075</span> ,<span class="pl-c1">0.00000000075</span>,<span class="pl-c1">0.00000000075</span>]</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#weights = [0.9999995, 0.000000000, 0.00000000,0.000000000,0.00000005]</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#Below setup got: .485588</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#weights = [0.9999995, 0.0000000005, 0.0000004700,0.000000028,0.00000000075 ,0.00000000075 ]</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#Below got .49234</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#weights = [0.9999995, 0.0000000005, 0.000000480,0.000000045,0.00000000075 ,0.0000000008 ]</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#Below got .492409</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#weights = [0.9999995, 0.0000000005, 0.000000480,0.000000045,0.00000000075 ,0.00000000075,0.00000000075]</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Feature 1</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">isAllCapitalRE <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-k">^</span><span class="pl-c1">[<span class="pl-c1">A-Z</span>]</span><span class="pl-k">+</span><span class="pl-k">$</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Feature 2</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">isFirstCapitalRE <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-k">^</span><span class="pl-c1">[<span class="pl-c1">A-Z</span>]</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Feature 3</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">isNumberAndCapRE <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-k">^</span>(?=<span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-c1">\d</span>)(?=<span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-c1">[<span class="pl-c1">a-zA-Z</span>]</span>)<span class="pl-c1">[<span class="pl-c1">A-Z</span><span class="pl-c1">\d</span>]</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Feature 4</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">isInSuffix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-k">^</span><span class="pl-c1">.</span><span class="pl-k">+</span>in<span class="pl-k">$</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Feature 5</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">isAseSuffix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-k">^</span><span class="pl-c1">.</span><span class="pl-k">+</span>ase<span class="pl-c1">[s]</span><span class="pl-k">*</span><span class="pl-k">$</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Feature 6</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">AllLowerChars <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-k">^</span><span class="pl-c1">[<span class="pl-c1">a-z</span>]</span><span class="pl-k">+</span><span class="pl-k">$</span><span class="pl-pds">&quot;</span></span> </td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#Not currently used</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">between2and4chars <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-k">^</span><span class="pl-c1">.</span><span class="pl-k">{2,4}</span><span class="pl-k">$</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">ContainsMultCapitalRE <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-c1">[<span class="pl-c1">A-Z</span>]</span><span class="pl-k">+</span><span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-c1">[<span class="pl-c1">A-Z</span>]</span><span class="pl-k">+</span><span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">ContainsCapIwithlowercasebefore <span class="pl-k">=</span> <span class="pl-s"><span class="pl-k">r</span><span class="pl-pds">&quot;</span><span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-c1">[<span class="pl-c1">a-z</span>]</span><span class="pl-k">+</span><span class="pl-c1">.</span><span class="pl-k">*</span>I<span class="pl-k">+</span><span class="pl-c1">.</span><span class="pl-k">*</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">extractFeature</span>(<span class="pl-smi">word</span>):</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">	<span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	Given one word, return the matching of the feature</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	1 for True, 0 for False</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	word = &quot;AAb&quot; -&gt; return [0, 1]</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	word = &quot;AAB&quot; -&gt; return [0, 0]</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	word = &quot;bbA&quot; -&gt; return [0, 0]</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#if (re.match(ContainsCapitalRE,&quot;aaaAsaa&quot;)):</span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#	print &quot;match&quot;</span></td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#else:</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#	print &quot;not match&quot;</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> [<span class="pl-c1">1</span> <span class="pl-k">if</span> (t <span class="pl-k">!=</span> <span class="pl-c1">None</span>) <span class="pl-k">else</span> <span class="pl-c1">0</span> <span class="pl-k">for</span> t <span class="pl-k">in</span> [re.match(isAllCapitalRE, word), re.match(isFirstCapitalRE, word), re.match(isNumberAndCapRE, word),re.match(isInSuffix, word),re.match(isAseSuffix, word),re.match(AllLowerChars, word)]]</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">viterbiPath</span>(<span class="pl-smi">tokenList</span>):</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">	<span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	Given the a list of token(word), go through the viterbi algorithm</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">	viterbiTable <span class="pl-k">=</span> [ [ <span class="pl-c1">0.0</span> <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList)) ] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tokenList)) ]</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">	backPointer <span class="pl-k">=</span> [ [ <span class="pl-k">-</span><span class="pl-c1">1</span> <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList)) ] <span class="pl-k">for</span> _ <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tokenList)) ]</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">	tinyProb <span class="pl-k">=</span> math.exp(<span class="pl-k">-</span><span class="pl-c1">100</span>)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">	startOfBacktrace <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-c1">len</span>(tokenList) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">return</span> []</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> (wordIdx, word) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(tokenList):</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">		(isAllCapital, isFirstCapital, feature3,feature4,feaure5,feature6) <span class="pl-k">=</span> extractFeature(word)</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> tagID <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList)):</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> wordIdx <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># first word: just use the emission prob</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">				<span class="pl-c">#viterbiTable[wordIdx][tagID] = (tinyProb if firstTag_prob[tagID] == None else firstTag_prob[tagID]) * (tinyProb if word not in emission_prob[tagID] else emission_prob[tagID][word]</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> firstTag_prob[tagID] <span class="pl-k">==</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">					viterbiTable[wordIdx][tagID] <span class="pl-k">=</span> tinyProb</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">					viterbiTable[wordIdx][tagID] <span class="pl-k">=</span> firstTag_prob[tagID]</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> word <span class="pl-k">not</span> <span class="pl-k">in</span> emission_prob[tagID]:</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">					viterbiTable[wordIdx][tagID] <span class="pl-k">*=</span> tinyProb</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">					viterbiTable[wordIdx][tagID] <span class="pl-k">*=</span> emission_prob[tagID][word]</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># following word: use both emission prob (mixture) and transition prob</span></td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">				maxProb <span class="pl-k">=</span> <span class="pl-c1">0.0</span></td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># transition prob</span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> prevTagID <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList)):</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">					tProb <span class="pl-k">=</span> (tinyProb <span class="pl-k">if</span> transition_prob[prevTagID][tagID] <span class="pl-k">==</span> <span class="pl-c1">None</span> <span class="pl-k">else</span> transition_prob[prevTagID][tagID]) <span class="pl-k">*</span> viterbiTable[wordIdx<span class="pl-k">-</span><span class="pl-c1">1</span>][prevTagID]</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> tProb <span class="pl-k">&gt;</span> maxProb:</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">						maxProb <span class="pl-k">=</span> tProb </td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">						backPointer[wordIdx][tagID] <span class="pl-k">=</span> prevTagID</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># omission prob</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">				tProb <span class="pl-k">=</span> weights[<span class="pl-c1">0</span>] <span class="pl-k">*</span>  (tinyProb <span class="pl-k">if</span> word <span class="pl-k">not</span> <span class="pl-k">in</span> emission_prob[tagID] <span class="pl-k">else</span> emission_prob[tagID][word])</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">				tProb <span class="pl-k">+=</span> weights[<span class="pl-c1">1</span>] <span class="pl-k">*</span> (tinyProb <span class="pl-k">if</span> emission_allCapital_prob[tagID][isAllCapital] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_allCapital_prob[tagID][isAllCapital])</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">				tProb <span class="pl-k">+=</span> weights[<span class="pl-c1">2</span>] <span class="pl-k">*</span> (tinyProb <span class="pl-k">if</span> emission_firstCapital_prob[tagID][isFirstCapital] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_firstCapital_prob[tagID][isFirstCapital])</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">				tProb <span class="pl-k">+=</span> weights[<span class="pl-c1">3</span>] <span class="pl-k">*</span> (tinyProb <span class="pl-k">if</span> emission_feature3_prob[tagID][feature3] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature3_prob[tagID][feature3])</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">				tProb <span class="pl-k">+=</span> weights[<span class="pl-c1">4</span>] <span class="pl-k">*</span> (tinyProb <span class="pl-k">if</span> emission_feature4_prob[tagID][feature4] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature4_prob[tagID][feature4])</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">				tProb <span class="pl-k">+=</span> weights[<span class="pl-c1">5</span>] <span class="pl-k">*</span> (tinyProb <span class="pl-k">if</span> emission_feature5_prob[tagID][feature5] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature5_prob[tagID][feature5])</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">				tProb <span class="pl-k">+=</span> weights[<span class="pl-c1">6</span>] <span class="pl-k">*</span> (tinyProb <span class="pl-k">if</span> emission_feature6_prob[tagID][feature6] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature6_prob[tagID][feature6])</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># and calculate other feature</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">				maxProb <span class="pl-k">=</span>  maxProb <span class="pl-k">*</span> tProb</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">				viterbiTable[wordIdx][tagID] <span class="pl-k">=</span> maxProb</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">				<span class="pl-c">#print &quot;Just updated table for word: &quot; + tokenList[wordIdx] + &quot; and tag: &quot; + tagList[tagID] + &quot; to be: &quot; + str(maxProb)</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">				<span class="pl-c">#print str(emission_prob[1][1])</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#Trace back to find out the best labeling path by using backPointer</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"># return the label for each token</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">	labelSent <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">	startOfBackTrace <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">	maxVal <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> tag <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">0</span>,<span class="pl-c1">3</span>):</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">		<span class="pl-c">#print &quot; tag: &quot; + tagList[tag] +&quot; &quot;+ str(viterbiTable[len(testSent)-1][tag])</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">		<span class="pl-c">#print &quot;tag:&quot; + str(tag)</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">		viterbiVal <span class="pl-k">=</span> viterbiTable[<span class="pl-c1">len</span>(tokenList)<span class="pl-k">-</span><span class="pl-c1">1</span>][tag]</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># Check if this is the maximum final viterbi value, aka the start point for our backtrace. </span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> (viterbiVal <span class="pl-k">&gt;</span> maxVal):</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">			maxVal <span class="pl-k">=</span> viterbiVal</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">			startOfBacktrace <span class="pl-k">=</span> tag</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#print str(startOfBacktrace)</span></td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#print &quot;starting our backtrace at: &quot; + tagList[startOfBacktrace]</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">	cur <span class="pl-k">=</span> startOfBacktrace</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#print &quot;cur: &quot; + str(cur)</span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#print &quot;appending: &quot; + tagList[cur]</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">	labelSent.insert(<span class="pl-c1">0</span>,tagList[cur])</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> (wordIdx, word) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(tokenList):</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> <span class="pl-c1">len</span>(tokenList)<span class="pl-k">-</span><span class="pl-c1">1</span><span class="pl-k">-</span>wordIdx <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">else</span>: </td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">			cur <span class="pl-k">=</span> backPointer[<span class="pl-c1">len</span>(tokenList)<span class="pl-k">-</span><span class="pl-c1">1</span><span class="pl-k">-</span>wordIdx][cur]</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">			<span class="pl-c">#print &quot;appending: &quot; + tagList[cur]</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">			labelSent.insert(<span class="pl-c1">0</span>,tagList[cur])</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> labelSent</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">	<span class="pl-c">#Check the input parameter is correct</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-c1">len</span>(sys.argv) <span class="pl-k">!=</span> <span class="pl-c1">4</span>:</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">raise</span> <span class="pl-c1">Exception</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Please follow this input format: python pa3_tutorial.py TRAIN_FILE DEV_FILE LABEL_FILE<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">	trainFile <span class="pl-k">=</span> sys.argv[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">	devFile <span class="pl-k">=</span> sys.argv[<span class="pl-c1">2</span>]</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">	labelFile <span class="pl-k">=</span> sys.argv[<span class="pl-c1">3</span>]</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> os.path.exists(trainFile) <span class="pl-k">!=</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">raise</span> <span class="pl-c1">Exception</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Train file <span class="pl-c1">%s</span> does not exist<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> trainFile)</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> os.path.exists(devFile) <span class="pl-k">!=</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">raise</span> <span class="pl-c1">Exception</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Dev file <span class="pl-c1">%s</span> does not exist<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> devFile)</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"># Read train file</span></td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(trainFile, <span class="pl-s"><span class="pl-pds">&quot;</span>r<span class="pl-pds">&quot;</span></span>) <span class="pl-k">as</span> fhd:</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># Initialize prevTagID to be -1 to start. </span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">		prevTagID <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># Counting</span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># Read each line. </span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> line <span class="pl-k">in</span> fhd.xreadlines():</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">			<span class="pl-c"># Strip any newlines from the end</span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">			line <span class="pl-k">=</span> line.strip()</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">			<span class="pl-c"># If we have a blank line, reset the prevTag</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> line <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">				prevTagID <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Grab the word/tag</span></td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">				(word, tag) <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Extract all the possible features of the word. </span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">				(isAllCapital, isFirstCapital,feature3,feature4,feature5,feature6) <span class="pl-k">=</span> extractFeature(word)</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Get the tag</span></td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">				tagID <span class="pl-k">=</span> tagType[tag]</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">				tagTotalCounts[tagID] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># If this is the start of the sentence</span></td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> prevTagID <span class="pl-k">==</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">					<span class="pl-c"># Add to the firstTag cnt for this tag. </span></td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">					firstTag_cnt[tagID] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">					<span class="pl-c"># Otherwise update our ransition count matrix </span></td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">					transition_cnt[prevTagID][tagID] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Save this tag as the previous tag. </span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">				prevTagID <span class="pl-k">=</span> tagID</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># deal with the emission_cnt, emission_allCapital_cnt, emission_firstCapital_cnt, and other emission feature count by yourself</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> word <span class="pl-k">not</span> <span class="pl-k">in</span> emission_cnt[tagID]:</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">					emission_cnt[tagID][word] <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">				emission_cnt[tagID][word] <span class="pl-k">+=</span> <span class="pl-c1">1</span> </td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">				emission_allCapital_cnt[tagID][isAllCapital] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">				emission_firstCapital_cnt[tagID][isFirstCapital] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">				emission_feature3_cnt[tagID][feature3] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">				emission_feature4_cnt[tagID][feature4] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">				emission_feature5_cnt[tagID][feature5] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">				emission_feature6_cnt[tagID][feature6] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"># calculate the prob</span></td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">	total_firstTag <span class="pl-k">=</span> <span class="pl-c1">sum</span>(firstTag_cnt)</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"># For each possible tag</span></td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> tagID <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList)):</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># Calculate all of our transition probabilities. </span></td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">		total_prevTag <span class="pl-k">=</span> <span class="pl-c1">sum</span>( [transition_cnt[tagID][currentTagID] <span class="pl-k">for</span> currentTagID <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList))] )</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">		transition_prob[tagID] <span class="pl-k">=</span> [ <span class="pl-c1">None</span> <span class="pl-k">if</span> transition_cnt[tagID][currentTagID] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> transition_cnt[tagID][currentTagID]<span class="pl-k">/</span><span class="pl-c1">float</span>(total_prevTag) <span class="pl-k">for</span> currentTagID <span class="pl-k">in</span> <span class="pl-c1">xrange</span>(<span class="pl-c1">len</span>(tagList)) ]</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># Calculate all of our emission probabilities. </span></td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> word <span class="pl-k">in</span> emission_cnt[tagID]:</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">			emission_prob[tagID][word] <span class="pl-k">=</span> emission_cnt[tagID][word]<span class="pl-k">/</span><span class="pl-c1">float</span>(tagTotalCounts[tagID])</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">		<span class="pl-c">#print tagTotalCounts[tagID]</span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">		<span class="pl-c">#emission_prob[tagID] = [ None if emission_cnt[tagID][word] == 0 else emission_cnt[tagID][word]/float(tagTotalCounts[tagID]) for word in emission_cnt[tagID] ]</span></td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">		<span class="pl-c">#print tagID</span></td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">		emission_allCapital_prob[tagID] <span class="pl-k">=</span> [ <span class="pl-c1">0</span> <span class="pl-k">if</span> emission_allCapital_cnt[tagID][num] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_allCapital_cnt[tagID][num]<span class="pl-k">/</span><span class="pl-c1">float</span>(emission_allCapital_cnt[tagID][<span class="pl-c1">0</span>] <span class="pl-k">+</span> emission_allCapital_cnt[tagID][<span class="pl-c1">1</span>]) <span class="pl-k">for</span> num <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">2</span>) ]</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">		emission_firstCapital_prob[tagID] <span class="pl-k">=</span> [ <span class="pl-c1">0</span> <span class="pl-k">if</span> emission_firstCapital_cnt[tagID][num] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_firstCapital_cnt[tagID][num]<span class="pl-k">/</span><span class="pl-c1">float</span>(emission_firstCapital_cnt[tagID][<span class="pl-c1">0</span>] <span class="pl-k">+</span> emission_firstCapital_cnt[tagID][<span class="pl-c1">1</span>]) <span class="pl-k">for</span> num <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">2</span>) ]</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">		emission_feature3_prob[tagID] <span class="pl-k">=</span> [ <span class="pl-c1">0</span> <span class="pl-k">if</span> emission_feature3_cnt[tagID][num] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature3_cnt[tagID][num]<span class="pl-k">/</span><span class="pl-c1">float</span>(emission_feature3_cnt[tagID][<span class="pl-c1">0</span>] <span class="pl-k">+</span> emission_feature3_cnt[tagID][<span class="pl-c1">1</span>]) <span class="pl-k">for</span> num <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">2</span>) ]</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">		emission_feature4_prob[tagID] <span class="pl-k">=</span> [ <span class="pl-c1">0</span> <span class="pl-k">if</span> emission_feature4_cnt[tagID][num] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature4_cnt[tagID][num]<span class="pl-k">/</span><span class="pl-c1">float</span>(emission_feature4_cnt[tagID][<span class="pl-c1">0</span>] <span class="pl-k">+</span> emission_feature4_cnt[tagID][<span class="pl-c1">1</span>]) <span class="pl-k">for</span> num <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">2</span>) ]</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">		emission_feature5_prob[tagID] <span class="pl-k">=</span> [ <span class="pl-c1">0</span> <span class="pl-k">if</span> emission_feature5_cnt[tagID][num] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature5_cnt[tagID][num]<span class="pl-k">/</span><span class="pl-c1">float</span>(emission_feature5_cnt[tagID][<span class="pl-c1">0</span>] <span class="pl-k">+</span> emission_feature5_cnt[tagID][<span class="pl-c1">1</span>]) <span class="pl-k">for</span> num <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">2</span>) ]</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">		emission_feature6_prob[tagID] <span class="pl-k">=</span> [ <span class="pl-c1">0</span> <span class="pl-k">if</span> emission_feature6_cnt[tagID][num] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> emission_feature6_cnt[tagID][num]<span class="pl-k">/</span><span class="pl-c1">float</span>(emission_feature6_cnt[tagID][<span class="pl-c1">0</span>] <span class="pl-k">+</span> emission_feature6_cnt[tagID][<span class="pl-c1">1</span>]) <span class="pl-k">for</span> num <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">2</span>) ]</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"># Read Test, write the label to labelFile</span></td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">	testSent <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(devFile, <span class="pl-s"><span class="pl-pds">&quot;</span>r<span class="pl-pds">&quot;</span></span>) <span class="pl-k">as</span> fhd, <span class="pl-c1">open</span>(labelFile, <span class="pl-s"><span class="pl-pds">&quot;</span>w<span class="pl-pds">&quot;</span></span>) <span class="pl-k">as</span> fhd_write:</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># For every line of the test file</span></td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> line <span class="pl-k">in</span> fhd.xreadlines():</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">			<span class="pl-c"># Read the line</span></td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">			line <span class="pl-k">=</span> line.strip()</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">			<span class="pl-c"># If it&#39;s a blank line</span></td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> line <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Send the current sentence to the viterbi algorithm. </span></td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">				labelSent <span class="pl-k">=</span> viterbiPath(testSent)</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># write label file</span></td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">0</span>,<span class="pl-c1">len</span>(testSent)):</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">					fhd_write.write(testSent[i] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> labelSent[i] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">				fhd_write.write(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Empty the test set. </span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">				testSent <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">			<span class="pl-c"># If it&#39;s not a blank line</span></td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">				<span class="pl-c">#print line</span></td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Read each line</span></td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">					(word, label) <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">					word <span class="pl-k">=</span> line</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"># Append the current word to the testSent</span></td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">				testSent.append(word)</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">		<span class="pl-c">#deal with the last sentence</span></td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">		labelSent <span class="pl-k">=</span> viterbiPath(testSent)</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"># write  label file</span></td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">0</span>,<span class="pl-c1">len</span>(testSent)):</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">			fhd_write.write(testSent[i] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\t</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> labelSent[i] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.08633s from github-fe136-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-2c8ae50712a47d2b83d740cb875d55cdbbb3fdbccf303951cc6b7e63731e0c38.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-fe1102a627c0f0eb4c8ccd94ee4ecb4ea91eb19e1ea462b1d6fe0435bb27e366.js"></script>
      
      

      <div class="js-socket-channel" data-channel="test:MattBubernak"></div>

  </body>
</html>

