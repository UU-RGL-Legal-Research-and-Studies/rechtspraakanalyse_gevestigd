#Code where all ECLIs are stored after webparsing from rechtspraak.nl
#The ECLIs are later imported in ECLI_cache_affectieschade for cache purposes

raw_ECLI = ['ECLI:NL:RBAMS:2022:6284', 'ECLI:NL:GHAMS:2022:1179', 'ECLI:NL:RBGEL:2020:1397', 'ECLI:NL:RBLIM:2022:2418', 'ECLI:NL:RBROT:2020:9481', 'ECLI:NL:RBAMS:2021:362', 'ECLI:NL:RBNNE:2021:1458', 'ECLI:NL:RBROT:2023:7185', 'ECLI:NL:RBGEL:2020:2436', 'ECLI:NL:PHR:2021:642', 'ECLI:NL:HR:2021:1750', 'ECLI:NL:GHSHE:2021:2934', 'ECLI:NL:RBLIM:2020:5198', 'ECLI:NL:HR:2022:1907', 'ECLI:NL:RBGEL:2023:759', 'ECLI:NL:RBNNE:2022:305', 'ECLI:NL:RBNHO:2020:8510', 'ECLI:NL:RBGEL:2020:5450', 'ECLI:NL:RBNHO:2022:1356', 'ECLI:NL:RBZWB:2022:216', 'ECLI:NL:RBNHO:2021:11946', 'ECLI:NL:RBDHA:2020:11332', 'ECLI:NL:RBOBR:2021:217', 'ECLI:NL:RBGEL:2022:4130', 'ECLI:NL:RBZWB:2021:280', 'ECLI:NL:GHSHE:2022:1543', 'ECLI:NL:RBMNE:2020:1046', 'ECLI:NL:RBAMS:2020:51', 'ECLI:NL:RBNHO:2021:11942', 'ECLI:NL:RBAMS:2021:1530', 'ECLI:NL:GHDHA:2023:586', 'ECLI:NL:RBDHA:2022:5409', 'ECLI:NL:RBMNE:2023:2738', 'ECLI:NL:RBMNE:2023:2743', 'ECLI:NL:RBDHA:2023:2882', 'ECLI:NL:GHARL:2022:6258', 'ECLI:NL:RBROT:2023:2367', 'ECLI:NL:GHAMS:2021:2001', 'ECLI:NL:GHAMS:2022:2852', 'ECLI:NL:RBAMS:2022:2452', 'ECLI:NL:RBDHA:2022:6727', 'ECLI:NL:RBZWB:2020:440', 'ECLI:NL:GHAMS:2019:1295', 'ECLI:NL:RBROT:2020:9453', 'ECLI:NL:RBZWB:2022:6760', 'ECLI:NL:RBNHO:2022:6866', 'ECLI:NL:GHAMS:2020:2439', 'ECLI:NL:RBZWB:2020:455', 'ECLI:NL:RBROT:2022:7613', 'ECLI:NL:RBZWB:2020:456', 'ECLI:NL:RBZWB:2020:363', 'ECLI:NL:RBROT:2022:4222', 'ECLI:NL:RBROT:2020:10238', 'ECLI:NL:RBDHA:2020:10373', 'ECLI:NL:RBOBR:2021:1464', 'ECLI:NL:RBNHO:2022:10379', 'ECLI:NL:RBROT:2022:1177', 'ECLI:NL:RBROT:2020:8205', 'ECLI:NL:RBNHO:2023:4432', 'ECLI:NL:RBLIM:2022:10473', 'ECLI:NL:RBOBR:2020:5134', 'ECLI:NL:GHSHE:2023:1157', 'ECLI:NL:RBLIM:2020:7098', 'ECLI:NL:RBROT:2020:1460', 'ECLI:NL:RBZWB:2020:362', 'ECLI:NL:RBNNE:2023:2478', 'ECLI:NL:RBROT:2022:10723', 'ECLI:NL:GHAMS:2023:2551', 'ECLI:NL:RBZWB:2022:7251', 'ECLI:NL:GHARL:2022:6880', 'ECLI:NL:RBMNE:2021:2655', 'ECLI:NL:RBROT:2019:10581', 'ECLI:NL:RBMNE:2023:2735', 'ECLI:NL:RBZWB:2023:1313', 'ECLI:NL:RBNHO:2022:10699', 'ECLI:NL:RBLIM:2022:1403', 'ECLI:NL:RBZWB:2020:357', 'ECLI:NL:RBNNE:2023:2480', 'ECLI:NL:GHARL:2023:5899', 'ECLI:NL:RBZWB:2023:1423', 'ECLI:NL:RBDHA:2021:11497', 'ECLI:NL:RBROT:2023:8858', 'ECLI:NL:RBNHO:2023:3506', 'ECLI:NL:RBNHO:2021:11425', 'ECLI:NL:RBNHO:2019:5823', 'ECLI:NL:RBAMS:2022:615', 'ECLI:NL:RBOBR:2022:231', 'ECLI:NL:HR:2021:1750', 'ECLI:NL:PHR:2021:642', 'ECLI:NL:RBNHO:2023:6053', 'ECLI:NL:RBZWB:2022:6753', 'ECLI:NL:RBOBR:2022:1039', 'ECLI:NL:RBAMS:2021:5665', 'ECLI:NL:RBAMS:2021:5666', 'ECLI:NL:GHDHA:2023:1934', 'ECLI:NL:RBDHA:2023:227', 'ECLI:NL:RBNNE:2022:3754', 'ECLI:NL:RBROT:2020:9311', 'ECLI:NL:RBAMS:2023:4658', 'ECLI:NL:RBAMS:2023:4657', 'ECLI:NL:RBNHO:2023:1372', 'ECLI:NL:RBGEL:2021:1995', 'ECLI:NL:RBNHO:2022:3278', 'ECLI:NL:RBZWB:2023:3995', 'ECLI:NL:RBMNE:2021:293', 'ECLI:NL:GHAMS:2019:3502', 'ECLI:NL:HR:2020:1962', 'ECLI:NL:RBZWB:2022:7250', 'ECLI:NL:RBOBR:2021:4038', 'ECLI:NL:GHSHE:2022:2145', 'ECLI:NL:RBMNE:2020:4378', 'ECLI:NL:RBNHO:2023:4113', 'ECLI:NL:RBNHO:2023:628', 'ECLI:NL:RBROT:2022:8337', 'ECLI:NL:RBMNE:2023:3966', 'ECLI:NL:RBROT:2023:2624', 'ECLI:NL:RBOBR:2022:2275', 'ECLI:NL:RBOBR:2021:1921', 'ECLI:NL:GHARL:2021:2890', 'ECLI:NL:RBOBR:2020:4349', 'ECLI:NL:RBDHA:2021:11487', 'ECLI:NL:RBOBR:2023:4756', 'ECLI:NL:RBROT:2023:6401', 'ECLI:NL:RBNHO:2022:11185', 'ECLI:NL:GHARL:2022:10586', 'ECLI:NL:RBMNE:2021:5975', 'ECLI:NL:RBNHO:2022:853', 'ECLI:NL:GHDHA:2021:1997', 'ECLI:NL:RBGEL:2021:894', 'ECLI:NL:RBROT:2019:10334', 'ECLI:NL:RBROT:2019:1772', 'ECLI:NL:RBROT:2022:300', 'ECLI:NL:RBAMS:2023:4656', 'ECLI:NL:RBDHA:2022:5082', 'ECLI:NL:RBROT:2022:3101', 'ECLI:NL:GHDHA:2021:152', 'ECLI:NL:RBOBR:2020:3751', 'ECLI:NL:RBNHO:2020:5305', 'ECLI:NL:RBROT:2020:5895', 'ECLI:NL:RBAMS:2022:5385', 'ECLI:NL:RBGEL:2022:7338', 'ECLI:NL:RBROT:2023:5916', 'ECLI:NL:RBDHA:2021:11794', 'ECLI:NL:RBNHO:2022:5080', 'ECLI:NL:GHAMS:2023:2456', 'ECLI:NL:RBZWB:2021:2878', 'ECLI:NL:RBAMS:2022:7628', 'ECLI:NL:RBGEL:2022:4097', 'ECLI:NL:RBAMS:2022:7501', 'ECLI:NL:HR:2023:1495', 'ECLI:NL:PHR:2023:782', 'ECLI:NL:GHDHA:2022:365', 'ECLI:NL:GHAMS:2023:1181', 'ECLI:NL:RBNHO:2020:10959', 'ECLI:NL:RBGEL:2023:3322', 'ECLI:NL:RBOBR:2021:2238', 'ECLI:NL:GHAMS:2023:2457', 'ECLI:NL:RBDHA:2023:8915', 'ECLI:NL:RBGEL:2022:7222', 'ECLI:NL:RBAMS:2021:6332', 'ECLI:NL:RBDHA:2023:8914', 'ECLI:NL:RBAMS:2022:7502', 'ECLI:NL:RBAMS:2023:3855', 'ECLI:NL:RBDHA:2023:10123', 'ECLI:NL:RBZWB:2022:1645', 'ECLI:NL:RBDHA:2023:8917', 'ECLI:NL:RBAMS:2020:4640', 'ECLI:NL:PHR:2020:500', 'ECLI:NL:HR:2020:1057', 'ECLI:NL:RBGEL:2020:7021', 'ECLI:NL:GHAMS:2023:1580', 'ECLI:NL:RBDHA:2021:3281', 'ECLI:NL:RBROT:2022:5218', 'ECLI:NL:RBGEL:2021:2618', 'ECLI:NL:RBZWB:2022:7599', 'ECLI:NL:RBGEL:2021:587', 'ECLI:NL:RBDHA:2022:12371', 'ECLI:NL:RBMNE:2022:805', 'ECLI:NL:HR:2020:1057', 'ECLI:NL:PHR:2020:500', 'ECLI:NL:PHR:2020:398', 'ECLI:NL:GHSHE:2018:4181', 'ECLI:NL:RBAMS:2021:878', 'ECLI:NL:RBOVE:2022:1507', 'ECLI:NL:RBNNE:2022:4339', 'ECLI:NL:GHSHE:2022:2027', 'ECLI:NL:GHAMS:2022:331', 'ECLI:NL:RBROT:2021:5925', 'ECLI:NL:RBGEL:2020:3156', 'ECLI:NL:RBNHO:2022:9705', 'ECLI:NL:RBAMS:2021:879', 'ECLI:NL:RBGEL:2020:3155', 'ECLI:NL:RBDHA:2020:2714', 'ECLI:NL:RBDHA:2023:10309', 'ECLI:NL:RBZWB:2021:1283', 'ECLI:NL:GHSHE:2022:1551', 'ECLI:NL:GHSHE:2022:3691', 'ECLI:NL:RBMNE:2020:920', 'ECLI:NL:RBROT:2023:1840', 'ECLI:NL:RBAMS:2021:4349', 'ECLI:NL:RBAMS:2022:7688', 'ECLI:NL:RBLIM:2021:4119', 'ECLI:NL:RBAMS:2021:7378', 'ECLI:NL:GHAMS:2019:1707', 'ECLI:NL:RBNHO:2018:5988', 'ECLI:NL:RBAMS:2020:3529', 'ECLI:NL:RBDHA:2023:10119', 'ECLI:NL:RBAMS:2021:3941', 'ECLI:NL:RBNNE:2021:542', 'ECLI:NL:RBROT:2022:8230', 'ECLI:NL:RBLIM:2021:526', 'ECLI:NL:GHDHA:2022:908', 'ECLI:NL:RBOVE:2023:426', 'ECLI:NL:RBAMS:2020:5479', 'ECLI:NL:RBROT:2021:11776', 'ECLI:NL:RBROT:2020:10949', 'ECLI:NL:RBGEL:2023:2823', 'ECLI:NL:RBLIM:2022:5044', 'ECLI:NL:RBDHA:2022:11622', 'ECLI:NL:RBGEL:2021:2222', 'ECLI:NL:RBNNE:2021:1675', 'ECLI:NL:GHARL:2022:2877', 'ECLI:NL:RBGEL:2021:2205', 'ECLI:NL:RBDHA:2020:10201', 'ECLI:NL:RBDHA:2022:12446', 'ECLI:NL:RBGEL:2023:5281', 'ECLI:NL:RBGEL:2023:3167', 'ECLI:NL:RBROT:2023:4715', 'ECLI:NL:RBAMS:2020:2814', 'ECLI:NL:RBOBR:2023:1622', 'ECLI:NL:RBGEL:2021:6439', 'ECLI:NL:RBZWB:2023:3718', 'ECLI:NL:RBZWB:2021:5561', 'ECLI:NL:RBDHA:2023:15274', 'ECLI:NL:RBZWB:2023:3715', 'ECLI:NL:RBGEL:2021:2243', 'ECLI:NL:RBROT:2020:13006', 'ECLI:NL:RBOVE:2022:3781', 'ECLI:NL:RBLIM:2021:4156', 'ECLI:NL:GHSHE:2021:1001', 'ECLI:NL:RBLIM:2018:8802', 'ECLI:NL:RBAMS:2021:909', 'ECLI:NL:GHAMS:2022:1424', 'ECLI:NL:RBDHA:2022:12464', 'ECLI:NL:RBDHA:2022:2426', 'ECLI:NL:RBNHO:2021:7899', 'ECLI:NL:RBOBR:2021:2921', 'ECLI:NL:RBOBR:2021:2131', 'ECLI:NL:HR:2019:720', 'ECLI:NL:PHR:2019:255', 'ECLI:NL:GHARL:2018:2456', 'ECLI:NL:RBROT:2023:6164', 'ECLI:NL:RBDHA:2022:12459', 'ECLI:NL:RBDHA:2021:11983', 'ECLI:NL:RBDHA:2022:12655', 'ECLI:NL:RBOBR:2021:1509', 'ECLI:NL:RBDHA:2023:8720', 'ECLI:NL:RBLIM:2022:6684', 'ECLI:NL:RBGEL:2021:4870', 'ECLI:NL:GHARL:2023:5898', 'ECLI:NL:RBNHO:2022:41', 'ECLI:NL:RBROT:2021:9243', 'ECLI:NL:RBAMS:2021:6434', 'ECLI:NL:RBGEL:2022:2977', 'ECLI:NL:RBAMS:2022:2249', 'ECLI:NL:RBGEL:2021:3682', 'ECLI:NL:RBLIM:2020:5198', 'ECLI:NL:GHSHE:2021:2934', 'ECLI:NL:RBAMS:2020:1620', 'ECLI:NL:RBROT:2022:6746', 'ECLI:NL:RBZWB:2023:2844', 'ECLI:NL:RBDHA:2022:12436', 'ECLI:NL:GHAMS:2022:3738', 'ECLI:NL:RBROT:2023:9337', 'ECLI:NL:RBROT:2023:9345', 'ECLI:NL:RBGEL:2022:3952', 'ECLI:NL:RBGEL:2021:2246', 'ECLI:NL:RBOVE:2023:2266', 'ECLI:NL:RBGEL:2023:1723', 'ECLI:NL:RBAMS:2022:6269', 'ECLI:NL:RBLIM:2020:8377', 'ECLI:NL:GHAMS:2021:2125', 'ECLI:NL:RBROT:2023:7348', 'ECLI:NL:RBZWB:2019:5033', 'ECLI:NL:RBOVE:2021:4821', 'ECLI:NL:RBAMS:2023:2762', 'ECLI:NL:RBNHO:2020:10959', 'ECLI:NL:GHAMS:2023:1181', 'ECLI:NL:RBDHA:2021:11984', 'ECLI:NL:RBAMS:2023:6146', 'ECLI:NL:RBDHA:2020:5934', 'ECLI:NL:RBDHA:2023:15273', 'ECLI:NL:RBDHA:2023:1778', 'ECLI:NL:RBOVE:2021:4823', 'ECLI:NL:RBROT:2022:9376', 'ECLI:NL:RBGEL:2021:3987', 'ECLI:NL:GHDHA:2023:1844', 'ECLI:NL:RBMNE:2022:2474', 'ECLI:NL:RBNNE:2020:2116', 'ECLI:NL:GHSHE:2022:2144', 'ECLI:NL:GHSHE:2022:2145', 'ECLI:NL:RBOBR:2021:4038', 'ECLI:NL:HR:2023:1420', 'ECLI:NL:RBNNE:2020:3678', 'ECLI:NL:RBMNE:2023:2554', 'ECLI:NL:RBZWB:2023:3940', 'ECLI:NL:GHDHA:2022:1786', 'ECLI:NL:RBROT:2022:1350', 'ECLI:NL:RBLIM:2021:5661', 'ECLI:NL:RBOBR:2023:3293', 'ECLI:NL:RBAMS:2022:1391', 'ECLI:NL:RBOBR:2022:2515', 'ECLI:NL:RBOBR:2020:4011', 'ECLI:NL:GHSHE:2022:2945', 'ECLI:NL:HR:2019:718', 'ECLI:NL:PHR:2019:256', 'ECLI:NL:GHARL:2018:2457', 'ECLI:NL:RBROT:2023:3562', 'ECLI:NL:RBDHA:2020:12793', 'ECLI:NL:RBDHA:2020:450', 'ECLI:NL:RBOVE:2021:647', 'ECLI:NL:RBROT:2023:9342', 'ECLI:NL:GHAMS:2023:1188', 'ECLI:NL:RBAMS:2020:6643', 'ECLI:NL:RBAMS:2022:7500', 'ECLI:NL:RBMNE:2023:1941', 'ECLI:NL:RBZWB:2022:7144', 'ECLI:NL:GHAMS:2022:1424', 'ECLI:NL:RBAMS:2021:909', 'ECLI:NL:RBNNE:2020:2387', 'ECLI:NL:RBNNE:2023:4127', 'ECLI:NL:RBGEL:2021:2248', 'ECLI:NL:RBROT:2023:2713', 'ECLI:NL:RBOVE:2019:4656', 'ECLI:NL:RBDHA:2021:5626', 'ECLI:NL:GHDHA:2023:580', 'ECLI:NL:RBDHA:2023:15276', 'ECLI:NL:RBAMS:2022:4251', 'ECLI:NL:GHAMS:2021:2124', 'ECLI:NL:HR:2023:414', 'ECLI:NL:RBMNE:2021:3163', 'ECLI:NL:RBROT:2021:3905', 'ECLI:NL:RBNHO:2023:3870', 'ECLI:NL:RBZWB:2022:1469', 'ECLI:NL:RBAMS:2021:1419', 'ECLI:NL:RBAMS:2021:1417', 'ECLI:NL:GHAMS:2022:1944', 'ECLI:NL:RBAMS:2020:3129', 'ECLI:NL:RBROT:2022:634', 'ECLI:NL:RBGEL:2022:5525', 'ECLI:NL:RBLIM:2020:9689', 'ECLI:NL:RBNHO:2023:9267', 'ECLI:NL:RBLIM:2021:2748', 'ECLI:NL:RBNNE:2020:2369', 'ECLI:NL:RBNNE:2020:2117', 'ECLI:NL:GHAMS:2021:2123', 'ECLI:NL:HR:2023:415', 'ECLI:NL:RBOBR:2021:3133', 'ECLI:NL:RBDHA:2021:5667', 'ECLI:NL:RBROT:2019:10582', 'ECLI:NL:RBLIM:2022:576', 'ECLI:NL:RBROT:2021:9957', 'ECLI:NL:RBZWB:2023:4977', 'ECLI:NL:GHSHE:2022:4174', 'ECLI:NL:GHDHA:2023:1792', 'ECLI:NL:RBMNE:2022:2523', 'ECLI:NL:GHARL:2023:1254', 'ECLI:NL:RBMNE:2022:1584', 'ECLI:NL:RBNNE:2022:1250', 'ECLI:NL:RBROT:2021:3906', 'ECLI:NL:RBROT:2020:5764', 'ECLI:NL:RBNHO:2021:5549', 'ECLI:NL:RBMNE:2020:2643', 'ECLI:NL:GHSHE:2019:203', 'ECLI:NL:RBZWB:2016:5916', 'ECLI:NL:HR:2020:4', 'ECLI:NL:RBOBR:2022:4761', 'ECLI:NL:RBNNE:2022:1515', 'ECLI:NL:GHDHA:2020:2236', 'ECLI:NL:RBROT:2021:8989', 'ECLI:NL:RBZWB:2021:1681', 'ECLI:NL:RBNHO:2023:3879', 'ECLI:NL:RBDHA:2023:10120', 'ECLI:NL:GHARL:2023:1254', 'ECLI:NL:RBMNE:2022:2523', 'ECLI:NL:RBMNE:2021:4651', 'ECLI:NL:RBLIM:2020:5621', 'ECLI:NL:GHSHE:2022:868', 'ECLI:NL:RBGEL:2021:4173', 'ECLI:NL:RBLIM:2023:6128', 'ECLI:NL:RBNNE:2021:3077', 'ECLI:NL:PHR:2022:166', 'ECLI:NL:HR:2022:560', 'ECLI:NL:RBMNE:2019:3892', 'ECLI:NL:RBNNE:2021:2569', 'ECLI:NL:RBMNE:2021:5975', 'ECLI:NL:GHARL:2022:10586', 'ECLI:NL:RBAMS:2022:4090', 'ECLI:NL:GHSHE:2023:753', 'ECLI:NL:RBDHA:2020:10211', 'ECLI:NL:RBROT:2022:5677', 'ECLI:NL:RBOBR:2021:2212', 'ECLI:NL:GHAMS:2019:3762', 'ECLI:NL:RBGEL:2021:1150', 'ECLI:NL:RBROT:2023:4683', 'ECLI:NL:RBAMS:2021:2498', 'ECLI:NL:RBMNE:2023:164', 'ECLI:NL:RBOVE:2022:3', 'ECLI:NL:GHAMS:2019:2270', 'ECLI:NL:RBMNE:2022:1583', 'ECLI:NL:RBROT:2021:1424', 'ECLI:NL:RBAMS:2019:1685', 'ECLI:NL:RBDHA:2021:14537', 'ECLI:NL:RBAMS:2021:8164', 'ECLI:NL:RBNHO:2020:5582', 'ECLI:NL:GHARL:2019:6248', 'ECLI:NL:RBGEL:2017:6132', 'ECLI:NL:RBAMS:2022:4255', 'ECLI:NL:RBAMS:2022:4256', 'ECLI:NL:RBAMS:2023:2661', 'ECLI:NL:RBNNE:2022:4996', 'ECLI:NL:RBROT:2021:3212', 'ECLI:NL:RBDHA:2022:13645', 'ECLI:NL:RBROT:2020:6264', 'ECLI:NL:RBAMS:2023:2620', 'ECLI:NL:RBDHA:2022:12654', 'ECLI:NL:RBROT:2021:3100', 'ECLI:NL:RBAMS:2022:6286', 'ECLI:NL:RBMNE:2023:166', 'ECLI:NL:RBOVE:2022:2952', 'ECLI:NL:RBAMS:2021:3710', 'ECLI:NL:RBAMS:2021:3709', 'ECLI:NL:RBAMS:2023:1076', 'ECLI:NL:RBNNE:2021:2892', 'ECLI:NL:GHSHE:2022:868', 'ECLI:NL:RBLIM:2020:5621', 'ECLI:NL:HR:2023:1295', 'ECLI:NL:RBOVE:2022:3883', 'ECLI:NL:RBAMS:2023:4719', 'ECLI:NL:RBAMS:2022:6285', 'ECLI:NL:RBMNE:2021:3297', 'ECLI:NL:RBNHO:2023:2767', 'ECLI:NL:RBGEL:2021:1987', 'ECLI:NL:RBDHA:2020:12055', 'ECLI:NL:GHSHE:2020:2750', 'ECLI:NL:RBZWB:2020:198', 'ECLI:NL:RBDHA:2021:14529', 'ECLI:NL:RBNHO:2020:5583', 'ECLI:NL:RBLIM:2023:3900', 'ECLI:NL:RBAMS:2022:4089', 'ECLI:NL:RBAMS:2022:4091', 'ECLI:NL:RBAMS:2022:3751', 'ECLI:NL:RBAMS:2022:3781', 'ECLI:NL:RBROT:2020:6263', 'ECLI:NL:RBAMS:2023:4721', 'ECLI:NL:RBNNE:2021:4482', 'ECLI:NL:RBZWB:2020:6099', 'ECLI:NL:RBOVE:2022:1593', 'ECLI:NL:RBAMS:2023:5048', 'ECLI:NL:RBAMS:2021:3708', 'ECLI:NL:RBMNE:2023:18', 'ECLI:NL:RBOBR:2020:5225', 'ECLI:NL:RBDHA:2023:8838', 'ECLI:NL:GHAMS:2022:115', 'ECLI:NL:RBAMS:2022:3780', 'ECLI:NL:RBNHO:2023:3793', 'ECLI:NL:RBZWB:2021:534', 'ECLI:NL:RBDHA:2023:8391', 'ECLI:NL:GHARL:2019:5542', 'ECLI:NL:RBMNE:2018:3330', 'ECLI:NL:HR:2020:1092', 'ECLI:NL:RBROT:2023:6468', 'ECLI:NL:GHAMS:2023:1327', 'ECLI:NL:GHARL:2023:2695', 'ECLI:NL:RBNHO:2022:11063', 'ECLI:NL:RBROT:2022:5597', 'ECLI:NL:PHR:2019:1150', 'ECLI:NL:HR:2020:4', 'ECLI:NL:RBLIM:2019:2219', 'ECLI:NL:GHSHE:2021:25', 'ECLI:NL:RBAMS:2021:1141', 'ECLI:NL:RBDHA:2020:7046', 'ECLI:NL:RBROT:2022:9197', 'ECLI:NL:RBLIM:2022:8267', 'ECLI:NL:GHARL:2021:10549', 'ECLI:NL:RBNHO:2021:3215', 'ECLI:NL:GHSHE:2022:4287', 'ECLI:NL:RBDHA:2021:11800', 'ECLI:NL:RBDHA:2022:9734', 'ECLI:NL:RBGEL:2020:1902', 'ECLI:NL:GHAMS:2020:910', 'ECLI:NL:HR:2021:1050', 'ECLI:NL:RBROT:2023:2948', 'ECLI:NL:GHARL:2022:9812', 'ECLI:NL:RBAMS:2022:6225', 'ECLI:NL:RBNHO:2021:4030', 'ECLI:NL:GHSHE:2023:2138', 'ECLI:NL:RBROT:2023:1225', 'ECLI:NL:RBROT:2023:6467', 'ECLI:NL:GHARL:2021:10550', 'ECLI:NL:GHARL:2021:4519', 'ECLI:NL:RBMNE:2020:3808', 'ECLI:NL:PHR:2023:782', 'ECLI:NL:HR:2023:1495', 'ECLI:NL:HR:2022:560', 'ECLI:NL:GHARL:2020:5686', 'ECLI:NL:PHR:2022:166', 'ECLI:NL:RBOVE:2022:2349', 'ECLI:NL:RBROT:2022:1654', 'ECLI:NL:RBZWB:2021:5986', 'ECLI:NL:RBAMS:2021:910', 'ECLI:NL:GHAMS:2022:1423', 'ECLI:NL:GHDHA:2020:2049', 'ECLI:NL:RBOVE:2020:3168', 'ECLI:NL:RBDHA:2021:1069', 'ECLI:NL:GHARL:2021:10551', 'ECLI:NL:PHR:2023:16', 'ECLI:NL:HR:2023:599', 'ECLI:NL:RBGEL:2019:932', 'ECLI:NL:PHR:2023:435', 'ECLI:NL:HR:2023:984', 'ECLI:NL:PHR:2023:436', 'ECLI:NL:HR:2023:982', 'ECLI:NL:GHARL:2023:5898', 'ECLI:NL:RBGEL:2021:4870', 'ECLI:NL:GHARL:2022:7821', 'ECLI:NL:RBOVE:2022:1173', 'ECLI:NL:RBMNE:2020:4479', 'ECLI:NL:RBLIM:2022:2339', 'ECLI:NL:RBNNE:2020:3239', 'ECLI:NL:RBZWB:2020:1184', 'ECLI:NL:RBROT:2022:4633', 'ECLI:NL:PHR:2019:255', 'ECLI:NL:HR:2019:720', 'ECLI:NL:RBNNE:2022:527', 'ECLI:NL:GHAMS:2022:3573', 'ECLI:NL:RBNNE:2021:4420', 'ECLI:NL:RBZWB:2023:6737', 'ECLI:NL:RBMNE:2023:165', 'ECLI:NL:RBOVE:2021:883', 'ECLI:NL:RBROT:2019:8958', 'ECLI:NL:RBMNE:2023:5681', 'ECLI:NL:RBNHO:2023:7408', 'ECLI:NL:RBGEL:2022:7421', 'ECLI:NL:RBMNE:2020:3811', 'ECLI:NL:PHR:2023:437', 'ECLI:NL:HR:2023:983', 'ECLI:NL:GHAMS:2020:915', 'ECLI:NL:HR:2021:1049', 'ECLI:NL:RBMNE:2022:42', 'ECLI:NL:RBNHO:2022:1306', 'ECLI:NL:RBMNE:2022:5869', 'ECLI:NL:RBZWB:2022:5814', 'ECLI:NL:GHSHE:2022:2945', 'ECLI:NL:RBOBR:2020:4011', 'ECLI:NL:RBOVE:2022:1172', 'ECLI:NL:RBDHA:2021:10146', 'ECLI:NL:GHDHA:2023:255', 'ECLI:NL:RBAMS:2021:816', 'ECLI:NL:RBNNE:2019:3908', 'ECLI:NL:GHARL:2020:5447', 'ECLI:NL:RBOVE:2023:4204', 'ECLI:NL:RBOVE:2023:4210', 'ECLI:NL:RBROT:2023:3273', 'ECLI:NL:RBDHA:2022:3363', 'ECLI:NL:GHARL:2021:10552', 'ECLI:NL:RBGEL:2019:951', 'ECLI:NL:PHR:2023:15', 'ECLI:NL:HR:2023:633', 'ECLI:NL:RBNNE:2020:4411', 'ECLI:NL:RBLIM:2022:2288', 'ECLI:NL:RBLIM:2022:2311', 'ECLI:NL:RBMNE:2020:3808', 'ECLI:NL:GHARL:2021:4519', 'ECLI:NL:RBROT:2022:4632', 'ECLI:NL:RBGEL:2022:7176', 'ECLI:NL:GHSHE:2019:4531', 'ECLI:NL:RBOBR:2018:5515', 'ECLI:NL:RBGEL:2022:7407', 'ECLI:NL:RBZWB:2021:2251', 'ECLI:NL:RBAMS:2020:192', 'ECLI:NL:GHAMS:2023:1115', 'ECLI:NL:RBZWB:2023:5382', 'ECLI:NL:RBLIM:2022:2340', 'ECLI:NL:RBAMS:2021:826', 'ECLI:NL:RBROT:2021:10177', 'ECLI:NL:RBOVE:2021:880', 'ECLI:NL:PHR:2020:454', 'ECLI:NL:HR:2020:1087', 'ECLI:NL:RBROT:2019:5994', 'ECLI:NL:OGEAA:2023:214', 'ECLI:NL:RBAMS:2023:1075', 'ECLI:NL:RBDHA:2023:956', 'ECLI:NL:RBZWB:2021:237', 'ECLI:NL:RBDHA:2020:8099', 'ECLI:NL:RBZWB:2020:198', 'ECLI:NL:GHSHE:2020:2750', 'ECLI:NL:RBDHA:2023:1861', 'ECLI:NL:RBAMS:2021:1667', 'ECLI:NL:RBNNE:2022:4379', 'ECLI:NL:RBAMS:2021:7613', 'ECLI:NL:RBAMS:2022:1291', 'ECLI:NL:RBLIM:2020:4534', 'ECLI:NL:GHSHE:2023:392', 'ECLI:NL:HR:2019:793', 'ECLI:NL:PHR:2018:600', 'ECLI:NL:RBNHO:2022:11033', 'ECLI:NL:RBROT:2021:10176', 'ECLI:NL:RBDHA:2021:221', 'ECLI:NL:RBOBR:2020:393', 'ECLI:NL:RBROT:2019:5993', 'ECLI:NL:PHR:2021:230', 'ECLI:NL:HR:2021:536', 'ECLI:NL:RBOVE:2022:510', 'ECLI:NL:GHARL:2020:2126', 'ECLI:NL:RBNNE:2018:4190', 'ECLI:NL:OGEAC:2019:169', 'ECLI:NL:RBZWB:2023:5225', 'ECLI:NL:RBAMS:2023:299', 'ECLI:NL:RBDHA:2022:2500', 'ECLI:NL:RBOVE:2022:158', 'ECLI:NL:RBLIM:2021:8936', 'ECLI:NL:RBROT:2021:5487', 'ECLI:NL:RBROT:2020:10292', 'ECLI:NL:RBOBR:2020:4309', 'ECLI:NL:RBNNE:2023:1792', 'ECLI:NL:RBOBR:2023:164', 'ECLI:NL:RBAMS:2021:7612', 'ECLI:NL:RBROT:2022:9462', 'ECLI:NL:GHAMS:2023:1510', 'ECLI:NL:RBNHO:2021:11426', 'ECLI:NL:RBMNE:2019:4949', 'ECLI:NL:GHSHE:2022:2409', 'ECLI:NL:RBROT:2022:1352', 'ECLI:NL:RBROT:2021:6457', 'ECLI:NL:RBNNE:2021:540', 'ECLI:NL:RBGEL:2022:7425', 'ECLI:NL:GHARL:2022:7031', 'ECLI:NL:HR:2023:250', 'ECLI:NL:HR:2022:958', 'ECLI:NL:PHR:2022:255', 'ECLI:NL:GHARL:2021:159', 'ECLI:NL:RBDHA:2022:2793', 'ECLI:NL:RBZWB:2021:3536', 'ECLI:NL:RBOVE:2020:3658', 'ECLI:NL:RBROT:2023:9332', 'ECLI:NL:RBAMS:2023:4512', 'ECLI:NL:RBZWB:2022:4596', 'ECLI:NL:RBROT:2021:7937', 'ECLI:NL:RBGEL:2020:7051', 'ECLI:NL:RBMNE:2023:884', 'ECLI:NL:RBDHA:2022:12469', 'ECLI:NL:RBROT:2022:5596', 'ECLI:NL:RBMNE:2022:544', 'ECLI:NL:RBMNE:2022:1519', 'ECLI:NL:RBLIM:2021:5591', 'ECLI:NL:RBMNE:2022:4621', 'ECLI:NL:RBMNE:2020:2520', 'ECLI:NL:RBGEL:2023:4056', 'ECLI:NL:PHR:2019:256', 'ECLI:NL:HR:2019:718', 'ECLI:NL:RBZWB:2021:4410', 'ECLI:NL:RBDHA:2022:7065', 'ECLI:NL:RBAMS:2022:1749', 'ECLI:NL:RBOVE:2021:2454', 'ECLI:NL:RBZWB:2021:4459', 'ECLI:NL:RBLIM:2022:10259', 'ECLI:NL:GHDHA:2021:221', 'ECLI:NL:GHSHE:2023:3270', 'ECLI:NL:GHSHE:2023:3277', 'ECLI:NL:RBGEL:2022:2474', 'ECLI:NL:RBGEL:2022:7440', 'ECLI:NL:RBOVE:2023:4203', 'ECLI:NL:GHAMS:2023:2182', 'ECLI:NL:RBNNE:2022:2401', 'ECLI:NL:RBMNE:2022:293', 'ECLI:NL:RBDHA:2023:14981', 'ECLI:NL:RBMNE:2021:4730', 'ECLI:NL:RBNHO:2023:4374', 'ECLI:NL:RBNHO:2023:4434', 'ECLI:NL:RBAMS:2023:269', 'ECLI:NL:RBDHA:2022:12414', 'ECLI:NL:RBAMS:2019:7229', 'ECLI:NL:RBAMS:2019:7232', 'ECLI:NL:RBAMS:2019:7227', 'ECLI:NL:RBAMS:2019:7228', 'ECLI:NL:RBROT:2021:10178', 'ECLI:NL:RBGEL:2022:2445', 'ECLI:NL:PHR:2023:84', 'ECLI:NL:HR:2023:400', 'ECLI:NL:RBOVE:2023:3035', 'ECLI:NL:GHARL:2020:9692', 'ECLI:NL:RBGEL:2018:2591', 'ECLI:NL:RBAMS:2019:7231', 'ECLI:NL:RBGEL:2022:7105', 'ECLI:NL:RBMNE:2022:1819', 'ECLI:NL:RBOVE:2022:497', 'ECLI:NL:RBDHA:2023:8850', 'ECLI:NL:RBOVE:2021:3519', 'ECLI:NL:GHAMS:2022:1011', 'ECLI:NL:RBROT:2020:3181', 'ECLI:NL:RBROT:2023:8461', 'ECLI:NL:GHSHE:2023:1157', 'ECLI:NL:RBOBR:2020:5134', 'ECLI:NL:RBNNE:2022:2386', 'ECLI:NL:RBROT:2022:5595', 'ECLI:NL:RBNNE:2021:2636', 'ECLI:NL:RBZWB:2020:6012', 'ECLI:NL:GHSHE:2021:3342', 'ECLI:NL:RBAMS:2019:7233', 'ECLI:NL:RBAMS:2019:7234', 'ECLI:NL:RBAMS:2019:7226', 'ECLI:NL:GHSHE:2022:1543', 'ECLI:NL:RBZWB:2021:280', 'ECLI:NL:GHSHE:2023:738', 'ECLI:NL:GHSHE:2023:392', 'ECLI:NL:RBLIM:2020:4534', 'ECLI:NL:RBMNE:2022:427', 'ECLI:NL:RBZWB:2021:4437', 'ECLI:NL:GHARL:2023:2644', 'ECLI:NL:RBNNE:2021:1688', 'ECLI:NL:RBDHA:2022:7061', 'ECLI:NL:RBAMS:2021:1425', 'ECLI:NL:GHAMS:2022:1945', 'ECLI:NL:RBROT:2019:9637', 'ECLI:NL:RBDHA:2022:12415', 'ECLI:NL:RBDHA:2022:12416', 'ECLI:NL:RBDHA:2022:12426', 'ECLI:NL:RBGEL:2022:3714', 'ECLI:NL:GHAMS:2019:4534', 'ECLI:NL:HR:2020:1938', 'ECLI:NL:GHAMS:2023:2184', 'ECLI:NL:RBNHO:2022:5998', 'ECLI:NL:RBMNE:2023:3797', 'ECLI:NL:OGHACMB:2022:274', 'ECLI:NL:RBNHO:2022:5536', 'ECLI:NL:RBMNE:2022:4618', 'ECLI:NL:RBMNE:2022:4619', 'ECLI:NL:RBMNE:2022:4620', 'ECLI:NL:RBLIM:2019:10222', 'ECLI:NL:GHSHE:2022:1848', 'ECLI:NL:GHARL:2023:2690', 'ECLI:NL:RBDHA:2023:1291', 'ECLI:NL:RBGEL:2023:375', 'ECLI:NL:RBLIM:2022:2976', 'ECLI:NL:RBDHA:2021:12628', 'ECLI:NL:RBAMS:2021:1421', 'ECLI:NL:GHAMS:2022:1946', 'ECLI:NL:RBNHO:2020:7125', 'ECLI:NL:RBNHO:2019:5490', 'ECLI:NL:GHARL:2023:3611', 'ECLI:NL:RBNNE:2022:4134', 'ECLI:NL:RBOVE:2021:1477', 'ECLI:NL:RBMNE:2022:4616', 'ECLI:NL:HR:2023:415', 'ECLI:NL:GHAMS:2021:2123', 'ECLI:NL:PHR:2023:44', 'ECLI:NL:RBAMS:2023:440', 'ECLI:NL:RBOVE:2021:4185', 'ECLI:NL:RBNNE:2022:3909', 'ECLI:NL:GHARL:2021:10548', 'ECLI:NL:RBDHA:2022:10386', 'ECLI:NL:GHSHE:2023:447', 'ECLI:NL:RBGEL:2020:1170', 'ECLI:NL:RBAMS:2019:9736', 'ECLI:NL:RBAMS:2023:1524', 'ECLI:NL:RBAMS:2023:1525', 'ECLI:NL:RBNNE:2023:597', 'ECLI:NL:RBAMS:2023:362', 'ECLI:NL:RBOBR:2022:3595', 'ECLI:NL:RBROT:2022:6907', 'ECLI:NL:RBNNE:2022:2374', 'ECLI:NL:GHARL:2022:4707', 'ECLI:NL:RBDHA:2021:10112', 'ECLI:NL:RBAMS:2021:5165', 'ECLI:NL:RBOVE:2020:3435', 'ECLI:NL:RBROT:2020:5609', 'ECLI:NL:GHDHA:2022:2288', 'ECLI:NL:RBMNE:2022:4617', 'ECLI:NL:RBMNE:2022:5409', 'ECLI:NL:RBAMS:2022:7466', 'ECLI:NL:GHSHE:2021:3342', 'ECLI:NL:RBZWB:2020:6012', 'ECLI:NL:HR:2023:265', 'ECLI:NL:RBNNE:2021:2644', 'ECLI:NL:RBMNE:2022:3205', 'ECLI:NL:GHDHA:2021:2483', 'ECLI:NL:RBAMS:2020:5819', 'ECLI:NL:RBGEL:2019:955', 'ECLI:NL:RBNNE:2021:2635', 'ECLI:NL:GHARL:2019:2271', 'ECLI:NL:RBGEL:2016:1715', 'ECLI:NL:GHAMS:2022:291', 'ECLI:NL:HR:2023:984', 'ECLI:NL:RBAMS:2021:1982', 'ECLI:NL:GHDHA:2019:1532', 'ECLI:NL:HR:2021:211', 'ECLI:NL:RBMNE:2022:2307', 'ECLI:NL:RBMNE:2022:2308', 'ECLI:NL:RBROT:2022:1284', 'ECLI:NL:RBOBR:2021:1785', 'ECLI:NL:RBLIM:2020:9691', 'ECLI:NL:GHAMS:2022:514', 'ECLI:NL:HR:2023:983', 'ECLI:NL:RBDHA:2019:7308', 'ECLI:NL:RBZWB:2023:2581', 'ECLI:NL:GHDHA:2021:171', 'ECLI:NL:RBLIM:2019:10219', 'ECLI:NL:GHSHE:2021:25', 'ECLI:NL:RBLIM:2019:2219', 'ECLI:NL:RBAMS:2023:2621', 'ECLI:NL:RBROT:2022:10680', 'ECLI:NL:RBNNE:2022:2141', 'ECLI:NL:RBAMS:2019:9738', 'ECLI:NL:RBAMS:2023:1523', 'ECLI:NL:RBLIM:2022:2729', 'ECLI:NL:GHAMS:2021:1137', 'ECLI:NL:GHARL:2020:5686', 'ECLI:NL:RBMNE:2019:2469', 'ECLI:NL:HR:2022:560', 'ECLI:NL:GHDHA:2020:1306', 'ECLI:NL:HR:2022:176', 'ECLI:NL:RBROT:2020:473', 'ECLI:NL:RBLIM:2019:10390', 'ECLI:NL:GHSHE:2021:680', 'ECLI:NL:RBDHA:2019:11950', 'ECLI:NL:PHR:2019:581', 'ECLI:NL:HR:2019:1295', 'ECLI:NL:PHR:2019:427', 'ECLI:NL:HR:2019:1465', 'ECLI:NL:RBMNE:2022:4615', 'ECLI:NL:RBDHA:2022:12217', 'ECLI:NL:RBDHA:2022:12218', 'ECLI:NL:RBDHA:2022:12216', 'ECLI:NL:RBROT:2020:2020', 'ECLI:NL:RBLIM:2019:10220', 'ECLI:NL:GHSHE:2022:4006', 'ECLI:NL:OGEAA:2023:2', 'ECLI:NL:GHARL:2022:4800', 'ECLI:NL:RBAMS:2021:7333', 'ECLI:NL:RBNNE:2021:1688', 'ECLI:NL:GHARL:2022:2876', 'ECLI:NL:GHARL:2023:2644', 'ECLI:NL:RBROT:2020:5742', 'ECLI:NL:RBROT:2019:3265', 'ECLI:NL:RBGEL:2019:951', 'ECLI:NL:GHARL:2021:10552', 'ECLI:NL:RBAMS:2023:5588', 'ECLI:NL:GHDHA:2022:665', 'ECLI:NL:GHAMS:2021:1136', 'ECLI:NL:GHAMS:2021:1138', 'ECLI:NL:RBLIM:2021:645', 'ECLI:NL:RBZWB:2020:5236', 'ECLI:NL:RBLIM:2019:5777', 'ECLI:NL:GHAMS:2022:317', 'ECLI:NL:HR:2023:982', 'ECLI:NL:RBZWB:2023:2952', 'ECLI:NL:OGEAC:2023:213', 'ECLI:NL:PHR:2022:1142', 'ECLI:NL:HR:2023:15', 'ECLI:NL:GHDHA:2021:1399', 'ECLI:NL:PHR:2021:12', 'ECLI:NL:HR:2021:1024', 'ECLI:NL:PHR:2020:188', 'ECLI:NL:HR:2020:868', 'ECLI:NL:PHR:2019:562', 'ECLI:NL:HR:2019:830', 'ECLI:NL:RBOVE:2023:2460', 'ECLI:NL:PHR:2023:44', 'ECLI:NL:HR:2023:415', 'ECLI:NL:RBNNE:2022:1697', 'ECLI:NL:GHAMS:2019:4432', 'ECLI:NL:HR:2021:536', 'ECLI:NL:GHSHE:2021:680', 'ECLI:NL:RBLIM:2019:10390', 'ECLI:NL:RBROT:2023:9340', 'ECLI:NL:RBNNE:2022:4338', 'ECLI:NL:RBROT:2022:9464', 'ECLI:NL:RBAMS:2021:3711', 'ECLI:NL:RBNHO:2020:7124', 'ECLI:NL:RBNNE:2019:4033', 'ECLI:NL:GHDHA:2022:365', 'ECLI:NL:HR:2023:1495', 'ECLI:NL:RBZWB:2019:1474', 'ECLI:NL:RBDHA:2022:12219', 'ECLI:NL:RBAMS:2023:3868', 'ECLI:NL:GHDHA:2021:856', 'ECLI:NL:PHR:2023:83', 'ECLI:NL:HR:2023:398', 'ECLI:NL:RBNNE:2021:1683', 'ECLI:NL:GHARL:2022:2878', 'ECLI:NL:OGEAC:2020:292', 'ECLI:NL:OGHACMB:2023:99', 'ECLI:NL:OGEAC:2020:293', 'ECLI:NL:OGHACMB:2023:98', 'ECLI:NL:RBNNE:2019:3060', 'ECLI:NL:OGEAC:2019:371', 'ECLI:NL:GHDHA:2021:293', 'ECLI:NL:HR:2022:498', 'ECLI:NL:RBROT:2020:11745', 'ECLI:NL:GHDHA:2022:2003', 'ECLI:NL:GHAMS:2020:3077', 'ECLI:NL:RBAMS:2019:7566', 'ECLI:NL:RBAMS:2019:116', 'ECLI:NL:RBDHA:2022:12601', 'ECLI:NL:GHDHA:2022:2288', 'ECLI:NL:RBROT:2020:5609', 'ECLI:NL:RBNNE:2022:2707', 'ECLI:NL:PHR:2020:1022', 'ECLI:NL:HR:2020:2046', 'ECLI:NL:PHR:2020:991', 'ECLI:NL:HR:2020:1967', 'ECLI:NL:PHR:2023:43', 'ECLI:NL:HR:2023:414', 'ECLI:NL:GHSHE:2022:2712', 'ECLI:NL:RBZWB:2020:2486', 'ECLI:NL:RBROT:2020:11744', 'ECLI:NL:GHDHA:2022:2002', 'ECLI:NL:OGHACMB:2021:57', 'ECLI:NL:RBGEL:2021:4989', 'ECLI:NL:RBOBR:2021:3815', 'ECLI:NL:RBOBR:2021:3814', 'ECLI:NL:GHSHE:2023:2110', 'ECLI:NL:RBNNE:2021:1962', 'ECLI:NL:OGEAC:2020:294', 'ECLI:NL:RBGEL:2020:6016', 'ECLI:NL:RBOVE:2022:1188', 'ECLI:NL:RBNNE:2023:81', 'ECLI:NL:RBOBR:2021:3134', 'ECLI:NL:RBMNE:2019:3031', 'ECLI:NL:GHARL:2020:1141', 'ECLI:NL:RBMNE:2021:5213', 'ECLI:NL:RBROT:2019:4283', 'ECLI:NL:RBROT:2019:4284', 'ECLI:NL:RBAMS:2023:3292', 'ECLI:NL:PHR:2021:1029', 'ECLI:NL:GHDHA:2020:2423', 'ECLI:NL:PHR:2021:910', 'ECLI:NL:HR:2021:1947', 'ECLI:NL:PHR:2020:1018', 'ECLI:NL:HR:2020:2012', 'ECLI:NL:RBROT:2020:8862', 'ECLI:NL:RBGEL:2019:4278', 'ECLI:NL:RBNHO:2019:7395', 'ECLI:NL:GHAMS:2023:455', 'ECLI:NL:RBMNE:2022:2543', 'ECLI:NL:RBMNE:2022:2459', 'ECLI:NL:GHARL:2023:3648', 'ECLI:NL:RBNNE:2023:1715', 'ECLI:NL:GHDHA:2023:1679', 'ECLI:NL:RBNNE:2023:998', 'ECLI:NL:RBOVE:2023:732', 'ECLI:NL:RBDHA:2023:31', 'ECLI:NL:GHARL:2022:11130', 'ECLI:NL:PHR:2021:863', 'ECLI:NL:GHAMS:2019:1181', 'ECLI:NL:HR:2021:1911', 'ECLI:NL:GHAMS:2021:2030', 'ECLI:NL:RBNHO:2021:5561', 'ECLI:NL:OGHACMB:2020:271', 'ECLI:NL:RBMNE:2020:4354', 'ECLI:NL:GHAMS:2020:3215', 'ECLI:NL:RBAMS:2018:3721', 'ECLI:NL:PHR:2020:1106', 'ECLI:NL:HR:2021:211', 'ECLI:NL:RBAMS:2019:4555', 'ECLI:NL:GHAMS:2023:456', 'ECLI:NL:RBAMS:2022:1364', 'ECLI:NL:PHR:2022:16', 'ECLI:NL:HR:2022:176', 'ECLI:NL:GHARL:2021:1917', 'ECLI:NL:RBMNE:2017:405', 'ECLI:NL:HR:2022:900', 'ECLI:NL:GHARL:2021:1918', 'ECLI:NL:RBMNE:2017:408', 'ECLI:NL:RBOBR:2020:1612', 'ECLI:NL:OGEAC:2023:71', 'ECLI:NL:GHSHE:2023:1181', 'ECLI:NL:RBLIM:2022:2975', 'ECLI:NL:GHAMS:2021:2025', 'ECLI:NL:GHAMS:2021:2031', 'ECLI:NL:GHAMS:2021:2032', 'ECLI:NL:HR:2023:397', 'ECLI:NL:GHAMS:2021:2034', 'ECLI:NL:HR:2023:400', 'ECLI:NL:PHR:2021:705', 'ECLI:NL:HR:2021:1127', 'ECLI:NL:RBROT:2020:10171', 'ECLI:NL:RBROT:2019:9745', 'ECLI:NL:RBOBR:2019:5920', 'ECLI:NL:GHSHE:2023:1845', 'ECLI:NL:RBZWB:2019:1475', 'ECLI:NL:GHSHE:2023:333', 'ECLI:NL:RBOBR:2017:6555', 'ECLI:NL:RBMNE:2022:2531', 'ECLI:NL:GHSHE:2020:3785', 'ECLI:NL:RBLIM:2018:5958', 'ECLI:NL:GHARL:2023:7372', 'ECLI:NL:GHAMS:2021:2026', 'ECLI:NL:HR:2023:401', 'ECLI:NL:GHAMS:2021:2033', 'ECLI:NL:HR:2023:398', 'ECLI:NL:RBNNE:2020:3975', 'ECLI:NL:GHARL:2021:9523', 'ECLI:NL:RBLIM:2022:5544', 'ECLI:NL:GHAMS:2021:2027', 'ECLI:NL:RBMNE:2022:2467', 'ECLI:NL:RBMNE:2022:2461', 'ECLI:NL:RBOVE:2020:3694', 'ECLI:NL:GHARL:2021:6274', 'ECLI:NL:GHARL:2021:9523', 'ECLI:NL:RBNNE:2020:3975', 'ECLI:NL:HR:2022:1905', 'ECLI:NL:PHR:2023:141', 'ECLI:NL:HR:2023:485', 'ECLI:NL:RBOVE:2020:3666', 'ECLI:NL:GHARL:2021:6275', 'ECLI:NL:RBAMS:2023:4098', 'ECLI:NL:RBZWB:2023:3096', 'ECLI:NL:GHARL:2022:2574', 'ECLI:NL:RBOVE:2019:1347', 'ECLI:NL:RBGEL:2021:4990', 'ECLI:NL:RBLIM:2020:5514', 'ECLI:NL:RBAMS:2019:3208', 'ECLI:NL:PHR:2023:50', 'ECLI:NL:HR:2023:321', 'ECLI:NL:PHR:2023:54', 'ECLI:NL:HR:2023:317', 'ECLI:NL:PHR:2023:55', 'ECLI:NL:HR:2023:322', 'ECLI:NL:RBLIM:2020:5510', 'ECLI:NL:RBOVE:2020:582', 'ECLI:NL:GHARL:2021:7542', 'ECLI:NL:RBMNE:2022:2562', 'ECLI:NL:OGEAC:2019:168', 'ECLI:NL:RBMNE:2022:2541', 'ECLI:NL:RBNHO:2022:291', 'ECLI:NL:RBMNE:2019:1448', 'ECLI:NL:GHARL:2020:10689', 'ECLI:NL:RBNNE:2019:1188', 'ECLI:NL:GHARL:2019:7845', 'ECLI:NL:RBOVE:2020:3678', 'ECLI:NL:GHARL:2021:6276', 'ECLI:NL:PHR:2023:53', 'ECLI:NL:HR:2023:320', 'ECLI:NL:GHDHA:2022:973', 'ECLI:NL:GHDHA:2022:1674', 'ECLI:NL:RBROT:2022:4297', 'ECLI:NL:RBNHO:2022:272', 'ECLI:NL:RBMNE:2022:2403', 'ECLI:NL:PHR:2022:433', 'ECLI:NL:HR:2022:1250', 'ECLI:NL:GHAMS:2020:2767', 'ECLI:NL:RBDHA:2022:14037', 'ECLI:NL:RBDHA:2022:14036', 'ECLI:NL:RBDHA:2022:14039']

unique_list = list(set(raw_ECLI))


