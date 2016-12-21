class UserObject(dict):
    def __init__(s):
        object = {
            "type" : "template",
            "id" : "DEFAULT",
            "lines": [
                { "weight": 10, "resizable": False }, # top border
                { "weight": 30, "resizable": False }, # title
                { "weight": 20, "resizable": False }, #subtitle
                { "weight": 20, "resizable": False, "hidden": False }, # title area 0
                { "weight": 80, "resizable": True, "hidden": False }, # area 0
                { "weight": 20, "resizable": False, "hidden": True }, # title area 1
                { "weight": 80, "resizable": True, "hidden": True }, # area 1
                { "weight": 20, "resizable": False, "hidden": True }, # title area 2
                { "weight": 80, "resizable": True, "hidden": True }, # area 2
                { "weight": 20, "resizable": False, "hidden": True }, # title area 3
                { "weight": 80, "resizable": True, "hidden": True }, # area 3
                { "weight": 20, "resizable": False, "hidden": True }, # title area 4
                { "weight": 80, "resizable": True, "hidden": True }, # area 4
                { "weight": 20, "resizable": False, "hidden": True }, # title area 5
                { "weight": 80, "resizable": True, "hidden": True }, # area 5
                { "weight": 20, "resizable": False, "hidden": True }, # title area 6
                { "weight": 80, "resizable": True, "hidden": True }, # area 6
                { "weight": 20, "resizable": False, "hidden": True }, # title area 7
                { "weight": 80, "resizable": True, "hidden": True }, # area 7
                { "weight": 30, "resizable": False }, # xaxis area
                { "weight": 80, "resizable": False }, # legend area
                { "weight": 10, "resizable": False }, # bottom border
            ],
            "columns": [
                { "weight": 10, "resizable": False }, # left border
                { "weight": 50, "resizable": False, "hidden": False }, # yaxis left 0
                { "weight": 50, "resizable": False, "hidden": True }, # yaxis left 1
                { "weight": 50, "resizable": False, "hidden": True }, # yaxis left 2
                { "weight": 100, "resizable": True, "hidden": False }, # area 0
                { "weight": 100, "resizable": True, "hidden": True }, # area 1
                { "weight": 100, "resizable": True, "hidden": True }, # area 2
                { "weight": 100, "resizable": True, "hidden": True }, # area 3
                { "weight": 100, "resizable": True, "hidden": True }, # area 4
                { "weight": 100, "resizable": True, "hidden": True }, # area 5
                { "weight": 100, "resizable": True, "hidden": True }, # area 6
                { "weight": 100, "resizable": True, "hidden": True }, # area 7
                { "weight": 50, "resizable": False, "hidden": True }, # yaxis right 0
                { "weight": 50, "resizable": False, "hidden": True }, # yaxis right 1
                { "weight": 50, "resizable": False, "hidden": True }, # yaxis right 2
                { "weight": 10, "resizable": False }, # right border
            ],
            "main": { "style": { "fill": "white", "stroke": "black" }},
            "margintop": { "eline": 0 },
            "marginbottom": { "bline": -1 },
            "marginleft": { "ecolumn": 0 },
            "marginright": { "bcolumn": -1 },
            "title": { "bline": 1, "eline": 1, "bcolumn": 4, "ecolumn": -5},
            "subtitle": { "bline": 2, "eline": 2, "bcolumn": 4, "ecolumn": -5},
            "yaxis0left0": { "bline": 3, "eline": 4, "bcolumn": 1, "ecolumn": 1},
            "yaxis1left0": { "bline": 5, "eline": 6, "bcolumn": 1, "ecolumn": 1},
            "yaxis2left0": { "bline": 7, "eline": 8, "bcolumn": 1, "ecolumn": 1},
            "yaxis3left0": { "bline": 9, "eline": 10, "bcolumn": 1, "ecolumn": 1},
            "yaxis4left0": { "bline": 11, "eline": 12, "bcolumn": 1, "ecolumn": 1},
            "yaxis5left0": { "bline": 13, "eline": 14, "bcolumn": 1, "ecolumn": 1},
            "yaxis6left0": { "bline": 15, "eline": 16, "bcolumn": 1, "ecolumn": 1},
            "yaxis7left0": { "bline": 17, "eline": 18, "bcolumn": 1, "ecolumn": 1},
            "yaxis0left1": { "bline": 3, "eline": 4, "bcolumn": 2, "ecolumn": 2},
            "yaxis1left1": { "bline": 5, "eline": 6, "bcolumn": 2, "ecolumn": 2},
            "yaxis2left1": { "bline": 7, "eline": 8, "bcolumn": 2, "ecolumn": 2},
            "yaxis3left1": { "bline": 9, "eline": 10, "bcolumn": 2, "ecolumn": 2},
            "yaxis4left1": { "bline": 11, "eline": 12, "bcolumn": 2, "ecolumn": 2},
            "yaxis5left1": { "bline": 13, "eline": 14, "bcolumn": 2, "ecolumn": 2},
            "yaxis6left1": { "bline": 15, "eline": 16, "bcolumn": 2, "ecolumn": 2},
            "yaxis7left1": { "bline": 17, "eline": 18, "bcolumn": 2, "ecolumn": 2},
            "yaxis0left2": { "bline": 3, "eline": 4, "bcolumn": 3, "ecolumn": 3},
            "yaxis1left2": { "bline": 5, "eline": 6, "bcolumn": 3, "ecolumn": 3},
            "yaxis2left2": { "bline": 7, "eline": 8, "bcolumn": 3, "ecolumn": 3},
            "yaxis3left2": { "bline": 9, "eline": 10, "bcolumn": 3, "ecolumn": 3},
            "yaxis4left2": { "bline": 11, "eline": 12, "bcolumn": 3, "ecolumn": 3},
            "yaxis5left2": { "bline": 13, "eline": 14, "bcolumn": 3, "ecolumn": 3},
            "yaxis6left2": { "bline": 15, "eline": 16, "bcolumn": 3, "ecolumn": 3},
            "yaxis7left2": { "bline": 17, "eline": 18, "bcolumn": 3, "ecolumn": 3},
            "plot00": { "bline": 3, "eline": 4, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot10": { "bline": 5, "eline": 6, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot20": { "bline": 7, "eline": 8, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot30": { "bline": 9, "eline": 10, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot40": { "bline": 11, "eline": 12, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot50": { "bline": 13, "eline": 14, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot60": { "bline": 15, "eline": 16, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot70": { "bline": 17, "eline": 18, "bcolumn": 4, "ecolumn": 4, "style": { "fill": "white", "stroke": "black" }},
            "plot01": { "bline": 3, "eline": 4, "bcolumn": 5, "ecolumn": 5, "style": { "fill": "white", "stroke": "black" }},
            "plot02": { "bline": 3, "eline": 4, "bcolumn": 6, "ecolumn": 6, "style": { "fill": "white", "stroke": "black" }},
            "plot03": { "bline": 3, "eline": 4, "bcolumn": 7, "ecolumn": 7, "style": { "fill": "white", "stroke": "black" }},
            "plot04": { "bline": 3, "eline": 4, "bcolumn": 8, "ecolumn": 8, "style": { "fill": "white", "stroke": "black" }},
            "plot05": { "bline": 3, "eline": 4, "bcolumn": 9, "ecolumn": 9, "style": { "fill": "white", "stroke": "black" }},
            "plot06": { "bline": 3, "eline": 4, "bcolumn": 10, "ecolumn": 10, "style": { "fill": "white", "stroke": "black" }},
            "plot07": { "bline": 3, "eline": 4, "bcolumn": 11, "ecolumn": 11, "style": { "fill": "white", "stroke": "black" }},
            "plottitle00": { "bline": 3, "eline": 3, "bcolumn": 4, "ecolumn": 4 },
            "plottitle10": { "bline": 5, "eline": 5, "bcolumn": 4, "ecolumn": 4 },
            "plottitle20": { "bline": 7, "eline": 7, "bcolumn": 4, "ecolumn": 4 },
            "plottitle30": { "bline": 9, "eline": 9, "bcolumn": 4, "ecolumn": 4 },
            "plottitle40": { "bline": 11, "eline": 11, "bcolumn": 4, "ecolumn": 4 },
            "plottitle50": { "bline": 13, "eline": 13, "bcolumn": 4, "ecolumn": 4 },
            "plottitle60": { "bline": 15, "eline": 15, "bcolumn": 4, "ecolumn": 4 },
            "plottitle70": { "bline": 17, "eline": 17, "bcolumn": 4, "ecolumn": 4 },
            "plottitle01": { "bline": 3, "eline": 3, "bcolumn": 5, "ecolumn": 5 },
            "plottitle02": { "bline": 3, "eline": 3, "bcolumn": 6, "ecolumn": 6 },
            "plottitle03": { "bline": 3, "eline": 3, "bcolumn": 7, "ecolumn": 7 },
            "plottitle04": { "bline": 3, "eline": 3, "bcolumn": 8, "ecolumn": 8 },
            "plottitle05": { "bline": 3, "eline": 3, "bcolumn": 9, "ecolumn": 9 },
            "plottitle06": { "bline": 3, "eline": 3, "bcolumn": 10, "ecolumn": 10 },
            "plottitle07": { "bline": 3, "eline": 3, "bcolumn": 11, "ecolumn": 11 },
            "yaxis0right0": { "bline": 3, "eline": 4, "bcolumn": -4, "ecolumn": -4},
            "yaxis1right0": { "bline": 5, "eline": 6, "bcolumn": -4, "ecolumn": -4},
            "yaxis2right0": { "bline": 7, "eline": 8, "bcolumn": -4, "ecolumn": -4},
            "yaxis3right0": { "bline": 9, "eline": 10, "bcolumn": -4, "ecolumn": -4},
            "yaxis4right0": { "bline": 11, "eline": 12, "bcolumn": -4, "ecolumn": -4},
            "yaxis5right0": { "bline": 13, "eline": 14, "bcolumn": -4, "ecolumn": -4},
            "yaxis6right0": { "bline": 15, "eline": 16, "bcolumn": -4, "ecolumn": -4},
            "yaxis7right0": { "bline": 17, "eline": 18, "bcolumn": -3, "ecolumn": -3},
            "yaxis0right1": { "bline": 3, "eline": 4, "bcolumn": -3, "ecolumn": -3},
            "yaxis1right1": { "bline": 5, "eline": 6, "bcolumn": -3, "ecolumn": -3},
            "yaxis2right1": { "bline": 7, "eline": 8, "bcolumn": -3, "ecolumn": -3},
            "yaxis3right1": { "bline": 9, "eline": 10, "bcolumn": -3, "ecolumn": -3},
            "yaxis4right1": { "bline": 11, "eline": 12, "bcolumn": -3, "ecolumn": -3},
            "yaxis5right1": { "bline": 13, "eline": 14, "bcolumn": -3, "ecolumn": -3},
            "yaxis6right1": { "bline": 15, "eline": 16, "bcolumn": -3, "ecolumn": -3},
            "yaxis7right1": { "bline": 17, "eline": 18, "bcolumn": -3, "ecolumn": -3},
            "yaxis0right2": { "bline": 3, "eline": 4, "bcolumn": -2, "ecolumn": -2},
            "yaxis1right2": { "bline": 5, "eline": 6, "bcolumn": -2, "ecolumn": -2},
            "yaxis2right2": { "bline": 7, "eline": 8, "bcolumn": -2, "ecolumn": -2},
            "yaxis3right2": { "bline": 9, "eline": 10, "bcolumn": -2, "ecolumn": -2},
            "yaxis4right2": { "bline": 11, "eline": 12, "bcolumn": -2, "ecolumn": -2},
            "yaxis5right2": { "bline": 13, "eline": 14, "bcolumn": -2, "ecolumn": -2},
            "yaxis6right2": { "bline": 15, "eline": 16, "bcolumn": -2, "ecolumn": -2},
            "yaxis7right2": { "bline": 17, "eline": 18, "bcolumn": -2, "ecolumn": -2},
            "xaxis0": { "bline": -3, "eline": -3, "bcolumn": 4, "ecolumn": 4},
            "xaxis1": { "bline": -3, "eline": -3, "bcolumn": 5, "ecolumn": 5},
            "xaxis2": { "bline": -3, "eline": -3, "bcolumn": 6, "ecolumn": 6},
            "xaxis3": { "bline": -3, "eline": -3, "bcolumn": 7, "ecolumn": 7},
            "xaxis4": { "bline": -3, "eline": -3, "bcolumn": 8, "ecolumn": 8},
            "xaxis5": { "bline": -3, "eline": -3, "bcolumn": 9, "ecolumn": 9},
            "xaxis6": { "bline": -3, "eline": -3, "bcolumn": 10, "ecolumn": 10},
            "xaxis7": { "bline": -3, "eline": -3, "bcolumn": 11, "ecolumn": 11},
            "legend": { "bline": -2, "eline": -2, "bcolumn": 4, "ecolumn": -5}
        }
        super(UserObject, s).__init__(**object)
