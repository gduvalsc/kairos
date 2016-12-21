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

var VERSION = "3.00";
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

var ajax_get_first_in_async_waterfall = function (s, p) {
    var f = function (next) {
        var logging = desktop.settings === undefined ? 'info' : desktop.settings.logging;
        if (p === undefined) {
            p = {logging: logging};
        } else {
            p.logging = p.logging === undefined ? logging : p.logging;
        }
        ajaxcpt += 1;
        document.body.className = 'waiting';
        var ferror = function (text, data, x) {
            ajaxcpt -= 1;
            if (ajaxcpt === 0) {
                document.body.className = '';
            }
            return next("XMLHttpRequest, status: " + x.status + ", statusText: " + x.statusText + ", URL: " + x.responseURL);
        };
        var fdone = function (text, data, x) {
            ajaxcpt -= 1;
            if (ajaxcpt === 0) {
                document.body.className = '';
            }
            var result = data.json();
            if (!result.success) {
                return next(result.message);
            }
            return next(null, result.data);
        };
        webix.ajax().get(s, p, {error: ferror, success: fdone});
    };
    return f;
};

var ajax_get_in_async_parallel = ajax_get_first_in_async_waterfall;

var ajax_get_next_in_async_waterfall = function (s, p) {
    var f = function (_, next) {
        var logging = desktop.settings === undefined ? 'info' : desktop.settings.logging;
        if (p === undefined) {
            p = {logging: logging};
        } else {
            p.logging = p.logging === undefined ? logging : p.logging;
        }
        ajaxcpt += 1;
        document.body.className = 'waiting';
        var ferror = function (text, data, x) {
            ajaxcpt -= 1;
            if (ajaxcpt === 0) {
                document.body.className = '';
            }
            return next("XMLHttpRequest, status: " + x.status + ", statusText: " + x.statusText + ", URL: " + x.responseURL);
        };
        var fdone = function (text, data, x) {
            ajaxcpt -= 1;
            if (ajaxcpt === 0) {
                document.body.className = '';
            }
            var result = data.json();
            if (!result.success) {
                return next(result.message);
            }
            return next(null, result.data);
        };
        webix.ajax().get(s, p, {error: ferror, success: fdone});
    };
    return f;
};

var waterfall = function (a, fposterr) {
    async.waterfall(a, function (err, result) {
        if (err) {
            webix.message({type: "error", text: err});
            if (fposterr !== undefined) {
                fposterr();
            }
        }
    });
};

var parallel = function (o, callback) {
    async.parallel(o, function (err, results) {
        if (err) {
            webix.message({type: "error", text: err});
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
            webix.message({type: "error", text: err});
        } else {
            _.each(aresult, function (v, i) {
                results[ak[i]] = v;
            });
            callback(results);
        }
    });
};

var refresh = function (explorertreeid) {
    var op = $$(explorertreeid).getOpenItems();
    var opendict = {};
    _.each(op, function (e) {
        opendict[e] = null;
    });
    var selected = $$(explorertreeid).getSelectedId();
    var afterload = $$(explorertreeid).attachEvent("onAfterLoad", function () {
        $$(explorertreeid).detachEvent(afterload);
        if (Object.keys(opendict).length  > 0) {
            var afterload2 = $$(explorertreeid).attachEvent("onAfterLoad", function () {
                if (Object.keys(opendict).length  > 0) {
                    var found = null;
                    _.some(opendict, function (v, k) {
                        if ($$(explorertreeid).exists(k)) {
                            $$(explorertreeid).open(k);
                            found = k;
                            return true;
                        }
                    });
                    delete opendict[found];
                } else {
                    $$(explorertreeid).detachEvent(afterload2);
                    if (selected !== '' && $$(explorertreeid).exists(selected)){
                        $$(explorertreeid).select(selected);
                    }
                }
            });
            var found = null;
            _.some(opendict, function (v, k) {
                if ($$(explorertreeid).exists(k)) {
                    $$(explorertreeid).open(k);
                    found = k;
                    return true;
                }
            });
            delete opendict[found];
        } else {
            if (selected !== '' && $$(explorertreeid).exists(selected)){
                $$(explorertreeid).select(selected);
            }
        }
    });
    $$(explorertreeid).clearAll();
    $$(explorertreeid).define({url: "gettree?nodesdb=" + $$(explorertreeid).nodesdb});
};

var postpone = function (n, f) {
    setTimeout(f, n);
};

var hash = function (x) {
    var md5 = CryptoJS.MD5(x);
    return md5.toString();
};

var showbackground = function () {
    var canvas = document.getElementById('maincanvas');
    var context = canvas.getContext('2d');
    var x = 0;
    var y = 0;
    var width = $$('mainarea').$width;
    var height = $$('mainarea').$height;
    canvas.width = width;
    canvas.height = height;

    var loglevel = log4javascript.Level.ALL;
    if (desktop.settings !== undefined && desktop.settings.logging !== undefined) {
        loglevel = desktop.settings.logging === 'all' ? log4javascript.Level.ALL : loglevel;
        loglevel = desktop.settings.logging === 'trace' ? log4javascript.Level.TRACE : loglevel;
        loglevel = desktop.settings.logging === 'debug' ? log4javascript.Level.DEBUG : loglevel;
        loglevel = desktop.settings.logging === 'info' ? log4javascript.Level.INFO : loglevel;
        loglevel = desktop.settings.logging === 'warn' ? log4javascript.Level.WARN : loglevel;
        loglevel = desktop.settings.logging === 'error' ? log4javascript.Level.ERROR : loglevel;
        loglevel = desktop.settings.logging === 'fatal' ? log4javascript.Level.FATAL : loglevel;
        loglevel = desktop.settings.logging === 'off' ? log4javascript.Level.OFF : loglevel;
    }
    log.info("Setting logging level to: ", loglevel);
    log.setLevel(loglevel);


    var imageObj = new Image();
    imageObj.onload = function () {
        context.drawImage(imageObj, x, y, width, height);
    };
    if (desktop.settings !== undefined && desktop.settings.wallpaper !== undefined) {
        waterfall([
            ajax_get_first_in_async_waterfall("checkwallpaper", {wallpaper: desktop.settings.wallpaper, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
            function (x) {
                imageObj.src = x;
            }
        ]);
    } else {
        imageObj.src = "/resources/DEFAULT.jpg";
    }
};

window.onresize = function (event) {
    showbackground();
};

var getallusers = function (data) {
    var result = [];
    _.each(data, function (x) {
        result.push({id: x._id, value: x.user});
    });
    return result;
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

var getallcollections = function (data) {
    var result = [];
    _.each(data, function (x) {
        result.push({id: x.name, count: x.stats.count, size: x.stats.size, storagesize: x.stats.storageSize, numextents: x.stats.numExtents, numindexes: x.stats.nindexes});
    });
    return result;
};

var getallqueries = function (data) {
    var result = [];
    _.each(data, function (x) {
        result.push({id: x.id, value: x.id + ' / ' + x.origin});
    });
    return result;
};

var getallcharts = function (data) {
    var result = [];
    _.each(data, function (x) {
        result.push({id: x.id, value: x.id + ' / ' + x.origin});
    });
    return result;
};
var getallchoyces = function (data) {
    var result = [];
    _.each(data, function (x) {
        result.push({id: x.id, value: x.id + ' / ' + x.origin});
    });
    return result;
};

var getproducers = function (node) {
    var result = [];
    _.each(node.datasource.producers, function (x) {
        result.push({path: x.path, id: x.id});
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

var logout = function (desktop) {
    desktop.closeallwindows();
    if ($$('loginwindow') !== undefined) {
        $$('loginwindow').destructor();
    }
    waterfall([
        ajax_get_first_in_async_waterfall("listusers"),
        function (x) {
            document.title = 'KAIROS V' + VERSION;
            delete desktop.settings;
            delete desktop.user;
            showbackground();
            webix.ui(desktop.LOGINWINDOW(x));
            $$('user').define({value: ""});
            $$('user').refresh();
            $$('password').define({value: ""});
            $$('password').refresh();
            $$('loginwindow').show();
            $$('user').focus();
        }
    ]);
};

var manage_password = function (desktop) {
    $$('mainwindow').hide();
    $$('mainwindow').show();
    if ($$('passwordwindow') !== undefined) {
        $$('passwordwindow').destructor();
    }
    webix.ui(desktop.PASSWORDWINDOW());
    $$('apassword').define({value: ""});
    $$('apassword').refresh();
    $$('npassword').define({value: ""});
    $$('npassword').refresh();
    $$('rpassword').define({value: ""});
    $$('rpassword').refresh();
    $$('passwordwindow').show();
    $$('apassword').focus();
};

var manage_grants = function (desktop) {
    if ($$('grantswindow') !== undefined) {
        $$('grantswindow').destructor();
    }
    waterfall([
        ajax_get_first_in_async_waterfall("listgrants"),
        function (x) {
            webix.ui(desktop.GRANTSWINDOW());
            $$('grantsgrid').define({data: getallgrants(x)});
            $$('grantsgrid').refresh();
            $$('grantswindow').show();
        }
    ]);
};

var manage_users = function (desktop) {
    if ($$('userswindow') !== undefined) {
        $$('userswindow').destructor();
    }
    webix.ui(desktop.USERSWINDOW());
    waterfall([
        ajax_get_first_in_async_waterfall("listusers"),
        function (x) {
            $$('usersgrid').define({data: getallusers(x)});
            $$('usersgrid').refresh();
            $$('userswindow').show();
        }
    ]);
};

var manage_objects = function (desktop) {
    if ($$('objectswindow') !== undefined) {
        $$('objectswindow').destructor();
    }
    webix.ui(desktop.OBJECTSWINDOW());
    waterfall([
        ajax_get_first_in_async_waterfall("listobjects", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        function (x) {
            $$('objectsgrid').define({data: getallobjects(x)});
            $$('objectsgrid').refresh();
            $$('objectswindow').show();
        }
    ]);
};

var manage_collections = function (desktop) {
    if ($$('collectionswindow') !== undefined) {
        $$('collectionswindow').destructor();
    }
    webix.ui(desktop.COLLECTIONSWINDOW());
    waterfall([
        ajax_get_first_in_async_waterfall("listcollections", {database: desktop.manageddb}),
        function (x) {
            $$('collectionsgrid').define({data: getallcollections(x)});
            $$('collectionsgrid').refresh();
            $$('collectionswindow').show();
        }
    ]);
};

var list_databases = function (desktop) {
    if ($$('databaseswindow') !== undefined) {
        $$('databaseswindow').destructor();
    }
    webix.ui(desktop.DATABASESWINDOW());
    waterfall([
        ajax_get_first_in_async_waterfall("listdatabases"),
        function (x) {
            $$('databasesgrid').define({data: getalldatabases(x)});
            $$('databasesgrid').refresh();
            $$('databaseswindow').show();
        }
    ]);
};

var manage_roles = function (desktop) {
    if ($$('roleswindow') !== undefined) {
        $$('roleswindow').destructor();
    }
    webix.ui(desktop.ROLESWINDOW());
    waterfall([
        ajax_get_first_in_async_waterfall("listroles"),
        function (x) {
            $$('rolesgrid').define({data: getallroles(x)});
            $$('rolesgrid').refresh();
            $$('roleswindow').show();
        }
    ]);
};

var manage_settings = function (desktop) {
    if ($$('settingswindow') !== undefined) {
        $$('settingswindow').destructor();
    }
    falseparallel({
        systemdb: ajax_get_in_async_parallel("listsystemdb"),
        nodesdb: ajax_get_in_async_parallel("listnodesdb", {user: desktop.user}),
        templates: ajax_get_in_async_parallel("listtemplates", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        wallpapers: ajax_get_in_async_parallel("listwallpapers", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        colors: ajax_get_in_async_parallel("listcolors", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb})
    }, function (x) {
        webix.ui(desktop.SETTINGSWINDOW(x));
        $$('settingswindow').show();
        $$('systemdb').focus();
    });
};


var manage_log = function(desktop, url, title, file) {
    var ws = new WebSocket(url);
    var uniqueid;
    var data = '';
    ws.onopen = function () {
        uniqueid = _.uniqueId('log');
        desktop.createwindow({title: title, type: "log", icon: "newspaper-o", body: {scroll: true, template: '<div id="' + uniqueid + '"></div>'}, top: $$('mainarea').$height / 6, left: $$('mainarea').$width / 6, width: $$('mainarea').$width * 2 / 3, height: $$('mainarea').$height * 2 / 3});
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
        webix.message({ type: "error", text: e.data});
    };
    ws.onclose = function (e) {
        //webix.message("Communication is closed");
        return;
    }
}

var manage_kairos_documentation = function (desktop) {
    window.location.href = '/resources/kairos.pdf';
};

var manage_table = function (desktop, explorer, nodeid, query) {
    waterfall([
        ajax_get_first_in_async_waterfall("executequery", {nodesdb: $$(explorer).nodesdb, systemdb: desktop.settings.systemdb, query: query, id: nodeid, top: desktop.settings.top, variables: desktop.variables}),
        function (x) {
            var body = {
                rows: [
                    {
                        view: "datatable",
                        select: "row",
                        scrollY: false,
                        scrollX: true,
                        resizeColumn: true,
                        columns: [],
                        data: x,
                        on: {
                            onColumnResize: function (id) {
                                if (this.getColumnConfig(id).width === 20) {
                                    this.hideColumn(id);
                                }
                            }
                        }
                    }
                ]
            };
            _.each(Object.keys(x[0]), function (k) {
                var sorter = typeof x[0][k] === 'number' ? 'int' : 'string';
                var z = {
                    id: k,
                    header: [k, {content: "textFilter"}],
                    sort: sorter,
                    adjust: true
                };
                body.rows[0].columns.push(z);
            });
            desktop.createwindow({title: query + ' - ' + $$(explorer).nodesdb + ':/' + $$(explorer).getpath(), type: "table", icon: "table", body: body, top: $$('mainarea').$height / 6, left: $$('mainarea').$width / 6, width: $$('mainarea').$width * 2 / 3, height: $$('mainarea').$height * 2 / 3});
        }
    ]);
};

var manage_node = function (desktop, explorertreeid) {
    var selectednodeid = $$(explorertreeid).getSelectedId();
    var nodesdb = $$(explorertreeid).nodesdb;
    var aggregatormethod = "aggregatormethod" + desktop.windowscounter + 1;
    var aggregatorskip = "aggregatorskip" + desktop.windowscounter + 1;
    var aggregatorsort = "aggregatorsort" + desktop.windowscounter + 1;
    var aggregatortake = "aggregatortake" + desktop.windowscounter + 1;
    var aggregatortimefilter = "aggregatortimefilter" + desktop.windowscounter + 1;
    var aggregatorselector = "aggregatorselector" + desktop.windowscounter + 1;
    var liveobject = "liveobject" + desktop.windowscounter + 1;
    var vcollectionsgrid = "nodevirtualcollectionsgrid" + desktop.windowscounter + 1;
    // var vcollectionscachegrid = "nodevirtualcollectionscachegrid" + desktop.windowscounter + 1;
    var buildcache = "buildcache" + desktop.windowscounter + 1;
    var dropcache = "dropcache" + desktop.windowscounter + 1;
    var closer;
    falseparallel({
        node: ajax_get_in_async_parallel("getnode", {nodesdb: nodesdb, id: selectednodeid}),
        aggregators: ajax_get_in_async_parallel("listaggregators", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        liveobjects: ajax_get_in_async_parallel("listliveobjects", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb})
    }, function (x) {
        var body = {
            rows: [
                {
                    view: "form",
                    borderless: true,
                    scroll: true,
                    elements: [
                        {
                            view: "fieldset",
                            label: "Node properties",
                            body: {
                                rows: [
                                    {
                                        margin: 10,
                                        cols: [
                                            {
                                                view: "text",
                                                label: "Type",
                                                value: x.node.datasource.type,
                                                readonly: true
                                            },
                                            {
                                                view: "datepicker",
                                                timepicker: true,
                                                label: "Created",
                                                value: new Date(Date.parse(x.node.created)),
                                                readonly: true
                                            },
                                            {
                                                view: "text",
                                                label: "Status",
                                                value: x.node.status,
                                                readonly: true
                                            }
                                        ]
                                    },
                                    {
                                        margin: 10,
                                        hidden: _.contains(["L", "A", "N", "C", "T", "D"], x.node.datasource.type) ? true : false,
                                        cols: [
                                            {
                                                view: "datepicker",
                                                timepicker: true,
                                                label: "Uploaded",
                                                value: new Date(Date.parse(x.node.datasource.uploaded)),
                                                readonly: true
                                            }
                                        ]
                                    },
                                    {
                                        view: "fieldset",
                                        hidden: _.contains(["B", "C", "T", "D"], x.node.datasource.type) ? true : false,
                                        label: "Aggregator",
                                        body: {
                                            rows: [
                                                {
                                                    cols: [
                                                        {
                                                            view: "text",
                                                            label: "Selector",
                                                            id: aggregatorselector,
                                                            value: x.node.datasource.aggregatorselector === undefined ? "/" : x.node.datasource.aggregatorselector,
                                                            readonly: false
                                                        },
                                                    ],
                                                },
                                                {
                                                    cols: [
                                                        {
                                                            view: "counter",
                                                            label: "Take",
                                                            id: aggregatortake,
                                                            step: 1,
                                                            min: 1,
                                                            value: x.node.datasource.aggregatortake === undefined ? 1 : x.node.datasource.aggregatortake
                                                        },
                                                        {
                                                            view: "counter",
                                                            label: "Skip",
                                                            id: aggregatorskip,
                                                            step: 1,
                                                            min: 0,
                                                            value: x.node.datasource.aggregatorskip === undefined ? 0 : x.node.datasource.aggregatorskip
                                                        },
                                                        {
                                                            view: "combo",
                                                            label: "Sort",
                                                            id: aggregatorsort,
                                                            value: x.node.datasource.aggregatorsort === undefined ? "desc" : x.node.datasource.aggregatorsort,
                                                            yCount: ['asc', 'desc'].length,
                                                            options: ['asc', 'desc']
                                                        },
                                                    ],
                                                },
                                                {
                                                    cols: [
                                                        {
                                                            view: "text",
                                                            label: "TimeFilter",
                                                            id: aggregatortimefilter,
                                                            value: x.node.datasource.aggregatortimefilter === undefined ? "." : x.node.datasource.aggregatortimefilter,
                                                            readonly: false
                                                        },
                                                    ],
                                                },
                                                {
                                                    cols: [
                                                        {
                                                            view: "combo",
                                                            label: "Method",
                                                            id: aggregatormethod,
                                                            value: x.node.datasource.aggregatormethod === undefined ? '$none' : x.node.datasource.aggregatormethod,
                                                            yCount: _.uniq(_.sortBy(_.map(x.aggregators, function (a) { return a.id; }), function (x) { return x; })).length,
                                                            options: _.uniq(_.sortBy(_.map(x.aggregators, function (a) { return a.id; }), function (x) { return x; }))
                                                        },
                                                        {
                                                            view: "datepicker",
                                                            timepicker: true,
                                                            label: "Aggregated",
                                                            value: new Date(Date.parse(x.node.datasource.aggregated)),
                                                            readonly: true
                                                        },
                                                        {
                                                            view: "button",
                                                            value: "Apply aggregator",
                                                            click: function () {
                                                                waterfall([
                                                                    ajax_get_first_in_async_waterfall("applyaggregator", {nodesdb: nodesdb, id: selectednodeid, aggregatorselector: $$(aggregatorselector).getValue(), aggregatortake: $$(aggregatortake).getValue(), aggregatortimefilter: $$(aggregatortimefilter).getValue(), aggregatorskip: $$(aggregatorskip).getValue(), aggregatorsort: $$(aggregatorsort).getValue(), aggregatormethod: $$(aggregatormethod).getValue(), systemdb: desktop.settings.systemdb}),
                                                                    function (node) {
                                                                        var row = $$(explorertreeid).getItem(selectednodeid);
                                                                        row.icon = node.datasource.type;
                                                                        $$(explorertreeid).updateItem(selectednodeid, row);
                                                                        refresh(explorertreeid);
                                                                        $$(explorertreeid).unselect(selectednodeid);
                                                                        $$(explorertreeid).select(selectednodeid);
                                                                        closer.config.click();
                                                                    }
                                                                ]);
                                                            }
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        view: "fieldset",
                                        hidden: _.contains(["L", "A", "B", "C", "T"], x.node.datasource.type) ? true : false,
                                        label: "Live node",
                                        body: {
                                            rows: [
                                                {
                                                    cols: [
                                                        {
                                                            view: "combo",
                                                            label: "Live object",
                                                            id: liveobject,
                                                            value: x.node.datasource.liveobject === undefined ? 'None' : x.node.datasource.liveobject,
                                                            yCount: _.uniq(_.sortBy(_.map(x.liveobjects, function (a) { return a.id; }), function (x) { return x; })).length,
                                                            options: _.uniq(_.sortBy(_.map(x.liveobjects, function (a) { return a.id; }), function (x) { return x; }))
                                                        },
                                                        {
                                                            view: "button",
                                                            value: "Apply live object",
                                                            click: function () {
                                                                waterfall([
                                                                    ajax_get_first_in_async_waterfall("applyliveobject", {nodesdb: nodesdb, id: selectednodeid, liveobject: $$(liveobject).getValue(), systemdb: desktop.settings.systemdb}),
                                                                    function (node) {
                                                                        var row = $$(explorertreeid).getItem(selectednodeid);
                                                                        row.icon = node.datasource.type;
                                                                        $$(explorertreeid).updateItem(selectednodeid, row);
                                                                        $$(explorertreeid).unselect(selectednodeid);
                                                                        $$(explorertreeid).select(selectednodeid);
                                                                        closer.config.click();
                                                                    }
                                                                ]);
                                                            }
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        view: "fieldset",
                                        hidden: _.contains(["B", "N", "T", "D"], x.node.datasource.type) ? true : false,
                                        label: "Producers",
                                        body: {
                                            rows: [
                                                {
                                                    view: "datatable",
                                                    height: 200,
                                                    select: "row",
                                                    scrollY: false,
                                                    scrollX: false,
                                                    columns: [
                                                        {
                                                            id: "path",
                                                            header: [
                                                                "Node path",
                                                                {
                                                                    content: "textFilter"
                                                                }
                                                            ],
                                                            sort: "string",
                                                            fillspace: true
                                                        },
                                                        {
                                                            id: "id",
                                                            header: "Node id",
                                                            adjust: true,
                                                            sort: "string"
                                                        }
                                                    ],
                                                    data: getproducers(x.node)
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        view: "fieldset",
                                        hidden: _.contains(["N", "L", "T"], x.node.datasource.type) ? true : false,
                                        label: "Collections",
                                        body: {
                                            rows: [
                                                {
                                                    view: "datatable",
                                                    id: vcollectionsgrid,
                                                    height: 300,
                                                    select: "row",
                                                    scrollY: false,
                                                    scrollX: false,
                                                    on: {
                                                        onSelectChange: function () {
                                                            if ($$(vcollectionsgrid).getSelectedId(true).length === 0) {
                                                                $$(buildcache).disable();
                                                                $$(dropcache).disable();
                                                            } else {
                                                                $$(buildcache).enable();
                                                                $$(dropcache).enable();
                                                            }
                                                        }
                                                    },
                                                    columns: [
                                                        {
                                                            id: "id",
                                                            header: "Id",
                                                            sort: "string",
                                                            fillspace: true
                                                        },
                                                        {
                                                            id: "collection",
                                                            header: [
                                                                "Collection",
                                                                {
                                                                    content: "textFilter"
                                                                }
                                                            ],
                                                            sort: "string",
                                                            fillspace: true
                                                        },
                                                        {
                                                            id: "partition",
                                                            hidden: _.contains(["L", "C"], x.node.datasource.type) ? true : false,
                                                            header: [
                                                                "Partition",
                                                                {
                                                                    content: "textFilter"
                                                                }
                                                            ],
                                                            sort: "string",
                                                            fillspace: true
                                                        },
                                                        {
                                                            id: "analyzer",
                                                            hidden: _.contains(["D"], x.node.datasource.type) ? true : false,
                                                            header: "Analyzer",
                                                            adjust: true,
                                                            sort: "string"
                                                        },
                                                        {
                                                            id: "created",
                                                            hidden: _.contains(["L", "C"], x.node.datasource.type) ? true : false,
                                                            header: "Cache creation date",
                                                            adjust: true,
                                                            sort: "string"
                                                        }
                                                    ],
                                                    data: getcollections(x.node)
                                                },
                                                {
                                                    hidden: _.contains(["L", "C"], x.node.datasource.type) ? true : false,
                                                    cols: [
                                                        {
                                                            view: "button",
                                                            value: "Build all caches",
                                                            disabled: false,
                                                            click: function () {
                                                                waterfall([
                                                                    ajax_get_first_in_async_waterfall("buildallcollectioncaches", {nodesdb: nodesdb, id: selectednodeid, systemdb: desktop.settings.systemdb}),
                                                                    function (x) {
                                                                        closer.config.click();
                                                                    }
                                                                ]);
                                                            }
                                                        },
                                                        {
                                                            view: "button",
                                                            id: buildcache,
                                                            value: "Build collection cache",
                                                            disabled: true,
                                                            click: function () {
                                                                var rowselected = $$(vcollectionsgrid).getSelectedId(true);
                                                                var collection = $$(vcollectionsgrid).getItem(rowselected[0].id).collection;
                                                                waterfall([
                                                                    ajax_get_first_in_async_waterfall("buildcollectioncache", {nodesdb: nodesdb, id: selectednodeid, systemdb: desktop.settings.systemdb, collection: collection}),
                                                                    function (x) {
                                                                        closer.config.click();
                                                                    }
                                                                ]);
                                                            }
                                                        },
                                                        {
                                                            view: "button",
                                                            id: dropcache,
                                                            value: "Drop collection cache",
                                                            disabled: true,
                                                            hidden: _.contains(["D"], x.node.datasource.type) ? true : false,
                                                            click: function () {
                                                                var rowselected = $$(vcollectionsgrid).getSelectedId(true);
                                                                var collection = $$(vcollectionsgrid).getItem(rowselected[0].id).collection;
                                                                waterfall([
                                                                    ajax_get_first_in_async_waterfall("dropcollectioncache", {nodesdb: nodesdb, id: selectednodeid, collection: collection, systemdb: desktop.settings.systemdb}),
                                                                    function (x) {
                                                                        closer.config.click();
                                                                    }
                                                                ]);
                                                            }
                                                        },
                                                        {
                                                            view: "button",
                                                            value: "Clear collections caches",
                                                            hidden: _.contains(["D"], x.node.datasource.type) ? true : false,
                                                            click: function () {
                                                                waterfall([
                                                                    ajax_get_first_in_async_waterfall("clearcollectioncache", {nodesdb: nodesdb, systemdb: desktop.settings.systemdb, id: selectednodeid}),
                                                                    function (x) {
                                                                        closer.config.click();
                                                                    }
                                                                ]);
                                                            }
                                                        }
                                                    ]
                                                }

                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            ]
        };
        var win = desktop.createwindow({title: $$(explorertreeid).getpath(selectednodeid) + ' (' + nodesdb + ')', type: "node", icon: "bullseye", body: body, top: $$('mainarea').$height / 6, left: $$('mainarea').$width / 6, width: $$('mainarea').$width * 2 / 3, height: $$('mainarea').$height * 2 / 3});
        closer = win.getcloser();
    });
};

var dispchoice = function (explorertreeid, node, choice) {
    desktop.lastfunction = "dispchoice";
    desktop.lastchoice = choice;
    falseparallel({
        choice: ajax_get_in_async_parallel("getchoice", {choice: choice, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb, variables: desktop.variables}),
    }, function (x) {
        waterfall([
            ajax_get_first_in_async_waterfall("executequery", {nodesdb: $$(explorertreeid).nodesdb, systemdb: desktop.settings.systemdb, id: $$(explorertreeid).getSelectedId(), query: x.choice.query, top: desktop.settings.top, variables: desktop.variables}),
            function (y) {
                if ($$('choicepicker') !== undefined) {
                    $$('choicepicker').destructor();
                }
                webix.ui(desktop.CHOICEPICKER(y, explorertreeid, node, x.choice));
                $$('choicepicker').show();
            }
        ]);
    });
};

var dispmember = function (explorertreeid, node, member) {
    waterfall([
        ajax_get_first_in_async_waterfall("getmember", {nodesdb: $$(explorertreeid).nodesdb, id: $$(explorertreeid).getSelectedId(), member: member}),
        function (x) {
            var uniquecid = _.uniqueId('member');
            desktop.createwindow({title: node.name + ' - ' + member, type: "file", icon: "file-text-o", body: {id: uniquecid, scroll: true, template: x}, top: 0, left: 0, width: $$('mainarea').$width, height: $$('mainarea').$height});
        }
    ]);
};

var dispchart = function (explorertreeid, node, chart, layoutpiece) {
    log.debug('Starting chart display');
    log.debug('Getting chart, template & colors');
    desktop.lastfunction = "dispchart";
    desktop.lastchart = chart;
    falseparallel({
        chart: ajax_get_in_async_parallel("getchart", {chart: chart, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb, variables: desktop.variables}),
        template: ajax_get_in_async_parallel("gettemplate", {template: desktop.settings.template, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        colors: ajax_get_in_async_parallel("getcolors", {colors: desktop.settings.colors, systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
    }, function (x) {
        log.debug('Executing queries');
        var chartqueries = {};
        if (x.chart.reftime !== undefined) {
            chartqueries[x.chart.reftime] = ajax_get_first_in_async_waterfall("executequery", {nodesdb: $$(explorertreeid).nodesdb, systemdb: desktop.settings.systemdb, id: $$(explorertreeid).getSelectedId(), query: x.chart.reftime, top: desktop.settings.top, variables: desktop.variables});

        }
        _.each(x.chart.yaxis, function (y) {
            _.each(y.renderers, function (r) {
                _.each(r.datasets, function (d) {
                    chartqueries[d.query] = ajax_get_first_in_async_waterfall("executequery", {nodesdb: $$(explorertreeid).nodesdb, systemdb: desktop.settings.systemdb, id: $$(explorertreeid).getSelectedId(), query: d.query, top: desktop.settings.top, variables: desktop.variables});
                });
            });
        });
        falseparallel(chartqueries, function (q) {
            log.debug('Preparing chart');
            var uniquecid;
            var container;
            if (layoutpiece === undefined) {
                uniquecid = _.uniqueId('chart');
                container = desktop.createwindow({title: node.name + ' - ' + x.chart.id, type: "chart", icon: x.chart.icon, body: {id: uniquecid}, top: 0, left: 0, width: $$('mainarea').$width, height: $$('mainarea').$height});
            } else {
                uniquecid = layoutpiece;
                container = $$(layoutpiece);
            }
            var g = new KairosCharter.Chart({width: $$(uniquecid).$width, height: $$(uniquecid).$height}, desktop.settings.logging);
            $$(container).kairosg = g;
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
                                            dispchart(explorertreeid, node, d.onclick.chart);
                                        }
                                    }
                                }
                                if (d.info !== undefined && dataset.info[z[d.label]] === undefined) {
                                    dataset.info[z[d.label]] = function () {
                                        desktop.variables[d.info.variable] = z[d.label];
                                        waterfall([
                                            ajax_get_first_in_async_waterfall("executequery", {nodesdb: $$(explorertreeid).nodesdb, systemdb: desktop.settings.systemdb, id: $$(explorertreeid).getSelectedId(), query: d.info.query, top: desktop.settings.top, variables: desktop.variables}),
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
            log.debug('Drawing chart');
            var selector = '[view_id=' + uniquecid + ']';
            g.draw(selector, uniquecid);
            log.debug('End of drawing');
        });
    });
};

var manage_explorer = function (desktop) {
    var explorerwindowsid;
    var explorerfilterid = "explorerfilter" + desktop.windowscounter + 1;
    var explorertreeid = "explorertree" + desktop.windowscounter + 1;
    var uploaderdroparea = "uploaderdroparea" + desktop.windowscounter + 1;
    var toolbarid = "nodetoolbar" + desktop.windowscounter + 1;
    var uploaderid = "uploadertree" + desktop.windowscounter + 1;
    var contextmenuid = "contextmenu" + desktop.windowscounter + 1;
    var contextuploadid = "contextupload" + desktop.windowscounter + 1;
    var contextcreatenodeid = "contextcreatenodeid" + desktop.windowscounter + 1;
    var contextdeletenodeid = "contextdeletenodeid" + desktop.windowscounter + 1;
    var contextexecutequeryid = "contextexecutequeryid" + desktop.windowscounter + 1;
    var contextrunchartid = "contextrunchartid" + desktop.windowscounter + 1;
    var contextrunchoiceid = "contextrunchoiceid" + desktop.windowscounter + 1;
    var contextopennodeid = "contextopennodeid" + desktop.windowscounter + 1;
    var contextdownloadid = "contextdownloadid" + desktop.windowscounter + 1;
    var contextunloadid = "unloadid" + desktop.windowscounter + 1;
    var contextdisplaymemberid = "contextdisplaymemberid" + desktop.windowscounter + 1;
    var tree = {
        rows: [
            {
                view: "toolbar",
                id: toolbarid,
                css: "xtoolbar",
                height: 34,
                paddingY: 0,
                cols : [
                ]
            },
            {
                id: explorerfilterid,
                view: "text",
                label: "Filter",
                labelAlign: "right"
            },
            {
                id: explorertreeid,
                view: "edittree",
                editable: true,
                editor: "popup",
                editValue: "value",
                editaction: "custom",
                type: "lineTree",
                select: true,
                drag: true,
                onContext: {},
                url: "gettree?nodesdb=" + desktop.settings.nodesdb,
                on: {
                    onBeforeEditStart: function (state, editor) {
                        if (desktop.lastkeycode !== 16) {
                            return false;
                        }
                    },
                    onBeforeEditStop: function (state, editor) {
                        if (state.old !== state.value) {
                            var brothername;
                            var selectednodeid = $$(explorertreeid).getSelectedId();
                            var parent = $$(explorertreeid).getParentId(selectednodeid);
                            var brother = $$(explorertreeid).getFirstChildId(parent);
                            while (brother !== null) {
                                brothername = $$(explorertreeid).getItem(brother).value;
                                if (state.value === brothername && brother !== selectednodeid) {
                                    return false;
                                }
                                brother = $$(explorertreeid).getNextSiblingId(brother);
                            }
                            waterfall([
                                ajax_get_first_in_async_waterfall("renamenode", {nodesdb: $$(explorertreeid).nodesdb, id: selectednodeid, new: state.value})
                            ], function () {
                                refresh(explorertreeid);
                            });
                        }
                    },
                    onBeforeDrop: function (context, ev) {
                        var move = true;
                        move = ev.altKey ? false : move;
                        move = ev.ctrlKey ? false : move;
                        move = ev.metaKey ? false : move;
                        var compare = ev.ctrlKey ? true : false;
                        var aggregate = ev.altKey ? true : false;
                        var link = ev.metaKey ? true : false;
                        var rowtarget = $$(explorertreeid).getItem(context.target);
                        var rowsource = $$(explorertreeid).getItem(context.start);
                        if (context.target === null) {
                            return false;
                        }
                        if (move) {
                            if (context.target === $$(explorertreeid).getParentId(context.start)) {
                                return false;
                            }
                            var brothername;
                            var curname = $$(explorertreeid).getItem(context.start).value;
                            var brother = $$(explorertreeid).getFirstChildId(context.target);
                            while (brother !== null) {
                                brothername = $$(explorertreeid).getItem(brother).value;
                                if (curname === brothername) {
                                    return false;
                                }
                                brother = $$(explorertreeid).getNextSiblingId(brother);
                            }
                            if ($$(context.from.config.id).nodesdb !== $$(context.to.config.id).nodesdb) {
                                webix.message({ type: "error", text: "Moving a node from one database to another is not yet implemented !"});
                                return false;
                            }
                            waterfall([
                                ajax_get_first_in_async_waterfall("movenode", {origindb: $$(context.from.config.id).nodesdb, targetdb: $$(context.to.config.id).nodesdb, from: context.start, to: context.target}),
                                function (x) {
                                    refresh(explorertreeid);
                                }
                            ]);
                            context.parent = context.target;
                            return true;
                        }
                        if (compare) {
                            if (_.contains(["N", "C", "L"], rowsource.icon)) {
                                return false;
                            }
                            if (_.contains(["A", "B", "L"], rowtarget.icon)) {
                                return false;
                            }
                            if ($$(context.from.config.id).nodesdb !== $$(context.to.config.id).nodesdb) {
                                webix.message({ type: "error", text: "Linking a node from one database to another is not yet implemented !"});
                                return false;
                            }
                            waterfall([
                                ajax_get_first_in_async_waterfall("compareaddnode", {origindb: $$(context.from.config.id).nodesdb, targetdb: $$(context.to.config.id).nodesdb, from: context.start, to: context.target, path: $$(explorertreeid).getpath(context.start)}),
                                function (x) {
                                    rowtarget.icon = "C";
                                    $$(explorertreeid).updateItem(context.target, rowtarget);
                                    $$(explorertreeid).unselect(context.target);
                                    $$(explorertreeid).select(context.target);
                                    refresh(explorertreeid);
                                }
                            ]);
                            return false;
                        }
                        if (aggregate) {
                            if (_.contains(["N", "C", "L"], rowsource.icon)) {
                                return false;
                            }
                            if (_.contains(["B", "L", "C"], rowtarget.icon)) {
                                return false;
                            }
                            if ($$(context.from.config.id).nodesdb !== $$(context.to.config.id).nodesdb) {
                                webix.message({ type: "error", text: "Aggegating a node from one database to another is not yet implemented !"});
                                return false;
                            }
                            waterfall([
                                ajax_get_first_in_async_waterfall("aggregateaddnode", {origindb: $$(context.from.config.id).nodesdb, targetdb: $$(context.to.config.id).nodesdb, from: context.start, to: context.target, path: $$(explorertreeid).getpath(context.start)}),
                                function (x) {
                                    rowtarget.icon = "A";
                                    $$(explorertreeid).updateItem(context.target, rowtarget);
                                    $$(explorertreeid).unselect(context.target);
                                    $$(explorertreeid).select(context.target);
                                    refresh(explorertreeid);
                                }
                            ]);
                            return false;
                        }
                        if (link) {
                            if (_.contains(["A", "B", "C"], rowsource.icon)) {
                                return false;
                            }
                            if (_.contains(["A", "B", "C"], rowtarget.icon)) {
                                return false;
                            }
                            if ($$(context.from.config.id).nodesdb !== $$(context.to.config.id).nodesdb) {
                                webix.message({ type: "error", text: "Linking a node from one database to another is not yet implemented !"});
                                return false;
                            }
                            waterfall([
                                ajax_get_first_in_async_waterfall("linkfathernode", {origindb: $$(context.from.config.id).nodesdb, targetdb: $$(context.to.config.id).nodesdb, from: context.start, to: context.target, path: $$(explorertreeid).getpath(context.start)}),
                                function (x) {
                                    rowtarget.icon = "L";
                                    $$(explorertreeid).updateItem(context.target, rowtarget);
                                    $$(explorertreeid).unselect(context.target);
                                    $$(explorertreeid).select(context.target);
                                    refresh(explorertreeid);
                                }
                            ]);
                            return false;
                        }
                        return false;
                    },
                    onxxxxxAfterLoad: function () {
                        $$(explorertreeid).sort("#value#", "desc");               
                    },
                    onAfterSelect: function (c) {
                        var collections = new Set();
                        var nodesdb = $$(explorertreeid).nodesdb;
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        waterfall([
                            ajax_get_first_in_async_waterfall("getnode", {nodesdb: nodesdb, id: selectednodeid}),
                            function (node) {
                                if (node.datasource.type === 'T') {
                                    $$(contextuploadid).disable();
                                    $$(contextcreatenodeid).disable();
                                    $$(contextdeletenodeid).disable();
                                    $$(contextexecutequeryid).disable();
                                    $$(contextrunchartid).disable();
                                    $$(contextrunchoiceid).disable();
                                    $$(contextopennodeid).enable();
                                    $$(contextdownloadid).disable();
                                    $$(contextunloadid).disable();
                                    $$(contextdisplaymemberid).disable();
                                }
                                if (node.datasource.type === 'N') {
                                    $$(contextuploadid).enable();
                                    $$(contextcreatenodeid).enable();
                                    $$(contextdeletenodeid).enable();
                                    $$(contextexecutequeryid).disable();
                                    $$(contextrunchartid).disable();
                                    $$(contextrunchoiceid).disable();
                                    $$(contextopennodeid).enable();
                                    $$(contextdownloadid).disable();
                                    $$(contextunloadid).disable();
                                    $$(contextdisplaymemberid).disable();
                                }
                                if (node.datasource.type === 'B') {
                                    $$(contextuploadid).enable();
                                    $$(contextcreatenodeid).enable();
                                    $$(contextdeletenodeid).enable();
                                    $$(contextexecutequeryid).enable();
                                    $$(contextrunchartid).enable();
                                    $$(contextrunchoiceid).enable();
                                    $$(contextopennodeid).enable();
                                    $$(contextdownloadid).enable();
                                    $$(contextunloadid).enable();
                                    $$(contextdisplaymemberid).enable();
                                }
                                if (node.datasource.type === 'A') {
                                    $$(contextuploadid).disable();
                                    $$(contextcreatenodeid).enable();
                                    $$(contextdeletenodeid).enable();
                                    $$(contextexecutequeryid).enable();
                                    $$(contextrunchartid).enable();
                                    $$(contextrunchoiceid).enable();
                                    $$(contextopennodeid).enable();
                                    $$(contextdownloadid).disable();
                                    $$(contextunloadid).enable();
                                    $$(contextdisplaymemberid).disable();
                                }
                                if (node.datasource.type === 'C') {
                                    $$(contextuploadid).disable();
                                    $$(contextcreatenodeid).enable();
                                    $$(contextdeletenodeid).enable();
                                    $$(contextexecutequeryid).enable();
                                    $$(contextrunchartid).enable();
                                    $$(contextrunchoiceid).enable();
                                    $$(contextopennodeid).enable();
                                    $$(contextdownloadid).disable();
                                    $$(contextunloadid).disable();
                                    $$(contextdisplaymemberid).disable();
                                }
                                if (node.datasource.type === 'L') {
                                    $$(contextuploadid).disable();
                                    $$(contextcreatenodeid).enable();
                                    $$(contextdeletenodeid).enable();
                                    $$(contextexecutequeryid).enable();
                                    $$(contextrunchartid).enable();
                                    $$(contextrunchoiceid).enable();
                                    $$(contextopennodeid).enable();
                                    $$(contextdownloadid).disable();
                                    $$(contextdisplaymemberid).disable();
                                }
                                if (node.datasource.type === 'D') {
                                    $$(contextuploadid).disable();
                                    $$(contextcreatenodeid).enable();
                                    $$(contextdeletenodeid).enable();
                                    $$(contextexecutequeryid).enable();
                                    $$(contextrunchartid).enable();
                                    $$(contextrunchoiceid).enable();
                                    $$(contextdownloadid).disable();
                                    $$(contextopennodeid).enable();
                                    $$(contextdownloadid).disable();
                                    $$(contextdisplaymemberid).disable();
                                    $$(contextunloadid).enable();
                                }
                                _.each(node.datasource.collections, function (collection, c) {
                                    collections.add(c);
                                });
                                var menus = [];
                                _.each($$(toolbarid).getChildViews(), function (view) {
                                    menus.push(view.config.id);
                                });
                                _.each(menus, function (menu) {
                                    $$(toolbarid).removeView(menu);
                                });
                                _.each($$(toolbarid).potentialmenus, function (menu) {
                                    if (collections.has(menu.tablecondition)) {
                                        var cmenubuilder = function (x) {
                                            var cmenu = {};
                                            cmenu.view = "contextmenu";
                                            cmenu.on = {
                                                onMenuItemClick: function (e) {
                                                    var entry = this.getMenuItem(e);
                                                    if (entry.custom.action === "displayout") {
                                                        waterfall([
                                                            ajax_get_first_in_async_waterfall("getlayout", {layout: entry.custom.layout, nodesdb: nodesdb, systemdb: desktop.settings.systemdb, variables: desktop.variables}),
                                                            function (layout) {
                                                                var body = {};
                                                                body.rows = [];
                                                                _.each(layout.rows, function (row) {
                                                                    if (row.chart !== undefined) {
                                                                        row.id = _.uniqueId(layout.id + row.chart);
                                                                    }
                                                                    _.each(row.cols, function (col) {
                                                                        if (col.chart !== undefined) {
                                                                            col.id = _.uniqueId(layout.id + col.chart);
                                                                        }
                                                                    });
                                                                    body.rows.push(row);
                                                                });
                                                                desktop.createwindow({title: node.name + ' - ' + layout.label, type: "layout", icon: layout.icon, body: body, top: 0, left: 0, width: $$('mainarea').$width, height: $$('mainarea').$height});
                                                                _.each(body.rows, function (row) {
                                                                    if (row.chart !== undefined) {
                                                                        dispchart(explorertreeid, node, row.chart, row.id);
                                                                    }
                                                                    _.each(row.cols, function (col) {
                                                                        if (col.chart !== undefined) {
                                                                            dispchart(explorertreeid, node, col.chart, col.id);
                                                                        }
                                                                    });
                                                                });
                                                            }
                                                        ]);
                                                    }
                                                    if (entry.custom.action === "dispchoice") {
                                                        dispchoice(explorertreeid, node, entry.custom.choice);
                                                    }
                                                    if (entry.custom.action === "dispchart") {
                                                        dispchart(explorertreeid, node, entry.custom.chart);
                                                    }
                                                }
                                            };
                                            if (x.itemswidth !== undefined) {
                                                // cmenu.width = menu.itemswidth;
                                                cmenu.width = x.itemswidth;
                                            }
                                            cmenu.data = [];
                                            _.each(x.items, function (item) {
                                                if (item.keyfunc !== undefined) {
                                                    if (item.action === "dispchart") {
                                                        $$(explorerwindowsid)["keydown_" + item.keyfunc.charCodeAt(0)] = function () {
                                                            dispchart(explorertreeid, node, item.chart);
                                                        };
                                                    }
                                                    if (item.action === "dispchoice") {
                                                        $$(explorerwindowsid)["keydown_" + item.keyfunc.charCodeAt(0)] = function () {
                                                            dispchoice(explorertreeid, node, item.choice);
                                                        };
                                                    }
                                                    item.label = '<span title="Keyboard Shortcut: ' + String.fromCharCode(desktop.settings.keycode) + 'E' + item.keyfunc + '">' + item.label + '</span>';
                                                }
                                                if (item.keycode !== undefined) {
                                                    if (item.action === "dispchart") {
                                                        $$(explorerwindowsid)["keydown_" + item.keycode] = function () {
                                                            dispchart(explorertreeid, node, item.chart);
                                                        };
                                                    }
                                                    if (item.action === "dispchoice") {
                                                        $$(explorerwindowsid)["keydown_" + item.keycode] = function () {
                                                            dispchoice(explorertreeid, node, item.choice);
                                                        };
                                                    }
                                                    item.label = '<span title="Keyboard Shortcut: ' + String.fromCharCode(desktop.settings.keycode) + 'E' + String.fromCharCode(item.keycode) + '">' + item.label + '</span>';
                                                }
                                                var record;
                                                record = item.type === "separator" ? {$template: "Separator"} : record;
                                                record = item.type === "menuitem" ? {view: "button", type: "icon", icon: item.icon, value: item.label, custom: {action: item.action, layout: item.layout, chart: item.chart, choice: item.choice}} : record;
                                                record = item.type === "submenu" ? {view: "button", type: "icon", icon: item.icon, value: item.label, width: item.itemswidth, submenu: cmenubuilder(item)} : record;
                                                if (item.condition === undefined || eval(item.condition)) {
                                                    cmenu.data.push(record);
                                                }
                                            });
                                            $$(explorerwindowsid).keydown_33 = function () {
                                                if (desktop.lastfunction === 'dispchart') {
                                                    dispchart(explorertreeid, node, desktop.lastchart);
                                                }
                                                if (desktop.lastfunction === 'dispchoice') {
                                                    dispchoice(explorertreeid, node, desktop.lastchoice);
                                                }
                                            };
                                            var ret = x.type === "menu" ? cmenu : cmenu.data;
                                            return ret;
                                        };
                                        var contextmenu = webix.ui(cmenubuilder(menu));
                                        var menubutton = {
                                            view: "button",
                                            id: menu.id,
                                            type: "icon",
                                            icon: menu.icon === undefined ? "" : menu.icon,
                                            label: menu.label,
                                            width: menu.menuwidth === undefined ? 150 : menu.menuwidth,
                                            click: function () {
                                                var buttonpos = $$(menu.id).getNode().getBoundingClientRect();
                                                contextmenu.config.top = buttonpos.top + buttonpos.height;
                                                contextmenu.config.left = buttonpos.left;
                                                contextmenu.refresh();
                                                contextmenu.show();
                                            }
                                        };
                                        $$(toolbarid).addView(menubutton);
                                    }
                                });
                            }
                        ]);
                    },
                    onItemDblClick: function (c) {
                        manage_node(desktop, explorertreeid);
                    }
                }
            },
            {
                view: "resizer"
            },
            {
                view: "list",
                id: uploaderdroparea,
                type: "uploader",
                scroll: true,
                height: $$("mainarea").$height / 10000
            }
        ]
    };
    var contextmenu = {
        view: "context",
        id: contextmenuid,
        width: 150,
        body: {
            rows: [
                {
                    view: "button",
                    label: "Upload",
                    id: contextuploadid,
                    height: 30,
                    disabled: true,
                    click: function () {
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        $$(contextmenuid).hide();
                        var onerror = function (x, ret) {
                            document.body.className = '';
                            webix.message({ type: "error", text: ret.message});
                        };
                        var ondone = function () {
                            document.body.className = '';
                            var row = $$(explorertreeid).getItem(selectednodeid);
                            row.icon = "B";
                            $$(explorertreeid).updateItem(selectednodeid, row);
                            $$(explorertreeid).unselect(selectednodeid);
                            $$(explorertreeid).select(selectednodeid);
                            refresh(explorertreeid);
                        };
                        webix.ui(desktop.UPLOADOBJECT("uploadnode?nodesdb=" + $$(explorertreeid).nodesdb + "&systemdb=" + $$(explorertreeid).systemdb + "&id=" + encodeURIComponent(selectednodeid) + "&logging=" + desktop.settings.logging, onerror, ondone));
                        $$("uploadobject").fileDialog();
                    }
                },
                {
                    view: "button",
                    label: "Create node",
                    id: contextcreatenodeid,
                    height: 30,
                    disabled: true,
                    click: function () {
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        $$(contextmenuid).hide();
                        waterfall([
                            ajax_get_first_in_async_waterfall("createnode", {nodesdb: $$(explorertreeid).nodesdb, id: selectednodeid}),
                            function (x) {
                                refresh(explorertreeid);
                            }
                        ]);
                    }
                },
                {
                    view: "button",
                    label: "Open node",
                    id: contextopennodeid,
                    height: 30,
                    disabled: true,
                    click: function () {
                        $$(contextmenuid).hide();
                        manage_node(desktop, explorertreeid);
                    }
                },
                {
                    view: "button",
                    label: "Delete node",
                    id: contextdeletenodeid,
                    height: 30,
                    disabled: true,
                    click: function () {
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        $$(contextmenuid).hide();
                        waterfall([
                            ajax_get_first_in_async_waterfall("deletenode", {nodesdb: $$(explorertreeid).nodesdb, id: selectednodeid}),
                            function (x) {
                                refresh(explorertreeid);
                            }
                        ]);
                    }
                },
                {
                    view: "button",
                    height: 10,
                    disabled: "true"
                },
                {
                    view: "button",
                    label: "Sort asc",
                    height: 30,
                    click: function () {
                        $$(contextmenuid).hide();
                        $$(explorertreeid).sort("#value#", "asc");
                    }
                },
                {
                    view: "button",
                    label: "Sort desc",
                    height: 30,
                    click: function () {
                        $$(contextmenuid).hide();
                        $$(explorertreeid).sort("#value#", "desc");
                    }
                },
                {
                    view: "button",
                    height: 10,
                    disabled: "true"
                },
                {
                    view: "button",
                    label: "Execute query",
                    height: 30,
                    id: contextexecutequeryid,
                    disabled: true,
                    click: function () {
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        $$(contextmenuid).hide();
                        waterfall([
                            ajax_get_first_in_async_waterfall("getqueries", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
                            function (x) {
                                if ($$('querypicker') !== undefined) {
                                    $$('querypicker').destructor();
                                }
                                webix.ui(desktop.QUERYPICKER(x, explorertreeid, selectednodeid));
                                $$('querypicker').show();
                            }
                        ]);
                    }
                },
                {
                    view: "button",
                    label: "Run chart",
                    height: 30,
                    id: contextrunchartid,
                    disabled: true,
                    click: function () {
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        $$(contextmenuid).hide();
                        falseparallel({
                            list: ajax_get_in_async_parallel("getcharts", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
                            node: ajax_get_in_async_parallel("getnode", {nodesdb: $$(explorertreeid).nodesdb, id: selectednodeid}),
                        }, function (x) {
                            if ($$('chartpicker') !== undefined) {
                                $$('chartpicker').destructor();
                            }
                            webix.ui(desktop.CHARTPICKER(x.list, explorertreeid, x.node));
                            $$('chartpicker').show();
                        });
                    }
                },
                {
                    view: "button",
                    label: "Run choice",
                    height: 30,
                    id: contextrunchoiceid,
                    disabled: true,
                    click: function () {
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        $$(contextmenuid).hide();
                        falseparallel({
                            list: ajax_get_in_async_parallel("getchoices", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
                            node: ajax_get_in_async_parallel("getnode", {nodesdb: $$(explorertreeid).nodesdb, id: selectednodeid}),
                        }, function (x) {
                            if ($$('choycepicker') !== undefined) {
                                $$('choycepicker').destructor();
                            }
                            webix.ui(desktop.CHOYCEPICKER(x.list, explorertreeid, x.node));
                            $$('choycepicker').show();
                        });
                    }
                },
                {
                    view: "button",
                    height: 10,
                    disabled: "true"
                },
                {
                    view: "button",
                    label: "Download",
                    height: 30,
                    id: contextdownloadid,
                    disabled: true,
                    click: function () {
                        $$(contextmenuid).hide();
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        window.location.href = '/downloadsource?id=' + encodeURIComponent(selectednodeid) + '&nodesdb=' + $$(explorertreeid).nodesdb;
                    }
                },
                {
                    view: "button",
                    label: "Display member",
                    height: 30,
                    id: contextdisplaymemberid,
                    disabled: true,
                    click: function () {
                        $$(contextmenuid).hide();
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        falseparallel({
                            list: ajax_get_in_async_parallel("getmemberlist", {nodesdb: $$(explorertreeid).nodesdb, id: selectednodeid}),
                            node: ajax_get_in_async_parallel("getnode", {nodesdb: $$(explorertreeid).nodesdb, id: selectednodeid}),
                        }, function (x) {
                            var choice = {
                                action: "dispmember",
                                id: "dispmember",
                                type: "choice"
                            };
                            if ($$('choicepicker') !== undefined) {
                                $$('choicepicker').destructor();
                            }
                            webix.ui(desktop.CHOICEPICKER(x.list, explorertreeid, x.node, choice));
                            $$('choicepicker').show();
                        });
                    }
                },
                {
                    view: "button",
                    label: "Unload",
                    height: 30,
                    id: contextunloadid,
                    disabled: true,
                    click: function () {
                        $$(contextmenuid).hide();
                        var selectednodeid = $$(explorertreeid).getSelectedId();
                        window.location.href = '/unload?id=' + encodeURIComponent(selectednodeid) + '&nodesdb=' + $$(explorertreeid).nodesdb + '&systemdb=' + desktop.settings.systemdb;
                    }
                },
                {
                    view: "button",
                    height: 10,
                    disabled: "true"
                },
                {
                    view: "button",
                    label: "Empty Trash",
                    height: 30,
                    click: function () {
                        $$(contextmenuid).hide();
                        waterfall([
                            ajax_get_first_in_async_waterfall("emptytrash", {nodesdb: $$(explorertreeid).nodesdb}),
                            function () {
                                refresh(explorertreeid);
                            }
                        ]);
                    }
                },
                {
                    view: "button",
                    label: "Refresh",
                    height: 30,
                    click:  function () {
                        $$(contextmenuid).hide();
                        refresh(explorertreeid);
                    }
                },
            ]
        }
    };
    webix.ui(contextmenu);
    explorerwindowsid = desktop.createwindow({title: desktop.settings.nodesdb, type: "explorer", icon: "university", body: tree, top: $$('mainarea').$height / 6, left: $$('mainarea').$width / 6, width: $$('mainarea').$width * 2 / 3, height: $$('mainarea').$height * 2 / 3});
    webix.UIManager.addHotKey("any", function (view) {
        var pos = view.getSelectedId();
        view.edit(pos);
    }, $$(explorertreeid));
    $$(explorertreeid).nodesdb = desktop.settings.nodesdb;
    $$(explorertreeid).systemdb = desktop.settings.systemdb;
    $$(explorertreeid).getpath = function (x) {
        var selectednodeid = x === undefined ? $$(explorertreeid).getSelectedId() : x;
        var selected = $$(explorertreeid).getItem(selectednodeid);
        var path = selected.value;
        var parentid = $$(explorertreeid).getParentId(selectednodeid);
        var parent = $$(explorertreeid).getItem(parentid);
        if (parent === undefined) {
            path = '/' + path;
        }
        while (parent !== undefined) {
            path = parent.value + "/" + path;
            parentid = $$(explorertreeid).getParentId(parentid);
            parent = $$(explorertreeid).getItem(parentid);
        }
        return path.substring(1);
    };
    $$(explorertreeid).sort("#value#", "asc");
    $$(explorertreeid).select(0);
    $$(contextmenuid).attachTo($$(explorertreeid));
    $$(explorerfilterid).attachEvent("onTimedKeyPress", function () {
        $$(explorertreeid).filter("#value#", this.getValue());
    });
    webix.ui({
        id: uploaderid,
        view: "uploader",
        upload: "uploadnode?nodesdb=" + $$(explorertreeid).nodesdb + "&systemdb=" + $$(explorertreeid).systemdb + "&logging=" + desktop.settings.logging,
        on: {
            onAfterFileAdd: function () {
                document.body.className = 'waiting';
            },
            onUploadComplete: function (x) {
                document.body.className = '';
                refresh(explorertreeid);
            },
            onFileUploadError: function (x, ret) {
                document.body.className = '';
                webix.message({ type: "error", text: ret.message});
            }
        },
        link: uploaderdroparea,
        apiOnly: true
    });
    $$(uploaderid).addDropZone($$(uploaderdroparea).$view);
    $$(toolbarid).potentialmenus = {};
    waterfall([
        ajax_get_first_in_async_waterfall("getmenus", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
        function (menus) {
            _.each(menus, function (menu) {
                if ($$(toolbarid).potentialmenus[menu.id] === undefined) {
                    $$(toolbarid).potentialmenus[menu.id] = menu;
                } else {
                    if (menu.origin.indexOf("kairos_system") === -1) {
                        $$(toolbarid).potentialmenus[menu.id] = menu;
                    }
                }
            });
        }
    ]);
};

var manage_iconify = function (dektop) {
    _.each(desktop.windowsproperties, function (p, wid) {
        p.visible = false;
        $$(wid).hide();
        webix.html.removeCss($$(desktop.windowsproperties[wid].iconid).getNode(), "active");
        webix.html.addCss($$(desktop.windowsproperties[wid].iconid).getNode(), "inactive");
    });
};


desktop.windows = {};
desktop.windowsproperties = {};
desktop.windowscounter = 0;

desktop.closeallwindows = function () {
    _.each(desktop.windowsproperties, function (p, wid) {
        $$(wid).close();
        $$(desktop.windowsproperties[wid].iconid).hide();
    });
    desktop.windows = {};
    desktop.windowsproperties = {};
    desktop.windowscounter = 0;
};

desktop.createwindow = function (parameters) {
    var param = {};
    param.view = "window";
    param.resize = true;
    desktop.windowscounter += 1;
    var closerid = "closer" + desktop.windowscounter;
    param.id = "w" + desktop.windowscounter;
    param.head = {};
    param.head.view = "toolbar";
    param.head.height = 34;
    param.head.cols = [];
    if (parameters.icon === undefined) {
        param.head.cols.push({view: "icon", icon: ""});
    } else {
        param.head.cols.push({view: "icon", icon: parameters.icon});
    }
    if (parameters.title === undefined) {
        param.head.cols.push({view: "label", label: "Window " + desktop.windowscounter});
    } else {
        param.head.cols.push({view: "label", label: parameters.title});
    }
    var iconifier = {
        view: "button",
        type: "icon",
        icon: "arrow-down",
        width: 30,
        click: function () {
            $$(param.id).hide();
            desktop.windowsproperties[param.id].visible = false;
            webix.html.removeCss($$(desktop.windowsproperties[param.id].iconid).getNode(), "active");
            webix.html.addCss($$(desktop.windowsproperties[param.id].iconid).getNode(), "inactive");
            _.each(desktop.windowsproperties, function (p, wid) {
                if (p.visible === true) {
                    $$(wid).show();
                }
            });
        }
    };
    var closer = {
        view: "button",
        type: "icon",
        icon: "close",
        id: closerid,
        width: 30,
        click: function () {
            if ($$(param.id).kairosg !== undefined) {
                $$(param.id).kairosg.destroy();
            }
            $$(param.id).close();
            $$(desktop.windowsproperties[param.id].iconid).hide();
            delete desktop.windows[desktop.windowsproperties[param.id].iconid];
            delete desktop.windowsproperties[param.id];
            _.each(desktop.windowsproperties, function (p, wid) {
                if (p.visible === true) {
                    $$(wid).show();
                }
            });
        }
    };
    var minimizer = {
        view: "button",
        type: "icon",
        icon: "minus",
        width: 30,
        click: function () {
            $$(param.id).setPosition(desktop.windowsproperties[param.id].left, desktop.windowsproperties[param.id].top);
            $$(param.id).config.height = desktop.windowsproperties[param.id].height;
            $$(param.id).config.width = desktop.windowsproperties[param.id].width;
            $$(param.id).resize();
            $$(param.id).show();
        }
    };
    var maximizer = {
        view: "button",
        type: "icon",
        icon: "plus",
        width: 30,
        click: function () {
            $$(param.id).setPosition(1, 1);
            $$(param.id).config.height = $$("mainarea").$height - 5;
            $$(param.id).config.width = $$("mainarea").$width - 2;
            $$(param.id).resize();
            $$(param.id).show();
        }
    };
    param.head.cols.push(iconifier);
    param.head.cols.push(closer);
    param.head.cols.push(minimizer);
    param.head.cols.push(maximizer);
    if (parameters.width !== undefined) {
        param.width = parameters.width;
    } else {
        param.width = $$("mainarea").$width / 3;
    }
    if (parameters.height !== undefined) {
        param.height = parameters.height;
    } else {
        param.height = $$("mainarea").$height / 3;
    }
    var x = (desktop.windowscounter - 1) % 9;
    var div = Math.floor(x / 3);
    var rem = x % 3;
    if (parameters.top !== undefined) {
        param.top = parameters.top;
    } else {
        param.top = div * param.height;
    }
    if (parameters.left !== undefined) {
        param.left = parameters.left;
    } else {
        param.left = rem * param.width;
    }
    param.move = true;
    param.body = {};
    if (parameters.body === undefined) {
        param.body.template = "Window content";
    } else {
        param.body = parameters.body;
    }
    var shower = {
        view: "button",
        type: "base",
        icon: param.head.cols[0].icon,
        label: param.head.cols[1].label,
        tooltip: param.head.cols[1].label,
        labelPosition: "right",
        maxWidth: 250,
        click: function () {
            $$(param.id).show();
            desktop.windowsproperties[param.id].visible = true;
            webix.html.removeCss($$(desktop.windowsproperties[param.id].iconid).getNode(), "inactive");
            webix.html.addCss($$(desktop.windowsproperties[param.id].iconid).getNode(), "active");
        }
    };

    var button = $$('windowsicons').addView(shower);
    var win = webix.ui(param);
    $$(param.id).keydown = function (keycode) {
        var attr = 'keydown_' + keycode;
        if ($$(param.id)[attr] !== undefined) {
            $$(param.id)[attr]();
        } else {
            log.debug("windows:", param.id, "keycode:", keycode);
        }
    };
    desktop.windows[button] = param.id;
    desktop.windowsproperties[param.id] = {};
    desktop.windowsproperties[param.id].type = parameters.type;
    desktop.windowsproperties[param.id].visible = true;
    desktop.windowsproperties[param.id].top = $$(param.id).config.top;
    desktop.windowsproperties[param.id].left = $$(param.id).config.left;
    desktop.windowsproperties[param.id].width = $$(param.id).config.width;
    desktop.windowsproperties[param.id].height = $$(param.id).config.height;
    desktop.windowsproperties[param.id].iconid = button;
    webix.html.addCss($$(desktop.windowsproperties[param.id].iconid).getNode(), "active");
    win.attachEvent("onViewMoveEnd", function () {
        desktop.windowsproperties[param.id].top = win.getNode().offsetTop;
        desktop.windowsproperties[param.id].left = win.getNode().offsetLeft;
    });
    win.attachEvent("onResize", function () {
        desktop.windowsproperties[param.id].width = win.getNode().offsetWidth;
        desktop.windowsproperties[param.id].height = win.getNode().offsetHeight;
        win.config.height = desktop.windowsproperties[param.id].height;
        win.config.width = desktop.windowsproperties[param.id].width;
        win.resize();
        win.show();
    });
    win.getcloser = function () {
        return $$(closerid);
    };
    setTimeout(function () {
        win.show();
    }, 50);

    return win;
};

desktop.LOGINWINDOW = function (x) {
    return {
        id: "loginwindow",
        view: "window",
        width: $$('mainarea').$width / 4,
        position: "center",
        modal: true,
        head: "Login to KAIROS Portal",
        body: {
            view: "form",
            borderless: true,
            elements: [
                {
                    view: "text",
                    label: "User",
                    name: "user",
                    id: "user",
                    suggest: getallusers(x)
                },
                {
                    view: "text",
                    label: "Password",
                    type: "password",
                    name: "password",
                    id: "password"
                },
                {
                    view: "button",
                    label: "Login",
                    icon: "sign-in",
                    id: "loginbutton",
                    type: "icon",
                    click: function () {
                        if (this.getParentView().validate()) {
                            waterfall([
                                ajax_get_first_in_async_waterfall("checkuserpassword", {password: $$('password').getValue(), user: $$('user').getValue(), logging: 'fatal'}),
                                function (x) {
                                    desktop.user = $$('user').getValue();
                                    desktop.password = $$('password').getValue();
                                    desktop.userid = x.userid;
                                    desktop.adminrights = x.adminrights;
                                    if (desktop.adminrights) {
                                        $$('startmenu').showItem("manageroles");
                                        $$('startmenu').showItem("manageusers");
                                        $$('startmenu').showItem("managegrants");
                                    } else {
                                        $$('startmenu').hideItem("manageroles");
                                        $$('startmenu').hideItem("manageusers");
                                        $$('startmenu').hideItem("managegrants");
                                    }
                                    $$('loginwindow').hide();
                                    document.title = 'KAIROS V' + VERSION + ' / ' + desktop.user;
                                    waterfall([
                                        ajax_get_first_in_async_waterfall("getsettings", {user: desktop.user}),
                                        function (y) {
                                            desktop.settings = y.settings;
                                            showbackground();
                                        }
                                    ]);
                                }
                            ]);
                        } else {
                            webix.message({ type: "error", text: "Login form data is invalid !" });
                        }
                    }
                }
            ],
            rules: {
                user: webix.rules.isNotEmpty,
                password: webix.rules.isNotEmpty
            },
            elementsConfig: {
                on: {
                    onChange: function (old_v, new_v) {
                        this.getParentView().validate();
                    }
                }
            }

        }
    };
};

desktop.PASSWORDWINDOW = function () {
    return {
        id: "passwordwindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "key"
                },
                {
                    view: "label",
                    label: "Manage password"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('passwordwindow').hide();
                    }
                }
            ]
        },
        body: {
            view: "form",
            borderless: true,
            elements: [
                {
                    view: "text",
                    labelWidth: 200,
                    label: "Actual Password",
                    type: "password",
                    name: "apassword",
                    id: "apassword"
                },
                {
                    view: "text",
                    labelWidth: 200,
                    label: "New Password",
                    type: "password",
                    name: "npassword",
                    id: "npassword"
                },
                {
                    view: "text",
                    labelWidth: 200,
                    label: "Repeat New Password",
                    type: "password",
                    name: "rpassword",
                    id: "rpassword"
                },
                {
                    view: "button",
                    value: "Set new password",
                    click: function () {
                        if (this.getParentView().validate()) {
                            if ($$('npassword').getValue() !== $$('rpassword').getValue()) {
                                webix.message({ type: "error", text: "New and repeated passwords are not identicals !" });
                                return false;
                            }
                            waterfall([
                                ajax_get_first_in_async_waterfall("changepassword", {password: $$('apassword').getValue(), new: $$('npassword').getValue(), user: desktop.user, logging: 'fatal'}),
                                function (x) {
                                    webix.message({text: x.msg});
                                    desktop.password = $$('npassword').getValue();
                                    $$('passwordwindow').hide();
                                }
                            ]);
                        } else {
                            webix.message({ type: "error", text: "Password form data is invalid !" });
                        }
                    }
                }
            ],
            rules: {
                apassword: webix.rules.isNotEmpty,
                npassword: webix.rules.isNotEmpty,
                rpassword: webix.rules.isNotEmpty
            },
            elementsConfig: {
                on: {
                    onChange: function (old_v, new_v) {
                        this.getParentView().validate();
                    }
                }
            }

        }
    };
};

desktop.CRROLEWINDOW = function () {
    return {
        id: "crrolewindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "users"
                },
                {
                    view: "label",
                    label: "Create role"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('crrolewindow').hide();
                    }
                }

            ]
        },
        body: {
            view: "form",
            borderless: true,
            elements: [
                {
                    view: "text",
                    labelWidth: 100,
                    label: "Role",
                    name: "crrole",
                    id: "crrole"
                },
                {
                    view: "button",
                    label: "Create",
                    click: function () {
                        if (this.getParentView().validate()) {
                            waterfall([
                                ajax_get_first_in_async_waterfall("createrole", {role: $$('crrole').getValue()}),
                                function (x) {
                                    $$('crrolewindow').hide();
                                    webix.message({text: x.msg});
                                    waterfall([
                                        ajax_get_first_in_async_waterfall("listroles"),
                                        function (y) {
                                            $$('rolesgrid').define({data: getallroles(y)});
                                            $$('rolesgrid').refresh();
                                            $$('roleswindow').show();
                                        }
                                    ]);
                                }
                            ]);
                        } else {
                            webix.message({ type: "error", text: "Create role form data is invalid !" });
                        }
                    }
                }
            ],
            rules: {
                crrole: webix.rules.isNotEmpty
            },
            elementsConfig: {
                on: {
                    onChange: function (old_v, new_v) {
                        this.getParentView().validate();
                    }
                }
            }

        }
    };
};

desktop.CRUSERWINDOW = function () {
    return {
        id: "cruserwindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "user"
                },
                {
                    view: "label",
                    label: "Create user"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('cruserwindow').hide();
                    }
                }

            ]
        },
        body: {
            view: "form",
            borderless: true,
            elements: [
                {
                    view: "text",
                    labelWidth: 100,
                    label: "User",
                    name: "cruser",
                    id: "cruser"
                },
                {
                    view: "button",
                    label: "Create",
                    click: function () {
                        if (this.getParentView().validate()) {
                            waterfall([
                                ajax_get_first_in_async_waterfall("createuser", {user: $$('cruser').getValue()}),
                                function (x) {
                                    $$('cruserwindow').hide();
                                    webix.message({text: x.msg});
                                    waterfall([
                                        ajax_get_first_in_async_waterfall("listusers"),
                                        function (y) {
                                            $$('usersgrid').define({data: getallusers(y)});
                                            $$('usersgrid').refresh();
                                            $$('userswindow').show();
                                        }
                                    ]);
                                }
                            ]);
                        } else {
                            webix.message({ type: "error", text: "Create user form data is invalid !" });
                        }
                    }
                }
            ],
            rules: {
                cruser: webix.rules.isNotEmpty
            },
            elementsConfig: {
                on: {
                    onChange: function (old_v, new_v) {
                        this.getParentView().validate();
                    }
                }
            }

        }
    };
};

desktop.CRGRANTWINDOW = function (x) {
    return {
        id: "crgrantwindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "book"
                },
                {
                    view: "label",
                    label: "Grant role"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('crgrantwindow').hide();
                    }
                }

            ]
        },
        body: {
            view: "form",
            borderless: true,
            elements: [
                {
                    view: "text",
                    labelWidth: 100,
                    label: "User",
                    name: "crugrant",
                    id: "crugrant",
                    suggest: getallusers(x.users)
                },
                {
                    view: "text",
                    labelWidth: 100,
                    label: "Role",
                    name: "crrgrant",
                    id: "crrgrant",
                    suggest: getallroles(x.roles)
                },
                {
                    view: "button",
                    label: "Grant",
                    click: function () {
                        if (this.getParentView().validate()) {
                            waterfall([
                                ajax_get_first_in_async_waterfall("creategrant", {user: $$('crugrant').getValue(), role: $$('crrgrant').getValue()}),
                                function (x) {
                                    $$('crgrantwindow').hide();
                                    webix.message({text: x.msg});
                                    waterfall([
                                        ajax_get_first_in_async_waterfall("listgrants"),
                                        function (y) {
                                            $$('grantsgrid').define({data: getallgrants(y)});
                                            $$('grantsgrid').refresh();
                                            $$('grantswindow').show();
                                        }
                                    ]);
                                }
                            ]);
                        } else {
                            webix.message({ type: "error", text: "Grant role form data is invalid !" });
                        }
                    }
                }
            ],
            rules: {
                crugrant: webix.rules.isNotEmpty,
                crrgrant: webix.rules.isNotEmpty
            },
            elementsConfig: {
                on: {
                    onChange: function (old_v, new_v) {
                        this.getParentView().validate();
                    }
                }
            }

        }
    };
};

desktop.DATABASESWINDOW = function () {
    return {
        id: "databaseswindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "database"
                },
                {
                    view: "label",
                    label: "Manage databases"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('databaseswindow').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "datatable",
                    height: 400,
                    id: "databasesgrid",
                    select: "row",
                    editable: true,
                    editaction: "dblclick",
                    scrollY: false,
                    scrollX: false,
                    on: {
                        onSelectChange: function () {
                            if ($$('databasesgrid').getSelectedId(true).length === 0) {
                                $$('dropdatabase').disable();
                                $$('managecontent').disable();
                            } else {
                                if (desktop.adminrights) {
                                    $$('dropdatabase').enable();
                                    $$('managecontent').enable();
                                } else {
                                    var rowselected = $$('databasesgrid').getSelectedId(true);
                                    waterfall([
                                        ajax_get_first_in_async_waterfall("listnodesdb", {user: desktop.user}),
                                        function (x) {
                                            var listdb = _.map(x, function (e) {
                                                return e.db;
                                            });
                                            if (_.contains(listdb, $$('databasesgrid').getItem(rowselected[0].id).id)) {
                                                $$('managecontent').enable();
                                            } else {
                                                $$('managecontent').disable();
                                            }
                                        }
                                    ]);
                                }
                            }
                        }
                    },
                    columns: [
                        {
                            id: "id",
                            header: [
                                "Database",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: 3
                        },
                        {
                            id: "size",
                            header: "Size on disk - GB",
                            fillspace: 1,
                            css: {'text-align': 'right'},
                            sort: "int"
                        }
                    ],
                }
            ]
        }
    };
};

desktop.OBJECTSWINDOW = function () {
    return {
        id: "objectswindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "spinner"
                },
                {
                    view: "label",
                    label: "Manage objects"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('objectswindow').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "datatable",
                    height: 400,
                    id: "objectsgrid",
                    select: "row",
                    editable: false,
                    scrollY: false,
                    scrollX: false,
                    on: {
                        onSelectChange: function () {
                            if ($$('objectsgrid').getSelectedId(true).length === 0) {
                                $$('deleteobject').disable();
                                $$('downloadobject').disable();
                            } else {
                                $$('deleteobject').enable();
                                $$('downloadobject').enable();
                            }
                        }
                    },

                    columns: [
                        {
                            id: "id",
                            header: "Id",
                            sort: "string",
                            fillspace: 1
                        },
                        {
                            id: "name",
                            header: [
                                "Object",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: 1
                        },
                        {
                            id: "type",
                            header: [
                                "Type",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: 1
                        },
                        {
                            id: "created",
                            header: "Created",
                            sort: "string",
                            fillspace: 1
                        },
                        {
                            id: "origin",
                            header: [
                                "Origin",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: 1
                        }
                    ],
                },
                {
                    type: "clear",
                    height: 30,
                    cols: [
                        {
                            view: "button",
                            value: "Upload Object",
                            disabled: false,
                            click: function () {
                                var onerror = function (x, ret) {
                                    webix.message({ type: "error", text: ret.message.message});
                                };
                                var ondone = function () {
                                    waterfall([
                                        ajax_get_first_in_async_waterfall("listobjects", {systemdb: desktop.settings.systemdb, nodesdb: desktop.settings.nodesdb}),
                                        function (x) {
                                            $$('objectsgrid').clearAll();
                                            $$('objectsgrid').define({data: getallobjects(x)});
                                            $$('objectsgrid').refresh();
                                        }
                                    ]);
                                };
                                webix.ui(desktop.UPLOADOBJECT("uploadobject?nodesdb=" + desktop.settings.nodesdb, onerror, ondone));
                                $$("uploadobject").fileDialog();
                            }
                        },
                        {
                            view: "button",
                            id: "downloadobject",
                            value: "Download Object",
                            disabled: true,
                            click: function () {
                                var rowselected = $$('objectsgrid').getSelectedId(true);
                                window.location.href = '/downloadobject?id=' + $$('objectsgrid').getItem(rowselected[0].id).name + '&type=' + $$('objectsgrid').getItem(rowselected[0].id).type + '&database=' + $$('objectsgrid').getItem(rowselected[0].id).origin;
                            }
                        },
                        {
                            view: "button",
                            value: "Delete Object",
                            id: "deleteobject",
                            disabled: true,
                            click: function () {
                                var rowselected = $$('objectsgrid').getSelectedId(true);
                                waterfall([
                                    ajax_get_first_in_async_waterfall("deleteobject", {id : $$('objectsgrid').getItem(rowselected[0].id).name, type: $$('objectsgrid').getItem(rowselected[0].id).type, database: $$('objectsgrid').getItem(rowselected[0].id).origin}),
                                    function (x) {
                                        webix.message({text: x.msg});
                                        $$('objectsgrid').remove(rowselected);
                                        $$('objectsgrid').refresh();
                                    }
                                ]);
                            }
                        }
                    ]
                }
            ]
        }
    };
};


desktop.COLLECTIONSWINDOW = function () {
    return {
        id: "collectionswindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "tags"
                },
                {
                    view: "label",
                    label: "Manage collections for database: " + desktop.manageddb
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('collectionswindow').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "datatable",
                    height: 400,
                    id: "collectionsgrid",
                    select: "row",
                    editable: true,
                    editaction: "dblclick",
                    scrollY: false,
                    scrollX: false,
                    on: {
                        onSelectChange: function () {
                            if ($$('collectionsgrid').getSelectedId(true).length === 0) {
                                $$('dropcollection').disable();
                                $$('exportcollection').disable();
                            } else {
                                $$('exportcollection').enable();
                                $$('dropcollection').enable();
                            }
                        }
                    },
                    columns: [
                        {
                            id: "id",
                            header: [
                                "Collection",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: 2
                        },
                        {
                            id: "count",
                            header: "Count",
                            sort: "int",
                            css: {'text-align': 'right'},
                            fillspace: 2
                        },
                        {
                            id: "size",
                            header: "Size",
                            sort: "int",
                            css: {'text-align': 'right'},
                            fillspace: 2
                        },
                        {
                            id: "storagesize",
                            header: "Storage Size",
                            sort: "int",
                            css: {'text-align': 'right'},
                            fillspace: 2
                        },
                        {
                            id: "numextents",
                            header: "Extents",
                            sort: "int",
                            css: {'text-align': 'right'},
                            fillspace: 1
                        },
                        {
                            id: "numindexes",
                            header: "Indexes",
                            sort: "int",
                            css: {'text-align': 'right'},
                            fillspace: 1
                        }
                    ],
                },
                {
                    type: "clear",
                    height: 30,
                    cols: [
                        {
                            view: "button",
                            value: "Import Collection",
                            id: "importcollection",
                            disabled: false,
                            click: function () {
                                var onerror = function (x, ret) {
                                    webix.message({ type: "error", text: ret.message});
                                };
                                var ondone = function () {
                                    waterfall([
                                        ajax_get_first_in_async_waterfall("listcollections", {database: desktop.manageddb}),
                                        function (x) {
                                            $$('collectionsgrid').clearAll();
                                            $$('collectionsgrid').define({data: getallcollections(x)});
                                            $$('collectionsgrid').refresh();
                                        }
                                    ]);
                                };
                                webix.ui(desktop.UPLOADOBJECT("importcollection?database=" + desktop.manageddb, onerror, ondone));
                                $$("uploadobject").fileDialog();
                                return null;
                            }
                        },
                        {
                            view: "button",
                            value: "Export Collection",
                            id: "exportcollection",
                            disabled: true,
                            click: function () {
                                var rowselected = $$('collectionsgrid').getSelectedId(true);
                                window.location.href = '/exportcollection?database=' + desktop.manageddb + '&collection=' + $$('collectionsgrid').getItem(rowselected[0].id).id;
                            }
                        },
                        {
                            view: "button",
                            value: "Drop Collection",
                            id: "dropcollection",
                            disabled: true,
                            click: function () {
                                var rowselected = $$('collectionsgrid').getSelectedId(true);
                                waterfall([
                                    ajax_get_first_in_async_waterfall("dropcollection", {database: desktop.manageddb, collection : $$('collectionsgrid').getItem(rowselected[0].id).id}),
                                    function (x) {
                                        webix.message({text: x.msg});
                                        $$('collectionsgrid').remove(rowselected);
                                        $$('collectionsgrid').refresh();
                                    }
                                ]);
                            }
                        }
                    ]
                }
            ]
        }
    };
};

desktop.ROLESWINDOW = function () {
    return {
        id: "roleswindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "users"
                },
                {
                    view: "label",
                    label: "Manage roles"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('roleswindow').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "datatable",
                    height: 400,
                    id: "rolesgrid",
                    select: "row",
                    editable: true,
                    editaction: "dblclick",
                    scrollY: false,
                    scrollX: false,
                    on: {
                        onSelectChange: function () {
                            if ($$('rolesgrid').getSelectedId(true).length === 0) {
                                $$('deleterole').disable();
                            } else {
                                $$('deleterole').enable();
                            }
                        }
                    },
                    columns: [
                        {
                            id: "id",
                            header: "Rid",
                            sort: "string",
                            width: 250
                        },
                        {
                            id: "value",
                            header: [
                                "Role",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: true
                        }
                    ],
                },
                {
                    type: "clear",
                    height: 30,
                    cols: [
                        {
                            view: "button",
                            value: "Create Role",
                            click: function () {
                                if ($$('crrolewindow') !== undefined) {
                                    $$('crrolewindow').destructor();
                                }
                                webix.ui(desktop.CRROLEWINDOW());
                                $$('crrolewindow').show();
                                $$('crrole').focus();
                            }
                        },
                        {
                            view: "button",
                            value: "Delete Role",
                            id: "deleterole",
                            disabled: true,
                            click: function () {
                                var rowselected = $$('rolesgrid').getSelectedId(true);
                                waterfall([
                                    ajax_get_first_in_async_waterfall("deleterole", {role : $$('rolesgrid').getItem(rowselected[0].id).value}),
                                    function (x) {
                                        webix.message({text: x.msg});
                                        $$('rolesgrid').remove(rowselected);
                                        $$('rolesgrid').refresh();
                                    }
                                ]);
                            }
                        }
                    ]
                }
            ]
        }
    };
};

desktop.USERSWINDOW = function () {
    return {
        id: "userswindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "user"
                },
                {
                    view: "label",
                    label: "Manage users"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('userswindow').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "datatable",
                    height: 400,
                    id: "usersgrid",
                    select: "row",
                    editable: true,
                    editaction: "dblclick",
                    scrollY: false,
                    scrollX: false,
                    on: {
                        onSelectChange: function () {
                            if ($$('usersgrid').getSelectedId(true).length === 0) {
                                $$('deleteuser').disable();
                            } else {
                                $$('deleteuser').enable();
                            }
                        }
                    },
                    columns: [
                        {
                            id: "id",
                            header: "Uid",
                            sort: "string",
                            width: 250
                        },
                        {
                            id: "value",
                            header: [
                                "User",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: true

                        }
                    ],
                },
                {
                    type: "clear",
                    height: 30,
                    cols: [
                        {
                            view: "button",
                            value: "Create User",
                            click: function () {
                                if ($$('cruserwindow') !== undefined) {
                                    $$('cruserwindow').destructor();
                                }
                                webix.ui(desktop.CRUSERWINDOW());
                                $$('cruserwindow').show();
                                $$('cruser').focus();
                            }
                        },
                        {
                            view: "button",
                            value: "Delete User",
                            id: "deleteuser",
                            disabled: true,
                            click: function () {
                                var rowselected = $$('usersgrid').getSelectedId(true);
                                waterfall([
                                    ajax_get_first_in_async_waterfall("deleteuser", {user : $$('usersgrid').getItem(rowselected[0].id).value}),
                                    function (x) {
                                        webix.message({text: x.msg});
                                        $$('usersgrid').remove(rowselected);
                                        $$('usersgrid').refresh();
                                    }
                                ]);
                            }
                        }
                    ]
                }
            ]
        }
    };
};

desktop.GRANTSWINDOW = function () {
    return {
        id: "grantswindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "book"
                },
                {
                    view: "label",
                    label: "Manage grants"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('grantswindow').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "datatable",
                    height: 400,
                    id: "grantsgrid",
                    select: "row",
                    editable: true,
                    editaction: "dblclick",
                    scrollY: false,
                    scrollX: false,
                    on: {
                        onSelectChange: function () {
                            if ($$('grantsgrid').getSelectedId(true).length === 0) {
                                $$('revokerole').disable();
                            } else {
                                $$('revokerole').enable();
                            }
                        }
                    },
                    columns: [
                        {
                            id: "id",
                            header: "Gid",
                            sort: "string",
                            width: 250
                        },
                        {
                            id: "user",
                            header: [
                                "User",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: true
                        },
                        {
                            id: "role",
                            header: [
                                "Role",
                                {
                                    content: "textFilter"
                                }
                            ],
                            sort: "string",
                            fillspace: true
                        }
                    ]
                },
                {
                    type: "clear",
                    height: 30,
                    cols: [
                        {
                            view: "button",
                            value: "Grant Role",
                            click: function () {
                                if ($$('crgrantwindow') !== undefined) {
                                    $$('crgrantwindow').destructor();
                                }
                                falseparallel({
                                    roles: ajax_get_in_async_parallel("listroles"),
                                    users: ajax_get_in_async_parallel("listusers")
                                }, function (x) {
                                    webix.ui(desktop.CRGRANTWINDOW(x));
                                    $$('crgrantwindow').show();
                                    $$('crugrant').focus();
                                });
                            }
                        },
                        {
                            view: "button",
                            value: "Revoke Role",
                            id: "revokerole",
                            disabled: true,
                            click: function () {
                                var rowselected = $$('grantsgrid').getSelectedId(true);
                                waterfall([
                                    ajax_get_first_in_async_waterfall("deletegrant", {user : $$('grantsgrid').getItem(rowselected[0].id).user, role: $$('grantsgrid').getItem(rowselected[0].id).role}),
                                    function (x) {
                                        webix.message({text: x.msg});
                                        $$('grantsgrid').remove(rowselected);
                                        $$('grantsgrid').refresh();
                                    }
                                ]);
                            }
                        }
                    ]
                }
            ]
        }
    };
};

desktop.UPLOADOBJECT = function (url, err, done) {
    return {
        id: "uploadobject",
        view: "uploader",
        upload: url,
        on: {
            onAfterFileAdd: function () {
                document.body.className = 'waiting';
            },
            onUploadComplete: done,
            onFileUploadError: err
        }
    };
};

desktop.QUERYPICKER = function (x, explorer, nodeid) {
    return {
        id: "querypicker",
        view: "window",
        width: $$('mainarea').$width / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "question"
                },
                {
                    view: "label",
                    label: "Query picker"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('querypicker').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "select",
                    id: "querypickerout",
                    options: getallqueries(x)
                },
                {
                    view: "button",
                    value: "Execute",
                    click: function () {
                        $$('querypicker').hide();
                        manage_table(desktop, explorer, nodeid, $$('querypickerout').getValue());
                    }
                }
            ]
        }
    };
};

desktop.CHARTPICKER = function (x, explorer, node) {
    return {
        id: "chartpicker",
        view: "window",
        width: $$('mainarea').$width / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "question"
                },
                {
                    view: "label",
                    label: "Chart picker"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('chartpicker').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "select",
                    id: "chartpickerout",
                    options: getallcharts(x)
                },
                {
                    view: "button",
                    value: "Execute",
                    click: function () {
                        $$('chartpicker').hide();
                        var chart = $$('chartpickerout').getValue();
                        dispchart(explorer, node, chart);
                    }
                }
            ]
        }
    };
};

desktop.CHOYCEPICKER = function (x, explorer, node) {
    return {
        id: "choycepicker",
        view: "window",
        width: $$('mainarea').$width / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "question"
                },
                {
                    view: "label",
                    label: "Choice picker"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('choycepicker').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "select",
                    id: "choycepickerout",
                    options: getallchoyces(x)
                },
                {
                    view: "button",
                    value: "Execute",
                    click: function () {
                        $$('choycepicker').hide();
                        var choice = $$('choycepickerout').getValue();
                        dispchoice(explorer, node, choice);
                    }
                }
            ]
        }
    };
};

desktop.CHOICEPICKER = function (x, explorer, node, choice) {
    return {
        id: "choicepicker",
        view: "window",
        width: $$('mainarea').$width / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "question"
                },
                {
                    view: "label",
                    label: "Choice picker"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('choicepicker').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "select",
                    id: "choicepickerout",
                    options: getallchoices(x, node.datasource.type)
                },
                {
                    view: "button",
                    value: "Execute",
                    click: function () {
                        $$('choicepicker').hide();
                        desktop.variables[choice.id] = $$('choicepickerout').getValue();
                        if (choice.action === 'dispchart') {
                            dispchart(explorer, node, choice.chart);
                        }
                        if (choice.action === 'dispchoice') {
                            dispchoice(explorer, node, choice.choice);
                        }
                        if (choice.action === 'dispmember') {
                            dispmember(explorer, node, desktop.variables[choice.id]);
                        }
                    }
                }
            ]
        }
    };
};

desktop.SETTINGSWINDOW = function (x) {
    return {
        id: "settingswindow",
        view: "window",
        width: $$('mainarea').$width * 2 / 3,
        position: "center",
        modal: true,
        head: {
            view: "toolbar",
            cols: [
                {
                    view: "icon",
                    icon: "cog"
                },
                {
                    view: "label",
                    label: "Settings"
                },
                {
                    view: "icon",
                    icon: "close",
                    click: function () {
                        $$('settingswindow').hide();
                    }
                }

            ]
        },
        body: {
            type: "clear",
            rows: [
                {
                    view: "select",
                    label: "System database",
                    name: "systemdb",
                    id: "systemdb",
                    labelWidth: 300,
                    labelAlign: "right",
                    value: desktop.settings.systemdb,
                    options: getallsystemdb(x.systemdb)
                },
                {
                    view: "select",
                    label: "Nodes database",
                    name: "nodesdb",
                    id: "nodesdb",
                    labelWidth: 300,
                    labelAlign: "right",
                    value: desktop.settings.nodesdb,
                    options: getallnodesdb(x.nodesdb)
                },
                {
                    view: "counter",
                    label: "Log lines to display",
                    name: "loglines",
                    id: "loglines",
                    labelWidth: 300,
                    labelAlign: "right",
                    step: 50,
                    min: 100,
                    value: desktop.settings.loglines,
                },
                {
                    view: "select",
                    label: "Charts template",
                    name: "template",
                    id: "template",
                    labelWidth: 300,
                    labelAlign: "right",
                    value: desktop.settings.template,
                    options: getalltemplates(x.templates)
                },
                {
                    view: "select",
                    label: "Colors definition",
                    name: "colors",
                    id: "colors",
                    labelWidth: 300,
                    labelAlign: "right",
                    value: desktop.settings.colors,
                    options: getallcolors(x.colors)
                },
                {
                    view: "select",
                    label: "Wallpaper",
                    name: "wallpaper",
                    id: "wallpaper",
                    labelWidth: 300,
                    labelAlign: "right",
                    value: desktop.settings.wallpaper,
                    options: getallwallpapers(x.wallpapers)
                },
                {
                    view: "counter",
                    label: "Request labels limit",
                    name: "top",
                    id: "top",
                    labelWidth: 300,
                    labelAlign: "right",
                    step: 1,
                    min: 0,
                    max: 100,
                    value: desktop.settings.top,
                },
                {
                    view: "counter",
                    label: "Keyboard main function code",
                    name: "keycode",
                    id: "keycode",
                    labelWidth: 300,
                    labelAlign: "right",
                    step: 1,
                    min: 0,
                    max: 255,
                    value: desktop.settings.keycode,
                },
                {
                    view: "select",
                    label: "Plot Orientation",
                    name: "plotorientation",
                    id: "plotorientation",
                    labelWidth: 300,
                    labelAlign: "right",
                    value: desktop.settings.plotorientation,
                    options: [
                        {id: "horizontal", value: "horizontal"},
                        {id: "vertical", value: "vertical"},
                    ]
                },
                {
                    view: "select",
                    label: "Logging",
                    name: "logging",
                    id: "logging",
                    labelWidth: 300,
                    labelAlign: "right",
                    value: desktop.settings.logging,
                    options: [
                        {id: "off", value: "off"},
                        {id: "fatal", value: "fatal"},
                        {id: "error", value: "error"},
                        {id: "warn", value: "warn"},
                        {id: "info", value: "info"},
                        {id: "debug", value: "debug"},
                        {id: "trace", value: "trace"},
                        {id: "all", value: "all"},
                    ]
                },
                {
                    view: "button",
                    value: "Update settings",
                    id: "updatesettings",
                    click: function () {
                        waterfall([
                            ajax_get_first_in_async_waterfall("updatesettings", {user: desktop.user, systemdb: $$('systemdb').getValue(), nodesdb: $$('nodesdb').getValue(), loglines: $$('loglines').getValue(), template: $$('template').getValue(), colors: $$('colors').getValue(), wallpaper: $$('wallpaper').getValue(), top: $$('top').getValue(), keycode: $$('keycode').getValue(), plotorientation: $$('plotorientation').getValue(), logging: $$('logging').getValue()}),
                            function (x) {
                                waterfall([
                                    ajax_get_first_in_async_waterfall("getsettings", {user: desktop.user}),
                                    function (y) {
                                        desktop.settings = y.settings;
                                        showbackground();
                                        $$('settingswindow').hide();
                                    }
                                ]);
                            }
                        ]);
                    }
                }
            ]
        }
    };
};


desktop.MAINWINDOW = function () {
    return {
        view: "window",
        id: "mainwindow",
        fullscreen: true,
        head: false,
        body: {
            rows: [
                {
                    id: "mainarea",
                    template: function (obj) {
                        return '<canvas id="maincanvas" style="margin-left:-5px;margin-top:-5px"/></canvas>';
                    }
                },
                {
                    view: "toolbar",
                    id: "windowsicons",
                    css: "xtoolbar",
                    height: 34,
                    paddingY: 0,
                    cols : [
                        {
                            id: "kairosbutton",
                            view: "button",
//                            type: "imageButton",
//                            image: "resources/kairos.gif",
                            type: "icon",
                            icon: "home",
                            label: "KAIROS",
                            width: 100,
                            click: function () {
                                $$('startmenu').config.top = $$('mainarea').$height - $$('startmenu').$height - 3;
                                $$('startmenu').config.left = 3;
                                $$('startmenu').refresh();
                                $$('startmenu').show();
                            }
                        },
                        {
                            id: "mainsettings",
                            view: "button",
                            type: "icon",
                            width: 30,
                            icon: "cog",
                            click: function () {
                                manage_settings(desktop);
                            }
                        },
                        {
                            id: "mainexplorer",
                            view: "button",
                            type: "icon",
                            width: 30,
                            icon: "university",
                            click: function () {
                                manage_explorer(desktop);
                            }
                        },
                        {
                            id: "mainiconifier",
                            view: "button",
                            type: "icon",
                            width: 30,
                            icon: "arrow-down",
                            click: function () {
                                manage_iconify(desktop);
                            }
                        },
                        {
                            id: "maincloser",
                            view: "button",
                            type: "icon",
                            width: 30,
                            icon: "close",
                            click: desktop.closeallwindows
                        }
                    ]
                }
            ]
        }
    };
};

desktop.MAINMENU = function () {
    return {
        id: "startmenu",
        view: "contextmenu",
        width: 230,
        data: [
            {
                view: "button",
                type: "icon",
                icon: "newspaper-o",
                value: "KAIROS log",
            },
            {
                view: "button",
                type: "icon",
                icon: "newspaper-o",
                value: "ORIENTDB errfile",
            },
            {
                view: "button",
                type: "icon",
                icon: "file-pdf-o",
                value: "KAIROS documentation",
            },
            {
                $template: "Separator"
            },
            {
                view: "button",
                type: "icon",
                icon: "university",
                value: "Explorer"
            },
            {
                $template: "Separator"
            },
            {
                view: "button",
                id: "manageobjects",
                type: "icon",
                icon: "spinner",
                value: "Manage objects"
            },
            {
                $template: "Separator"
            },
            {
                view: "button",
                id: "listdatabases",
                type: "icon",
                icon: "database",
                value: "List databases"
            },
            {
                view: "button",
                id: "manageroles",
                type: "icon",
                icon: "users",
                value: "Manage roles"
            },
            {
                view: "button",
                id: "manageusers",
                type: "icon",
                icon: "user",
                value: "Manage users"
            },
            {
                view: "button",
                id: "managegrants",
                type: "icon",
                icon: "book",
                value: "Manage grants"
            },
            {
                view: "button",
                type: "icon",
                icon: "key",
                value: "Manage password"
            },
            {
                $template: "Separator"
            },
            {
                view: "button",
                type: "icon",
                icon: "cog",
                value: "Settings"
            },
            {
                $template: "Separator"
            },
            {
                view: "button",
                type: "icon",
                icon: "sign-out",
                value: "Logout",
            }
        ],
        on: {
            onMenuItemClick: function (id) {
                var me = this;
                var itemvalue = me.getMenuItem(id).value;
		var wsprotocol = location.protocol === 'https:' ? 'wss' : 'ws';
		var prefix = wsprotocol + "://" + location.host;

                if (itemvalue === 'KAIROS log') {
                    manage_log(desktop, prefix + "/get_kairos_log", "KAIROS log", "/var/log/kairos/kairos.log");
                }
                if (itemvalue === 'ORIENTDB errfile') {
                    manage_log(desktop, prefix + "/get_orientdb_errfile", "ORIENTDB errfile", "/orientdb/log/orientdb.err");
                }
                if (itemvalue === 'KAIROS documentation') {
                    manage_kairos_documentation(desktop);
                }
                if (itemvalue === 'Explorer') {
                    manage_explorer(desktop);
                }
                if (itemvalue === 'Manage objects') {
                    manage_objects(desktop);
                }
                if (itemvalue === 'List databases') {
                    list_databases(desktop);
                }
                if (itemvalue === 'Manage roles') {
                    manage_roles(desktop);
                }
                if (itemvalue === 'Manage users') {
                    manage_users(desktop);
                }
                if (itemvalue === 'Manage grants') {
                    manage_grants(desktop);
                }
                if (itemvalue === 'Manage password') {
                    manage_password(desktop);
                }
                if (itemvalue === 'Settings') {
                    manage_settings(desktop);
                }
                if (itemvalue === 'Logout') {
                    logout(desktop);
                }
            }
        }
    };
};

webix.protoUI({name: "edittree"}, webix.EditAbility, webix.ui.tree);
webix.ui(desktop.MAINMENU());
webix.ui(desktop.MAINWINDOW());

d3.select("body")
    .on("keydown", function () {
        var windowsid;
        var zindex;
        desktop.lastkeycode = d3.event.keyCode;
        if (desktop.user !== undefined) {
            log.debug("Last key code:", d3.event.keyCode);
        }
        if (desktop.keyfunc === "C") {
            _.each(desktop.windowsproperties, function (p, wid) {
                if (p.type === 'chart') {
                    var x = d3.select("[view_id=" + wid + "]").style("z-index");
                    if (windowsid === undefined) {
                        windowsid = wid;
                        zindex = x;
                    } else {
                        if (x > zindex) {
                            windowsid = wid;
                            zindex = x;
                        }
                    }
                }
            });
            if (windowsid !== undefined) {
                $$(windowsid).kairosg.keydown(d3.event.keyCode);
            }
            delete desktop.keyfunc;
        }
        if (desktop.keyfunc === "D") {
            desktop.keydown(d3.event.keyCode);
            delete desktop.keyfunc;
        }
        if (desktop.keyfunc === "E") {
            _.each(desktop.windowsproperties, function (p, wid) {
                if (p.type === 'explorer') {
                    var x = d3.select("[view_id=" + wid + "]").style("z-index");
                    if (windowsid === undefined) {
                        windowsid = wid;
                        zindex = x;
                    } else {
                        if (x > zindex) {
                            windowsid = wid;
                            zindex = x;
                        }
                    }
                }
            });
            if (windowsid !== undefined) {
                $$(windowsid).keydown(d3.event.keyCode);
            }
            delete desktop.keyfunc;
        }
        if (desktop.settings === undefined) {
            desktop.settings = {};
            desktop.settings.keycode = "192";
        }
        if (d3.event.keyCode === parseInt(desktop.settings.keycode, 10)) {
            desktop.keyfunc = "KEYF";
        }
        if (d3.event.keyCode === 67 && desktop.keyfunc === "KEYF") {
            desktop.keyfunc = "C";
        }
        if (d3.event.keyCode === 68 && desktop.keyfunc === "KEYF") {
            desktop.keyfunc = "D";
        }
        if (d3.event.keyCode === 69 && desktop.keyfunc === "KEYF") {
            desktop.keyfunc = "E";
        }
    });

desktop.keydown = function (keycode) {
    if (desktop.settings !== undefined) {
        if (keycode === 35) { // End
            logout(desktop);
        }
        if (keycode === 40) { // Down
            manage_iconify(desktop);
        }
        if (keycode === 68) { // d
            list_databases(desktop);
        }
        if (keycode === 69) { // e
            manage_explorer(desktop);
        }
        if (keycode === 72) { // h
            manage_kairos_documentation(desktop);
        }
        if (keycode === 76) { // l
            manage_kairos_log(desktop);
        }
        if (keycode === 79) { // o
            manage_objects(desktop);
        }
        if (keycode === 80) { // p
            manage_password(desktop);
        }
        if (keycode === 83) { // s
            manage_settings(desktop);
        }
        if (keycode === 88) { // x
            desktop.closeallwindows();
        }
    }
};
waterfall([
    ajax_get_first_in_async_waterfall("checkserverconfig"),
    ajax_get_next_in_async_waterfall("listusers"),
    function (x) {
        webix.ui(desktop.LOGINWINDOW(x));
        document.title = "KAIROS V" + VERSION;
        $$('mainwindow').show();
        showbackground();
        $$('loginwindow').show();
        $$('user').focus();
    }
]);
