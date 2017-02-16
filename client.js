// 
//    This file is part of Kairos.
//
//    Kairos is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    Kairos is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with Kairos.  If not, see <http://www.gnu.org/licenses/>.
//


dhtmlxEvent(window,"load",function(){

    var VERSION = "3.1";
    var ajaxcpt = 0;
    var desktop = {};
    desktop.variables = {};
    desktop.current = {};
    var log = log4javascript.getLogger('CLIENT ');
    var appender = new log4javascript.BrowserConsoleAppender();
    var popUpLayout = new log4javascript.PatternLayout("%d{HH:mm:ss.SSS} %-5p %-7c - %m%n");
    appender.setLayout(popUpLayout);
    log.addAppender(appender);
    log.info('KAIROS V' + VERSION);

    document.onkeydown = function (e) {
        e = e || window.event;
        desktop.keydown = e;
        log.debug("onkeydown");
        console.log(e);
    };

    document.onclick = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        log.debug("onclick");
        console.log(e);
    }

    document.ondblclick = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        log.debug("ondblclick");
        console.log(e);

    }

    document.onmousedown = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        desktop.click = null;
        log.debug("onmousedown");
        console.log(e);

    }

    document.onmouseup = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        desktop.click = e;
        log.debug("onmouseup");
        console.log(e);
    }

    dhtmlXLayoutCell.prototype.setBG = function(url){
        var cont = this.cell.childNodes[this.conf.idx.cont];
        cont.style.backgroundImage = "url("+url+")";
        cont.style.backgroundSize = "100% 100%";
        cont = null;
    };

    dhtmlXWindowsCell.prototype.setBG = function(url){
        var cont = this.cell.childNodes[this.conf.idx.cont];
        cont.style.backgroundImage = "url("+url+")";
        cont.style.backgroundSize = "100% 100%";
        cont = null;
    };

    dhtmlXTreeView.prototype.getItem = function(id) {
        return this.items[id];
    };

    dhtmlXTreeView.prototype.forEachItem = function(f) {
        _.each(this.items, function (v, x) {
            f(x);
        });
    };


    var makeURL = function (s, p) {
        var esc = encodeURIComponent;
        var query = Object.keys(p).map(k => esc(k) + '=' + esc(p[k])).join('&');
        return query === '' ? s : s + '?' + query;
    };

    var genajax = function (method, type) {
        var h = function (s, p) {
            var f = function (next) {
                var logging = desktop.settings === undefined ? 'info' : desktop.settings.logging;
                if (p === undefined) {
                    p = {logging: logging};
                } else {
                    p.logging = p.logging === undefined ? logging : p.logging;
                }
                ajaxcpt += 1;
                desktop.layout.cells("a").cell.style.cursor = "wait";
                var ferror = function (result) {
                    ajaxcpt -= 1;
                    if (ajaxcpt === 0) {
                        desktop.layout.cells("a").cell.style.cursor = "default";
                    }
                    return next("Kairos server connection error!");
                };
                var fwarn = function (result) {
                    ajaxcpt -= 1;
                    if (ajaxcpt === 0) {
                        desktop.layout.cells("a").cell.style.cursor = "default";
                    }
                    return next("Kairos server returned: " + result.status + ", " + result.statusText);
                };
                var fdone = function (result) {
                    result = JSON.parse(result);
                    ajaxcpt -= 1;
                    if (ajaxcpt === 0) {
                        desktop.layout.cells("a").cell.style.cursor = "default";
                    }
                    if (!result.success) {
                        return next(result.message);
                    }
                    return next(null, result.data);
                };
                microAjax({url: makeURL(s, p), method: method, success: fdone, warning: fwarn, error: ferror})
            };
            var g = function(_, next) {
                f(next);
            };
            return type === 'first' ? f : g;
        };
        return h;
    };
    var ajax_get_first_in_async_waterfall = genajax("GET", "first");
    var ajax_post_first_in_async_waterfall = genajax("POST", "first");
    var ajax_get_in_async_parallel = genajax("GET", "first");
    var ajax_get_next_in_async_waterfall = genajax("GET", "next");
    
    var waterfall = function (a, fposterr) {
        async.waterfall(a, function (err, result) {
            if (err) {
                dhtmlx.message({type: "error", text: err});
                if (fposterr !== undefined) {
                    fposterr();
                }
            }
        });
    };

    var parallel = function (o, callback) {
        async.parallel(o, function (err, results) {
            if (err) {
                dhtmlx.message({type: "error", text: err});
            } else {
                callback(results);
            }
        });
    };

    var falseparallel = function (o, callback) {
        var af = [];
        var ak = [];
        _.each(o, function (f, k) {
            af.push(f);
            ak.push(k);
        });
        var results = {};
        async.series(af, function (err, aresult) {
            if (err) {
                dhtmlx.message({type: "error", text: err});
            } else {
                _.each(aresult, function (v, i) {
                    results[ak[i]] = v;
                });
                callback(results);
            }
        });
    };

    var getallusers = function (data) {
        var result = [];
        _.each(data, function (x) {
            result.push({id: x._id, value: x.user});
        });
        return result;
    };

    var getallroles = function (data) {
        var result = [];
        _.each(data, function (x) {
            result.push({id: x._id, value: x.role});
        });
        return result;
    };

    var getallgrants = function (x) {
        var result = [];
        _.each(x, function (g) {
            result.push({id: g._id, user: g.user, role: g.role});
        });
        return result;
    };

    var getallsystemdb = function (data) {
        var result = [];
        _.each(data, function (s) {
            result.push({id: s.name, value: s.name});
        });
        return result;
    };

    var getallnodesdb = function (data) {
        var result = [];
        _.each(data, function (s) {
            result.push({id: s.name, value: s.name});
        });
        return result;
    };

    var getalltemplates = function (data) {
        var result = [];
        _.each(data, function (t) {
            result.push({id: t.id, value: t.id});
        });
        return _.uniq(result);
    };

    var getallwallpapers = function (data) {
        var result = [];
        _.each(data, function (t) {
            result.push({id: t.id, value: t.id});
        });
        return _.uniq(result);
    };

    var getallcolors = function (data) {
        var result = [];
        _.each(data, function (t) {
            result.push({id: t.id, value: t.id});
        });
        return _.uniq(result);
    };


    var getallobjects = function (data) {
        var result = [];
        var idx = {};
        var iv = -1;
        _.each(data, function (x) {
            if (idx[x.origin] === undefined) {
                iv = iv + 1;
                idx[x.origin] = iv;
            }
            result.push({id: idx[x.origin] + '/' + x.rid, name: x.id, type: x.type, created: x.created, origin: x.origin});
        });
        return result;
    };

    var getalldatabases = function (data) {
        var result = [];
        _.each(data, function (x) {
            var size = x.size / 1024;
            result.push({id: x.name, size: size.toFixed(3)});
        });
        return result;
    };

    var manage_log = function(url, id, title, file) {
        var ws = new WebSocket(url);
        var uniqueid;
        var data = '';
        ws.onopen = function () {
            uniqueid = _.uniqueId('log');
            var wml = create_window(id, title);
            wml.attachHTMLString('<div id="' + uniqueid + '" style="width:100%;height:100%;overflow:auto"></div>');
            ws.send("tail -" + desktop.settings.loglines + " " + file);
        };
        ws.onmessage = function (e) {
            if (e.data === '__END_OF_PIPE__') {
                ws.close()
            } else {
                data += '<span style="white-space:pre">' + e.data + "</span>"
                setTimeout(function () { document.getElementById(uniqueid).innerHTML=data; }, 50);
            }
        };
        ws.onerror = function (e) {
            dhtmlx.message({ type: "error", text: e.data});
        };
        ws.onclose = function (e) {
            return;
        }
    }

    var create_window = function(id, title, w, h) {
        var uid = _.uniqueId(id);
        var width = w === undefined ? desktop.layout.cells("a").getWidth() / 3 * 2 : w;
        var height = h === undefined ? desktop.layout.cells("a").getHeight() / 3 * 2 : h;
        var top = h === undefined ? desktop.layout.cells("a").getHeight() / 6 : (desktop.layout.cells("a").getHeight() - h) / 2;
        var left = w === undefined ? desktop.layout.cells("a").getWidth() / 6 : (desktop.layout.cells("a").getWidth() - w) / 2;
        var win = desktop.windows.createWindow(uid, left, top, width, height);
        win.setText(title);
        desktop.toolbar.addListOption("windows", uid, -1, "button", title);
        win.attachEvent("onParkUp", function () {
            win.hide();
        });
        win.attachEvent("onClose", function () {
            desktop.toolbar.removeListOption("windows", uid);
            return true;
        });
        return win;
    };

    var login = function (x) {
        var listusers = [];
        _.each(_.sortBy(getallusers(x), function(u) {
            return u.id;
        }), function(u) {
            listusers.push({text: u.id, value: u.value});
        });
        var logindata = [
            {type: "settings", position: "label-left", labelWidth: 200, inputWidth: 200},
            {type: "fieldset", label: "Welcome", inputWidth: 420, list:[
                {type: "select", label: "Login", options: listusers, name: "user", required: true},
                {type: "password", label: "Password", value: "", name: "password", required: true},
                {type: "button", value: "Login", name: "login", width: 400}
            ]},
        ];
        var loginform = desktop.layout.cells("a").attachForm();
        loginform.loadStruct(logindata);
        loginform.base[0].style.position="absolute";
        loginform.base[0].style.width="auto";
        loginform.base[0].style.marginLeft=-Math.round(loginform.base[0].offsetWidth/2)+"px";
        loginform.base[0].style.marginTop=-Math.round(loginform.base[0].offsetHeight/2)+"px";
        loginform.base[0].style.left="50%";
        loginform.base[0].style.top="33%";
        loginform.enableLiveValidation(true);
        loginform.attachEvent("onButtonClick", function(){
            waterfall([
                ajax_post_first_in_async_waterfall("checkuserpassword", {password: loginform.getItemValue("password"), user: loginform.getItemValue("user"), logging: 'fatal'}),
                function (x) {
                    loginform.cont.style.display = "none";               
                    desktop.layout.cells("a").showToolbar();  
                    desktop.user = loginform.getItemValue("user");
                    desktop.password = loginform.getItemValue("password");
                    desktop.adminrights = x.adminrights;
                    if (! desktop.adminrights) {
                        desktop.toolbar.disableListOption("kairos", "manage_roles");
                        desktop.toolbar.disableListOption("kairos", "manage_users");
                        desktop.toolbar.disableListOption("kairos", "manage_grants");
                    }
                    document.title = 'KAIROS V' + VERSION + ' / ' + desktop.user;
                    waterfall([
                        ajax_get_first_in_async_waterfall("getsettings", {user: desktop.user}),
                        function (y) {
                            desktop.settings = y.settings;
                        }
                    ]);
                }
            ]);
        });
    };

    var settings = function () {
        var wsettings = create_window("settings", "Settings", 500, 530);
        parallel({
            systemdb: ajax_get_in_async_parallel("listsystemdb"),
            nodesdb: ajax_get_in_async_parallel("listnodesdb", {user: desktop.user}),
            templates: ajax_get_in_async_parallel("listtemplates", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
            wallpapers: ajax_get_in_async_parallel("listwallpapers", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
            colors: ajax_get_in_async_parallel("listcolors", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb})
        }, function (x) {
            var listsystemdb = [];
            _.each(_.sortBy(getallsystemdb(x.systemdb), function(s) {
                return s.id;
            }), function(s) {
                listsystemdb.push({text: s.id, value: s.value, selected: s.value === desktop.settings.systemdb ? true : false});
            });
            var listnodesdb = [];
            _.each(_.sortBy(getallnodesdb(x.nodesdb), function(n) {
                return n.id;
            }), function(n) {
                listnodesdb.push({text: n.id, value: n.value, selected: n.value === desktop.settings.nodesdb ? true : false});
            });
            var listtemplates = [];
            _.each(_.sortBy(getalltemplates(x.templates), function(t) {
                return t.id;
            }), function(t) {
                listtemplates.push({text: t.id, value: t.value, selected: t.value === desktop.settings.template ? true : false});
            });
            var listcolors = [];
            _.each(_.sortBy(getallcolors(x.colors), function(c) {
                return c.id;
            }), function(c) {
                listcolors.push({text: c.id, value: c.value, selected: c.value === desktop.settings.colors ? true : false});
            });
            var listwallpapers = [];
            _.each(_.sortBy(getallwallpapers(x.wallpapers), function(w) {
                return w.id;
            }), function(w) {
                listwallpapers.push({text: w.id, value: w.value, selected: w.value === desktop.settings.wallpaper ? true : false});
            });
            var plotorientation = [];
            _.each(['horizontal', 'vertical'], function (o) {
                plotorientation.push({text: o, value: o, selected: o === desktop.settings.plotorientation ? true : false});
            });
            var listlogging = [];
            _.each(['off', 'fatal', 'error', 'warn', 'info', 'debug', 'trace', 'all'], function (l) {
                listlogging.push({text: l, value: l, selected: l === desktop.settings.logging ? true : false});
            });
            var listloglines = [];
            _.each(_.range(100, 10000, 100), function (n) {
                listloglines.push({text: n, value: n, selected: n === desktop.settings.loglines ? true : false});
            });
            var listtop = [];
            _.each(_.range(1, 101), function (n) {
                listtop.push({text: n, value: n, selected: n === desktop.settings.top ? true : false});
            });
            var listkeycode = [];
            _.each(_.range(256), function (n) {
                listkeycode.push({text: n, value: n, selected: n === desktop.settings.keycode ? true : false});
            });

            var settingsdata = [
                {type: "settings", position: "label-left", labelWidth: 200, inputWidth: 200},
                {type: "fieldset", label: "Settings", inputWidth: 450, list:[
                    {type: "select", label: "System database", options: listsystemdb, name: "systemdb"},
                    {type: "select", label: "Nodes database", options: listnodesdb, name: "nodesdb"},
                    {type: "select", label: "Charts template", options: listtemplates, name: "template"},
                    {type: "select", label: "Colors definition", options: listcolors, name: "color"},
                    {type: "select", label: "Wallpaper", options: listwallpapers, name: "wallpaper"},
                    {type: "select", label: "Plot orientation", options: plotorientation, name: "plotorientation"},
                    {type: "select", label: "Logging", options: listlogging, name: "logging"},
                    {type: "select", label: "Log lines to display", options: listloglines, name: "loglines"},
                    {type: "select", label: "Request labels limit", options: listtop, name: "top"},
                    {type: "select", label: "Keycode", options: listkeycode, name: "keycode"}
                ]},
                {type: "button", value: "Update settings", name: "updatesettings", width: 450}
            ];
            var settingsform = wsettings.attachForm();
            settingsform.loadStruct(settingsdata);
            settingsform.base[0].style.position="absolute";
            settingsform.base[0].style.width="auto";
            settingsform.base[0].style.marginLeft=-Math.round(settingsform.base[0].offsetWidth/2)+"px";
            settingsform.base[0].style.marginTop=-Math.round(settingsform.base[0].offsetHeight/2)+"px";
            settingsform.base[0].style.left="50%";
            settingsform.base[0].style.top="50%";
            settingsform.attachEvent("onButtonClick", function(){
                waterfall([
                    ajax_get_first_in_async_waterfall("updatesettings", {user: desktop.user, systemdb: settingsform.getItemValue("systemdb"), nodesdb: settingsform.getItemValue("nodesdb"), loglines: settingsform.getItemValue("loglines"), template: settingsform.getItemValue("template"), colors: settingsform.getItemValue("color"), wallpaper: settingsform.getItemValue("wallpaper"), top: settingsform.getItemValue("top"), keycode: settingsform.getItemValue("keycode"), plotorientation: settingsform.getItemValue("plotorientation"), logging: settingsform.getItemValue("logging")}),
                    function (x) {
                        waterfall([
                            ajax_get_first_in_async_waterfall("getsettings", {user: desktop.user}),
                            function (y) {
                                desktop.settings = y.settings;
                                wsettings.close();
                            }
                        ]);
                    }
                ]);
            });
        });
    };

    var manage_objects = function () {
        var wmo = create_window("manage_objects", "Manage objects");
        var mog = wmo.attachGrid();
        mog.setHeader("Id,Object,Type,Created,Origin");
        mog.setColSorting("str,str,str,str,str");
        mog.attachHeader("#text_filter,#text_filter,#text_filter,#text_filter,#text_filter")
        mog.init();
        mog.enableSmartRendering(true);
        var mot = wmo.attachToolbar({});
        var currow = null;
        mog.attachEvent("onRowSelect", function(id){
            currow = id;
            mot.enableItem("download_object");
            mot.enableItem("delete_object");
        });
        var upload_object = function () {
            upload(makeURL("uploadobject", {nodesdb: desktop.settings.nodesdb}), refresh);
        };
        var download_object = function () {
            window.location.href = '/downloadobject?id=' + mog.cellById(currow, 1).getValue() + '&type=' + mog.cellById(currow, 2).getValue() + '&database=' + mog.cellById(currow,4).getValue();
        };
        var delete_object = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("deleteobject", {id : mog.cellById(currow, 1).getValue(), type: mog.cellById(currow, 2).getValue(), database: mog.cellById(currow,4).getValue()}),
                function (x) {
                    dhtmlx.message({text: x.msg});
                    mog.deleteRow(currow);
                    mot.disableItem("download_object");
                    mot.disableItem("delete_object");
                }
            ]);
        };

        var toolbardata = [
            {type: "button", id: "upload_object", text: "Upload object", title: "Upload object"},
            {type: "separator"},
            {type: "button", id: "download_object", text: "Download object", title: "Download object", enabled: false},
            {type: "separator"},
            {type: "button", id: "delete_object", text: "Delete object", title: "Delete object", enabled: false},
        ];
        mot.loadStruct(toolbardata);
        mot.attachEvent("onClick", function(id){
            if (id === "upload_object") {
                upload_object();
            }
            if (id === "download_object") {
                download_object();
            }
            if (id === "delete_object") {
                delete_object();
            }
        });

        var refresh = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("listobjects", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
                function (x) {
                    var datarows = [];
                    _.each(_.sortBy(getallobjects(x), function(o) {
                        return o.id;
                    }), function(o) {
                        datarows.push({id: o.id, data: [o.id, o.name, o.type, o.created, o.origin]});
                    });
                    mog.clearAll();
                    mog.parse({rows: datarows}, "json");
                }
            ]);
        };

        refresh();

    };

    var manage_roles = function () {
        var wmr = create_window("manage_roles", "Manage roles");
        var mrg = wmr.attachGrid();
        mrg.setHeader("Rid,Role");
        mrg.setColSorting("str,str");
        mrg.attachHeader("#text_filter,#text_filter")
        mrg.init();
        mrg.enableSmartRendering(true);
        var mrt = wmr.attachToolbar({});
        var currow = null;
        mrg.attachEvent("onRowSelect", function(id){
            currow = id;
            mrt.enableItem("delete_role");
        });
        var create_role = function () {
            var wcr = create_window("crrole", "Create role", 540, 200);
            var data = [
                {type: "settings", position: "label-left", labelWidth: 100, inputWidth: 300},
                {type: "fieldset", label: "Create role", inputWidth: 450, list:[
                    {type: "input", label: "Role", name: "role"},
                ]},
                {type: "button", value: "Create", name: "createrole", width: 450}
            ];
            var crf = wcr.attachForm();
            crf.loadStruct(data);
            crf.base[0].style.position="absolute";
            crf.base[0].style.width="auto";
            crf.base[0].style.marginLeft=-Math.round(crf.base[0].offsetWidth/2)+"px";
            crf.base[0].style.marginTop=-Math.round(crf.base[0].offsetHeight/2)+"px";
            crf.base[0].style.left="50%";
            crf.base[0].style.top="50%";
            crf.attachEvent("onButtonClick", function() {
                waterfall([
                    ajax_get_first_in_async_waterfall("createrole", {role: crf.getItemValue("role")}),
                    function (x) {
                        wcr.close();
                        dhtmlx.message({text: x.msg});
                        refresh();
                    }
                ]);
            });
        };
        var delete_role = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("deleterole", {role : mrg.cellById(currow, 0).getValue()}),
                function (x) {
                    dhtmlx.message({text: x.msg});
                    mrg.deleteRow(currow);
                    mrt.disableItem("delete_role");
                }
            ]);
        };

        var toolbardata = [
            {type: "button", id: "create_role", text: "Create role", title: "Create role"},
            {type: "separator"},
            {type: "button", id: "delete_role", text: "Delete role", title: "Delete role", enabled: false},
        ];
        mrt.loadStruct(toolbardata);
        mrt.attachEvent("onClick", function(id){
            if (id === "create_role") {
                create_role();
            }
            if (id === "delete_role") {
                delete_role();
            }
        });

        var refresh = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("listroles"),
                function (x) {
                    var datarows = [];
                    _.each(_.sortBy(getallroles(x), function(r) {
                        return r.id;
                    }), function(r) {
                        datarows.push({id: r.id, data: [r.id, r.value]});
                    });
                    mrg.clearAll();
                    mrg.parse({rows: datarows}, "json");
                }
            ]);
        };

        refresh();

    };

    var manage_users = function () {
        var wmu = create_window("manage_users", "Manage users");
        var mug = wmu.attachGrid();
        mug.setHeader("Uid,User");
        mug.setColSorting("str,str");
        mug.attachHeader("#text_filter,#text_filter")
        mug.init();
        mug.enableSmartRendering(true);
        var mut = wmu.attachToolbar({});
        var currow = null;
        mug.attachEvent("onRowSelect", function(id){
            currow = id;
            mut.enableItem("delete_user");
        });
        var create_user = function () {
            var wcu = create_window("cruser", "Create user", 540, 200);
            var data = [
                {type: "settings", position: "label-left", labelWidth: 100, inputWidth: 300},
                {type: "fieldset", label: "Create user", inputWidth: 450, list:[
                    {type: "input", label: "User", name: "user"},
                ]},
                {type: "button", value: "Create", name: "createuser", width: 450}
            ];
            var crf = wcu.attachForm();
            crf.loadStruct(data);
            crf.base[0].style.position="absolute";
            crf.base[0].style.width="auto";
            crf.base[0].style.marginLeft=-Math.round(crf.base[0].offsetWidth/2)+"px";
            crf.base[0].style.marginTop=-Math.round(crf.base[0].offsetHeight/2)+"px";
            crf.base[0].style.left="50%";
            crf.base[0].style.top="50%";
            crf.attachEvent("onButtonClick", function() {
                waterfall([
                    ajax_get_first_in_async_waterfall("createuser", {user: crf.getItemValue("user")}),
                    function (x) {
                        wcu.close();
                        dhtmlx.message({text: x.msg});
                        refresh();
                    }
                ]);
            });
        };
        var delete_user = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("deleteuser", {user : mug.cellById(currow, 0).getValue()}),
                function (x) {
                    dhtmlx.message({text: x.msg});
                    mug.deleteRow(currow);
                    mut.disableItem("delete_user");
                }
            ]);
        };

        var toolbardata = [
            {type: "button", id: "create_user", text: "Create user", title: "Create user"},
            {type: "separator"},
            {type: "button", id: "delete_user", text: "Delete user", title: "Delete user", enabled: false},
        ];
        mut.loadStruct(toolbardata);
        mut.attachEvent("onClick", function(id){
            if (id === "create_user") {
                create_user();
            }
            if (id === "delete_user") {
                delete_user();
            }
        });

        var refresh = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("listusers"),
                function (x) {
                    var datarows = [];
                    _.each(_.sortBy(getallusers(x), function(r) {
                        return r.id;
                    }), function(r) {
                        datarows.push({id: r.id, data: [r.id, r.value]});
                    });
                    mug.clearAll();
                    mug.parse({rows: datarows}, "json");
                }
            ]);
        };

        refresh();

    };

    var manage_grants = function () {
        var wmg = create_window("manage_grants", "Manage grants");
        var mgg = wmg.attachGrid();
        mgg.setHeader("Gid,user,role");
        mgg.setColSorting("str,str,str");
        mgg.attachHeader("#text_filter,#text_filter,#text_filter")
        mgg.init();
        mgg.enableSmartRendering(true);
        var mgt = wmg.attachToolbar({});
        var currow = null;
        mgg.attachEvent("onRowSelect", function(id){
            currow = id;
            mgt.enableItem("revoke_role");
        });
        var grant_role = function () {
            var wcg = create_window("crgrant", "Grant role", 540, 200);
            var data = [
                {type: "settings", position: "label-left", labelWidth: 100, inputWidth: 300},
                {type: "fieldset", label: "Grant role to user", inputWidth: 450, list:[
                    {type: "input", label: "User", name: "user"},
                    {type: "input", label: "Role", name: "role"},
                ]},
                {type: "button", value: "Grant", name: "grant", width: 450}
            ];
            var crf = wcg.attachForm();
            crf.loadStruct(data);
            crf.base[0].style.position="absolute";
            crf.base[0].style.width="auto";
            crf.base[0].style.marginLeft=-Math.round(crf.base[0].offsetWidth/2)+"px";
            crf.base[0].style.marginTop=-Math.round(crf.base[0].offsetHeight/2)+"px";
            crf.base[0].style.left="50%";
            crf.base[0].style.top="50%";
            crf.attachEvent("onButtonClick", function() {
                waterfall([
                    ajax_get_first_in_async_waterfall("creategrant", {user: crf.getItemValue("user"), role: crf.getItemValue("role")}),
                    function (x) {
                        wcg.close();
                        dhtmlx.message({text: x.msg});
                        refresh();
                    }
                ]);
            });
        };
        var revoke_role = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("deletegrant", {user : mgg.cellById(currow, 1).getValue(), role: mgg.cellById(currow, 2).getValue()}),
                function (x) {
                    dhtmlx.message({text: x.msg});
                    mgg.deleteRow(currow);
                    mgt.disableItem("revoke_role");
                }
            ]);
        };

        var toolbardata = [
            {type: "button", id: "grant_role", text: "Grant role", title: "Grant role"},
            {type: "separator"},
            {type: "button", id: "revoke_role", text: "Revoke role", title: "Revoke role", enabled: false},
        ];
        mgt.loadStruct(toolbardata);
        mgt.attachEvent("onClick", function(id){
            if (id === "grant_role") {
                grant_role();
            }
            if (id === "revoke_role") {
                revoke_role();
            }
        });

        var refresh = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("listgrants"),
                function (x) {
                    var datarows = [];
                    _.each(_.sortBy(getallgrants(x), function(g) {
                        return g.id;
                    }), function(g) {
                        datarows.push({id: g.id, data: [g.id, g.user, g.role]});
                    });
                    mgg.clearAll();
                    mgg.parse({rows: datarows}, "json");
                }
            ]);
        };
        refresh();
    };

    var manage_password = function () {
        var wpassword = create_window("manage_password", "Manage password", 500, 300);
        var passworddata = [
            {type: "settings", position: "label-left", labelWidth: 140, inputWidth: 260},
            {type: "fieldset", label: "Manage password", inputWidth: 450, list:[
                {type: "password", label: "Actual password", value: "", name: "actual", required: true},
                {type: "password", label: "New password", value: "", name: "new", required: true},
                {type: "password", label: "Repeat new password", value: "", name: "repeat", required: true},
            ]},
            {type: "button", value: "Set new password", name: "setpassword", width: 450}
        ];
        var passwordform = wpassword.attachForm();
        passwordform.loadStruct(passworddata);
        passwordform.base[0].style.position="absolute";
        passwordform.base[0].style.width="auto";
        passwordform.base[0].style.marginLeft=-Math.round(passwordform.base[0].offsetWidth/2)+"px";
        passwordform.base[0].style.marginTop=-Math.round(passwordform.base[0].offsetHeight/2)+"px";
        passwordform.base[0].style.left="50%";
        passwordform.base[0].style.top="50%";
        passwordform.attachEvent("onButtonClick", function(){
            if (passwordform.getItemValue("new") !== passwordform.getItemValue("repeat")) {
                dhtmlx.message({type: "error", text: "New and repeated passwords are not identicals !"});
            } else {
                waterfall([
                    ajax_post_first_in_async_waterfall("changepassword", {user: desktop.user, password: passwordform.getItemValue("actual"), new: passwordform.getItemValue("new"), logging: 'fatal'}),
                    function (x) {
                        dhtmlx.message({text: x.msg});
                        desktop.password = passwordform.getItemValue("new");
                        wpassword.close();
                    }
                ]);
            }
        });
    };

    var kairos_log = function () {
		var prefix = "wss://" + window.location.host;
        manage_log(prefix + "/get_kairos_log", "kairos_log", "KAIROS log", "/var/log/kairos/kairos.log");
    };

    var orientdb_errfile = function () {
		var prefix = "wss://" + window.location.host;
        manage_log(prefix + "/get_orientdb_errfile", "orientdb_errfile", "ORIENTDB errfile", "/orientdb/log/orientdb.err");
    };

    var webserver_log = function () {
		var prefix = "wss://" + window.location.host;
        manage_log(prefix + "/get_webserver_log", "webserver_log", "WEBSERVER log", "/var/log/kairos/webserver.log");
    };

    var documentation = function () {
        window.location.href = '/resources/kairos.pdf';
    };

    var list_databases = function () {
        var wld = create_window("list_databases", "List databases");
        var ldg = wld.attachGrid();
        ldg.setHeader("Database,Size on disk (GB)");
        ldg.setColTypes("ro,ron"); 
        ldg.setColSorting("str,int");
        ldg.init();
        ldg.enableSmartRendering(true);
        waterfall([
            ajax_get_first_in_async_waterfall("listdatabases", {user: desktop.user, admin: desktop.adminrights}),
            function (x) {
                var datarows = [];
                _.each(_.sortBy(getalldatabases(x), function(d) {
                    return d.id;
                }), function(d) {
                    datarows.push({id: d.id, data: [d.id, d.size]});
                });
                ldg.parse({rows: datarows}, "json");
            }
        ]);
    };

    var upload = function (url, onClose) {
        var wu = create_window("upload", "Upload ...");
        wu.attachEvent("onClose", function() {
            onClose();
            return true;
        });
        var vault = wu.attachVault({
            uploadUrl:  url
        });
    };

    var rename = function (oldname, callback) {
        var wr = create_window("rename", "Rename ...", 500, 200);
        var data = [
            {type: "settings", label: "", position: "label-left", labelWidth: 200, inputWidth: 200},
            {type: "fieldset", inputWidth: 450, list:[
                {type: "input", label: "Rename to ...",  name: "new", value: oldname},
            ]},
            {type: "button", value: "Rename", name: "rename", width: 450}
        ];
        var wf = wr.attachForm();
        wf.loadStruct(data);
        wf.base[0].style.position="absolute";
        wf.base[0].style.width="auto";
        wf.base[0].style.marginLeft=-Math.round(wf.base[0].offsetWidth/2)+"px";
        wf.base[0].style.marginTop=-Math.round(wf.base[0].offsetHeight/2)+"px";
        wf.base[0].style.left="50%";
        wf.base[0].style.top="50%";
        wf.attachEvent("onButtonClick", function(){
            var newname = wf.getItemValue("new");
            wr.close();
            callback(newname);
        });
    };

    var explorer = function () {
        var wexp = create_window("explorer", desktop.settings.nodesdb);
        var onclick = null;
        var tree = wexp.attachTreeView({
            dnd: true,
            context_menu: true,
            json: "gettree?nodesdb=" + desktop.settings.nodesdb + "&id={id}"
        });
        tree.attachEvent("OnDragOver", function () {
            return true;
        });
        tree.attachEvent("OnBeforeDrop", function () {
            return true;
        });
        tree.attachEvent("OnDrop", function (id, pid) {
            log.debug("from:", id);
            log.debug("to:", pid);
            console.log(desktop.click);
        });
        tree.attachEvent("onContextMenu", function(id, x, y, ev){
            return false;
        });
        var contextmenu = new dhtmlXMenuObject({
            context: true,
            items: [
				{id: "itemText"},
				{type: "separator"},
				{id: "upload", text: "Upload"},
				{type: "separator"},
				{id: "create_node", text: "Create node"},
				{id: "rename_node", text: "Rename node"},
				{id: "delete_node", text: "Delete node"},
				{id: "refresh_node", text: "Refresh node"},
				{type: "separator"},
			]
        });
        contextmenu.setIconset("awesome");
        contextmenu.setItemImage("upload","fa fa-upload");
        contextmenu.setItemImage("create_node","fa fa-magic");
        tree.attachEvent("onContextMenu", function(id, x, y, ev){
			contextmenu.setItemText("itemText", "Node: " + tree.getItemText(id));
            contextmenu.showContextMenu(x, y);
            tree.selectItem(id);
            log.debug("onContextMenu event, id: " + id + " (" + tree.getItemText(id) + ")");
            if (onclick !== null) {
                contextmenu.detachEvent(onclick);
            }
            onclick = contextmenu.attachEvent("onClick", function (fid) {
                if (fid === "upload") {
                    log.debug("Upload on item:" + id + " (" + tree.getItemText(id) + ")");
                }
                if (fid === "create_node") {
                    log.debug("Create node within item:" + id + " (" + tree.getItemText(id) + ")");
                    waterfall([
                        ajax_get_first_in_async_waterfall("createnode", {nodesdb: desktop.settings.nodesdb, id: id}),
                        function (x) {
                            tree.loadStruct("gettree?nodesdb=" + desktop.settings.nodesdb + "&id=" + id);
                        }
                    ]);
                }
                if (fid === "rename_node") {
                    log.debug("Rename node:" + id + " (" + tree.getItemText(id) + ")");
                    var oldname = tree.getItemText(id);
                    var aftergetnewname = function(name) {
                        if (name !== oldname) {
                            waterfall([
                                ajax_get_first_in_async_waterfall("renamenode", {nodesdb: desktop.settings.nodesdb, id: id, new: name}),
                                function (x) {
                                    tree.setItemText(id, name);
                                }
                            ]);
                        }
                    };
                    rename(oldname, aftergetnewname);
                }
                if (fid === "delete_node") {
                    log.debug("Delete node:" + id + " (" + tree.getItemText(id) + ")");
                    waterfall([
                        ajax_get_first_in_async_waterfall("deletenode", {nodesdb: desktop.settings.nodesdb, id: id}),
                        function (x) {
                            tree.deleteItem(id);
                        }
                    ]);
                }
                if (fid === "refresh_node") {
                    log.debug("Refresh node:" + id + " (" + tree.getItemText(id) + ")");
                    tree.loadStruct("gettree?nodesdb=" + desktop.settings.nodesdb + "&id=" + id);
                }
            });
            return false;
        });
    };

    // initMainLayout
    desktop.layout = new dhtmlXLayoutObject(document.body,"1C");
    desktop.layout.cells("a").hideHeader();
    desktop.layout.cells("a").setBG("resources/DEFAULT.jpg");
    desktop.windows = new dhtmlXWindows();
    desktop.layout.attachEvent("onPanelResizeFinish", function(cells){
        for (var q=0; q<cells.length; q++) {
            if (cells[q] == "a") {
                desktop.windows.forEachWindow(function(win){
                    win.adjustPosition();
                });
            }
        }
    });
    desktop.toolbar = desktop.layout.cells("a").attachToolbar();
    desktop.toolbar.setIconset("awesome");
    var toolbardata = [
        {type: "buttonSelect", id: "kairos", text: "KAIROS", title: "KAIROS", openAll: true, img: "fa fa-home yellow", options: [
            {type: "obj", id: "kairos_log", text: "KAIROS log", img: "fa fa-file-text-o yellow"},
            {type: "obj", id: "orientdb_errfile", text: "ORIENTDB errfile", img: "fa fa-file-text-o"},
            {type: "obj", id: "webserver_log", text: "WEBSERVER log", img: "fa fa-file-text-o"},
            {type: "separator"},
            {type: "obj", id: "documentation", text: "KAIROS documentation", img: "fa fa-file-pdf-o"},
            {type: "separator"},
            {type: "obj", id: "explorer", text: "Explorer", img: "fa fa-university"},
            {type: "separator"},
            {type: "obj", id: "manage_objects", text: "Manage objects", img: "fa fa-spinner"},
            {type: "separator"},
            {type: "obj", id: "list_databases", text: "List databases", img: "fa fa-database"},
            {type: "separator"},
            {type: "obj", id: "manage_roles", text: "Manage roles", img: "fa fa-users"},
            {type: "obj", id: "manage_users", text: "Manage users", img: "fa fa-user"},
            {type: "obj", id: "manage_grants", text: "Manage grants", img: "fa fa-book"},
            {type: "obj", id: "manage_password", text: "Manage password", img: "fa fa-key"},
            {type: "separator"},
            {type: "obj", id: "settings", text: "Settings", img: "fa fa-cog"},
            {type: "separator"},
            {type: "obj", id: "logout", text: "Logout", img: "fa fa-sign-out"}
        ]},
        {type: "separator"},
        {type: "button", id: "settings", title: "Settings", img: "fa fa-cog"},
        {type: "button", id: "explorer", title: "Explorer", img: "fa fa-university"},
        {type: "button", id: "wminimize", title: "Minize all windows", img: "fa fa-arrow-down"},
        {type: "button", id: "wclose", title: "Close all windows", img: "fa fa-close"},
        {type: "separator"},
        {type: "buttonSelect", id: "windows", text: "Windows", title: "Windows", openAll: true, img: "fa fa-th-list", options: [
        ]}
    ];
    desktop.toolbar.loadStruct(toolbardata);
    desktop.toolbar.attachEvent("onClick", function(id){
        if (id === "kairos_log") {
            kairos_log();
        }
        if (id === "orientdb_errfile") {
            orientdb_errfile();
        }
        if (id === "webserver_log") {
            webserver_log();
        }
        if (id === "documentation") {
            documentation();
        }
        if (id === "manage_objects") {
            manage_objects();
        }
        if (id === "list_databases") {
            list_databases();
        }
        if (id === "manage_roles") {
            manage_roles();
        }
        if (id === "manage_users") {
            manage_users();
        }
        if (id === "manage_grants") {
            manage_grants();
        }
        if (id === "manage_password") {
            manage_password();
        }
        if (id === "settings") {
            settings();
        }
        if (id === "explorer") {
            explorer();
        }
        if (id === "wminimize") {
            desktop.windows.forEachWindow(function (w) {
                if (!w.isParked()) {
                    w.hide();
                    w.park();
                }
            });
        }
        if (id === "wclose") {
            desktop.windows.forEachWindow(function (w) {
                w.close();
            });

        }
        if (id === "logout") {
            window.location.reload();
        }
        if (desktop.toolbar.getParentId(id) === "windows") {
            var win = desktop.windows.window(id);
            win.show();
            win.bringToTop();
            if (win.isParked()) {
                win.park();
            }
        }
    });
    desktop.layout.cells("a").hideToolbar();

    waterfall([
        ajax_get_first_in_async_waterfall("checkserverconfig"),
        ajax_get_next_in_async_waterfall("listusers"),
        function (x) {
            document.title = "KAIROS V" + VERSION;
            login(x);
        }
    ]);

});
