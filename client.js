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
    };

    document.onclick = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        log.debug("onclick");
    }

    document.ondblclick = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        log.debug("ondblclick");

    }

    document.onmousedown = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        desktop.click = null;
        log.debug("onmousedown");

    }

    document.onmouseup = function (e) {
        e = e || window.event;
        desktop.mousevent = e;
        desktop.click = e;
        log.debug("onmouseup");
    }

    dhtmlXLayoutCell.prototype.setBI = function(url){
        var cont = this.cell.childNodes[this.conf.idx.cont];
        cont.style.backgroundImage = "url("+url+")";
        cont.style.backgroundSize = "100% 100%";
        cont = null;
    };

    dhtmlXWindowsCell.prototype.setBI = function(url){
        var cont = this.cell.childNodes[this.conf.idx.cont];
        cont.style.backgroundImage = "url("+url+")";
        cont.style.backgroundSize = "100% 100%";
        cont = null;
    };

    dhtmlXWindowsCell.prototype.setBC = function(color){
        var cont = this.cell.childNodes[this.conf.idx.cont];
        cont.style.backgroundColor = color;
        cont = null;
    };

    dhtmlXForm.prototype.cross_and_load = function(data, top){
        this.loadStruct(data);
        this.base[0].style.position = "absolute";
        this.base[0].style.width = "auto";
        this.base[0].style.marginLeft = -Math.round(this.base[0].offsetWidth/2)+"px";
        //this.base[0].style.marginTop = -Math.round(this.base[0].offsetHeight/2)+"px";
        this.base[0].style.left = "50%";
        //this.base[0].style.top = top === undefined ? "50%" : top;
    };

    dhtmlXTreeView.prototype.refreshItem = function(id){
        var me = this;
        if (id !== undefined) {
            _.each(me.getSubItems(id), function (e) {
                me.deleteItem(e);
            });
            me.loadStruct("gettree?nodesdb=" + desktop.settings.nodesdb + "&id=" + id);
        }
    };

    dhtmlXTreeView.prototype.getPath = function(id){
        var me = this;
        var parent = me.getParentId(id);
        return parent === undefined ? me.getItemText(id) === "/" ? "" : me.getItemText(id) : me.getPath(parent) + '/' + me.getItemText(id);
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
                desktop.statusbar.setText("AJAX call running ...");
                desktop.statusbar.style.backgroundColor = "coral";
                var ferror = function (result) {
                    ajaxcpt -= 1;
                    if (ajaxcpt === 0) {
                        desktop.statusbar.setText("");
                        desktop.statusbar.style.backgroundColor = "lightskyblue";
                    }
                    return next("Kairos server connection error!");
                };
                var fwarn = function (result) {
                    ajaxcpt -= 1;
                    if (ajaxcpt === 0) {
                        desktop.statusbar.setText("");
                        desktop.statusbar.style.backgroundColor = "lightskyblue";
                    }
                    return next("Kairos server returned: " + result.status + ", " + result.statusText);
                };
                var fdone = function (result) {
                    result = JSON.parse(result);
                    ajaxcpt -= 1;
                    if (ajaxcpt === 0) {
                        desktop.statusbar.setText("");
                        desktop.statusbar.style.backgroundColor = "lightskyblue";
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
                alertify.error('<div style="font-size:150%;">' + err + "</div>");
                if (fposterr !== undefined) {
                    fposterr();
                }
            }
        });
    };

    var parallel = function (o, callback) {
        async.parallel(o, function (err, results) {
            if (err) {
                alertify.error('<div style="font-size:150%;">' + err + "</div>");
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
                alertify.error('<div style="font-size:150%;">' + err + "</div>");
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

    var getallchoices = function (data, type) {
        var result = [];
        if (type === "C") {
            _.each(data, function (array) {
                _.each(array, function (c) {
                    result.push(c.label);
                });
            });
        } else {
            _.each(data, function (c) {
                result.push(c.label);
            });
        }
        return _.uniq(result);
    };

    var gensubmenus = function (menu, items, parentid) {
        var cpt = 0;
        var previousid = null;
        _.each(items, function (i) {
            var id = parentid + '_' + cpt;
            if (i.type === 'separator') {
                menu.addNewSeparator(previousid, id);
            }
            if (i.type === 'menuitem') {
                menu.addNewChild(parentid, undefined, id, i.label);
                menu.actions[id] = {action: i.action, chart: i.chart, choice: i.choice, layout: i.layout, keyfunc: i.keyfunc};
            }
            if (i.type === 'submenu') {
                menu.addNewChild(parentid, undefined, id, i.label);
                gensubmenus(menu, i.items, id);
            }
            previousid = id;
            cpt += 1;
        });
    };

    var getcollections = function (node) {
        var result = [];
        _.each(node.datasource.collections, function (x, k) {
            if (node.datasource.cache === undefined || node.datasource.cache.collections === undefined || node.datasource.cache.collections[k] === undefined) {
                result.push({id: k, collection: k, analyzer: x.analyzer, partition: "", created: ""});
            } else {
                _.each(node.datasource.cache.collections[k], function (y, p) {
                    result.push({id: k + '_' + p, collection: k, analyzer: x.analyzer, partition: p, created: node.datasource.cache.collections[k][p]});
                });
            }
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
            alertify.error('<div style="font-size:150%;">' + e.data + "</div>");
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
                {type: "select", label: "Login", options: listusers, name: "user"},
                {type: "password", label: "Password", value: "", name: "password"},
                {type: "button", value: "Login", name: "login", width: 400}
            ]},
        ];
        var loginform = desktop.layout.cells("a").attachForm();
        loginform.cross_and_load(logindata, "33%");
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
        var wsettings = create_window("settings", "Settings", 500, 410);
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
            settingsform.cross_and_load(settingsdata);
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
                    alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
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
            var wcr = create_window("crrole", "Create role", 540, 160);
            var data = [
                {type: "settings", position: "label-left", labelWidth: 100, inputWidth: 300},
                {type: "fieldset", label: "Create role", inputWidth: 450, list:[
                    {type: "input", label: "Role", name: "role"},
                ]},
                {type: "button", value: "Create", name: "createrole", width: 450}
            ];
            var crf = wcr.attachForm();
            crf.cross_and_load(data);
            crf.attachEvent("onButtonClick", function() {
                waterfall([
                    ajax_get_first_in_async_waterfall("createrole", {role: crf.getItemValue("role")}),
                    function (x) {
                        wcr.close();
                        alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
                        refresh();
                    }
                ]);
            });
        };
        var delete_role = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("deleterole", {role : mrg.cellById(currow, 0).getValue()}),
                function (x) {
                    alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
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
            var wcu = create_window("cruser", "Create user", 540, 160);
            var data = [
                {type: "settings", position: "label-left", labelWidth: 100, inputWidth: 300},
                {type: "fieldset", label: "Create user", inputWidth: 450, list:[
                    {type: "input", label: "User", name: "user"},
                ]},
                {type: "button", value: "Create", name: "createuser", width: 450}
            ];
            var crf = wcu.attachForm();
            crf.cross_and_load(data);
            crf.attachEvent("onButtonClick", function() {
                waterfall([
                    ajax_get_first_in_async_waterfall("createuser", {user: crf.getItemValue("user")}),
                    function (x) {
                        wcu.close();
                        alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
                        refresh();
                    }
                ]);
            });
        };
        var delete_user = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("deleteuser", {user : mug.cellById(currow, 0).getValue()}),
                function (x) {
                    alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
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
            var wcg = create_window("crgrant", "Grant role", 540, 160);
            var data = [
                {type: "settings", position: "label-left", labelWidth: 100, inputWidth: 300},
                {type: "fieldset", label: "Grant role to user", inputWidth: 450, list:[
                    {type: "input", label: "User", name: "user"},
                    {type: "input", label: "Role", name: "role"},
                ]},
                {type: "button", value: "Grant", name: "grant", width: 450}
            ];
            var crf = wcg.attachForm();
            crf.cross_and_load(data);
            crf.attachEvent("onButtonClick", function() {
                waterfall([
                    ajax_get_first_in_async_waterfall("creategrant", {user: crf.getItemValue("user"), role: crf.getItemValue("role")}),
                    function (x) {
                        wcg.close();
                        alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
                        refresh();
                    }
                ]);
            });
        };
        var revoke_role = function () {
            waterfall([
                ajax_get_first_in_async_waterfall("deletegrant", {user : mgg.cellById(currow, 1).getValue(), role: mgg.cellById(currow, 2).getValue()}),
                function (x) {
                    alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
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
        var wpassword = create_window("manage_password", "Manage password", 500, 220);
        var passworddata = [
            {type: "settings", position: "label-left", labelWidth: 140, inputWidth: 260},
            {type: "fieldset", label: "Manage password", inputWidth: 450, list:[
                {type: "password", label: "Actual password", value: "", name: "actual"},
                {type: "password", label: "New password", value: "", name: "new"},
                {type: "password", label: "Repeat new password", value: "", name: "repeat"},
            ]},
            {type: "button", value: "Set new password", name: "setpassword", width: 450}
        ];
        var passwordform = wpassword.attachForm();
        passwordform.cross_and_load(passworddata);
        passwordform.attachEvent("onButtonClick", function(){
            if (passwordform.getItemValue("new") !== passwordform.getItemValue("repeat")) {
                alertify.error('<div style="font-size:150%;">' + "New and repeated passwords are not identicals !" + "</div>");
            } else {
                waterfall([
                    ajax_post_first_in_async_waterfall("changepassword", {user: desktop.user, password: passwordform.getItemValue("actual"), new: passwordform.getItemValue("new"), logging: 'fatal'}),
                    function (x) {
                        alertify.success('<div style="font-size:150%;">' + x.msg + "</div>");
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

    var manage_node = function (tree, id, nodeorigin) {
        var node = nodeorigin;
        var gendataform = function (w, listaggregators, listliveobjects, uid1, uid2) {
            var width = w.cont.clientWidth;
            var sizeunit = (width - 132) / 9;
            var type = node.datasource.type;

            var generalproperties = [];
            generalproperties.push({
                type: "block",
                list: [
                    {type: "input", label: "Type", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 2, value: type, readonly: true},
                    {type: "newcolumn"},
                    {type: "calendar", dateFormat: "%Y-%m-%d %H:%i", label: "Created", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 2, value: node.created, enableTime: true, readonly: true, calendarPosition: "right"},
                    {type: "newcolumn"},
                    {type: "input", label: "Status", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 2, value: node.status, readonly: true}
                ]
            });
            if (_.contains(["B"], type)) {
                generalproperties.push({
                    type: "block",
                    list: [
                        {type: "calendar", dateFormat: "%Y-%m-%d %H:%i", label: "Uploaded", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 8, value: node.datasource.uploaded, enableTime: true, readonly: true, calendarPosition: "right"},
                    ]
                });
            }
            var general = {type: "fieldset", label: "General properties", list: generalproperties};

            var aggregatorproperties = [];
            aggregatorproperties.push({
                type: "block",
                list: [
                    {type: "input", label: "Selector", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 8, name: "aggregatorselector", value: type === 'N' ? '/' : node.datasource.aggregatorselector}
                ]
            });
            aggregatorproperties.push({
                type: "block",
                list: [
                    {type: "input", label: "Take", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 2, name: "aggregatortake", value: type === 'N' ? 1 : node.datasource.aggregatortake},
                    {type: "newcolumn"},
                    {type: "input", label: "Skip", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 2, name: "aggregatorskip", value: type === 'N' ? 0 : node.datasource.aggregatorskip},
                    {type: "newcolumn"},
                    {type: "select", label: "Sort", labelAlign: "right", labelWidth: sizeunit, name: "aggregatorsort", inputWidth: sizeunit * 2, options: [
                        {text: 'asc', selected: type === 'N' ? false : node.datasource.aggregatorsort === 'asc' ? true : false},
                        {text: 'desc', selected: type === 'N' ? true : node.datasource.aggregatorsort === 'desc' ? true : false},
                    ]}
                ]
            });
            aggregatorproperties.push({
                type: "block",
                list: [
                    {type: "input", label: "TimeFilter", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 8, name: "aggregatortimefilter", value: type === 'N' ? '.' : node.datasource.aggregatortimefilter}
                ]
            });
            aggregatorproperties.push({
                type: "block",
                list: [
                    {type: "select", label: "Method", labelAlign: "right", labelWidth: sizeunit, name: "aggregatormethod", inputWidth: sizeunit * 2, options: listaggregators, value: type === "N" ? '$none' : node.datasource.aggregatormethod},
                    {type: "newcolumn"},
                    {type: "calendar", dateFormat: "%Y-%m-%d %H:%i", label: "Aggregated", labelAlign: "right", labelWidth: sizeunit, inputWidth: sizeunit * 2, value: type === "N" ? '' : node.datasource.aggregated, enableTime: true, readonly: true, calendarPosition: "right"},
                    {type: "newcolumn"},
                    {type: "button", width: sizeunit * 3, value: "Apply aggregator", name: "aggregate"}
                ]
            });
          
            var aggregator = {type: "fieldset", label: "Aggregator", list: aggregatorproperties};

            var livenodeproperties = [];
            livenodeproperties.push({
                type: "block",
                list: [
                    {type: "select", label: "Live object", labelAlign: "right", labelWidth: sizeunit, name: "liveobject", inputWidth: sizeunit * 7 / 2, options: listliveobjects},
                    {type: "newcolumn"},
                    {type: "button", width: sizeunit * 9 / 2, value: "Apply live object", name: "makelive"}
                ]
            });

            var livenode = {type: "fieldset", label: "Live node", list: livenodeproperties};

            var producersproperties = [];
            producersproperties.push({
                type: "block",
                list: [
                    {type: "container", name: uid1, inputWidth: sizeunit * 9, inputHeight: 300},
                ]
            });

            var producers = {type: "fieldset", label: "Producers", list: producersproperties};

            var collectionsproperties = [];
            collectionsproperties.push({
                type: "block",
                list: [
                    {type: "container", name : uid2, inputWidth: sizeunit * 9, inputHeight: 300},
                ]
            });
            collectionsproperties.push({
                type: "block",
                list: [
                    {type: "button", width: sizeunit * 9 / 4, value: "Build all caches", name: "buildall"},
                    {type: "newcolumn"},
                    {type: "button", width: sizeunit * 9 / 4, value: "Build collection cache", name: "buildcolcache", disabled: true},
                    {type: "newcolumn"},
                    {type: "button", width: sizeunit * 9 / 4, value: "Drop collection cache", name: "dropcolcache", disabled: true},
                    {type: "newcolumn"},
                    {type: "button", width: sizeunit * 9 / 4, value: "Clear collections caches", name: "clearall"}
                ]
            });

            var collections = {type: "fieldset", label: "Collections", list: collectionsproperties};

            var nodeproperties = [general];
            if (_.contains(["A", "N"], type)) {
                nodeproperties.push(aggregator);
            }
            if (_.contains(["D", "N"], type)) {
                nodeproperties.push(livenode);
            }
            if (_.contains(["A", "C"], type)) {
                nodeproperties.push(producers);
            }
            if (_.contains(["A", "B"], type)) {
                nodeproperties.push(collections);
            }
            var data = [
                {type: "fieldset", label: "Node properties", list: nodeproperties, name: "node_properties"}
            ];
            return data;
        };
        var genform = function (w, listaggregators, listliveobjects) {
            var wf = w.attachForm();

            var uid1= _.uniqueId('grid');
            var uid2= _.uniqueId('grid');
            var curcollection = null;
            wf.cross_and_load(gendataform(wf, listaggregators, listliveobjects, uid1, uid2));

            var gp = new dhtmlXGridObject(wf.getContainer(uid1));
            gp.setHeader("Node path, Node id");
            gp.setColSorting("str,str");
            gp.attachHeader("#text_filter,#text_filter")
            gp.init();
            gp.enableSmartRendering(true);
            var gprows = [];
            _.each(node.datasource.producers, function(r) {
                gprows.push({id: r.id, data: [r.path, r.id]});
            });
            gp.clearAll();
            gp.parse({rows: gprows}, "json");

            var gc = new dhtmlXGridObject(wf.getContainer(uid2));
            gc.setHeader("Id,Collection,Partition,Analyzer,Cache creation date");
            gc.setColSorting("str,str,str,str,str");
            gc.attachHeader("#text_filter,#text_filter,#text_filter,#text_filter,#text_filter")
            gc.init();
            gc.enableSmartRendering(true);
            var gcrows = [];
            _.each(getcollections(node), function(r) {
                gcrows.push({id: r.id, data: [r.id, r.collection, r.partition, r.analyzer, r.created]});
            });
            gc.clearAll();
            gc.parse({rows: gcrows}, "json");
            gc.attachEvent("onRowSelect", function(id){
                curcollection = gc.cells(id, 1).getValue();
                wf.enableItem("buildcolcache");
                wf.enableItem("dropcolcache");
            });
            wf.attachEvent("onButtonClick", function (btn) {
                var f = function(method, params) {
                    waterfall([
                        ajax_get_first_in_async_waterfall(method, params),
                        function () {
                            waterfall([
                                ajax_get_first_in_async_waterfall("getnode", {nodesdb: desktop.settings.nodesdb, id: '#' + id}),
                                function (x) {
                                    node = x;
                                    genform(w, listaggregators, listliveobjects);
                                    tree.unselectItem(id);
                                    tree.selectItem(id);
                                    var pid = tree.getParentId(id);
                                    tree.refreshItem(pid);
                                }
                            ]);
                        }
                    ]);                   
                }
                if (btn === 'buildall') {
                    f("buildallcollectioncaches", {nodesdb: desktop.settings.nodesdb, id: '#' + id, systemdb: desktop.settings.systemdb});
                }
                if (btn === 'buildcolcache') {
                    f("buildcollectioncache", {nodesdb: desktop.settings.nodesdb, id: '#' + id, systemdb: desktop.settings.systemdb, collection: curcollection});
                }
                if (btn === 'dropcolcache') {
                    f("dropcollectioncache", {nodesdb: desktop.settings.nodesdb, id: '#' + id, systemdb: desktop.settings.systemdb, collection: curcollection});
                }
                if (btn === 'clearall') {
                    f("clearcollectioncache", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: '#' + id});
                }
                if (btn === 'aggregate') {
                    f("applyaggregator", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: '#' + id, aggregatorselector: wf.getItemValue("aggregatorselector"), aggregatortake: wf.getItemValue("aggregatortake"), aggregatortimefilter: wf.getItemValue("aggregatortimefilter"), aggregatorskip: wf.getItemValue("aggregatorskip"), aggregatorsort: wf.getItemValue("aggregatorsort"), aggregatormethod: wf.getItemValue("aggregatormethod")});
                }
                if (btn === 'makelive') {
                    f("applyliveobject", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: '#' + id, liveobject: wf.getItemValue("liveobject")});
                }
            });
            return wf;
        };
        parallel({
            aggregators: ajax_get_in_async_parallel("listaggregators", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
            liveobjects: ajax_get_in_async_parallel("listliveobjects", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb})
        }, function (x) {
            var listaggregators = [];
            _.each(_.sortBy(x.aggregators, function(a) {
                return a.id;
            }), function(a) {
                listaggregators.push({text: a.id, value: a.id, selected: node.datasource.type === "N" ? a.id === "$none" ? true : false : a.id === node.datasource.aggregatormethod ? true : false});
            });
            var listliveobjects = [{text: "", value:""}];
            _.each(_.sortBy(x.liveobjects, function(l) {
                return l.id;
            }), function(l) {
                listliveobjects.push({text: l.id, value: l.id, selected: node.datasource.type === "N" ? l.id === undefined ? true : false : l.id === node.datasource.liveobject ? true : false});
            });
            var h = node.datasource.type === "A" ? 1120 : node.datasource.type === "B" ? 610 : node.datasource.type === "C" ? 540 : node.datasource.type === "N" ? 450 : node.datasource.type === "T" ? 175 : undefined;
            var wn = create_window("manage_node", desktop.settings.nodesdb + ':' + tree.getPath(id), undefined, h);
            var wf = genform(wn, listaggregators, listliveobjects);
            wn.attachEvent("onResizeFinish", function () {
                wf = genform(wn, listaggregators, listliveobjects);
            });
            wn.attachEvent("onMaximize", function () {
                wf = genform(wn, listaggregators, listliveobjects);
            });
            wn.attachEvent("onMinimize", function () {
                wf = genform(wn, listaggregators, listliveobjects);
            });
        });
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
        var wr = create_window("rename", "Rename ...", 500, 145);
        var data = [
            {type: "settings", label: "", position: "label-left", labelWidth: 200, inputWidth: 200},
            {type: "fieldset", inputWidth: 450, list:[
                {type: "input", label: "Rename to ...",  name: "new", value: oldname},
            ]},
            {type: "button", value: "Rename", name: "rename", width: 450}
        ];
        var wf = wr.attachForm();
        wf.cross_and_load(data);
        wf.attachEvent("onButtonClick", function(){
            var newname = wf.getItemValue("new");
            wr.close();
            callback(newname);
        });
    };

    var getchoice = function (listchoices, callback) {
        var wgc = create_window("get_choice", "Choose ...", 500, 145);
        var data = [
            {type: "settings", label: "", position: "label-left", labelWidth: 150, inputWidth: 250},
            {type: "fieldset", inputWidth: 450, list:[
                {type: "select", label: "Choose", options: listchoices, name: "choice"},
            ]},
            {type: "button", value: "Choose", name: "choose", width: 450}
        ];
        var wf = wgc.attachForm();
        wf.cross_and_load(data);
        wf.attachEvent("onButtonClick", function(){
            var choice = wf.getItemValue("choice");
            wgc.close();
            callback(choice);
        });
    };

    var explorer = function () {
        var wexp = create_window("explorer", desktop.settings.nodesdb);
        var onclick = null;
        var curnode = null;
        var rootid = null;
        var trashid = null;
        var startpid = null;
        var xid = null;
        var yid = null;
        var potentialmenus = null;
        var menu = wexp.attachMenu({});
        var tree = wexp.attachTreeView({
            dnd: true,
            multiselect: true,
            context_menu: true,
            json: "gettree?nodesdb=" + desktop.settings.nodesdb + "&id={id}"
        });
        tree.attachEvent("onContextMenu", function(id, x, y, ev){
            return false;
        });
        tree.attachEvent("onBeforeDrag", function (id) {
            startpid = tree.getParentId(id);
            if (tree.getUserData(id, "type") === "T" || tree.getItemText(id) === '/') {
                return false;
            } else {
                return true;
            }
        });
        tree.attachEvent("onBeforeDrop", function (id, pid) {
            var ret = true;
            if (desktop.mousevent.ctrlKey === false && desktop.mousevent.altKey === false && pid !== startpid) {
                if (tree.getUserData(pid, "type") !== "T") {
                    _.each(tree.getSubItems(pid), function (e) {
                        if (tree.getItemText(id) === tree.getItemText(e)) {
                            alertify.error('<div style="font-size:150%;">' + "A child of '" + tree.getItemText(pid) + "' has already the name: '" + tree.getItemText(e) + "'" + "</div>");
                            ret = false;
                        }
                    });
                }
            }
            if (desktop.mousevent.altKey) {
                if (_.contains(["C", "L", "N", "T"], tree.getUserData(id, "type"))) {
                    ret = false;
                }
                if (_.contains(["B", "C", "D", "L", "T"], tree.getUserData(pid, "type"))) {
                    ret = false;
                }
                xid = tree.getParentId(id);
                yid = tree.getParentId(pid);
            }
            if (desktop.mousevent.ctrlKey) {
                if (_.contains(["C", "L", "N", "T"], tree.getUserData(id, "type"))) {
                    ret = false;
                }
                if (_.contains(["A", "B", "D", "L", "T"], tree.getUserData(pid, "type"))) {
                    ret = false;
                }
                xid = tree.getParentId(id);
                yid = tree.getParentId(pid);
            }
            return ret;
        });
        tree.attachEvent("onDrop", function (id, pid) {
            if (desktop.mousevent.ctrlKey === false && desktop.mousevent.altKey === false && pid !== startpid) {
                waterfall([
                    ajax_get_first_in_async_waterfall("movenode", {origindb: desktop.settings.nodesdb, targetdb: desktop.settings.nodesdb, from: '#' + id, to: '#' + pid}),
                    function () {
                    }
                ]);
            }
            if (desktop.mousevent.altKey) {
                waterfall([
                    ajax_get_first_in_async_waterfall("aggregateaddnode", {origindb: desktop.settings.nodesdb, targetdb: desktop.settings.nodesdb, from: '#' + id, to: '#' + pid, path: tree.getPath(id)}),
                    function () {
                        waterfall([
                            ajax_get_first_in_async_waterfall("getnode", {nodesdb: desktop.settings.nodesdb, id: '#' + pid}),
                            function (x) {
                                curnode = x;
                                setTimeout(function () {tree.refreshItem(yid)}, 0);
                                setTimeout(function () {tree.refreshItem(xid)}, 0);
                                menu.clearAll();
                            }
                        ]);
                    }
                ]);
            }
            if (desktop.mousevent.ctrlKey) {
                waterfall([
                    ajax_get_first_in_async_waterfall("compareaddnode", {origindb: desktop.settings.nodesdb, targetdb: desktop.settings.nodesdb, from: '#' + id, to: '#' + pid, path: tree.getPath(id)}),
                    function () {
                        waterfall([
                            ajax_get_first_in_async_waterfall("getnode", {nodesdb: desktop.settings.nodesdb, id: '#' + pid}),
                            function (x) {
                                curnode = x;
                                setTimeout(function () {tree.refreshItem(yid)}, 0);
                                setTimeout(function () {tree.refreshItem(xid)}, 0);
                                menu.clearAll();
                            }
                        ]);
                    }
                ]);
            }

        });
        tree.attachEvent("onXLE", function () {
            if (rootid !== null && trashid === null) {
                _.each(tree.getSubItems(rootid), function (e) {
                    if (tree.getUserData(e, "type") === "T") {
                        trashid = e;
                    }
                });
            }
            if (rootid === null) {
                rootid = tree.getSubItems(undefined)[0];
            }
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
				{id: "open_node", text: "Open node"},
				{type: "separator"},
				{id: "execute_query", text: "Execute query"},
				{id: "run_chart", text: "Run chart"},
				{id: "run_choice", text: "Run choice"},
				{type: "separator"},
				{id: "download", text: "Download"},
				{id: "display_member", text: "Display member"},
				{id: "unload", text: "Unload"},
				{type: "separator"},
				{id: "empty_trash", text: "Empty trash"},
			]
        });
        contextmenu.setIconset("awesome");
        contextmenu.setItemImage("upload","fa fa-upload", "fa fa-upload");
        contextmenu.setItemImage("create_node","fa fa-magic", "fa fa-magic");
        contextmenu.setItemImage("rename_node","fa fa-pencil", "fa fa-pencil");
        contextmenu.setItemImage("delete_node","fa fa-trash", "fa fa-trash");
        contextmenu.setItemImage("refresh_node","fa fa-refresh", "fa fa-refresh");
        contextmenu.setItemImage("open_node","fa fa-hand-o-right", "fa fa-hand-o-right");
        contextmenu.setItemImage("execute_query","fa fa-question", "fa fa-question");
        contextmenu.setItemImage("run_chart","fa fa-line-chart", "fa fa-line-chart");
        contextmenu.setItemImage("run_choice","fa fa-sitemap", "fa fa-sitemap");
        contextmenu.setItemImage("download","fa fa-download", "fa fa-download");
        contextmenu.setItemImage("display_member","fa fa-file-text", "fa fa-file-text");
        contextmenu.setItemImage("unload","fa fa-cloud-download", "fa fa-cloud-download");
        contextmenu.setItemImage("empty_trash","fa fa-trash-o", "fa fa-trash-o");
        menu.attachEvent("onClick", function(id) {
            console.log(menu.actions[id]);
            if (menu.actions[id].action === "dispchart") {
                dispchart(curnode, menu.actions[id].chart);
            }
            if (menu.actions[id].action === "dispchoice") {
                dispchoice(curnode, menu.actions[id].choice);
            }
        });
        tree.attachEvent("onSelect", function(id, select){
            if (select) {
                var type = tree.getUserData(id, "type");
                var contextmenuenabled = {upload: false, create_node: true, rename_node: false, delete_node: false, refresh_node: true, open_node: true, execute_query: false, run_chart: false, run_choice: false, download: false, display_member: false, unload: false, empty_trash: false};
                if (_.contains(["B", "N"], type)) {
                    contextmenuenabled.upload = true;
                }
                if (_.contains(["A", "B", "C", "D", "L", "N"], type)) {
                    contextmenuenabled.rename_node = true;
                    contextmenuenabled.delete_node = true;
                }
                if (_.contains(["A", "B", "C", "D"], type)) {
                    contextmenuenabled.execute_query = true;
                    contextmenuenabled.run_chart = true;
                    contextmenuenabled.run_choice = true;
                }
                if (_.contains(["B"], type)) {
                    contextmenuenabled.download = true;
                    contextmenuenabled.display_member = true;
                }
                if (_.contains(["A", "B"], type)) {
                    contextmenuenabled.unload = true;
                }
                if (_.contains(["T"], type)) {
                    contextmenuenabled.empty_trash = true;
                }
                _.each(contextmenuenabled, function (v, k) {
                    if (v) {
                        contextmenu.setItemEnabled(k);
                    } else {
                        contextmenu.setItemDisabled(k);
                    }
                });
                menu.clearAll();
                menu.actions = {};
                waterfall([
                    ajax_get_first_in_async_waterfall("getnode", {nodesdb: desktop.settings.nodesdb, id: '#' + id}),
                    function (node) {
                        curnode = node;
                        if (_.contains(["A", "B", "C", "D"], type)) {
                            _.each(potentialmenus, function (m) {
                                if (_.contains(_.keys(node.datasource.collections), m.tablecondition)) {
                                    if (menu.getItemType(m.id) === null) {
                                        menu.addNewSibling(null, m.id, m.label);
                                        gensubmenus(menu, m.items, m.id);
                                    }
                                }
                            });
                        }
                    }
                ]);
            }
        });
        tree.attachEvent("onContextMenu", function(id, x, y, ev) {
			contextmenu.setItemText("itemText", "Node: " + tree.getItemText(id));
            contextmenu.showContextMenu(x, y);
            tree.selectItem(id);
            log.debug("onContextMenu event, id: " + id + " (" + tree.getItemText(id) + ")");
            if (onclick !== null) {
                contextmenu.detachEvent(onclick);
            }
            onclick = contextmenu.attachEvent("onClick", function (fid) {
                if (fid === "upload") {
                    log.debug("Upload on item: " + id + " (" + tree.getItemText(id) + ")");
                    upload(makeURL("uploadnode", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: '#' + id}), function () {
                        tree.loadStruct("gettree?nodesdb=" + desktop.settings.nodesdb + "&id=" + id);
                    });
                }
                if (fid === "create_node") {
                    log.debug("Create node within item: " + id + " (" + tree.getItemText(id) + ")");
                    waterfall([
                        ajax_get_first_in_async_waterfall("createnode", {nodesdb: desktop.settings.nodesdb, id: '#' + id}),
                        function (x) {
                            tree.loadStruct("gettree?nodesdb=" + desktop.settings.nodesdb + "&id=" + id);
                        }
                    ]);
                }
                if (fid === "rename_node") {
                    log.debug("Rename node: " + id + " (" + tree.getItemText(id) + ")");
                    var oldname = tree.getItemText(id);
                    var aftergetnewname = function(name) {
                        if (name !== oldname) {
                            waterfall([
                                ajax_get_first_in_async_waterfall("renamenode", {nodesdb: desktop.settings.nodesdb, id: '#' + id, new: name}),
                                function (x) {
                                    tree.setItemText(id, name);
                                }
                            ]);
                        }
                    };
                    rename(oldname, aftergetnewname);
                }
                if (fid === "delete_node") {
                    log.debug("Delete node: " + id + " (" + tree.getItemText(id) + ")");
                    waterfall([
                        ajax_get_first_in_async_waterfall("deletenode", {nodesdb: desktop.settings.nodesdb, id: '#' + id}),
                        function (x) {
                            tree.deleteItem(id);
                            tree.refreshItem(trashid);                           
                        }
                    ]);
                }
                if (fid === "refresh_node") {
                    log.debug("Refresh node:" + id + " (" + tree.getItemText(id) + ")");
                    tree.refreshItem(trashid);                           
                }
                if (fid === "open_node") {
                    log.debug("Open node: " + id + " (" + tree.getItemText(id) + ")");
                    manage_node(tree, id, curnode);
                }
                if (fid === "execute_query") {
                    log.debug("Execute query on node: " + id + " (" + tree.getItemText(id) + ")");
                    execute_query(tree, curnode);
                }
                if (fid === "run_chart") {
                    log.debug("Running chart on node: " + id + " (" + tree.getItemText(id) + ")");
                    run_chart(curnode);
                }
                if (fid === "run_choice") {
                    log.debug("Running choice on node: " + id + " (" + tree.getItemText(id) + ")");
                    run_choice(curnode);
                }
                if (fid === "download") {
                    log.debug("Download at node: " + id + " (" + tree.getItemText(id) + ")");
                    window.location.href = '/downloadsource?id=' + encodeURIComponent('#' + id) + '&nodesdb=' + desktop.settings.nodesdb;
                }
                if (fid === "display_member") {
                    log.debug("Display member at node: " + id + " (" + tree.getItemText(id) + ")");
                    var aftergetchoice = function(member) {
                        waterfall([
                            ajax_get_first_in_async_waterfall("getmember", {nodesdb: desktop.settings.nodesdb, id: '#' + id, member: member}),
                            function (x) {
                                var wmem = create_window("display_member", tree.getItemText(id) + ' / ' + member);
                                var uniqueid = _.uniqueId('display_member');
                                wmem.attachHTMLString('<div id="' + uniqueid + '" style="width:100%;height:100%;overflow:auto">' + x + '</div>');
                            }
                        ]);
                    };
                    waterfall([
                        ajax_get_first_in_async_waterfall("getmemberlist", {nodesdb: desktop.settings.nodesdb, id: '#' + id}),
                        function (x) {
                            var listmembers = [];
                            _.each(_.sortBy(getallchoices(x, tree.getUserData("type")), function(c) {
                                return c;
                            }), function(c) {
                                listmembers.push({text: c, value: c, selected: false});
                            });
                            getchoice(listmembers, aftergetchoice);
                        }
                    ]);
                }
                if (fid === "unload") {
                    log.debug("Unload at node: " + id + " (" + tree.getItemText(id) + ")");
                    window.location.href = '/unload?id=' + encodeURIComponent('#' + id) + '&nodesdb=' + desktop.settings.nodesdb + '&systemdb=' + desktop.settings.systemdb;
                }
                if (fid === "empty_trash") {
                    log.debug("Empty trash");
                    waterfall([
                        ajax_get_first_in_async_waterfall("emptytrash", {nodesdb: desktop.settings.nodesdb}),
                        function () {
                            _.each(tree.getSubItems(id), function (e) {
                                tree.deleteItem(e);
                            });
                            tree.loadStruct("gettree?nodesdb=" + desktop.settings.nodesdb + "&id=" + id);
                        }
                    ]);
                }
            });
            return false;
        });
        waterfall([
            ajax_get_first_in_async_waterfall("getmenus", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb}),
            function (menus) {
                potentialmenus = menus;
            }
        ]);
    };

    var dispchart = function (node, chart, layoutpiece, wlayout) {
        log.debug('Getting chart, template & colors');
        log.debug('Starting chart display');
        var uniquecid = _.uniqueId('chart');
        var wchart = null;
        if (layoutpiece === undefined) {
            wchart = create_window("chart", node.name + ' - ' + chart);
        } else {
            wchart = wlayout.tabs(layoutpiece);
        }
        wchart.attachHTMLString('<div id="' + uniquecid + '" style="width:100%;height:100%;overflow:auto"></div>');
        var prepare_and_draw = function(x, q) {
            console.log(chart, uniquecid, layoutpiece, wchart);
            log.debug('Preparing chart:' + chart);
            var g = new KairosCharter.Chart({width: wchart.cell.clientWidth - 3, height: wchart.cell.clientHeight - 3}, desktop.settings.logging);
            wchart.kairosg = g;
            var m = g.getChartTemplate();
            _.each(x.template.lines, function (y) {
                m.setLine(y);
            });
            _.each(x.template.columns, function (y) {
                m.setColumn(y);
            });
            var boundedobjects = {};
            m.setObject("main", x.template.main);
            m.setObject("margintop", x.template.margintop);
            m.setObject("marginbottom", x.template.marginbottom);
            m.setObject("marginleft", x.template.marginleft);
            m.setObject("marginright", x.template.marginright);
            m.setObject(uniquecid + "title", x.template.title);
            boundedobjects[uniquecid + "title"] = g.bindTitle(uniquecid + "title", x.chart.title);
            m.setObject(uniquecid + "subtitle", x.template.subtitle);
            boundedobjects[uniquecid + "subtitle"] = g.bindTitle(uniquecid + "subtitle", x.chart.subtitle);
            var numplots = node.datasource.type === 'C' ? node.datasource.producers.length : 1;
            var reftime = [];
            _.each(_.range(numplots), function (i) {
                reftime[i] = new KairosCharter.RefTime();
                if (x.chart.reftime !== undefined) {
                    var qreftime = node.datasource.type === 'C' ? q[x.chart.reftime][i] : q[x.chart.reftime];
                    _.each(qreftime, function (ref) {
                        reftime[i].store(ref);
                    });
                }
                var plotid = desktop.settings.plotorientation === 'vertical' ? "plot" + i + "0" : "plot0" + i;
                if (boundedobjects[uniquecid + plotid] === undefined) {
                    m.setObject(uniquecid + plotid, x.template[plotid]);
                    boundedobjects[uniquecid + plotid] = g.bindPlot(uniquecid + plotid);
                    m.getObject(uniquecid + plotid).unhidelines();
                    m.getObject(uniquecid + plotid).unhidecolumns();
                }
                var plottitleid = desktop.settings.plotorientation === 'vertical' ? "plottitle" + i + "0" : "plottitle0" + i;
                if (boundedobjects[uniquecid + plottitleid] === undefined) {
                    m.setObject(uniquecid + plottitleid, x.template[plottitleid]);
                    var title = node.datasource.type === "C" ? node.datasource.producers[i].path : node.name;
                    title = node.datasource.type === "L" ? node.datasource.producers[0].path : title;
                    boundedobjects[uniquecid + plottitleid] = g.bindTitle(uniquecid + plottitleid, title);
                }
                var xaxisid = desktop.settings.plotorientation === 'vertical' ? "xaxis0" : "xaxis" + i;
                if (boundedobjects[uniquecid + xaxisid] === undefined) {
                    m.setObject(uniquecid + xaxisid, x.template[xaxisid]);
                    boundedobjects[uniquecid + xaxisid] = g.bindXaxis(uniquecid + xaxisid, "", "linear");
                    var xaxistitleid = desktop.settings.plotorientation === 'vertical' ? "xaxistitle0" : "xaxistitle" + i;
                    m.setObject(uniquecid + xaxistitleid, x.template[xaxistitleid]);
                }
                if (boundedobjects[uniquecid + "legend"] === undefined) {
                    m.setObject(uniquecid + "legend", x.template.legend);
                    boundedobjects[uniquecid + "legend"] = g.bindLegend(uniquecid + "legend");
                }
                var il = -1;
                var ir = -1;
                _.each(x.chart.yaxis, function (y) {
                    ir = y.position === 'right' ? ir + 1 : ir;
                    il = y.position !== 'right' ? il + 1 : il;
                    var yaxisid = desktop.settings.plotorientation === 'vertical' ? "yaxis" + i : "yaxis0";
                    var yaxistitleid = "yaxistitle";
                    var ytn = y.position === 'right' ? yaxistitleid + "right" + ir : yaxistitleid + "left" + il;
                    var yn = y.position === 'right' ? yaxisid + "right" + ir : yaxisid + "left" + il;
                    if (boundedobjects[uniquecid + yn] === undefined) {
                        m.setObject(uniquecid + yn, x.template[yn]);
                        m.getObject(uniquecid + yn).unhidecolumns();
                        boundedobjects[uniquecid + yn] = g.bindYaxis(uniquecid + yn, y.title, y.position, y.scaling, y.properties, y.minvalue, y.maxvalue);
                    }
                    _.each(y.renderers, function (r) {
                        var renderer = {type: r.type};
                        var dataset = new KairosCharter.Dataset(reftime[i]);
                        _.each(r.datasets, function (d) {
                            var qquery = node.datasource.type === 'C' ? q[d.query][i] : q[d.query];
                            _.each(qquery, function (z) {
                                dataset.store(z);
                                if (dataset.color[z[d.label]] === undefined) {
                                    var color = x.colors.colors[z[d.label]] === undefined ? undefined : x.colors.colors[z[d.label]];
                                    dataset.color[z[d.label]] = dataset.getColor(z[d.label], "", color);
                                }
                                if (d.onclick !== undefined && dataset.onclick[z[d.label]] === undefined) {
                                    dataset.onclick[z[d.label]] = function () {
                                        desktop.variables[d.onclick.variable] = z[d.label];
                                        if (d.onclick.action === "dispchart") {
                                            dispchart(node, d.onclick.chart);
                                        }
                                    }
                                }
                                if (d.info !== undefined && dataset.info[z[d.label]] === undefined) {
                                    dataset.info[z[d.label]] = function () {
                                        desktop.variables[d.info.variable] = z[d.label];
                                        waterfall([
                                            ajax_get_first_in_async_waterfall("executequery", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: node.id, query: d.info.query, top: desktop.settings.top, variables: JSON.stringify(desktop.variables)}),
                                            function (y) {
                                                alertify.set({ delay: 15000 });
                                                var key = node.datasource.type === 'C' ? y[i][0].key : y[0].key;
                                                var value = node.datasource.type === 'C' ? y[i][0].value : y[0].value;
                                                alertify.log(key + "<hr/>" + value);
                                            }
                                        ]);
                                    }
                                }
                            });
                        });
                        var uniquebid = _.uniqueId('bind');
                        boundedobjects[uniquebid] = g.bind(uniquecid + uniquebid, dataset, uniquecid + plotid, renderer, uniquecid + xaxisid, uniquecid + yn, uniquecid + "legend");
                    });
                });
            });
            log.debug('Drawing chart: ' + chart);
            var selector = '[id=' + uniquecid + ']';
            g.draw(selector, uniquecid);
            log.debug('End of drawing');
        };
        parallel({
            chart: ajax_get_in_async_parallel("getchart", {chart: chart, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb, variables: JSON.stringify(desktop.variables)}),
            template: ajax_get_in_async_parallel("gettemplate", {template: desktop.settings.template, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
            colors: ajax_get_in_async_parallel("getcolors", {colors: desktop.settings.colors, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        }, function (x) {
            log.debug('Executing queries');
            var chartqueries = {};
            if (x.chart.reftime !== undefined) {
                chartqueries[x.chart.reftime] = ajax_get_first_in_async_waterfall("executequery", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: node.id, query: x.chart.reftime, top: desktop.settings.top, variables: JSON.stringify(desktop.variables)});

            }
            _.each(x.chart.yaxis, function (y) {
                _.each(y.renderers, function (r) {
                    _.each(r.datasets, function (d) {
                        chartqueries[d.query] = ajax_get_first_in_async_waterfall("executequery", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: node.id, query: d.query, top: desktop.settings.top, variables: JSON.stringify(desktop.variables)});
                    });
                });
            });
            falseparallel(chartqueries, function (q) {
                wchart.resultqueries = q;
                wchart.descchart = x;
                prepare_and_draw(x, q);
            });
        });
        wchart.attachEvent("onResizeFinish", function () {
            wchart.kairosg.destroy();
            prepare_and_draw(wchart.descchart, wchart.resultqueries);
        });
        wchart.attachEvent("onMaximize", function () {
            wchart.kairosg.destroy();
            prepare_and_draw(wchart.descchart, wchart.resultqueries);
        });
        wchart.attachEvent("onMinimize", function () {
            wchart.kairosg.destroy();
            prepare_and_draw(wchart.descchart, wchart.resultqueries);
        });
        if (wlayout !== undefined) {
            wlayout.attachEvent("onResizeFinish", function () {
                wchart.kairosg.destroy();
                prepare_and_draw(wchart.descchart, wchart.resultqueries);
            });
            wlayout.attachEvent("onPanelResizeFinish", function () {
                wchart.kairosg.destroy();
                prepare_and_draw(wchart.descchart, wchart.resultqueries);
            });
            wlayout.attachEvent("onCollapse", function () {
                wchart.kairosg.destroy();
                prepare_and_draw(wchart.descchart, wchart.resultqueries);
            });
            wlayout.attachEvent("onExpand", function () {
                wchart.kairosg.destroy();
                prepare_and_draw(wchart.descchart, wchart.resultqueries);
            });
            wlayout.attachEvent("onDock", function () {
                wchart.kairosg.destroy();
                prepare_and_draw(wchart.descchart, wchart.resultqueries);
            });
            wlayout.attachEvent("onUndock", function () {
                wchart.kairosg.destroy();
                prepare_and_draw(wchart.descchart, wchart.resultqueries);
            });
        }
    };

    var dispchoice = function (node, choice) {
        parallel({
            choice: ajax_get_in_async_parallel("getchoice", {choice: choice, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb, variables: JSON.stringify(desktop.variables)}),
        }, function (x) {
            var callback = function (c) {
                desktop.variables[x.choice.id] = c;
                if (x.choice.action === 'dispchart') {
                    dispchart(node, x.choice.chart);
                }
                if (x.choice.action === 'dispchoice') {
                    dispchoice(node, x.choice.choice);
                }
            };
            waterfall([
                ajax_get_first_in_async_waterfall("executequery", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, id: node.id, query: x.choice.query, top: desktop.settings.top, variables: JSON.stringify(desktop.variables)}),
                function (y) {
                    var options = [];
                    _.each(y, function(v) {
                        options.push({text: v.label, value: v.label, selected: false});
                    })
                    getchoice(options, callback);
                }
            ]);
        });
    };

    var dispquery = function (tree, node, query) {
        waterfall([
            ajax_get_first_in_async_waterfall("executequery", {nodesdb: desktop.settings.nodesdb, systemdb: desktop.settings.systemdb, query: query, id: node.id, top: desktop.settings.top, variables: JSON.stringify(desktop.variables)}),
            function (x) {
                var wq = create_window("query", query + ' - ' + desktop.settings.nodesdb + ':' + tree.getPath(node.id.replace('#', '')));
                var gq =wq.attachGrid();
                var header = '';
                var colsorting = '';
                var filter = '';
                _.each(x[0], function (v, k) {
                    header += k + ',';
                    colsorting += typeof(v) === 'string' ? 'str,' : 'int,';
                    filter += '#text_filter,';
                });
                gq.setHeader(header.slice(0, -1));
                gq.setColSorting(colsorting.slice(0, -1));
                gq.attachHeader(filter.slice(0, -1));
                gq.init();
                gq.enableSmartRendering(true);
                gq.clearAll();
                var datarows = [];
                var id = 0;
                _.each(x, function (e) {
                    var data = [];
                    _.each(e, function (v, k) {
                        data.push(v);
                    });
                    datarows.push({id:id, data:data});
                    id += 1;
                });
                gq.parse({rows: datarows}, "json");
            }
        ]);
    };

    var run_choice = function (node) {
        parallel({
            list: ajax_get_in_async_parallel("getchoices", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        }, function (x) {
            var callback = function (c) {
                dispchoice(node, c);
            };
            var options = [];
            _.each(_.sortBy(x.list, function(e) {
                return e.id;
            }), function(c) {
                options.push({text: c.id, value: c.id, selected: false});
            });
            options = _.uniq(options, function (e) {
                return e.text;
            });
            getchoice(options, callback);
        });
    };

    var run_chart = function (node) {
        parallel({
            list: ajax_get_in_async_parallel("getcharts", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        }, function (x) {
            var callback = function (c) {
                dispchart(node, c);
            };
            var options = [];
            _.each(_.sortBy(x.list, function(e) {
                return e.id;
            }), function(c) {
                options.push({text: c.id, value: c.id, selected: false});
            });
            options = _.uniq(options, function (e) {
                return e.text;
            });
            getchoice(options, callback);
        });
    };

    var execute_query = function (tree, node) {
        parallel({
            list: ajax_get_in_async_parallel("getqueries", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        }, function (x) {
            var callback = function (c) {
                dispquery(tree, node, c);
            };
            var options = [];
            _.each(_.sortBy(x.list, function(e) {
                return e.id;
            }), function(c) {
                options.push({text: c.id, value: c.id, selected: false});
            });
            options = _.uniq(options, function (e) {
                return e.text;
            });
            getchoice(options, callback);
        });
    };

    // initMainLayout
    desktop.layout = new dhtmlXLayoutObject(document.body,"1C");
    desktop.layout.cells("a").hideHeader();
    desktop.layout.cells("a").setBI("resources/DEFAULT.jpg");
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
    desktop.statusbar = desktop.layout.cells("a").attachStatusBar({height: 20, text:''});
    desktop.statusbar.style.backgroundColor = "lightskyblue";
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
