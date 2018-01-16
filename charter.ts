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
"use strict";

interface Event {
    wheelDelta: number;
}

interface Math {
    log10(x: number): number;
}

interface String {
    lpad(x: string, l: number): string;
}

interface Window {
    clientHeight: number;
    clientWidth: number;
}

module KairosCharter {

    var _, d3, CryptoJS, d3pie, paper, log4javascript; // to be removed after tsco
    let log = log4javascript.getLogger('CHARTER');
    let appender = new log4javascript.BrowserConsoleAppender();
    let popUpLayout = new log4javascript.PatternLayout("%d{HH:mm:ss.SSS} %-5p %-7c - %m%n");
    appender.setLayout(popUpLayout);
    log.addAppender(appender);
    let loglevel = log4javascript.Level.ALL;
    log.setLevel(loglevel);
 
    interface KaBound {
        bmin: number;
        dataset: KaDataset;
        legend: KaLegend;
        legendname: string;
        plot: KaPlot;
        plotname: string;
        renderer: KaRenderer;
        xaxis: KaXaxis;
        xaxisname: string;
        yaxis: KaYaxis;
        yaxisname: string;
        fx(x: number): number;
        fy(x: number): number;
    }

    interface KaBoundDataset {
        datasets: any[];
        getRefTime(): any;
        getVMinVMax(options: any): any;
        pop(bid: string): void;
        push(dataset: KaDataset, bid: string, stacked: boolean): void;
    }

    interface KaChart {
        charttemplate: KaChartTemplate;
        bind (bid: string, dataset: KaDataset, pid: string, renderer: KaRenderer, xid: string, yid: string, lid: string);
        bindLegend (lid: string) : KaLegend;
        bindPlot (pid : string) : KaPlot;
        bindTitle (tid: string, title: string, properties?: any) : KaTitle;
        bindXaxis (xid: string, title: string, scaling: string, properties?: any) : KaXaxis;
        bindYaxis (yid: string, title: string, position: string, scaling: string, properties?: any, minvalue?: number, maxvalue?: number) : KaYaxis;
        draw(attach?: string): void;
        finalize(): void;
        getBind(bid: string): KaBound;
        getHeight(): number;
        getLegend(lid: string): KaLegend;
        getChartTemplate(): KaChartTemplate;
        getPlot(pid: string): KaPlot;
        getWidth(): number;
        getXaxis(xid: string): KaXaxis;
        getYaxis(yid: string): KaYaxis;
    }

    interface KaDataset {
        base: KaMatrix;
        color: any;
        data: KaMatrix;
        info: any;
        labels: string[];
        hidden: boolean[];
        onclick: any;
        reftime: KaRefTime;
        finalize(): void;
        flipflop(p: number): boolean;
        getAngles(pid: number): number[];
        getOrderedPaths(): number[];
    }

    interface KaLegend {
        bounddataset: KaBoundDataset;
    }

    interface KaChartTemplate {
        objects: any;
        getObject(moid: string): any;
        jsonify(): string;
        setColumn(mcoptions : any): any;
        setLine(mloptions : any): any;
        setObject(moid: string, mooptions: any): any;
    }

    interface KaMatrix {
        nc : number;
        nl: number;
        add(m: KaMatrix): KaMatrix;
        each(f: any): void;
        getValue(i: number, j: number): number;
        multiply(m: KaMatrix): KaMatrix;
        reduce (ic: number[], callee: any): KaMatrix;
        setValue(i: number, j: number, v: number): void;
        sort(f: any): any;
        transpose(): KaMatrix;
    }

    interface KaPlot {
        angleslice: number;
        axisgrid: any;
        bounddataset: KaBoundDataset;
        height: number;
        numylabels: number;
        oneplot: string;
        radar: any;
        radarline: any;
        radius: number;
        raxis: any;
        rscale: any;
        width: number;
        ylabels: number[];
    }

    interface KaPoint {
        hidden: boolean;
        id: string;
        value: number;
        leftNeighbour: KaPoint;
        rightNeighbour: KaPoint;
    }

   interface KaRefTime {
           timestamps: KaMatrix;
           finalize(): void;
   }

    interface KaRenderer {
        type: string;
    }

    interface KaTitle {
        title: string;
        properties: any;
    }

    interface KaXaxis {
        bounddataset: KaBoundDataset;
        oneplot: string;
        properties: any;
        reftime: KaRefTime;
        scaling: string;
        translation: number;
        type: string;
        zoom: number;
        fctv(): number[];
        fx(x: number): number;
        panzoom(reftime: KaRefTime, maxticks: number, width: number, borderpercent: number, translation: number, zoom: number): any;
        rfx(x: number): number;
    }

    interface KaYaxis {
        bmin: number;
        bmax: number;
        bounddataset: KaBoundDataset;
        minvalue: number;
        maxvalue: number;
        numticks: number;
        oneplot: string;
        position: string;
        properties: any;
        scaling: string;
        type: string;
        title: string;
        step: number;
        fy(x: number): number;
        fctv(): number[];
    }

    String.prototype.lpad = function (padString, length) {
        var str = this;
        while (str.length < length) {
            str = padString + str;
        }
        return str;
    };


    function nicedate (mindate: any, maxdate: any, maxticks: number) : any {
        let weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
        let monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        let ticks = [];
        let niceticks = [];
        let step = (maxdate - mindate) / (maxticks - 1);
        let nicestep = step > 1 ? 2 : 1;    // milliseconds
        nicestep = step > 2 ? 5 : nicestep;
        nicestep = step > 5 ? 10 : nicestep;
        nicestep = step > 10 ? 20 : nicestep;
        nicestep = step > 20 ? 50 : nicestep;
        nicestep = step > 50 ? 100 : nicestep;
        nicestep = step > 100 ? 200 : nicestep;
        nicestep = step > 200 ? 500 : nicestep;
        nicestep = step > 500 ? 1000 : nicestep;
        nicestep = step > 1000 ? 5000 : nicestep; // seconds
        nicestep = step > 5000 ? 10000 : nicestep;
        nicestep = step > 10000 ? 15000 : nicestep;
        nicestep = step > 15000 ? 30000 : nicestep;
        nicestep = step > 30000 ? 60000 : nicestep;
        nicestep = step > 60000 ? 300000 : nicestep; // minutes
        nicestep = step > 300000 ? 600000 : nicestep;
        nicestep = step > 600000 ? 900000 : nicestep;
        nicestep = step > 900000 ? 1800000 : nicestep;
        nicestep = step > 1800000 ? 3600000 : nicestep;
        nicestep = step > 3600000 ? 10800000 : nicestep; // hours
        nicestep = step > 10800000 ? 21600000 : nicestep;
        nicestep = step > 21600000 ? 43200000 : nicestep;
        nicestep = step > 43200000 ? 86400000 : nicestep;
        nicestep = step > 86400000 ? 604800000 : nicestep;  // days
        nicestep = step > 604800000 ? 2419200000 : nicestep;  // weeks
        nicestep = step > 2419200000 ? 29030400000 : nicestep;  // months
        if (mindate === Infinity) {
            mindate = new Date();
            maxdate = mindate;
        }
        mindate = new Date(mindate);
        maxdate = new Date(maxdate);
        let nicems = nicestep >= 1000 ? 0 : Math.floor(mindate.getMilliseconds() / 100) * 100;
        nicems = nicestep < 100 && nicestep >= 10 ? Math.floor(mindate.getMilliseconds() / 10) * 10 : nicems;
        nicems = nicestep < 10 ? mindate.getMilliseconds() : nicems;
        let nicesecond = nicestep >= 60000 ? 0 : Math.floor(mindate.getSeconds() / 10) * 10;
        nicesecond = nicestep < 10000 ? mindate.getSeconds() : nicesecond;
        let niceminute = nicestep >= 3600000 ? 0 : Math.floor(mindate.getMinutes() / 10) * 10;
        niceminute = nicestep < 600000 ? mindate.getMinutes() : niceminute;
        let nicehour = nicestep >= 86400000 ? 0 : mindate.getUTCHours();
        let niceday = nicestep >= 2419200000 ? 1 : mindate.getUTCDate();
        let nicemonth = nicestep >= 29030400000 ? 0 : mindate.getUTCMonth();
        let niceyear = mindate.getUTCFullYear();

        let nicemin = new Date(Date.UTC(niceyear, nicemonth, niceday, nicehour, niceminute, nicesecond, nicems));
        ticks.push(nicemin);
        _.each(_.range(1, maxticks * 2), function(x) {
            let curelem;
            let before;
            if (nicestep < 2419200000) {
                curelem = new Date(nicemin.getTime() + nicestep * x);
                before = new Date(nicemin.getTime() + nicestep * (x - 1));
            }
            if (nicestep < 29030400000 && nicestep >= 2419200000) {
                curelem = new Date(Date.UTC(niceyear, nicemonth + x, niceday, nicehour, niceminute, nicesecond, nicems));
                before = new Date(Date.UTC(niceyear, nicemonth + x - 1, niceday, nicehour, niceminute, nicesecond, nicems));
            }
            if (nicestep >= 29030400000) {
                curelem = new Date(Date.UTC(niceyear + x, nicemonth, niceday, nicehour, niceminute, nicesecond, nicems));
                before = new Date(Date.UTC(niceyear + x - 1, nicemonth, niceday, nicehour, niceminute, nicesecond, nicems));
            }
            if (before < maxdate) {
                ticks.push(curelem);
            }
        });
        _.each(ticks, function(x) {
            if (x.getMilliseconds() !== 0) {
                niceticks.push({ tick: x, label: '.' + x.getMilliseconds().toString().lpad("0", 3) });
            }
            else if (x.getSeconds() !== 0) {
                niceticks.push({ tick: x, label: ':' + x.getSeconds().toString().lpad("0", 2) });
            }
            else if (x.getMinutes() !== 0) {
                niceticks.push({ tick: x, label: x.getUTCHours().toString().lpad("0", 2) + ':' + x.getMinutes().toString().lpad("0", 2) });
            }
            else if (x.getUTCHours() !== 0) {
                niceticks.push({ tick: x, label: x.getUTCHours().toString().lpad("0", 2) + ':00' });
            }
            else if (x.getUTCDate() !== 1) {
                niceticks.push({ tick: x, label: weekday[x.getDay()] + ' ' + x.getUTCDate().toString().lpad("0", 2) });
            }
            else if (x.getUTCMonth() !== 0) {
                niceticks.push({ tick: x, label: monthname[x.getUTCMonth()] });
            }
            else {
                niceticks.push({ tick: x, label: x.getUTCFullYear().toString() });
            }
        });
        let r = { nicemin: nicemin, nicemax: _.last(niceticks).tick, niceticks: niceticks.length, ticks: niceticks };
        return r;
    }

    function nicenum(minv: number, maxv: number, maxticks: number): any {
        let step = (maxv - minv) / (maxticks - 1);
        let exponent = Math.floor(Math.log10(step));
        let fraction = step / Math.pow(10, exponent);
        let nicefraction = fraction > 1 ? 2 : 1;
        nicefraction = fraction > 2 ? 5 : nicefraction;
        nicefraction = fraction > 5 ? 10 : nicefraction;
        let nicestep = nicefraction * Math.pow(10, exponent);
        let nmin = Math.floor(minv / nicestep) * nicestep;
        let nmax = Math.ceil(maxv / nicestep) * nicestep;
        let niceticks = ((nmax - nmin) / nicestep) + 1;
        return { nicemin: nmin, nicemax: nmax, nicestep: nicestep, niceticks: niceticks };
    }

    function parsecolor (color: any, container?: any) : any {
        return typeof color === 'object' ? new paper.Color({stops: color.stops, origin: new paper.Point(container.xs(), container.ys()), destination: new paper.Point(container.xs(), container.ye())}): color; 
    }

    function postpone (n: number, f: any) : void {
        setTimeout(f, n);
    }

    class Bound implements KaBound {

        private id: string;

        public bmin: number;
        public dataset: KaDataset;
        public legend: KaLegend;
        public legendname: string;
        public plot: KaPlot;
        public plotname: string;
        public renderer: KaRenderer;
        public xaxis: KaXaxis;
        public xaxisname: string;
        public yaxis: KaYaxis;
        public yaxisname: string;


        constructor (chart: KaChart, bid: string, dataset: KaDataset, pid: string, renderer: KaRenderer, xid: string, yid: string, lid: string) {
            let me = this;
            me.id = bid;
            me.dataset = dataset;
            me.plot = chart.getPlot(pid);
            me.plotname = pid;
            me.renderer = renderer;
            me.xaxis = chart.getXaxis(xid);
            me.xaxisname = xid;
            me.yaxis = chart.getYaxis(yid);
            me.yaxisname = yid;
            me.legend = chart.getLegend(lid);
            me.legendname = lid;
        }

        public fx (x: any) : number {
            return 0;
        }

        public fy (x: any) : number {
            return 0;
        }

    }

    class BoundDataset implements KaBoundDataset {

        public datasets: any[];

        constructor (datasets: KaDataset[]) {
            let me = this;
            me.datasets = [];
            _.each(datasets, function (d) {
                me.push(d, me.datasets.length.toString(), false);
            });
        }

        public getRefTime () : KaRefTime {
            let me = this;
            let list = [];
            let onedataset = _.find(me.datasets, function (o) {
                return true;
            });
            return onedataset.dataset.reftime;
        }

        public getVMinVMax (options: any) : any {
            let me = this;
            _.each(me.datasets, function(o) {
                if (o.stacked) {
                    o.dataset.computeBase();
                }
            });
            let dmax = _.max(me.datasets, function(o) {
                return o.dataset.getVMax({ stacked: o.stacked });
            }, me);
            let vmax = dmax !== -Infinity ? dmax.dataset.getVMax({ stacked: dmax.stacked }) : 0;
            let dmin = _.min(me.datasets, function(o) {
                return o.dataset.getVMin({ stacked: o.stacked });
            }, me);
            let vmin = dmin !== Infinity ? dmin.dataset.getVMin({ stacked: dmin.stacked }) : 0;
            let min = options !== undefined && options.min !== undefined ? options.min : vmin;
            let max = options !== undefined && options.max !== undefined ? options.max : vmax;
            return nicenum(min, max, 10);
        }

        public pop (bid: string) : void {
            let me = this;
            me.datasets = _.without(me.datasets, function(o) {
                return o.bid !== bid;
            });
        }

        public push (dataset: KaDataset, bid: string, stacked: boolean) : void {
            let me = this;
            me.datasets.push({ bid: bid, stacked: stacked, dataset: dataset });
        }


    }

    export class Chart implements KaChart {

        private bound: any;
        private height: number;
        private mouseover: any;
        private dom: any;
        private paper: any;
        private width: number;
        private desktop: any;

        public charttemplate: KaChartTemplate;

        constructor (options?: any, logging?: string) {
            let me = this;
            me.getOptions(options);
            me.dom = {};
            me.bound = {};
            me.paper = {};
            let loglevel = log4javascript.Level.ALL;
            if (logging !== undefined) {
                loglevel = logging === 'all' ? log4javascript.Level.ALL : loglevel;
                loglevel = logging === 'trace' ? log4javascript.Level.TRACE : loglevel;
                loglevel = logging === 'debug' ? log4javascript.Level.DEBUG : loglevel;
                loglevel = logging === 'info' ? log4javascript.Level.INFO : loglevel;
                loglevel = logging === 'warn' ? log4javascript.Level.WARN : loglevel;
                loglevel = logging === 'error' ? log4javascript.Level.ERROR : loglevel;
                loglevel = logging === 'fatal' ? log4javascript.Level.FATAL : loglevel;
                loglevel = logging === 'off' ? log4javascript.Level.OFF : loglevel;
                log.setLevel(loglevel);
            } else {
                log.setLevel(loglevel);
            }
            log.info("Setting logging level to: ", loglevel);
        }

        public bind (bid: string, dataset: KaDataset, pid: string, renderer: KaRenderer, xid: string, yid: string, lid: string) {
            let me = this;
            if (bid === undefined) {
                throw '*** A bind must have an id!';
            }
            if (me.getBind(bid) !== undefined) {
                me.unbind(bid);
            }
            if (dataset === undefined) {
                throw '*** A dataset object is mandatory!';
            }
            if (renderer === undefined) {
                throw '*** A renderer object is mandatory!';
            }
            if (pid === undefined) {
                throw '*** Plot object missing!';
            }
            if (renderer.type === undefined) {
                throw '*** Renderer object seems corrupted!';
            }
            if (renderer.type !== "P" && xid === undefined) {
                throw '*** A Xaxis object is mandatory for some renderer types!';
            }
            if (renderer.type !== "P" && yid === undefined) {
                throw '*** A Yaxis object is mandatory for some renderer types!';
            }

            me.bound[bid] = new Bound(me, bid, dataset, pid, renderer, xid, yid, lid);

            let stacked = false;

            if (me.getXaxis(xid).scaling === 'linear' || me.getYaxis(yid).scaling === 'linear') {
                if (_.contains(["SA", "SC", "WSA", "WSC"], renderer.type)) {
                    stacked = true;
                }
            }

            me.getPlot(pid).bounddataset.push(dataset, bid, stacked);
            me.getXaxis(xid).bounddataset.push(dataset, bid, stacked);
            me.getXaxis(xid).oneplot = pid;
            me.getYaxis(yid).bounddataset.push(dataset, bid, stacked);
            me.getYaxis(yid).oneplot = pid;
            me.getLegend(lid).bounddataset.push(dataset, bid, stacked);

            return me.getBind(bid);
        };


        public bindPlot (pid : string) : KaPlot {
            let me = this;
            if (me.charttemplate.getObject(pid) === undefined) {
                throw '*** You are trying to bind a plot to an unknown area: "' + pid + '" in the current object.';
            }
            me.charttemplate.getObject(pid).plot = new Plot(pid);
            return me.getPlot(pid);
        }

        public bindLegend (lid: string) : KaLegend {
            let me = this;
            if (me.charttemplate.getObject(lid) === undefined) {
                throw '*** You are trying to bind a legend to an unknown area: "' + lid + '" in the current object.';
            }
            me.charttemplate.getObject(lid).legend = new Legend(lid);
            return me.getLegend(lid);
        }

        public bindTitle (tid: string, title: string, properties?: any) : KaTitle {
            let me = this;
            if (me.charttemplate.getObject(tid) === undefined) {
                throw '*** You are trying to bind a title to an unknown area: "' + tid + '" in the current object.';
            }
            me.charttemplate.getObject(tid).title = new Title(tid, title, properties);
            return me.getTitle(tid);
        };

        public bindXaxis (xid: string, title: string, scaling: string, properties?: any) : KaXaxis {
            let me = this;
            if (me.charttemplate.getObject(xid) === undefined) {
                throw '*** You are trying to bind a x-axis to an unknown area: "' + xid + '" in the current object.';
            }
            scaling = scaling === undefined ? 'linear' : scaling.toLowerCase();
            if (!_.contains(['linear', 'ordinal'], scaling)) {
                throw '*** This scaling: "' + scaling + '"' + " isn't supported!";
            }
            me.charttemplate.getObject(xid).xaxis = new Xaxis(xid, title, scaling, properties);
            return me.getXaxis(xid);
        }

        public bindYaxis (yid: string, title: string, position: string, scaling: string, properties?: any, minvalue?: number, maxvalue?: number) : KaYaxis {
            let me = this;
            if (me.charttemplate.getObject(yid) === undefined) {
                throw '*** You are trying to bind a y-axis to an unknown area: "' + yid + '" in the current object.';
            }
            scaling = scaling === undefined ? 'linear' : scaling.toLowerCase();
            if (!_.contains(['linear', 'ordinal'], scaling)) {
                throw '*** This scaling: "' + scaling + '"' + " isn't supported!";
            }
            position = position === undefined ? 'left' : position.toLowerCase();
            if (!_.contains(['left', 'right'], position)) {
                throw '*** This position: "' + position + '"' + " isn't supported!";
            }
            me.charttemplate.getObject(yid).yaxis = new Yaxis(yid, title, position, scaling, properties, minvalue, maxvalue);
            return me.getYaxis(yid);
        }

        private color (moid: string, type: string) : string {
            let me = this;
            let color = me.charttemplate.objects.main !== undefined && me.charttemplate.objects.main.style !== undefined ? me.charttemplate.objects.main.style[type] : undefined;
            color = me.charttemplate.getObject(moid).style === undefined || me.charttemplate.getObject(moid).style[type] === undefined ? color : me.charttemplate.getObject(moid).style[type];
            return color === undefined ? "white" : color;
        }

        private computeAxisPosition (moid: string, axistype: string) : any {
            let me = this;
            let r = {position: undefined, move: undefined};
            if (axistype === 'x') {
                r.position = "bottom";
                r.move = 0;
                let pye = me.charttemplate.getObject(moid).ys();
                let pyp = me.charttemplate.getObject(me.getXaxis(moid).oneplot).ys();
                if (pye < pyp) {
                    r.position = "top";
                    r.move = me.charttemplate.getObject(moid).h();
                }
            } else {
                r.position = "right";
                r.move = 0;
                let pxe = me.charttemplate.getObject(moid).xs();
                let pxp = me.charttemplate.getObject(me.getYaxis(moid).oneplot).xs();
                if (pxe < pxp) {
                    r.position = "left";
                    r.move = me.charttemplate.getObject(moid).w();
                }
            }
            return r;
        }

        public destroy () : void {
            let me = this;
            _.each(me.dom, function (x) {
                x.remove();
            })
        }

        public draw (attach?: string, key?: string, desktop?: any) : void {
            let me = this;
            log.debug("Drawing chart");
            me.createCanvas(attach, key);
            me.desktop = desktop;
            me.paper.mainLayer.on({
                draw: function (event) {
                    me.paper.project.view.draw();
                }
            });
            //me.drawWaiterLayerBox();
            me.finalize();
            me.drawMain();
            me.prepareXaxiss();
            me.prepareYaxiss();
            me.drawPlots();
            me.drawLegends();
            me.drawYaxiss();
            me.drawXaxiss();
            me.drawTitles();
            window.status = 'Done!';
            log.debug("End of drawing");
        }

        private createCanvas (attach: string, key: string) : void {
            let me = this;
            if (attach === undefined) {
                attach = "body";
            }
            let ratio = window.devicePixelRatio;
            ratio = 1;
            let id = key === undefined ? 'canvas' + _.uniqId('') : 'canvas' + key;
            d3.select(attach)
                .append("canvas")
                .attr("width", me.getWidth() * ratio)
                .attr("height", me.getHeight() * ratio)
                .attr("resize", "true")
                .attr("id", id)
                .style("width", me.getWidth() + 'px')
                .style("height", me.getHeight() + 'px');

            me.dom.canvas = document.getElementById(id);
            me.dom.canvas.style.cursor = 'default';
            me.dom.canvas.getContext('2d').scale(ratio, ratio);

            let paperholder = paper.setup(me.dom.canvas);
            me.paper.project = paperholder.project;
            me.paper.mainLayer = paper.project.activeLayer;
            me.paper.waiterLayer = new paper.Layer();
            me.paper.helperLayer = new paper.Layer();
            me.paper.mainLayer.activate();
            me.paper.project.activate();
        }

        private drawWaiterLayerBox () : void {
            let me = this;
            let containerw = me.getWidth();
            let containerh = me.getHeight();
            me.paper.waiterLayer.activate();
            let rectpath = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(containerw * 3 / 8, containerh * 3 / 8), new paper.Size(containerw / 4, containerh / 4)));
            rectpath.strokeColor = "blue";
            rectpath.fillColor = parsecolor("lightyellow");
            rectpath.strokeWidth = 5;
            me.paper.waiterGroup = new paper.Group();
            me.paper.mainLayer.emit('draw', {});
            me.paper.mainLayer.activate();
        }

        private showWaiterProgress(message: string) : void {
            let me = this;
            me.desktop.statusbar.setText(message);            
            // let containerw = me.getWidth();
            // let containerh = me.getHeight();
            // me.paper.waiterLayer.activate();
            // me.paper.waiterGroup.removeChildren();
            // me.paper.waiterGroup.addChild(new paper.PointText({ point: [containerw / 2, containerh / 2 + 3], content: message, fontSize: 10, fillColor: parsecolor("black"), justification: 'center' }));
            // me.paper.mainLayer.emit('draw', {});
            // me.paper.mainLayer.activate();
        }

        private hideWaiterLayerBox () : void {
            let me = this;
            postpone(0, function () {
                me.desktop.statusbar.setText('');            
                // me.paper.waiterLayer.activate();
                // me.paper.waiterLayer.removeChildren();
                // me.paper.mainLayer.activate();
                // me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawDataset (moid: string, bindid: string, again: boolean) : void {
            let me = this;
            postpone(0, function () {
                log.debug("Drawing dataset:", moid, bindid);
                me.showWaiterProgress("Drawing dataset: " + moid);
                //me.drawWaiterLayerBox();
                let bind = me.getBind(bindid);
                let dataset = bind.dataset;
                _.each(dataset.getOrderedPaths(), function(id) {
                    me.drawPath(moid, bindid, id, again);
                });
                me.hideWaiterLayerBox();
                me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawLegend (moid: string) : void {
            let me = this;
            postpone(0, function () {
                me.showWaiterProgress("Drawing legend: " + moid);
            });
            postpone(0, function () {
                log.debug("Drawing legend:", moid);
                let grp = me.dom[moid];
                let legend = me.getLegend(moid);
                let mo = me.charttemplate.getObject(moid);
                let containerw = mo.w();
                let containerh = mo.h();
                let containerxs= mo.xs();
                let containerys = mo.ys();
                let containerxe = mo.xe();
                let containerye = mo.ye();
                let legendkeys = {};
                let curx = containerxs + 0;
                let cury = containerys + 0;
                grp.removeChildren();
                let rectpath = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(containerxs, containerys), new paper.Size(containerw, containerh)));
                grp.addChild(rectpath);
                if (mo.style !== undefined && mo.style.fill !== undefined) {
                    rectpath.fillColor = parsecolor(mo.style.fill, mo);
                }

                _.each(legend.bounddataset.datasets, function(d) {
                    let bind = me.getBind(d.bid);
                    _.each(d.dataset.getOrderedPaths(), function(i) {
                        let label = d.dataset.labels[i];
                        let color = d.dataset.color[label];
                        if (legendkeys[label] === undefined) {
                            if (cury < containerye) {
                                let group = new paper.Group();
                                let point = bind.renderer.type !== 'L' ? new paper.Point(curx, cury) : new paper.Point(curx, cury + 4);
                                let size = bind.renderer.type !== 'L' ? new paper.Size(20, 10) : new paper.Size(10, 2);
                                let rectangle = new paper.Rectangle(point, size);
                                let rectpath = new paper.Path.Rectangle(rectangle);
                                rectpath.fillColor = parsecolor(color.toString(), mo);
                                curx = curx + size.width + 5;
                                let text = new paper.PointText({ point: [curx, cury + 8], content: label, fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: 'left' });
                                curx = curx + text.bounds.width + 10;
                                group.addChild(rectpath);
                                group.addChild(text);
                                if (curx > containerxe) {
                                    rectpath.remove();
                                    text.remove();
                                    curx = containerxs;
                                    cury = cury + 20;
                                    if (cury < containerye) {
                                        point = bind.renderer.type !== 'L' ? new paper.Point(curx, cury) : new paper.Point(curx, cury + 4);
                                        rectangle = new paper.Rectangle(point, size);
                                        rectpath = new paper.Path.Rectangle(rectangle);
                                        rectpath.fillColor = parsecolor(color.toString(), mo);
                                        curx = curx + size.width + 5;
                                        text = new paper.PointText({ point: [curx, cury + 8], content: label, fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: 'left' });
                                        curx = curx + text.bounds.width + 10;
                                        group.addChild(rectpath);
                                        group.addChild(text);
                                    }
                                }
                                group.on({
                                    click: function (event) {
                                        _.each(legendkeys[label], function(id) {
                                            let arrid = id.split('_');
                                            let bindid = arrid[0];
                                            let pathid = arrid[1];
                                            let hidden = me.getBind(bindid).dataset.flipflop(pathid);
                                            if (hidden) {
                                                rectpath.fillColor = parsecolor("lightgray");
                                                text.fillColor = parsecolor("lightgray");
                                            } else {
                                                rectpath.fillColor = parsecolor(color.toString(), mo);
                                                text.fillColor = parsecolor(me.color(moid, "stroke"), mo);
                                            }
                                            //me.drawWaiterLayerBox();
                                            me.prepareXaxis(me.getBind(bindid).xaxisname);
                                            me.prepareYaxis(me.getBind(bindid).yaxisname);
                                            me.drawPlot(me.getBind(bindid).plotname, true);
                                            me.drawXaxis(me.getBind(bindid).xaxisname, true);
                                            me.drawYaxis(me.getBind(bindid).yaxisname, true);
                                        });
                                    },
                                    mouseenter: function(event) {
                                        me.dom.canvas.style.cursor = 'pointer';
                                    },
                                    mouseleave: function(event) {
                                        me.dom.canvas.style.cursor = 'default';
                                    }
                                });
                            }
                            legendkeys[label] = [];
                        }
                        legendkeys[label].push(d.bid + "_" + i);
                    });
                });
                me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawLegends () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).legend !== undefined) {
                    me.dom[c] = new paper.Group();
                    log.debug("Defining drawing group:", c);
                    me.drawLegend(c);
                }
            });
        };

        private drawMain () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, e) {
                if (e === "main") {
                    me.dom[e] = new paper.Group();
                    log.debug("Defining drawing group:", e);
                    let grp = me.dom[e];
                    let mo = me.charttemplate.getObject(e);
                    let containerw = mo.w();
                    let containerh = mo.h();
                    let containerxs= mo.xs();
                    let containerys = mo.ys();
                    let rectpath = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(containerxs, containerys), new paper.Size(containerw, containerh)));
                    grp.addChild(rectpath);
                    if (mo.style !== undefined && mo.style.fill !== undefined) {
                        rectpath.fillColor = parsecolor(mo.style.fill, mo);
                    } 
                }
            });
        }

        private drawPath (moid: string, bindid: string, pathid: number, again: boolean) : void {
            let me = this;
            postpone(0, function () {
                let bind = me.getBind(bindid);
                let dataset = bind.dataset;
                let label = dataset.labels[pathid];
                me.showWaiterProgress("Drawing path: " + bindid + " / " + label);
            });
            postpone(0, function () {
                log.debug("Drawing path:", moid, bindid);
                let grp = me.dom[moid];
                let mo = me.charttemplate.getObject(moid);
                let containerw = mo.w();
                let containerh = mo.h();
                let containerxs = mo.xs();
                let containerys = mo.ys();
                let containerxm = mo.xm();
                let containerym = mo.ym();
                let bind = me.getBind(bindid);
                let dataset = bind.dataset;
                let label = dataset.labels[pathid];
                let color = dataset.color[label].toString();
                let renderer = bind.renderer;
                let fx = bind.fx;
                let fy = bind.fy;
                let bmin = bind.bmin;
                let id = bindid + "_" + pathid;
                let dom = me.dom[moid];
                let spacebars = null;
                let dompth = d3.select('#' + id);
                let farea;
                let skipped = undefined;

                if (dataset.hidden[pathid]) {
                    return;
                }
                log.debug("Path label:", label);

                let numpaths = dataset.data.nl;
                let positiony = me.computeAxisPosition(bind.yaxisname, "y");

                let opacity = _.contains(["SA", "A", "C", "SC"], renderer.type) ? 0.8 : 1;
                me.paper.helperLayer.activate();
                let helper = new paper.Group();
                me.paper.mainLayer.activate();

                let ygv = function (x) {
                    return dataset.data.getValue(pathid, x);
                };

                let xgv = function (x) {
                    return dataset.reftime.timestamps.getValue(0, x);
                };

                let bgv = function (x) {
                    return dataset.base.getValue(pathid, x);
                };

                let fbase = function (x) {
                    return _.contains(['SA', 'SC'], renderer.type) ? bgv(x) : 0;
                };

                let showHelper = function(p, i) {
                    if (i + skipped >= dataset.data.nc) {
                        return;
                    }
                    me.paper.helperLayer.activate();
                    let yap = positiony.position === 'left' ? me.charttemplate.getObject(bind.yaxisname).xe() : me.charttemplate.getObject(bind.yaxisname).xs();
                    let trpy = containerys + fy(ygv(i + skipped));
                    let txpx = p.x;
                    let txpy = me.charttemplate.getObject(bind.xaxisname).ys() - 10;
                    let typx = positiony.position === 'left' ? me.charttemplate.getObject(bind.yaxisname).xe() + 15 : me.charttemplate.getObject(bind.yaxisname).xs() - 15;
                    let typy = _.contains(['SA','SC'], renderer.type) ? trpy + 3 : p.y + 3;
                    let ttpx = typx;
                    let ttpy = p.y + 3;
                    let tlpx = positiony.position === 'left' ?  p.x + 15 : p.x - 15;
                    let tlpy = typy;
                    let tyj = positiony.position === 'left' ? 'left' : 'right';
                    let tlj = tyj;
                    let ttj = tyj;
                    helper.removeChildren();
                    helper.addChild(new paper.Path.Circle({ center: p, radius: 8 }));
                    helper.fillColor = parsecolor(color, mo);
                    helper.addChild(new paper.Path.Line({ from: new paper.Point(p.x, p.y), to: new paper.Point(p.x, me.charttemplate.getObject(bind.xaxisname).ys()), strokeWidth: 1, strokeColor: color}));
                    helper.addChild(new paper.Path.Line({ from: new paper.Point(p.x, p.y), to: new paper.Point(yap, p.y), strokeWidth: 1, strokeColor: color}));
                    if (_.contains(['SA', 'SC'], renderer.type)) {
                        helper.addChild(new paper.Path.Line({ from: new paper.Point(p.x, trpy), to: new paper.Point(yap, trpy), strokeWidth: 1, strokeColor: color}));
                        let tt = new paper.PointText({ point: [ttpx, ttpy], content: (fbase(i + skipped) + ygv(i + skipped)).toFixed(3), fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: ttj });
                        let ctt = new paper.Path.Rectangle(tt.bounds.x - 5, tt.bounds.y - 3, tt.bounds.width + 10, tt.bounds.height + 6);
                        ctt.fillColor = parsecolor(me.color(moid, "fill"), mo);
                        helper.addChild(ctt);
                        helper.addChild(tt);
                    }
                    let tx = new paper.PointText({ point: [txpx, txpy], content: new Date(xgv(i + skipped)), fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: 'center' });
                    let ctx = new paper.Path.Rectangle(tx.bounds.x - 5, tx.bounds.y - 3, tx.bounds.width + 10, tx.bounds.height + 6);
                    ctx.fillColor = parsecolor(me.color(moid, "fill"), mo);
                    helper.addChild(ctx);
                    helper.addChild(tx);
                    let ty = new paper.PointText({ point: [typx, typy], content: ygv(i + skipped).toFixed(3), fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: tyj });
                    let cty = new paper.Path.Rectangle(ty.bounds.x - 5, ty.bounds.y - 3, ty.bounds.width + 10, ty.bounds.height + 6);
                    cty.fillColor = parsecolor(me.color(moid, "fill"), mo);
                    helper.addChild(cty);
                    helper.addChild(ty);
                    let tl = new paper.PointText({ point: [tlpx, tlpy], content: label, fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: tlj });
                    let ctl = new paper.Path.Rectangle(tl.bounds.x - 5, tl.bounds.y - 3, tl.bounds.width + 10, tl.bounds.height + 6);
                    ctl.fillColor = parsecolor(me.color(moid, "fill"), mo);
                    helper.addChild(ctl);
                    helper.addChild(tl);
                    helper.visible = true;
                };

                let showHelperP = function(p, c, r, a) {
                    me.paper.helperLayer.activate();
                    helper.removeChildren();
                    let tx = new paper.PointText({ point: [p.x, c.y + r + r / 4], content: label, fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: 'center' });
                    helper.addChild(new paper.Path.Line({ from: p, to: new paper.Point(p.x, tx.bounds.y - 3), strokeWidth: 1, strokeColor: color }));
                    let ctx = new paper.Path.Rectangle(tx.bounds.x - 5, tx.bounds.y - 3, tx.bounds.width + 10, tx.bounds.height + 6);
                    ctx.fillColor = parsecolor(me.color(moid, "fill"), mo);
                    helper.addChild(ctx);
                    helper.addChild(tx);
                    let ty = new paper.PointText({ point: [c.x - r - r / 4 , p.y], content: a.toPrecision(2) + "%" , fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: 'right' });
                    helper.addChild(new paper.Path.Line({ from: p, to: new paper.Point(ty.bounds.x + ty.bounds.width + 10, p.y), strokeWidth: 1, strokeColor: color }));
                    let cty = new paper.Path.Rectangle(ty.bounds.x - 5, ty.bounds.y - 3, ty.bounds.width + 10, ty.bounds.height + 6);
                    cty.fillColor = parsecolor(me.color(moid, "fill"), mo);
                    helper.addChild(cty);
                    helper.addChild(ty);
                    helper.visible = true;
                };

                let hideHelper = function () {
                    helper.visible = false;
                    me.paper.mainLayer.activate;
                }

                if (renderer.type === "P") {
                    let angles = dataset.getAngles(pathid);
                    let radius = _.min([containerh, containerw]) / 3;
                    let center = new paper.Point(containerxs + containerw / 2, containerys + containerh / 2);
                    let pfrom = new paper.Point(containerxs + containerw / 2 + radius, containerys + containerh / 2);
                    let pto = new paper.Point(containerxs + containerw / 2 + radius * Math.cos(angles[1]), containerys + containerh / 2 - radius * Math.sin(angles[1]));
                    let pthr = new paper.Point(containerxs + containerw / 2 + radius * Math.cos(angles[1] / 2), containerys + containerh / 2 - radius * Math.sin(angles[1] / 2));
                    let arc = new paper.Path.Arc(pfrom, pthr, pto);
                    arc.add(center);
                    arc.closed = true;
                    arc.fillColor = parsecolor(color, mo);
                    arc.rotate((angles[0] + angles[1] - Math.PI / 2) * 180 / Math.PI, center);
                    let position = arc.position;
                    grp.addChild(arc);
                    let context = { cursor: undefined, start: undefined, stop: undefined };
                    arc.on({
                        mousedown: function(event) {
                            context.start = new paper.Point(event.point);
                        },
                        mouseup: function(event) {
                            context.stop = new paper.Point(event.point);
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.onclick[label]();
                            }
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.info[label]();
                            }
                        },
                        mouseenter: function(event) {
                            context.cursor = me.dom.canvas.style.cursor;
                            me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                            me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                            let tx = position.x + 0.05 * radius * Math.cos(angles[0] + angles[1] / 2 - Math.PI / 2);
                            let ty = position.y + 0.05 * radius * Math.sin(angles[0] + angles[1] / 2 - Math.PI / 2);
                            arc.position = new paper.Point(tx, ty);
                            arc.strokeColor = "black";
                            arc.opacity = 0.5;
                            showHelperP(arc.position, center, radius, angles[1] * 100 / 2 / Math.PI);
                        },
                        mouseleave: function(event) {
                            arc.position = position;
                            me.dom.canvas.style.cursor = context.cursor;
                            arc.strokeColor = color;
                            arc.opacity = 1;
                            hideHelper();
                        }
                    });
                }

                if (renderer.type === "SA") {
                    let area = new paper.Path();
                    area.fillColor = parsecolor(color, mo);
                    area.strokeWidth = 2;
                    _.each(_.range(dataset.data.nc), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            skipped = skipped === undefined ? i : skipped;
                            area.add(new paper.Point(containerxs + fx(xgv(i)), containerys + fy(bgv(i) + ygv(i))));
                        }
                    });
                    _.each(_.range(dataset.data.nc-1, -1, -1), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            area.add(new paper.Point(containerxs + fx(xgv(i)), containerys + fy(bgv(i))));
                        }
                    });
                    area.closed = true;
                    grp.addChild(area);
                    let context = {cursor: undefined, start: undefined, stop: undefined};
                    area.on({
                        mousedown: function (event) {
                            context.start = new paper.Point(event.point);
                        },
                        mouseup: function (event) {
                            context.stop = new paper.Point(event.point);
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.onclick[label]();
                            }
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.info[label]();
                            }
                        },
                        mouseenter: function (event) {
                            context.cursor = me.dom.canvas.style.cursor;
                            me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                            me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                            area.strokeColor = "black";
                            area.opacity = 0.5;
                            let location = area.getNearestLocation(event.point)
                            showHelper(location.segment.point, location.segment.index);
                        },
                        mouseleave: function (event) {
                            me.dom.canvas.style.cursor = context.cursor;
                            area.strokeColor = color;
                            area.opacity = 1;
                            hideHelper();
                        }
                    });
                }

                if (renderer.type === "A") {
                    let area = new paper.Path();
                    area.fillColor = parsecolor(color, mo);
                    area.strokeWidth = 1;
                    _.each(_.range(dataset.data.nc), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            skipped = skipped === undefined ? i : skipped;
                            area.add(new paper.Point(containerxs + fx(xgv(i)), containerys + fy(ygv(i))));
                        }
                    });
                    _.each(_.range(dataset.data.nc-1, -1, -1), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            area.add(new paper.Point(containerxs + fx(xgv(i)), containerys + fy(0)));
                        }
                    });
                    area.closed = true;
                    grp.addChild(area);
                    let context = {cursor: undefined, start: undefined, stop: undefined};
                    area.on({
                        mousedown: function (event) {
                            context.start = new paper.Point(event.point);
                        },
                        mouseup: function (event) {
                            context.stop = new paper.Point(event.point);
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.onclick[label]();
                            }
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.info[label]();
                            }
                        },
                        mouseenter: function (event) {
                            context.cursor = me.dom.canvas.style.cursor;
                            me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                            me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                            area.strokeColor = "black";
                            area.opacity = 0.5;
                            let location = area.getNearestLocation(event.point)
                            showHelper(location.segment.point, location.segment.index);
                        },
                        mouseleave: function (event) {
                            me.dom.canvas.style.cursor = context.cursor;
                            area.strokeColor = color;
                            area.opacity = 1;
                            hideHelper();
                        }
                    });
                }

                if (renderer.type === "L") {
                    let line = new paper.Path();
                    line.strokeColor = color;
                    line.strokeWidth = 2;
                    _.each(_.range(dataset.data.nc), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            skipped = skipped === undefined ? i : skipped;
                            line.add(new paper.Point(containerxs + fx(xgv(i)), containerys + fy(ygv(i))));
                        }
                    });
                    grp.addChild(line);
                    let context = {cursor: undefined, start: undefined, stop: undefined};
                    line.on({
                        mousedown: function (event) {
                            context.start = new paper.Point(event.point);
                        },
                        mouseup: function (event) {
                            context.stop = new paper.Point(event.point);
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.onclick[label]();
                            }
                            if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                me.dom.canvas.style.cursor = 'progress';
                                dataset.info[label]();
                            }
                        },
                        mouseenter: function (event) {
                            context.cursor = me.dom.canvas.style.cursor;
                            me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                            me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                            line.strokeWidth = 4;
                            let location = line.getNearestLocation(event.point)
                            showHelper(location.segment.point, location.segment.index);
                        },
                        mouseleave: function (event) {
                            me.dom.canvas.style.cursor = context.cursor;
                            line.strokeWidth = 2;
                            hideHelper();
                        }
                    });
               }

                if (renderer.type === "C") {
                    _.each(_.range(dataset.data.nc), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            skipped = skipped === undefined ? i : skipped;
                            let pl = i === 0 ? containerw : fx(xgv(i)) - fx(xgv(i-1));
                            let pr = i === dataset.data.nc - 1 ? containerw : fx(xgv(i+1)) - fx(xgv(i));
                            let spacebars = _.min([pl, pr]);
                            let point = new paper.Point(containerxs + fx(xgv(i)) - spacebars / 2, containerys + fy(ygv(i)));
                            let size = new paper.Size(spacebars, containerh - fy(ygv(i) + bmin));
                            let rectangle = new paper.Rectangle(point, size);
                            let rectpath = new paper.Path.Rectangle(rectangle);
                            rectpath.fillColor = parsecolor(color, mo);
                            grp.addChild(rectpath);
                            let context = {cursor: undefined, start: undefined, stop: undefined};
                            rectpath.on({
                                mousedown: function (event) {
                                    context.start = new paper.Point(event.point);
                                },
                                mouseup: function (event) {
                                    context.stop = new paper.Point(event.point);
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.onclick[label]();
                                    }
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.info[label]();
                                    }
                                },
                                mouseenter: function (event) {
                                    context.cursor = me.dom.canvas.style.cursor;
                                    me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                                    me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                                    rectpath.strokeColor = "black";
                                    rectpath.opacity = 0.5;
                                    let hpoint = new paper.Point(point.x + spacebars / 2, point.y);
                                    showHelper(hpoint, i);
                                },
                                mouseleave: function (event) {
                                    me.dom.canvas.style.cursor = context.cursor;
                                    rectpath.strokeColor = color;
                                    rectpath.opacity = 1;
                                    hideHelper();
                                }
                            });
                        }
                    });
                }

                if (renderer.type === "CC") {
                    _.each(_.range(dataset.data.nc), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            skipped = skipped === undefined ? i : skipped;
                            let pl = i === 0 ? containerw : fx(xgv(i)) - fx(xgv(i-1));
                            let pr = i === dataset.data.nc - 1 ? containerw : fx(xgv(i+1)) - fx(xgv(i));
                            let spacebars = _.min([pl, pr]);
                            let point = new paper.Point(containerxs + fx(xgv(i)) - spacebars / 2 + pathid * spacebars / numpaths, containerys + fy(ygv(i)));
                            let size = new paper.Size(spacebars / numpaths, containerh - fy(ygv(i) + bmin));
                            let rectangle = new paper.Rectangle(point, size);
                            let rectpath = new paper.Path.Rectangle(rectangle);
                            rectpath.fillColor = parsecolor(color, mo);
                            grp.addChild(rectpath);
                            let context = {cursor: undefined, start: undefined, stop: undefined};
                            rectpath.on({
                                mousedown: function (event) {
                                    context.start = new paper.Point(event.point);
                                },
                                mouseup: function (event) {
                                    context.stop = new paper.Point(event.point);
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.onclick[label]();
                                    }
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.info[label]();
                                    }
                                },
                                mouseenter: function (event) {
                                    context.cursor = me.dom.canvas.style.cursor;
                                    me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                                    me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                                    rectpath.strokeColor = "black";
                                    rectpath.opacity = 0.5;
                                    let hpoint = new paper.Point(point.x + spacebars / numpaths / 2, point.y);
                                    showHelper(hpoint, i);
                                },
                                mouseleave: function (event) {
                                    me.dom.canvas.style.cursor = context.cursor;
                                    rectpath.strokeColor = color;
                                    rectpath.opacity = 1;
                                    hideHelper();
                                }
                            });
                        }
                    });
                }

                if (renderer.type === "CL") {
                    _.each(_.range(dataset.data.nc), function(i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            skipped = skipped === undefined ? i : skipped;
                            let pl = i === 0 ? containerw : fx(xgv(i)) - fx(xgv(i-1));
                            let pr = i === dataset.data.nc - 1 ? containerw : fx(xgv(i+1)) - fx(xgv(i));
                            let spacebars = _.min([pl, pr]);
                            let point = new paper.Point(containerxs + fx(xgv(i)) - spacebars / 2 / (pathid + 1), containerys + fy(ygv(i)));
                            let size = new paper.Size(spacebars / (pathid + 1), containerh - fy(ygv(i) + bmin));
                            let rectangle = new paper.Rectangle(point, size);
                            let rectpath = new paper.Path.Rectangle(rectangle);
                            rectpath.fillColor = parsecolor(color, mo);
                            grp.addChild(rectpath);
                            let context = {cursor: undefined, start: undefined, stop: undefined};
                            rectpath.on({
                                mousedown: function (event) {
                                    context.start = new paper.Point(event.point);
                                },
                                mouseup: function (event) {
                                    context.stop = new paper.Point(event.point);
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.onclick[label]();
                                    }
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.info[label]();
                                    }
                                },
                                mouseenter: function (event) {
                                    context.cursor = me.dom.canvas.style.cursor;
                                    me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                                    me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                                    rectpath.strokeColor = "black";
                                    rectpath.opacity = 0.5;
                                    let hpoint = new paper.Point(point.x + spacebars / 2, point.y);
                                    showHelper(hpoint, i);
                                },
                                mouseleave: function (event) {
                                    me.dom.canvas.style.cursor = context.cursor;
                                    rectpath.strokeColor = color;
                                    rectpath.opacity = 1;
                                    hideHelper();
                                }
                            });
                        }
                    });
                }

                if (renderer.type === "SC") {
                    _.each(_.range(dataset.data.nc), function (i) {
                        if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= containerw) {
                            skipped = skipped === undefined ? i : skipped;
                            let pl = i === 0 ? containerw : fx(xgv(i)) - fx(xgv(i-1));
                            let pr = i === dataset.data.nc - 1 ? containerw : fx(xgv(i+1)) - fx(xgv(i));
                            let spacebars = _.min([pl, pr]);
                            let point = new paper.Point(containerxs + fx(xgv(i)) - spacebars / 2, containerys + fy(bgv(i) + ygv(i)));
                            let size = new paper.Size(spacebars, containerh - fy(ygv(i) + bmin));
                            let rectangle = new paper.Rectangle(point, size);
                            let rectpath = new paper.Path.Rectangle(rectangle);
                            rectpath.fillColor = parsecolor(color, mo);
                            grp.addChild(rectpath);
                            let context = {cursor: undefined, start: undefined, stop: undefined};
                            rectpath.on({
                                mousedown: function (event) {
                                    context.start = new paper.Point(event.point);
                                },
                                mouseup: function (event) {
                                    context.stop = new paper.Point(event.point);
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.onclick[label]();
                                    }
                                    if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                        me.dom.canvas.style.cursor = 'progress';
                                        dataset.info[label]();
                                    }
                                },
                                mouseenter: function (event) {
                                    context.cursor = me.dom.canvas.style.cursor;
                                    me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                                    me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                                    rectpath.strokeColor = "black";
                                    rectpath.opacity = 0.5;
                                    let hpoint = new paper.Point(point.x + spacebars / 2, point.y);
                                    showHelper(hpoint, i);
                                },
                                mouseleave: function (event) {
                                    me.dom.canvas.style.cursor = context.cursor;
                                    rectpath.strokeColor = color;
                                    rectpath.opacity = 1;
                                    hideHelper();
                                }
                            });
                        }
                    });
                }

                if (renderer.type === "WA") {
                    _.each(_.range(dataset.data.nc), function(i) {
                        let radius = _.min([containerw, containerh]) * 3 / 8;
                        let area = new paper.Path();
                        area.fillColor = parsecolor(color, mo);
                        area.opacity = 0.3;
                        area.strokeWidth = 1;
                        _.each(_.range(dataset.data.nc), function(i) {
                            if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= 360) {
                                skipped = skipped === undefined ? i : skipped;
                                let px = containerxm + (radius - fy(ygv(i))) * Math.cos(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2); 
                                let py = containerym + (radius - fy(ygv(i))) * Math.sin(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2); 
                                area.add(new paper.Point(px, py));
                            }
                        });
                        area.closed = true;
                        grp.addChild(area);
                        let context = { cursor: undefined, start: undefined, stop: undefined };
                        area.on({
                            mousedown: function(event) {
                                context.start = new paper.Point(event.point);
                            },
                            mouseup: function(event) {
                                context.stop = new paper.Point(event.point);
                                if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                    me.dom.canvas.style.cursor = 'progress';
                                    dataset.onclick[label]();
                                }
                                if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                    me.dom.canvas.style.cursor = 'progress';
                                    dataset.info[label]();
                                }
                            },
                            mouseenter: function(event) {
                                context.cursor = me.dom.canvas.style.cursor;
                                me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                                me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                                area.strokeColor = "black";
                                area.opacity = 0.5;
                                let location = area.getNearestLocation(event.point)
                                showHelper(location.segment.point, location.segment.index);
                            },
                            mouseleave: function(event) {
                                me.dom.canvas.style.cursor = context.cursor;
                                area.strokeColor = color;
                                area.opacity = 1;
                                hideHelper();
                            }
                        });
                    });
                }

                if (renderer.type === "WSA") {
                    _.each(_.range(dataset.data.nc), function(i) {
                        let radius = _.min([containerw, containerh]) * 3 / 8;
                        let area = new paper.Path();
                        area.fillColor = parsecolor(color, mo);
                        area.opacity = 0.3;
                        area.strokeWidth = 1;
                        _.each(_.range(dataset.data.nc), function(i) {
                            if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= 360) {
                                skipped = skipped === undefined ? i : skipped;
                                let px = containerxm + (radius - fy(bgv(i) + ygv(i))) * Math.cos(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2); 
                                let py = containerym + (radius - fy(bgv(i) + ygv(i))) * Math.sin(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2); 
                                area.add(new paper.Point(px, py));
                            }
                        });
                        _.each(_.range(dataset.data.nc-1, -1, -1), function(i) {
                            if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= 360) {
                                let px = containerxm + (radius - fy(bgv(i))) * Math.cos(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2); 
                                let py = containerym + (radius - fy(bgv(i))) * Math.sin(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2); 
                                area.add(new paper.Point(px, py));
                            }
                        });
                        area.closed = true;
                        grp.addChild(area);
                        let context = { cursor: undefined, start: undefined, stop: undefined };
                        area.on({
                            mousedown: function(event) {
                                context.start = new paper.Point(event.point);
                            },
                            mouseup: function(event) {
                                context.stop = new paper.Point(event.point);
                                if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                    me.dom.canvas.style.cursor = 'progress';
                                    dataset.onclick[label]();
                                }
                                if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                    me.dom.canvas.style.cursor = 'progress';
                                    dataset.info[label]();
                                }
                            },
                            mouseenter: function(event) {
                                context.cursor = me.dom.canvas.style.cursor;
                                me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                                me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                                area.strokeColor = "black";
                                area.opacity = 0.5;
                                let location = area.getNearestLocation(event.point)
                                showHelper(location.segment.point, location.segment.index);
                            },
                            mouseleave: function(event) {
                                me.dom.canvas.style.cursor = context.cursor;
                                area.strokeColor = color;
                                area.opacity = 1;
                                hideHelper();
                            }
                        });
                    });
                }

                if (renderer.type === "WL") {
                    _.each(_.range(dataset.data.nc), function(i) {
                        let radius = _.min([containerw, containerh]) * 3 / 8;
                        let line = new paper.Path();
                        line.strokeColor = color;
                        line.strokeWidth = 2;
                        _.each(_.range(dataset.data.nc), function(i) {
                            if (fx(xgv(i)) >= 0 && fx(xgv(i)) <= 360) {
                                skipped = skipped === undefined ? i : skipped;
                                let px = containerxm + (radius - fy(ygv(i))) * Math.cos(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2);
                                let py = containerym + (radius - fy(ygv(i))) * Math.sin(fx(xgv(i)) * Math.PI / 180 - Math.PI / 2);
                                line.add(new paper.Point(px, py));
                            }
                        });
                        line.closed = true;
                        grp.addChild(line);
                        let context = { cursor: undefined, start: undefined, stop: undefined };
                        line.on({
                            mousedown: function(event) {
                                context.start = new paper.Point(event.point);
                            },
                            mouseup: function(event) {
                                context.stop = new paper.Point(event.point);
                                if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.onclick[label] !== undefined) {
                                    me.dom.canvas.style.cursor = 'progress';
                                    dataset.onclick[label]();
                                }
                                if (context.start.x === context.stop.x && context.start.y === context.stop.y && dataset.info[label] !== undefined && (event.event.altKey || dataset.onclick[label] === undefined)) {
                                    me.dom.canvas.style.cursor = 'progress';
                                    dataset.info[label]();
                                }
                            },
                            mouseenter: function(event) {
                                context.cursor = me.dom.canvas.style.cursor;
                                me.dom.canvas.style.cursor = dataset.onclick[label] === undefined ? context.cursor : context.cursor === 'default' ? 'pointer' : context.cursor;
                                me.dom.canvas.style.cursor = dataset.info[label] === undefined ? me.dom.canvas.style.cursor : context.cursor === 'default' ? 'help' : me.dom.canvas.style.cursor;
                                line.strokeColor = "black";
                                line.opacity = 0.5;
                                let location = line.getNearestLocation(event.point)
                                showHelper(location.segment.point, location.segment.index);
                            },
                            mouseleave: function(event) {
                                me.dom.canvas.style.cursor = context.cursor;
                                line.strokeColor = color;
                                line.opacity = 1;
                                hideHelper();
                            }
                        });
                    });
                }

                me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawPlot (moid: string, again: boolean) : void {
            let me = this;
            postpone(0, function () {
                log.debug("Drawing plot:", moid);
                let plot = me.getPlot(moid);
                let grp = me.dom[moid];
                let mo = me.charttemplate.getObject(moid);
                let containerw = mo.w();
                let containerh = mo.h();
                let containerxs= mo.xs();
                let containerys = mo.ys();
                let tickx = [];
                let ticky = [];
                grp.removeChildren();
                let rectpath = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(containerxs, containerys), new paper.Size(containerw, containerh)));
                grp.addChild(rectpath);
                if (mo.style !== undefined && mo.style.fill !== undefined) {
                    rectpath.fillColor = parsecolor(mo.style.fill, mo);
                }
                _.each(plot.bounddataset.datasets, function(o) {
                    me.drawDataset(moid, o.bid, again);
                });
                if (! again) {
                    let animation = {start: undefined, stop: undefined, path: undefined, line: undefined};
                    grp.on({
                        click: function(event) {
                            if (me.dom.canvas.style.cursor === 'default') {
                                let bind = me.getBindsFromPlot(plot)[0];
                                bind.xaxis.zoom = undefined;
                                bind.xaxis.translation = undefined;
                                //me.drawWaiterLayerBox();
                                me.prepareXaxis(bind.xaxisname);
                                var plots = [];
                                _.each(me.getBindsFromXaxis(bind.xaxis), function(b) {
                                    plots.push(b.plotname);
                                });
                                _.each(_.uniq(plots), function(p) {
                                    me.drawPlot(p, true);
                                });
                                me.drawXaxis(bind.xaxisname, true);
                            }
                        },
                        mousedown: function (event) {
                            if (event.event.buttons === 1 && event.event.button === 0) {
                                animation.start = new paper.Point(event.point);
                                animation.path = new paper.Path.Rectangle(new paper.Rectangle(animation.start, animation.start));
                                animation.line = new paper.Path();
                                me.dom.canvas.style.cursor = me.dom.canvas.style.cursor !== 'default' ? me.dom.canvas.style.cursor : 'ew-resize';
                            }
                        },
                        mousedrag: function (event) {
                            if (event.event.buttons === 1 && event.event.button === 0) {
                                me.dom.canvas.style.cursor = 'ew-resize';
                                animation.stop = new paper.Point(event.point);
                                animation.path.remove();
                                animation.line.remove()
                                animation.path = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(animation.start.x, containerys), new paper.Point(animation.stop.x, containerys + containerh)));
                                animation.path.fillColor = parsecolor('lightgray');
                                animation.path.opacity = 0.5;
                                animation.line = new paper.Path(new paper.Point((animation.start.x + animation.stop.x) / 2, containerys), new paper.Point((animation.start.x + animation.stop.x) / 2, containerys + containerh));
                                animation.line.strokeColor = me.color(moid, "stroke");
                            }
                        },
                        mouseup: function (event) {
                            animation.stop = new paper.Point(event.point);
                            animation.path.remove();
                            animation.line.remove();
                            me.dom.canvas.style.cursor = me.dom.canvas.style.cursor === 'progress' ? 'progress' : 'default';
                            if (animation.stop.x !== animation.start.x) {
                                let bind = me.getBindsFromPlot(plot)[0];
                                let focus = animation.stop.x;
                                let scale = containerw / Math.abs(animation.stop.x - animation.start.x);
                                bind.xaxis.zoom = bind.xaxis.zoom === undefined ? scale : bind.xaxis.zoom * scale;
                                bind.xaxis.translation = bind.xaxis.translation === undefined ? 0 : bind.xaxis.translation;
                                bind.xaxis.translation = bind.xaxis.translation * scale + (1 - scale) * ((animation.start.x + animation.stop.x) / 2 - containerxs);
                                bind.xaxis.translation = bind.xaxis.translation - ((animation.start.x + animation.stop.x) / 2 - containerw / 2) + containerxs;
                                me.prepareXaxis(bind.xaxisname);
                                var plots = [];
                                _.each(me.getBindsFromXaxis(bind.xaxis), function(b) {
                                    plots.push(b.plotname);
                                });
                                //me.drawWaiterLayerBox();
                                _.each(_.uniq(plots), function(p) {
                                    me.drawPlot(p, true);
                                });
                                me.drawXaxis(bind.xaxisname, true);
                            }
                        }
                    });
                }
                me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawPlots () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).plot !== undefined) {
                    me.dom[c] = new paper.Group();
                    log.debug("Defining drawing group:", c);
                    me.drawPlot(c, false);
                }
            });
            me.paper.mainLayer.emit('draw', {});
        }

        private drawTitle (moid: string) : void {
            let me = this;
            postpone(0, function () {
                me.showWaiterProgress("Drawing title: " + moid);
            });
            postpone(0, function () {
                log.debug("Drawing title:", moid);
                let grp = me.dom[moid];
                let title = me.getTitle(moid);
                let mo = me.charttemplate.getObject(moid);
                let containerw = mo.w();
                let containerh = mo.h();
                let containerxs = mo.xs();
                let containerys = mo.ys();
                let properties = title.properties === undefined ? {} : title.properties;
                let orientation = properties.orientation === undefined ? containerw < containerh ? "vertical" : "horizontal" : properties.orientation;
                let fs = properties.fs === undefined ? orientation === "vertical" ? containerw * 0.8 : containerh * 0.8 : properties.fs;
                let dy = properties.dy === undefined ? 0.3 * fs : properties.dy;
                let px = properties.x === undefined ? containerxs + containerw / 2 : containerxs + properties.x;
                let py = properties.y === undefined ? containerys + containerh / 2 + dy : containerys + properties.y + dy;
                let rotate = properties.rotate === undefined ? orientation === 'vertical' ? 270 : 0 : properties.rotate;
                let fill = properties.fill === undefined ? me.color(moid, "stroke") : properties.fill;
                let anchor = properties.anchor === undefined ? "center" : properties.anchor;
                let rectpath = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(containerxs, containerys), new paper.Size(containerw, containerh)));
                let text = new paper.PointText(new paper.Point(px, py));
                grp.removeChildren();
                grp.addChild(rectpath);
                if (mo.style !== undefined && mo.style.fill !== undefined) {
                    rectpath.fillColor = parsecolor(mo.style.fill, mo);
                }
                text.content = title.title;
                text.justification = anchor;
                text.fillColor = parsecolor(fill, mo);
                text.fontSize = fs;
                text.rotate(rotate);
                grp.addChild(text);
                me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawTitles () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).title !== undefined) {
                    me.dom[c] = new paper.Group();
                    log.debug("Defining drawing group:", c);
                    me.drawTitle(c);
                }
            });
            me.paper.mainLayer.emit('draw', {});
        }

        private drawXaxis (moid: string, again: boolean) : void {
            let me = this;
            postpone(0, function () {
                me.showWaiterProgress("Drawing xaxis: " + moid);
            });
            postpone(0, function () {
                log.debug("Drawing xaxis:", moid);
                let xaxis = me.getXaxis(moid);
                let grp = me.dom[moid];
                let mo = me.charttemplate.getObject(moid);
                let containerw = mo.w();
                let containerh = mo.h();
                let containerxs= mo.xs();
                let containerys = mo.ys();
                grp.removeChildren();
                let rectpath = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(containerxs, containerys), new paper.Size(containerw, containerh)));
                grp.addChild(rectpath);
                if (mo.style !== undefined && mo.style.fill !== undefined) {
                    rectpath.fillColor = parsecolor(mo.style.fill, mo);
                }

                if (xaxis.type === 'linear') {
                    if (xaxis.fctv().length > 1) {
                        grp.addChild(new paper.Path.Line({from: new paper.Point(containerxs, containerys), to: new paper.Point(containerxs + containerw, containerys), strokeWidth: 1, strokeColor: me.color(moid, "stroke")}));
                    }

                    _.each(xaxis.fctv(), function(e) {
                        if (e !== undefined) {
                            let x = xaxis.fx(e.tick);
                            if (!isNaN(x) && x >= 0 && x <= containerw) {
                                grp.addChild(new paper.Path.Line({from: new paper.Point(containerxs + x, containerys), to: new paper.Point(containerxs + x, containerys + 4), strokeWidth: 1, strokeColor: me.color(moid, "stroke")}));
                                grp.addChild(new paper.PointText({ point: [containerxs + x, containerys + 15], content: e.label, fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: 'center' }));
                                _.each(me.getBindsFromXaxis(xaxis), function(b) {
                                    let plot = b.plot;
                                    let mo = me.charttemplate.getObject(b.plotname);
                                    let containerh = mo.h();
                                    let containerxs = mo.xs();
                                    let containerys = mo.ys();
                                    grp.addChild(new paper.Path.Line({ from: new paper.Point(containerxs + x, containerys), to: new paper.Point(containerxs + x, containerys + containerh), strokeWidth: 0.2, strokeColor: "lightgray" }));
                                });
                            }
                        }
                    });
                }

                if (xaxis.type === 'polar') {
                    if (xaxis.fctv().length > 1) {
                        _.each(me.getBindsFromXaxis(xaxis), function(b) {
                            let plot = b.plot;
                            let mo = me.charttemplate.getObject(b.plotname);
                            let containerh = mo.h();
                            let containerw = mo.w();
                            let containerxm = mo.xm();
                            let containerym = mo.ym();
                            let center = new paper.Point(containerxm, containerym);
                            let radius = _.min([containerh, containerw]) * 3 / 8;
                            let circle = new paper.Path.Circle(center, radius);
                            circle.strokeColor = parsecolor(me.color(moid, "stroke"));
                            grp.addChild(circle);
                            _.each(xaxis.fctv(), function(e) {
                                if (e !== undefined) {
                                    let x = xaxis.fx(e.tick);
                                    let align = x < 5 || x > 355 ? 'center' : x > 175 && x < 185 ? 'center' : x >= 5 && x <= 175 ? 'left' : 'right';
                                    let y = x * Math.PI / 180 - Math.PI / 2;
                                    let newradius = radius + radius / 12;
                                    let plx = containerxm + newradius * Math.cos(y);
                                    let ply = containerym + newradius * Math.sin(y) + 5;
                                    if (x < 355) {
                                        grp.addChild(new paper.PointText({ point: [plx, ply], content: e.label, fontSize: 10, fillColor: parsecolor(me.color(moid, "stroke"), mo), justification: align }));
                                    }
                                    let px = containerxm + radius * Math.cos(y);
                                    let py = containerym + radius * Math.sin(y);
                                    grp.addChild(new paper.Path.Line({ from: center, to: new paper.Point(px, py), strokeWidth: 0.5, strokeColor: "lightgray" }));
                                }
                            });
                        });
                    }
                }

                me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawXaxiss () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).xaxis !== undefined) {
                    me.dom[c] = new paper.Group();
                    log.debug("Defining drawing group:", c);
                    me.drawXaxis(c, false);
                }
            });
            me.paper.mainLayer.emit('draw', {});
        }

        private drawYaxis (moid: string, again: boolean) : void {
            let me = this;
                me.showWaiterProgress("Drawing yaxis: " + moid);
            postpone(0, function () {
                log.debug("Drawing yaxis:", moid);
                let grp = me.dom[moid];
                let yaxis = me.getYaxis(moid);
                let mo = me.charttemplate.getObject(moid);
                let containerw = mo.w();
                let containerh = mo.h();
                let containerxs= mo.xs();
                let containerys = mo.ys();
                let computecoeff = function(e) {
                    let coeff = 0.000001;
                    coeff = yaxis.step >= 0.000001 ? 0.000001 : coeff;
                    coeff = yaxis.step >= 0.001 ? 0.001 : coeff;
                    coeff = yaxis.step >= 0.01 ? 0.01 : coeff;
                    coeff = yaxis.step >= 0.1 ? 0.1 : coeff;
                    coeff = yaxis.step >= 1 ? 1.0 : coeff;
                    coeff = yaxis.step >= 1000 ? 1000.0 : coeff;
                    coeff = yaxis.step >= 1000000 ? 1000000.0 : coeff;
                    coeff = yaxis.step >= 1000000000 ? 1000000000.0 : coeff;
                    let xxx = e / coeff;
                    let ecoeff = xxx.toFixed(0);
                    e = coeff === 1000000000 ? ecoeff + "G" : e;
                    e = coeff === 1000000 ? ecoeff + "M" : e;
                    e = coeff === 1000 ? ecoeff + "K" : e;
                    e = coeff === 1 ? ecoeff : e;
                    e = coeff === 0.001 ? ecoeff + " E-3" : e;
                    e = coeff === 0.000001 ? ecoeff + " E-6" : e;
                    return e;
                }
                grp.removeChildren();
                let rectpath = new paper.Path.Rectangle(new paper.Rectangle(new paper.Point(containerxs, containerys), new paper.Size(containerw, containerh)));
                grp.addChild(rectpath);
                if (mo.style !== undefined && mo.style.fill !== undefined) {
                    rectpath.fillColor = parsecolor(mo.style.fill, mo);
                }
                if (yaxis.type === 'linear') {
                    let orient = me.computeAxisPosition(moid, "y");
                    let lineproperties = yaxis.properties === undefined ? {} : yaxis.properties.line === undefined ? {} : yaxis.properties.line;
                    let textproperties = yaxis.properties === undefined ? {} : yaxis.properties.text === undefined ? {} : yaxis.properties.text;
                    let lsw = lineproperties["stroke-width"] === undefined ? 1 : lineproperties["stroke-width"];
                    let lst = lineproperties.stroke === undefined ? me.color(moid, "stroke") : lineproperties.stroke;
                    let tst = textproperties.fill === undefined ? me.color(moid, "stroke") : textproperties.fill;
                    let tickanchor = orient.position === 'left' ? 'right' : 'left';
                    let lcoeff = orient.position === 'left' ? -4 : 4;
                    let tcoeff = orient.position === 'left' ? -6 : 6;
                    let txcoeff = orient.position === 'left' ? -10 : 10;
                    if (yaxis.fctv().length > 0) {
                        grp.addChild(new paper.Path.Line({ from: new paper.Point(containerxs + orient.move, containerys), to: new paper.Point(containerxs + orient.move, containerys + containerh), strokeWidth: lsw, strokeColor: lst }));
                        grp.addChild(new paper.PointText({ point: [containerxs + orient.move - txcoeff, containerys + containerh / 2], content: yaxis.title, fontSize: 12, fillColor: parsecolor(tst, mo), justification: 'center'}).rotate(270));
                    }

                    _.each(yaxis.fctv(), function(e, i) {
                        if (e !== undefined) {
                            let y = yaxis.fy(e);
                            e = computecoeff(e);
                            grp.addChild(new paper.Path.Line({from: new paper.Point(containerxs + orient.move, containerys + y), to: new paper.Point(containerxs + orient.move + lcoeff, containerys + y), strokeWidth: lsw, strokeColor: lst}));
                            grp.addChild(new paper.PointText({ point: [containerxs + orient.move + tcoeff, containerys + y + 3], content: e, fontSize: 10, fillColor: parsecolor(tst, mo), justification: tickanchor }));
                            _.each(me.getBindsFromYaxis(yaxis), function(b) {
                                let plot = b.plot;
                                let mo = me.charttemplate.getObject(b.plotname);
                                let containerw = mo.w();
                                let containerxs = mo.xs();
                                let containerys = mo.ys();
                                grp.addChild(new paper.Path.Line({from: new paper.Point(containerxs, containerys + y), to: new paper.Point(containerxs + containerw, containerys + y), strokeWidth: 0.2, strokeColor: "lightgray"}));
                            });
                        }
                    });
                }

                if (yaxis.type === 'polar') {
                    _.each(me.getBindsFromYaxis(yaxis), function(b) {
                        let plot = b.plot;
                        let mo = me.charttemplate.getObject(b.plotname);
                        let containerh = mo.h();
                        let containerw = mo.w();
                        let containerxm = mo.xm();
                        let containerym = mo.ym();
                        let lineproperties = yaxis.properties === undefined ? {} : yaxis.properties.line === undefined ? {} : yaxis.properties.line;
                        let textproperties = yaxis.properties === undefined ? {} : yaxis.properties.text === undefined ? {} : yaxis.properties.text;
                        let lsw = lineproperties["stroke-width"] === undefined ? 1 : lineproperties["stroke-width"];
                        let lst = lineproperties.stroke === undefined ? me.color(moid, "stroke") : lineproperties.stroke;
                        let tst = textproperties.fill === undefined ? me.color(moid, "stroke") : textproperties.fill;
                        let center = new paper.Point(containerxm, containerym);
                        let radius = _.min([containerw, containerh]) * 3 / 8;
                        _.each(yaxis.fctv(), function(e, i) {
                            if (e !== undefined) {
                                let y = yaxis.fy(e);
                                e = computecoeff(e);
                                let circle = new paper.Path.Circle(center, y);
                                circle.strokeColor = parsecolor("lightgray");
                                circle.strokeWidth = 0.5;
                                grp.addChild(circle);
                                grp.addChild(new paper.PointText({ point: [containerxm, containerym + y - radius], content: e, fontSize: 10, fillColor: parsecolor(tst, mo), justification: 'center' }));
                            }
                        });
                    });
                }

                me.paper.mainLayer.emit('draw', {});
            });
        }

        private drawYaxiss () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).yaxis !== undefined) {
                    me.dom[c] = new paper.Group();
                    log.debug("Defining drawing group:", c);
                    me.drawYaxis(c, false);
                }
            });
            me.paper.mainLayer.emit('draw', {});
        }

        public finalize () : void  {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).plot !== undefined) {
                    var plot = me.charttemplate.getObject(c).plot;
                    _.each(me.getBindsFromPlot(plot), function (b) {
                        b.dataset.reftime.finalize();
                        b.dataset.finalize();
                    });
                }
            });
        }

        public getBind (bid: string) : KaBound {
            let me = this;
            return me.bound[bid];
        }

        private getBindsFromLegend (legend: KaLegend) : KaBound[] {
            let me = this;
            let binds = [];
            _.each(me.bound, function(bind, bindid) {
                if (bind.legend === legend) {
                    binds.push(bind);
                }
            });
            return binds;
        }

        private getBindsFromPlot (plot: KaPlot) : KaBound[] {
            let me = this;
            let bindnames = [];
            let binds = [];
            _.each(plot.bounddataset.datasets, function (dataset) {
                binds.push(me.bound[dataset.bid]);
            });
            return _.sortBy(binds, function(bind) {
                return bind.id;
            });
        }

        private getBindsFromXaxis (xaxis: KaXaxis) : KaBound[] {
            let me = this;
            let binds = [];
            _.each(me.bound, function(bind, bindid) {
                if (bind.xaxis === xaxis) {
                    binds.push(bind);
                }
            });
            return binds;
        }

        private getBindsFromYaxis (yaxis: KaYaxis) : KaBound[] {
            let me = this;
            let binds = [];
            _.each(me.bound, function(bind, bindid) {
                if (bind.yaxis === yaxis) {
                    binds.push(bind);
                }
            });
            return binds;
        }

        public getLegend (lid: string) : KaLegend {
            let me = this;
            return me.charttemplate.getObject(lid).legend;
        }

        public getChartTemplate () : KaChartTemplate {
            let me = this;
            return me.charttemplate;
        }

        private getNeighboursFromPlot (plotname: string) : any {
            let me = this;
            let ret = {left: undefined, right: undefined, north: undefined, south: undefined};
            let horizontal = {};
            let vertical = {};
            horizontal[plotname] = me.charttemplate.getObject(plotname).xs();
            vertical[plotname] = me.charttemplate.getObject(plotname).ys();
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).plot !== undefined) {
                    if (me.charttemplate.getObject(c).ys() === vertical[plotname]) {
                        horizontal[c] = me.charttemplate.getObject(c).xs();
                    }
                    if (me.charttemplate.getObject(c).xs() === horizontal[plotname]) {
                        vertical[c] = me.charttemplate.getObject(c).ys();
                    }
                }
            });
            let h = _.map(_.sortBy(_.pairs(horizontal, function(p) {
                return p[1];
            })), function(p) {
                return p[0];
            });
            let v = _.map(_.sortBy(_.pairs(vertical, function(p) {
                return p[1];
            })), function(p) {
                return p[0];
            });
            ret.left = _.filter(h, function(e, i) {
                return i < _.indexOf(h, plotname);
            });
            ret.right = _.filter(h, function(e, i) {
                return i > _.indexOf(h, plotname);
            });
            ret.north = _.filter(v, function(e, i) {
                return i < _.indexOf(v, plotname);
            });
            ret.south = _.filter(v, function(e, i) {
                return i > _.indexOf(v, plotname);
            });
            return ret;
        }

        private getOptions (options: any) : void {
            let me = this;
            let opt = options === undefined ? {height: undefined, width: undefined, charttemplate: undefined } : options
            me.width = opt.width;
            me.height = opt.height;
            me.charttemplate = new ChartTemplate(me, opt.charttemplate);
        }

        public getPlot (pid: string) : KaPlot {
            let me = this;
            return me.charttemplate.getObject(pid).plot;
        }

        private getTitle (tid: string) : KaTitle {
            let me = this;
            return me.charttemplate.getObject(tid).title;
        }

        public getXaxis (xid : string) : KaXaxis {
            let me = this;
            return me.charttemplate.getObject(xid).xaxis;
        }

        public getYaxis (yid: string) : KaYaxis {
            let me = this;
            return me.charttemplate.getObject(yid).yaxis;
        }

        public getHeight () : number {
            let me = this;
            return me.height === undefined ? isNaN(window.innerHeight) ? window.clientHeight : window.innerHeight : me.height;
        }

        public getWidth () : number {
            let me = this;
            return me.width === undefined ? isNaN(window.innerWidth) ? window.clientWidth : window.innerWidth : me.width;
        }

        public keydown (keycode: number) : void {
            let me = this;
            // if (keycode === 70) { // f
            //     me.dispchartpdf();
            // }
            // if (keycode === 74) { // j
            //     me.dispchartjpg();
            // }
            // if (keycode === 80) { // p
            //     me.dispchartpng();
            // }
            // if (keycode === 83) { // s
            //     me.dispchartsvg();
            // }
        }

        private prepareXaxis (moid: string) : void {
            let me = this;
            postpone(0, function () {
                me.showWaiterProgress("Preparing xaxis: " + moid);
            });
            postpone(0, function() {
                log.debug("Preparing xaxis:", moid);
                let xaxis = me.getXaxis(moid);
                let reftime = xaxis.bounddataset.getRefTime();
                let f = function (a) {
                    let g = function (b) {
                        return _.contains(a, b.renderer.type);
                    };
                    return g;
                };
                xaxis.type = _.some(me.getBindsFromXaxis(xaxis), f(["WL", "WA", "WSA"])) ? 'polar' : xaxis.type;
                xaxis.type = _.some(me.getBindsFromXaxis(xaxis), f(["P"])) ? 'no' : xaxis.type;
                let width = xaxis.type === 'polar' ? 360 : me.charttemplate.getObject(moid).w(); 
                let borderpercent = xaxis.type === 'polar' ? 0 : 1;
                xaxis.reftime = reftime;
                let pz = xaxis.panzoom(xaxis.reftime, 12,  width, borderpercent, xaxis.translation, xaxis.zoom);
                if (xaxis.scaling === 'linear') {
                    xaxis.fx = pz.fx;
                    xaxis.rfx = pz.rfx;
                    xaxis.fctv = pz.fctv;
                }
                _.each(me.getBindsFromXaxis(xaxis), function(bind) {
                    bind.fx = xaxis.fx;
                });
                me.paper.mainLayer.emit('draw', {});
            });
        }

        private prepareXaxiss () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).xaxis !== undefined) {
                    me.prepareXaxis(c);
                }
            });
            me.paper.mainLayer.emit('draw', {});
        }

        private prepareYaxis (moid: string) : void {
            postpone(0, function () {
                me.showWaiterProgress("Preparing yaxis: " + moid);
            });
            let me = this;
            postpone(0, function () {
                log.debug("Preparing yaxis:", moid);
                let yaxis = me.getYaxis(moid);
                let options = {min: undefined, max: undefined};
                let f = function (a) {
                    let g = function (b) {
                        return _.contains(a, b.renderer.type);
                    };
                    return g;
                };
                yaxis.type = _.some(me.getBindsFromYaxis(yaxis), f(["WL", "WA", "WSA"])) ? 'polar' : yaxis.type;
                yaxis.type = _.some(me.getBindsFromYaxis(yaxis), f(["P"])) ? 'no' : yaxis.type;
                if (yaxis.minvalue !== undefined && yaxis.minvalue !== null) {
                    options.min = yaxis.minvalue;
                }
                if (yaxis.maxvalue !== undefined && yaxis.maxvalue !== null) {
                    options.max = yaxis.maxvalue;
                }
                let nice = yaxis.bounddataset.getVMinVMax(options);
                yaxis.bmin = nice.nicemin;
                yaxis.bmax = nice.nicemax;
                yaxis.step = nice.nicestep;
                yaxis.numticks = nice.niceticks;
                let wp = me.charttemplate.getObject(yaxis.oneplot).w();
                let hp = me.charttemplate.getObject(yaxis.oneplot).h();
                let height = yaxis.type === 'polar' ? _.min([wp, hp]) * 3 / 8 : me.charttemplate.getObject(moid).h(); 

                if (yaxis.scaling === 'linear') {
                    let a = height / (yaxis.bmax - yaxis.bmin);
                    let b = -a * yaxis.bmin;
                    yaxis.fy = function(y) {
                        return height - a * y - b;
                    };
                    yaxis.fctv = function() {
                        let r = [];
                        if (!isNaN(yaxis.numticks)) {
                            _.each(_.range(1, yaxis.numticks - 1), function(v) {
                                r.push(Math.round((yaxis.bmin + (yaxis.step * v)) * 1000000) / 1000000);
                            });
                        }
                        return r;
                    };
                }

                _.each(me.getBindsFromYaxis(yaxis), function(bind) {
                    bind.fy = yaxis.fy;
                    bind.bmin = yaxis.bmin;
                });
                me.paper.mainLayer.emit('draw', {});
            });
        };


        private prepareYaxiss () : void {
            let me = this;
            _.each(me.charttemplate.objects, function(v, c) {
                if (me.charttemplate.getObject(c).yaxis !== undefined) {
                    me.prepareYaxis(c);
                }
            });
            me.paper.mainLayer.emit('draw', {});
        }

        private unbind (bid: string) : void {
            let me = this;
            if (bid === undefined) {
                throw '*** A bind must have an id!';
            }
            me.getBind(bid).plot.bounddataset.pop(bid);
            me.getBind(bid).xaxis.bounddataset.pop(bid);
            me.getBind(bid).yaxis.bounddataset.pop(bid);
            me.getBind(bid).legend.bounddataset.pop(bid);
            delete me.bound[bid];
        };


    }

    export class Dataset implements KaDataset {

        private finalized: boolean;
        private index: any;
        private reverse: any;
        private sorted: any;

        public base: KaMatrix;
        public color: any;
        public data: KaMatrix;
        public hidden: boolean[];
        public info: any;
        public labels: string[];
        public onclick: any;
        public reftime: KaRefTime;

        constructor (reftime: KaRefTime) {
            let me = this;
            me.color = {};
            me.finalized = false;
            me.hidden=[];
            me.index = {};
            me.info = {};
            me.onclick = {};
            me.reftime = reftime;
            me.sorted = {};
        }

        public computeBase () : void {
            let me = this;
            let nl = me.labels.length;
            let matbase = new Matrix(nl, nl);
            _.each(me.sorted.direct, function (v, k) {
                _.each(_.range(nl), function (j) {
                    if (me.sorted.reverse[j] < k && ! me.hidden[j]) {
                        matbase.setValue(v, j, 1);
                    }
                });
            });
            me.base = matbase.multiply(me.data);
        }

        public finalize () : void {
            let me = this;
            if (! me.finalized) {
                me.labels = _.keys(me.index);
                _.each(me.labels, function (l,i) {
                    me.hidden[i] = false;
                })
                let nl = me.labels.length;
                let nc = me.reftime.timestamps.nc;
                me.data = new Matrix(nl, nc);
                me.reftime.timestamps.each(function (t, i, j) {
                    _.each(me.labels, function (l, il) {
                        if (me.index[l][t] !== undefined) {
                            me.data.setValue(il, j, me.index[l][t]);
                        }
                    });
                });
                let sum = function (x, y) {return x + y};
                let reverse = function (x) {return -x};
                me.sorted = me.data.reduce([], sum).sort(reverse);
                me.finalized = true;
            }
        }

        public flipflop (pathid: number) : boolean {
            let me = this;
            me.hidden[pathid] = ! me.hidden[pathid];
            return me.hidden[pathid];
        }

        public getAngles (pid: number) : number[] {
            let me = this;
            let totalw = 0;
            let basew = 0;
            let itemw = 0;
            let found = false;
            let sum = function (x, y) {return x + y};
            let weights = me.data.reduce([], sum);
            _.each(me.getOrderedPaths(), function(id) {
                let w = weights.getValue(id, 0);
                totalw = me.hidden[id] ? totalw : totalw + w;
                itemw = pid == id ? me.hidden[id] ? 0 : w : itemw;
                found = pid == id ? true : found;
                basew = found ? basew : me.hidden[id] ? basew : basew + w;
            });
            let alpha = Math.PI * 2 * basew / totalw;
            let beta = Math.PI * 2 * itemw / totalw;
            return [alpha, beta];
        }

        public getColor (label: string, prefix: string, suggest: string) : string {
            let me = this;
            let md5 = CryptoJS.MD5(prefix + label);
            return suggest === undefined ? d3.rgb('#' + md5.toString().substring(0, 6)) : suggest;
        }

        public getOrderedPaths () : number[] {
            let me = this;
            let r = [];
            _.each(me.sorted.direct, function (v,k) {
                r[k] = v;
            });
            return r;
        }

        private getVisiblePaths () : number[] {
            let me = this;
            let r = [];
            _.each(me.hidden, function(v,i) {
                if (!v) {
                    r.push(i);
                }
            });
            return r;
        }

        private getVMax (options: any) : number {
            let me = this;
            let opt = {stacked: false};
            opt.stacked = options !== undefined ? options.stacked : false;
            let max = function (x, y) {return x > y ? x : y};
            let x = undefined;
            if (opt.stacked) {
                x = me.data.add(me.base).reduce([], max).transpose();
            } else {
                x = me.data.reduce([], max).transpose();
            }
            return x.reduce(me.getVisiblePaths(), max).getValue(0,0);
        }

        private getVMin (options: any) : number {
            let me = this;
            let opt = {stacked: false};
            opt.stacked = options !== undefined ? options.stacked : false;
            let min = function (x, y) {return x < y ? x : y};
            let x = undefined;
            if (opt.stacked) {
                x = me.data.add(me.base).reduce([], min).transpose();
            } else {
                x = me.data.reduce([], min).transpose();
            }
            return x.reduce(me.getVisiblePaths(), min).getValue(0,0);
        }

        public store = function (row) {
            let me = this;
            let date = me.reftime.store(row);
            me.index[row.label] = me.index[row.label] === undefined ? {} : me.index[row.label];
            me.index[row.label][date] = parseFloat(row.value);
        }

    }

    class Legend implements KaLegend {

        private id: string;

        public bounddataset: KaBoundDataset;

        constructor (lid: string) {
            let me = this;
            me.id = lid;
            me.bounddataset = new BoundDataset([]);
        }
    }

    class Matrix implements KaMatrix {

        private data: any;

        public nc: number;
        public nl: number;

        constructor (nl: number, nc: number) {
            let me = this;
            me.data = new Float64Array(nl * nc);
            me.nl = nl;
            me.nc = nc;
        }

        public add (m: KaMatrix) : KaMatrix {
            let me = this;
            let r = new Matrix (me.nl, me.nc);
            _.each(_.range(me.nc), function (j) {
                _.each(_.range(me.nl), function (i) {
                    r.setValue(i,j, me.getValue(i, j) + m.getValue(i, j));
                });
            });
            return r;
        }

        public each (callee: any): void {
            let me = this;
            _.each(_.range(me.nl), function (i) {
                _.each(_.range(me.nc), function (j) {
                    let v = me.getValue(i,j);
                    callee(v, i, j);
                });
            });
        }

        public getValue (i: number, j: number): number {
            let me = this;
            let k = i * me.nc + j;
            return me.data[k];
        }

        public multiply (m: KaMatrix): KaMatrix {
            let me = this;
            if (me.nc !== m.nl) {
                throw 'Invalid matrix product';
            }
            let r = new Matrix(me.nl, m.nc);
            _.each(_.range(m.nc), function(j) {
                _.each(_.range(me.nl), function(i) {
                    let e = 0;
                    _.each(_.range(me.nc), function (k) {
                        let y = m.getValue(k,j);
                        if (y !== 0) {
                            let x = me.getValue(i,k);
                            if (x !== 0) {
                                e += x * y;
                            }
                        }
                    });
                    r.setValue(i, j, e);
                });
            });
            return r;
        }

        public reduce (ic: number[], callee: any): KaMatrix {
            let me = this;
            let reduced = new Matrix(me.nl, 1);
            ic = ic === undefined || ic.length === 0 ? _.range(me.nc) : ic;
            _.each(_.range(me.nl), function (i) {
                reduced.setValue(i, 0, _.reduce(_.map(ic, function (j) {
                    return me.getValue(i,j);
                }), function (c, e) {
                    return callee(c, e);
                }, 0));
            });
            return reduced;
        }

        public transpose () : KaMatrix {
            let me = this;
            let r = new Matrix (me.nc, me.nl);
            _.each(_.range(me.nc), function (j) {
                _.each(_.range(me.nl), function (i) {
                    if (me.getValue(i,j) !== 0) {
                        r.setValue(j, i, me.getValue(i, j));
                    }
                });
            });
            return r;
        }

        public setValue (i: number, j: number, v: number): void {
            let me = this;
            let k = i * me.nc + j;
            me.data[k] = v;
        }

        public sort (callee: any): any {
            let me = this;
            if (me.nc !== 1) {
                throw 'Operation not supported with a number of columns not equal 1';
            }
            let r = {direct: {}, reverse: {}};
            let arv = [];
            me.each(function (v, i, j) {
                arv.push({v: v, i: i});
            });
            let sa = _.sortBy(arv, function (e) {
                return callee(e.v);
            });
            _.each(sa, function (e, i) {
                r.direct[i] = e.i;
                r.reverse[e.i] = i;
            });
            return r;
        }
    }

    class ChartTemplate implements KaChartTemplate {

        private chart: KaChart;
        private lines: any[];
        private columns: any[];
        public objects: any;

        constructor (chart: KaChart, options?: any) {
            let me = this;
            me.chart = chart;
            me.getOptions(options);
            me.setFunctions();
        }

        private getAllColumnsWeight () {
            let me = this;
            let w = 0;
            _.each(me.columns, function(c) {
                w += c.weight;
            });
            return w;
        }

        private getAllLinesWeight () {
            let me = this;
            let w = 0;
            _.each(me.lines, function(l) {
                w += l.weight;
            });
            return w;
        }

        private getColumn (mcid: number) : any {
            let me = this;
            return me.columns[mcid];
        }

        private getHeight () : number {
            let me = this;
            return me.chart.getHeight()
        }

        private getLine (mlid: number) : any {
            let me = this;
            return me.lines[mlid];
        }

        public getObject (moid: string) : any {
            let me = this;
            return me.objects[moid];
        }

        private getOptions (options: any) : void {
            let me = this;
            let opt = options === undefined ? {lines: [], columns: [], objects: {}} : options;
            if (typeof opt === 'string') {
                opt = JSON.parse(opt);
            }
            _.each(opt, function (xxx, e) {
                me[e] = opt[e];
            });
        }

        private getUnresizableVisibleColumnsWeight () : number {
            let me = this;
            let w = 0;
            _.each(me.columns, function(c) {
                if (!c.resizable && !c.hidden) {
                    w += c.weight;
                }
            });
            return w;
        }

        private getUnresizableVisibleLinesWeight () : number {
            let me = this;
            let w = 0;
            _.each(me.lines, function(l) {
                if (!l.resizable && !l.hidden) {
                    w += l.weight;
                }
            });
            return w;
        }

        private getVisibleAndResizableColumnsWeight () : number {
            let me = this;
            let w = 0;
            _.each(me.columns, function(c) {
                if (c.resizable && !c.hidden) {
                    w += c.weight;
                }
            });
            return w;
        }

        private getVisibleAndResizableLinesWeight () : number {
            let me = this;
            let w = 0;
            _.each(me.lines, function(l) {
                if (l.resizable && !l.hidden) {
                    w += l.weight;
                }
            });
            return w;
        }

        private getWidth () : number {
            let me = this;
            return me.chart.getWidth();
        }

        public jsonify () : string {
            let me = this;
            let o = {};
            _.each(me, function (xxx, e) {
                if (e !== 'chart') {
                    o[e] = me[e];
                }
            })
            return JSON.stringify(o);
        }

        public setColumn (mcoptions: any) : any {
            let me = this;
            let mc = { id: me.columns.length, weight: 100, resizable: true, hidden: false };
            _.each(mcoptions, function (xxx, o) {
                mc.hidden = o === 'hidden' ? mcoptions.hidden : mc.hidden;
                mc.resizable = o === 'resizable' ? mcoptions.resizable : mc.resizable;
                mc.weight = o === 'weight' ? mcoptions.weight : mc.weight;
            });
            me.columns.push(mc);
            me.setFunctions("c", mc);
            return mc;
        }

        private setFunctions (mot?: string, mo?: any) : void {
            let me = this;

            let fcolumns = { h: undefined, hide: undefined, unhide: undefined, w: undefined, xe: undefined, xm: undefined, xs: undefined, ye: undefined, ym: undefined, ys: undefined};
            let flines = { h: undefined, hide: undefined, unhide: undefined, w: undefined, xe: undefined, xm: undefined, xs: undefined, ye: undefined, ym: undefined, ys: undefined};
            let fobjects = { h: undefined, hidecolumns: undefined, hidelines: undefined, unhidecolumns: undefined, unhidelines: undefined, w: undefined, xe: undefined, xm: undefined, xs: undefined, ye: undefined, ym: undefined, ys: undefined };


            fcolumns.h = function () : number {
                return Math.round(me.getHeight());
            };

            fcolumns.hide = function () : void {
                let c = this;
                c.hidden = true;
            };

            fcolumns.unhide = function () : void  {
                let c = this;
                c.hidden = false;
            };

            fcolumns.w = function () : number {
                let c = this;
                return c.hidden ? 0 : c.resizable ? Math.round(c.weight * me.getWidth() * (me.getAllColumnsWeight() - me.getUnresizableVisibleColumnsWeight()) / me.getAllColumnsWeight() / me.getVisibleAndResizableColumnsWeight()) : Math.round(c.weight * me.getWidth() / me.getAllColumnsWeight());
            };

            fcolumns.xe = function () : number {
                let c = this;
                return Math.round(c.xs() + c.w());
            };

            fcolumns.xm = function () : number {
                let c = this;
                return Math.round(c.xs() + (c.w() / 2));
            };

            fcolumns.xs = function () : number {
                let c = this;
                return c.id === 0 ? 0 : Math.round(me.getColumn(c.id - 1).xe());
            };

            fcolumns.ye = function () : number {
                return Math.round(me.getHeight());
            };

            fcolumns.ym = function () : number {
                return Math.round(me.getHeight() / 2);
            };

            fcolumns.ys = function () : number {
                return 0;
            };

            flines.h = function () : number {
                let l = this;
                return l.hidden ? 0 : l.resizable ? Math.round(l.weight * me.getHeight() * (me.getAllLinesWeight() - me.getUnresizableVisibleLinesWeight()) / me.getAllLinesWeight() / me.getVisibleAndResizableLinesWeight()) : Math.round(l.weight * me.getHeight() / me.getAllLinesWeight());
            };

            flines.hide = function () : void {
                let l = this;
                l.hidden = true;
            };

            flines.unhide = function () : void {
                let l = this;
                l.hidden = false;
            };

            flines.w = function () : number {
                return Math.round(me.getWidth());
            };

            flines.xs = function () : number {
                return 0;
            };

            flines.xe = function () : number {
                return Math.round(me.getWidth());
            };

            flines.xm = function () : number {
                return Math.round(me.getWidth() / 2);
            };

            flines.ys = function () : number {
                let l = this;
                return l.id === 0 ? 0 : Math.round(me.getLine(l.id - 1).ye());
            };

            flines.ym = function () : number {
                let l = this;
                return Math.round(l.ys() + (l.h() / 2));
            };

            flines.ye = function () : number{
                let l = this;
                return Math.round(l.ys() + l.h());
            };

            fobjects.h = function () : number {
                let o = this;
                let bline = o.bline;
                let eline = o.eline;
                let h = 0;
                bline = bline < 0 ? bline + me.lines.length : bline;
                eline = eline < 0 ? eline + me.lines.length : eline;
                _.each(me.lines, function (l, i) {
                    if (i >= bline && i <= eline) {
                        h += me.getLine(i).h();
                    }
                });
                return Math.round(h);
            };

            fobjects.hidecolumns = function () : void {
                let o = this;
                let bcolumn = o.bcolumn;
                let ecolumn = o.ecolumn;
                bcolumn = bcolumn < 0 ? bcolumn + me.columns.length : bcolumn;
                ecolumn = ecolumn < 0 ? ecolumn + me.columns.length : ecolumn;
                for (let c = bcolumn; c < ecolumn + 1; c++) {
                    me.getColumn(c).hide();
                }
            };

            fobjects.hidelines = function () : void {
                let o = this;
                let bline = o.bline;
                let eline = o.eline;
                bline = bline < 0 ? bline + me.lines.length : bline;
                eline = eline < 0 ? eline + me.lines.length : eline;
                for (let l = bline; l < eline + 1; l++) {
                    me.getLine(l).hide();
                }
            };

            fobjects.unhidecolumns = function () : void {
                let o = this;
                let bcolumn = o.bcolumn;
                let ecolumn = o.ecolumn;
                bcolumn = bcolumn < 0 ? bcolumn + me.columns.length : bcolumn;
                ecolumn = ecolumn < 0 ? ecolumn + me.columns.length : ecolumn;
                for (let c = bcolumn; c < ecolumn + 1; c++) {
                    me.getColumn(c).unhide();
                }
            };

            fobjects.unhidelines = function () : void {
                let o = this;
                let bline = o.bline;
                let eline = o.eline;
                bline = bline < 0 ? bline + me.lines.length : bline;
                eline = eline < 0 ? eline + me.lines.length : eline;
                for (let l = bline; l < eline + 1; l++) {
                    me.getLine(l).unhide();
                }
            };

            fobjects.w = function () : number {
                let o = this;
                let bcolumn = o.bcolumn;
                let ecolumn = o.ecolumn;
                let w = 0;
                bcolumn = bcolumn < 0 ? bcolumn + me.columns.length : bcolumn;
                ecolumn = ecolumn < 0 ? ecolumn + me.columns.length : ecolumn;
                _.each(me.columns, function (c, i) {
                    if (i >= bcolumn && i <= ecolumn) {
                        w += me.getColumn(i).w();
                    }
                });
                return Math.round(w);
            };

            fobjects.xe = function () : number {
                let o = this;
                let ecolumn = o.ecolumn;
                ecolumn = ecolumn < 0 ? ecolumn + me.columns.length : ecolumn;
                return Math.round(me.getColumn(ecolumn).xe());
            };

            fobjects.xm = function () : number {
                let o = this;
                return Math.round((o.xe() + o.xs()) / 2);
            };

            fobjects.xs = function () : number {
                let o = this;
                let bcolumn = o.bcolumn;
                bcolumn = bcolumn < 0 ? bcolumn + me.columns.length : bcolumn;
                return Math.round(me.getColumn(bcolumn).xs());
            };

            fobjects.ye = function () : number {
                let o = this;
                let eline = o.eline;
                eline = eline < 0 ? eline + me.lines.length : eline;
                return Math.round(me.getLine(eline).ye());
            };

            fobjects.ym = function () : number {
                let o = this;
                return Math.round((o.ye() + o.ys()) / 2);
            };

            fobjects.ys = function () : number {
                let o = this;
                let bline = o.bline;
                bline = bline < 0 ? bline + me.lines.length : bline;
                return Math.round(me.getLine(bline).ys());
            };

            if (mo !== undefined) {
                if (mot === 'c') {
                    _.each(fcolumns, function (xxx, f) {
                        mo[f] = fcolumns[f];
                    });
                }
                if (mot === 'l') {
                    _.each(flines, function (xxx, f) {
                        mo[f] = flines[f];
                    });
                }
                if (mot === 'o') {
                    _.each(fobjects, function (xxx, f) {
                        mo[f] = fobjects[f];
                    });
                }
            } else {
                _.each(me.columns, function (c) {
                    _.each(fcolumns, function (xxx, f) {
                        c[f] = fcolumns[f];
                    });
                });
                _.each(me.lines, function (l) {
                    _.each(fcolumns, function (xxx, f) {
                        l[f] = fcolumns[f];
                    });
                });
                _.each(me.objects, function (o) {
                    _.each(fcolumns, function (xxx, f) {
                        o[f] = fcolumns[f];
                    });
                });
            }

        }

        public setLine (mloptions: any) : any {
            let me = this;
            let ml = { id: me.lines.length, weight: 100, resizable: true, hidden: false };
            _.each(mloptions, function (xxx, o) {
                ml.hidden = o === 'hidden' ? mloptions.hidden : ml.hidden;
                ml.resizable = o === 'resizable' ? mloptions.resizable : ml.resizable;
                ml.weight = o === 'weight' ? mloptions.weight : ml.weight;
            });
            me.lines.push(ml);
            me.setFunctions("l", ml);
            return ml;
        }

        public setObject (moid: string, mooptions: any) : any {
            let me = this;
            let mo = { bline: 0, eline: -1, bcolumn:0, ecolumn: -1};
            _.each(mooptions, function (xxx, o) {
                mo[o] = mooptions[o];
            });
            me.objects[moid] = mo;
            me.setFunctions("o", mo);
            return mo;
        }

    }

    class Plot implements KaPlot {

        private id: string;

        public angleslice: number;
        public axisgrid: any;
        public bounddataset: KaBoundDataset;
        public height: number;
        public numylabels: number;
        public oneplot: string;
        public radar: any;
        public radarline: any;
        public radius: number;
        public raxis: any;
        public rscale: any;
        public width: number;
        public ylabels: number[];

        constructor (pid: string) {
            let me = this;
            me.id = pid;
            me.bounddataset = new BoundDataset([]);
        }
    }

    export class Point implements KaPoint {

        public hidden: boolean;
        public id: string;
        public value: number;
        public leftNeighbour: KaPoint;
        public rightNeighbour: KaPoint;

        constructor (label: string, value: number) {
            let me = this;
            me.id = label;
            me.value = value;
            me.hidden = false;
            me.leftNeighbour = undefined;
            me.rightNeighbour = undefined;
        }
    }

    export class RefTime implements KaRefTime {

        private finalized: boolean;
        private index: any;

        public timestamps: KaMatrix;

        constructor () {
            let me = this;
                me.finalized = false;
                me.index = {};
        }

        public finalize () : void {
            let me = this;
            if (! me.finalized) {
                let nc = _.keys(me.index).length;
                me.timestamps = new Matrix(1, nc);
                _.each(_.sortBy(_.keys(me.index), function (x) { return x; }), function (t, i) {
                    me.timestamps.setValue(0, i, t);
                });
                me.finalized = true;               
            }
        }

        public store (ref: any) : number {
            let me = this;
            let timestamp = ref.timestamp;
            let pyear = parseInt(timestamp.substr(0, 4), 10);
            let pmonth = parseInt(timestamp.substr(4, 2), 10) - 1;
            let pday = parseInt(timestamp.substr(6, 2), 10);
            let phour = parseInt(timestamp.substr(8, 2), 10);
            let pminute = parseInt(timestamp.substr(10, 2), 10);
            let psecond = parseInt(timestamp.substr(12, 2), 10);
            let pmilli = parseInt(timestamp.substr(14, 3), 10);
            let date = new Date(Date.UTC(pyear, pmonth, pday, phour, pminute, psecond, pmilli)).getTime();
            me.index[date] = null;
            return date;
        }
    }

    class Title implements KaTitle {

        private id: string;

        public properties: any;
        public title: string;

        constructor (tid: string, title: string, properties: any) {
            let me = this;
            me.id = tid;
            me.title = title;
            me.properties = properties;
        }
    }

    class Xaxis implements KaXaxis {

        private id: string;
        private title: string;

        public bounddataset: KaBoundDataset;
        public oneplot: string;
        public properties: any;
        public reftime: KaRefTime;
        public scaling: string;
        public translation: number;
        public type: string;
        public zoom: number;

        constructor (xid: string, title: string, scaling: string, properties: any) {
            let me = this;
            me.id = xid;
            me.title = title;
            me.type = 'linear';
            me.scaling = scaling;
            me.properties = properties;
            me.bounddataset = new BoundDataset([]);
        }

        public panzoom (reftime: KaRefTime, maxticks: number, width: number, borderpercent: number, translation: number, zoom: number) : any {
            let me = this;
            let genfx = function(minv: number, maxv: number, width: number, borderpercent: number, reverse: boolean): any {
                let a = width * (100 - borderpercent * 2) / 100 / (maxv - minv);
                let b = -a * minv + (width * borderpercent / 100);
                let f = function(x: number): number {
                    return a * x + b;
                };
                let rf = function(y: number): any {
                    return new Date((y - b) / a);
                };
                let r = reverse ? rf : f;
                return r;
            };
            let gengx = function(reverse: boolean): any {
                let a = me.zoom === undefined ? 1 : me.zoom;
                let b = me.translation === undefined ? 0 : me.translation;
                let f = function(x: number): number {
                    return a * x + b;
                };
                let rf = function(y: number): number {
                    return (y - b) / a;
                };
                let r = reverse ? rf : f;
                return r;
            };
            let genhx = function(minv: number, maxv: number, width: number, borderpercent: number, reverse: boolean): any {
                let fx = genfx(minv, maxv, width, borderpercent, reverse);
                let gx = gengx(reverse);
                let f = function(x) {
                    return gx(fx(x));
                };
                let rf = function(y) {
                    return fx(gx(y));
                };
                let r = reverse ? rf : f;
                return r;
            };
            let nice = nicedate(reftime.timestamps.getValue(0, 0), reftime.timestamps.getValue(0, reftime.timestamps.nc - 1), maxticks);
            let hx = genhx(nice.nicemin, nice.nicemax, width, borderpercent, false);
            let rhx = genhx(nice.nicemin, nice.nicemax, width, borderpercent, true);
            let nicef = nicedate(rhx(0), rhx(width), maxticks);

            let fctv = function() {
                return nicef.ticks;
            };
            return { fx: hx, rfx: rhx, fctv: fctv };
        }

        public fctv () : number[] {
            return [];
        }

        public fx (x: any) : number {
            return 0;
        }

        public rfx (x: number) : any {
            return {};
        }

    }

    class Yaxis implements KaYaxis {

        private id: string;

        public bmin: number;
        public bmax: number;
        public bounddataset: KaBoundDataset;
        public minvalue: number;
        public maxvalue: number;
        public numticks: number;
        public oneplot: any;
        public position: string;
        public properties: any;
        public scaling: string;
        public step: number;
        public title: string;
        public type: string;

        constructor (yid: string, title: string, position: string, scaling: string, properties: any, minvalue: number, maxvalue: number) {
            let me = this;
            me.id = yid;
            me.title = title;
            me.type = 'linear';
            me.position = position;
            me.scaling = scaling;
            me.properties = properties;
            me.minvalue = minvalue;
            me.maxvalue = maxvalue;
            me.bounddataset = new BoundDataset([]);
        }

        public fctv () : number[] {
            return [];
        }

        public fy (x: number) : number {
            return 0;
        }
    }

}