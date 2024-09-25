<!DOCTYPE html>

<html  dir="ltr" lang="sv" xml:lang="sv">
<head>
    <title>Logga in på webbplatsen | ITHSdistans</title>
    <link rel="shortcut icon" href="https://www.ithsdistans.se/pluginfile.php/1/core_admin/favicon/64x64/1723553478/ITHS_LOGO_SMALL.png" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Logga in på webbplatsen | ITHSdistans" />
<link rel="stylesheet" type="text/css" href="https://www.ithsdistans.se/theme/yui_combo.php?rollup/3.18.1/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://www.ithsdistans.se/theme/styles.php/adaptable/1723553478_1722517005/all" />
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/www.ithsdistans.se","homeurl":{},"sesskey":"YZlCDaNFs2","sessiontimeout":"3600","sessiontimeoutwarning":"1200","themerev":"1723553478","slasharguments":1,"theme":"adaptable","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1721408063","admin":"admin","svgicons":true,"usertimezone":"Europa\/Stockholm","language":"sv","courseId":1,"courseContextId":2,"contextid":1,"contextInstanceId":0,"langrev":1724986657,"templaterev":"1721408063"};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''}
if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else{me.path=component+'/'+component+'.'+me.type}};
YUI_config = {"debug":false,"base":"https:\/\/www.ithsdistans.se\/lib\/yuilib\/3.18.1\/","comboBase":"https:\/\/www.ithsdistans.se\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/www.ithsdistans.se\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/www.ithsdistans.se\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/www.ithsdistans.se\/theme\/yui_combo.php?m\/1721408063\/","combine":true,"comboBase":"https:\/\/www.ithsdistans.se\/theme\/yui_combo.php?","ext":false,"root":"m\/1721408063\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-formchangechecker":{"requires":["base","event-focus","moodle-core-event"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core_availability-form":{"requires":["base","node","event","event-delegate","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_attendance-groupfilter":{"requires":["base","node"]},"moodle-mod_quiz-util":{"requires":["node","moodle-core-actionmenu"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_scheduler-studentlist":{"requires":["base","node","event","io"]},"moodle-mod_scheduler-saveseen":{"requires":["base","node","event"]},"moodle-mod_scheduler-delselected":{"requires":["base","node","event"]},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","node-event-html5","node-event-simulate","yui-throttle","moodle-core-notification-dialogue","moodle-editor_atto-rangy","handlebars","timers","querystring-stringify"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers","moodle-editor_atto-menu"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-qbank_editquestion-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-tool_lp-dragdrop-reorder":{"requires":["moodle-core-dragdrop"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","transition","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-alert","moodle-core-notification-warning","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emojipicker-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_h5p-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_html-beautify":{},"moodle-atto_html-codemirror":{"requires":["moodle-atto_html-codemirror-skin"]},"moodle-atto_html-button":{"requires":["promise","moodle-editor_atto-plugin","moodle-atto_html-beautify","moodle-atto_html-codemirror","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin","moodle-form-shortforms"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_recordrtc-recording":{"requires":["moodle-atto_recordrtc-button"]},"moodle-atto_recordrtc-button":{"requires":["moodle-editor_atto-plugin","moodle-atto_recordrtc-recording"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/www.ithsdistans.se\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/www.ithsdistans.se\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1721408063\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/www.ithsdistans.se\/lib\/javascript.php\/1721408063\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker","moodle-core-notification-dialogue"]},"core_comment":{"name":"core_comment","fullpath":"https:\/\/www.ithsdistans.se\/lib\/javascript.php\/1721408063\/comment\/comment.js","requires":["base","io-base","node","json","yui2-animation","overlay","escape"]}},"logInclude":[],"logExclude":[],"logLevel":null};
M.yui.loader = {modules: {}};

//]]>
</script>

<meta name="robots" content="noindex" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Twitter Card data -->
    <meta name="twitter:card" value="summary">
    <meta name="twitter:site" value="IT-Högskolan distans">
    <meta name="twitter:title" value="Logga in på webbplatsen | ITHSdistans">

    <!-- Open Graph data -->
    <meta property="og:title" content="Logga in på webbplatsen | ITHSdistans">
    <meta property="og:type" content="website" />
    <meta property="og:url" content="">
    <meta name="og:site_name" value="IT-Högskolan distans">

    <!-- Chrome, Firefox OS and Opera on Android topbar color -->
    <meta name="theme-color" content="#693250">

    <!-- Windows Phone topbar color -->
    <meta name="msapplication-navbutton-color" content="#693250">

    <!-- iOS Safari topbar color -->
    <meta name="apple-mobile-web-app-status-bar-style" content="#693250">

    <!-- Load Google main font -->
    <link href="https://fonts.googleapis.com/css?family=Lato:400,400i" rel="stylesheet" type="text/css">
    <!-- Load Google header font -->
    <link href="https://fonts.googleapis.com/css?family=Lato:400,400i" rel="stylesheet" type="text/css">
    <!-- Load Google title font -->
    <link href="https://fonts.googleapis.com/css?family=Lato:400,400i" rel="stylesheet" type="text/css">
</head><body  id="page-login-index" class="format-site  path-login dir-ltr lang-sv yui-skin-sam yui3-skin-sam www-ithsdistans-se pagelayout-login course-1 context-1 notloggedin theme theme_adaptable two-column standard fullin"><div>
    <a class="sr-only sr-only-focusable" href="#maincontent">Gå direkt till huvudinnehåll</a>
</div><script src="https://www.ithsdistans.se/lib/javascript.php/1721408063/lib/polyfills/polyfill.js"></script>
<script src="https://www.ithsdistans.se/theme/yui_combo.php?rollup/3.18.1/yui-moodlesimple-min.js"></script><script src="https://www.ithsdistans.se/theme/jquery.php/core/jquery-3.7.1.min.js"></script>
<script src="https://www.ithsdistans.se/theme/jquery.php/theme_adaptable/pace-min.js"></script>
<script src="https://www.ithsdistans.se/theme/jquery.php/theme_adaptable/jquery-flexslider-min.js"></script>
<script src="https://www.ithsdistans.se/theme/jquery.php/theme_adaptable/tickerme.js"></script>
<script src="https://www.ithsdistans.se/theme/jquery.php/theme_adaptable/jquery-easing-min.js"></script>
<script src="https://www.ithsdistans.se/theme/jquery.php/theme_adaptable/adaptable_v2_1_1_2.js"></script>
<script src="https://www.ithsdistans.se/lib/javascript.php/1721408063/lib/javascript-static.js"></script>
<script>
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>

<div id="page-wrapper"><div id="page" class="container-fluid"><div class="container outercont"><div id="page-content" class="row"><div id="region-main-box" class="col-12"><section id="region-main"><div class="login-wrapper"><div class="login-container"><div role="main"><span id="maincontent"></span><div class="loginform">
            <form class="login-form" action="https://www.ithsdistans.se/login/index.php" method="post" id="login">
                <input type="hidden" name="logintoken" value="KtF6h3c7QY35tZqJjP0FosnVRRAG4gZR">
                <div class="login-form-username form-group">
                    <label for="username" class="sr-only">
                            Användarnamn
                    </label>
                    <input type="text" name="username" id="username" class="form-control form-control-lg" value="" placeholder="Användarnamn" autocomplete="username">
                </div>
                <div class="login-form-password form-group">
                    <label for="password" class="sr-only">Lösenord</label>
                    <input type="password" name="password" id="password" value="" class="form-control form-control-lg" placeholder="Lösenord" autocomplete="current-password">
                </div>
                <div class="login-form-submit form-group">
                    <button class="loginbtn btn btn-primary btn-lg btn-block" type="submit" id="loginbtn">Logga in</button>
                </div>
                <div class="login-form-forgotpassword form-group">
                    <a href="https://www.ithsdistans.se/login/forgot_password.php">Glömt lösenordet?</a>
                </div>
            </form>
        <div class="login-divider"></div>
        <h2 class="login-heading">Några kurser kan tillåta gäster</h2>
        <form action="https://www.ithsdistans.se/login/index.php" method="post" id="guestlogin">
            <input type="hidden" name="logintoken" value="KtF6h3c7QY35tZqJjP0FosnVRRAG4gZR">
            <input type="hidden" name="username" value="guest">
            <input type="hidden" name="password" value="guest">
            <button class="loginbtn btn btn-secondary btn-block" type="submit">Logga in som gäst</button>
        </form>    <div class="login-divider"></div>
    <div class="d-flex">
            <div class="login-languagemenu">
                <div class="action-menu moodle-actionmenu" id="action-menu-0" data-enhance="moodle-core-actionmenu">
                
                        <div class="menubar d-flex " id="action-menu-0-menubar">
                
                            
                
                
                                <div class="action-menu-trigger">
                                    <div class="dropdown">
                                        <a
                                            href="#"
                                            tabindex="0"
                                            class=" dropdown-toggle icon-no-margin"
                                            id="action-menu-toggle-0"
                                            aria-label="Svenska ‎(sv)‎"
                                            data-toggle="dropdown"
                                            role="button"
                                            aria-haspopup="true"
                                            aria-expanded="false"
                                            aria-controls="action-menu-0-menu"
                                        >
                                            
                                            Svenska ‎(sv)‎
                                                
                                            <b class="caret"></b>
                                        </a>
                                            <div class="dropdown-menu menu dropdown-menu-right" id="action-menu-0-menu" data-rel="menu-content" aria-labelledby="action-menu-toggle-0" role="menu">
                                                                                                <a href="https://www.ithsdistans.se/login/index.php?lang=en" class="dropdown-item menu-action" data-lang="en" lang="en" role="menuitem" tabindex="-1" >
                                                <span class="menu-action-text">English ‎(en)‎</span>
                                        </a>
                                                                                                <a href="#" class="dropdown-item menu-action" role="menuitem" tabindex="-1" >
                                                <span class="menu-action-text">Svenska ‎(sv)‎</span>
                                        </a>
                                            </div>
                                    </div>
                                </div>
                
                        </div>
                
                </div>
            </div>
            <div class="divider border-left align-self-center mx-3"></div>
        <button type="button" class="btn btn-secondary"  data-modal="alert" data-modal-title-str='["cookiesenabled", "core"]'  data-modal-content-str='["cookiesenabled_help_html", "core"]'>Information om cookies</button>
    </div>
</div></div></div></div></section></div></div></div></div>
</div>

<script>
//<![CDATA[
var require = {
    baseUrl : 'https://www.ithsdistans.se/lib/requirejs.php/1721408063/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,
    waitSeconds : 0,

    paths: {
        jquery: 'https://www.ithsdistans.se/lib/javascript.php/1721408063/lib/jquery/jquery-3.7.1.min',
        jqueryui: 'https://www.ithsdistans.se/lib/javascript.php/1721408063/lib/jquery/ui-1.13.2/jquery-ui.min',
        jqueryprivate: 'https://www.ithsdistans.se/lib/javascript.php/1721408063/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },
      // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458).
      '*': { process: 'core/first' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script src="https://www.ithsdistans.se/lib/javascript.php/1721408063/lib/requirejs/require.min.js"></script>
<script>
//<![CDATA[
M.util.js_pending("core/first");
require(['core/first'], function() {
require(['core/prefetch'])
;
M.util.js_pending('filter_mathjaxloader/loader'); require(['filter_mathjaxloader/loader'], function(amd) {amd.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"sv"}); M.util.js_complete('filter_mathjaxloader/loader');});;
require(["media_videojs/loader"], function(loader) {
    loader.setUp('sv');
});;

    M.util.js_pending('theme_boost/loader');
    require(['theme_boost/loader', 'theme_boost/drawer'], function(Loader, Drawer) {
        Drawer.init();
        M.util.js_complete('theme_boost/loader');
    });
;

            var userNameField = document.getElementById('username');
            if (userNameField.value.length == 0) {
                userNameField.focus();
            } else {
                document.getElementById('password').focus();
            }
;
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(1, []); M.util.js_complete('core/notification');});;
M.util.js_pending('core/log'); require(['core/log'], function(amd) {amd.setConfig({"level":"warn"}); M.util.js_complete('core/log');});;
M.util.js_pending('core/page_global'); require(['core/page_global'], function(amd) {amd.init(); M.util.js_complete('core/page_global');});;
M.util.js_pending('core/utility'); require(['core/utility'], function(amd) {M.util.js_complete('core/utility');});
    M.util.js_complete("core/first");
});
//]]>
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@2.7.9/MathJax.js?delayStartupUntil=configured"></script>
<script>
//<![CDATA[
M.str = {"moodle":{"lastmodified":"Senast \u00e4ndrad","name":"Namn","error":"Fel","info":"Information","yes":"Ja","no":"Nej","cancel":"Avbryt","confirm":"Bekr\u00e4fta","areyousure":"\u00c4r du s\u00e4ker?","closebuttontitle":"St\u00e4ng","unknownerror":"Ok\u00e4nt fel","file":"Fil","url":"URL\/webbadress","collapseall":"F\u00e4ll ihop allt","expandall":"Expandera allt"},"repository":{"type":"Typ","size":"Storlek","invalidjson":"Ogiltig JSON-str\u00e4ng","nofilesattached":"Inga bifogade filer","filepicker":"Filv\u00e4ljare","logout":"Logga ut","nofilesavailable":"Det finns inga tillg\u00e4ngliga filer","norepositoriesavailable":"Tyv\u00e4rr kan ingen av dina nuvarande lagringsplatser returnera filer i det format som kr\u00e4vs.","fileexistsdialogheader":"Filen finns","fileexistsdialog_editor":"En fil med det namnet redan bifogats till texten som du redigerar.","fileexistsdialog_filemanager":"En fil med det namnet har redan bifogats","renameto":"Byt namn till &quot;{$a}&quot;","referencesexist":"Det finns {$a} l\u00e4nkar till den h\u00e4r filen","select":"V\u00e4lj"},"admin":{"confirmdeletecomments":"Du h\u00e5ller p\u00e5 att ta bort kommentarer, \u00e4r du s\u00e4ker?","confirmation":"Bekr\u00e4ftelse"},"debug":{"debuginfo":"Debuginformation","line":"Rad","stacktrace":"Stacksp\u00e5rning"},"langconfig":{"labelsep":":"}};
//]]>
</script>
<script>
//<![CDATA[
(function() {M.util.help_popups.setup(Y);
 M.util.js_pending('random66f46c92566f74'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random66f46c92566f74'); });
})();
//]]>
</script>






</body></html>