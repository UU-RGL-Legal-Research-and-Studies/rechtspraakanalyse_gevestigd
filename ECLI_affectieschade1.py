#Code where all ECLIs are stored after webparsing from rechtspraak.nl
#The ECLIs are later imported in ECLI_cache_affectieschade for cache purposes

raw_ECLI= ['ECLI:NL:RBROT:2023:7185', 'ECLI:NL:RBGEL:2023:759', 'ECLI:NL:GHDHA:2023:586', 'ECLI:NL:RBMNE:2023:2738', 'ECLI:NL:RBMNE:2023:2743', 'ECLI:NL:RBDHA:2023:2882', 'ECLI:NL:RBROT:2023:2367', 'ECLI:NL:GHARL:2023:9585', 'ECLI:NL:RBNHO:2023:4432', 'ECLI:NL:RBNNE:2023:2478', 'ECLI:NL:GHAMS:2023:2551', 'ECLI:NL:RBMNE:2023:2735', 'ECLI:NL:RBZWB:2023:1313', 'ECLI:NL:RBNNE:2023:2480', 'ECLI:NL:GHARL:2023:5899', 'ECLI:NL:RBZWB:2023:1423', 'ECLI:NL:RBROT:2023:8858', 'ECLI:NL:RBNHO:2023:3506', 'ECLI:NL:RBNHO:2023:6053', 'ECLI:NL:GHARL:2023:9371', 'ECLI:NL:GHDHA:2023:1934', 'ECLI:NL:RBDHA:2023:227', 'ECLI:NL:RBNHO:2023:11747', 'ECLI:NL:RBAMS:2023:4658', 'ECLI:NL:RBAMS:2023:4657', 'ECLI:NL:RBNHO:2023:1372', 'ECLI:NL:RBZWB:2023:3995', 'ECLI:NL:RBNHO:2023:4113', 'ECLI:NL:RBNHO:2023:628', 'ECLI:NL:RBMNE:2023:3966', 'ECLI:NL:RBROT:2023:2624', 'ECLI:NL:RBMNE:2023:6178', 'ECLI:NL:RBOBR:2023:4756', 'ECLI:NL:RBROT:2023:6401', 'ECLI:NL:RBMNE:2023:6175', 'ECLI:NL:RBAMS:2023:4656', 'ECLI:NL:RBROT:2023:5916', 'ECLI:NL:RBLIM:2023:6489', 'ECLI:NL:GHAMS:2023:2456', 'ECLI:NL:HR:2023:1495', 'ECLI:NL:PHR:2023:782', 'ECLI:NL:GHDHA:2022:365', 'ECLI:NL:GHAMS:2023:1181', 'ECLI:NL:RBNHO:2020:10959', 'ECLI:NL:RBGEL:2023:3322', 'ECLI:NL:GHAMS:2023:2457', 'ECLI:NL:RBDHA:2023:8915', 'ECLI:NL:RBDHA:2023:8914', 'ECLI:NL:RBAMS:2023:3855', 'ECLI:NL:RBDHA:2023:10123', 'ECLI:NL:RBDHA:2023:8917', 'ECLI:NL:GHAMS:2023:1580', 'ECLI:NL:RBDHA:2023:10309', 'ECLI:NL:RBROT:2023:1840', 'ECLI:NL:RBDHA:2023:10119', 'ECLI:NL:RBOVE:2023:426', 'ECLI:NL:RBGEL:2023:2823', 'ECLI:NL:RBGEL:2023:5281', 'ECLI:NL:RBGEL:2023:3167', 'ECLI:NL:RBROT:2023:4715', 'ECLI:NL:RBOBR:2023:1622', 'ECLI:NL:RBZWB:2023:3718', 'ECLI:NL:RBDHA:2023:15274', 'ECLI:NL:RBZWB:2023:3715', 'ECLI:NL:RBROT:2023:6164', 'ECLI:NL:RBDHA:2023:8720', 'ECLI:NL:RBZWB:2023:2844', 'ECLI:NL:RBROT:2023:11290', 'ECLI:NL:RBROT:2023:9345', 'ECLI:NL:RBROT:2023:9337', 'ECLI:NL:RBOVE:2023:2266', 'ECLI:NL:RBGEL:2023:1723', 'ECLI:NL:RBROT:2023:7348', 'ECLI:NL:RBAMS:2023:2762', 'ECLI:NL:RBAMS:2023:6146', 'ECLI:NL:RBDHA:2023:15273', 'ECLI:NL:RBDHA:2023:1778', 'ECLI:NL:RBOVE:2023:4780', 'ECLI:NL:GHDHA:2023:1844', 'ECLI:NL:RBMNE:2023:2554', 'ECLI:NL:RBZWB:2023:3940', 'ECLI:NL:RBOBR:2023:3293', 'ECLI:NL:RBROT:2023:3562', 'ECLI:NL:RBROT:2023:9342', 'ECLI:NL:GHAMS:2023:1188', 'ECLI:NL:RBMNE:2023:1941', 'ECLI:NL:GHAMS:2023:2636', 'ECLI:NL:RBNNE:2023:4127', 'ECLI:NL:RBROT:2023:2713', 'ECLI:NL:RBDHA:2023:15276', 'ECLI:NL:RBNHO:2023:3870', 'ECLI:NL:GHARL:2023:9761', 'ECLI:NL:RBNHO:2023:9267', 'ECLI:NL:RBZWB:2023:4977', 'ECLI:NL:GHDHA:2023:1792', 'ECLI:NL:RBNHO:2023:3879', 'ECLI:NL:RBDHA:2023:10120', 'ECLI:NL:GHARL:2023:1254', 'ECLI:NL:RBMNE:2022:2523', 'ECLI:NL:RBLIM:2023:6128', 'ECLI:NL:GHSHE:2023:753', 'ECLI:NL:RBROT:2023:4683', 'ECLI:NL:RBMNE:2023:164', 'ECLI:NL:RBAMS:2023:2661', 'ECLI:NL:RBAMS:2023:2620', 'ECLI:NL:RBMNE:2023:166', 'ECLI:NL:RBAMS:2023:1076', 'ECLI:NL:RBAMS:2023:4719', 'ECLI:NL:RBOBR:2023:5459', 'ECLI:NL:RBZWB:2023:8069', 'ECLI:NL:RBNHO:2023:2767', 'ECLI:NL:GHDHA:2023:2189', 'ECLI:NL:RBLIM:2023:3900', 'ECLI:NL:RBAMS:2023:4721', 'ECLI:NL:RBAMS:2023:5048', 'ECLI:NL:RBMNE:2023:18', 'ECLI:NL:RBZWB:2023:7959', 'ECLI:NL:RBZWB:2023:7952', 'ECLI:NL:RBDHA:2023:8838', 'ECLI:NL:RBZWB:2023:7973', 'ECLI:NL:RBNHO:2023:3793', 'ECLI:NL:RBDHA:2023:8391', 'ECLI:NL:RBROT:2023:6468', 'ECLI:NL:GHAMS:2023:1327', 'ECLI:NL:GHARL:2023:2695', 'ECLI:NL:RBROT:2023:2948', 'ECLI:NL:GHSHE:2023:2138', 'ECLI:NL:RBROT:2023:1225', 'ECLI:NL:RBROT:2023:6467', 'ECLI:NL:PHR:2023:782', 'ECLI:NL:HR:2023:1495', 'ECLI:NL:PHR:2023:435', 'ECLI:NL:HR:2023:984', 'ECLI:NL:PHR:2023:436', 'ECLI:NL:HR:2023:982', 'ECLI:NL:RBNNE:2023:4484', 'ECLI:NL:GHARL:2023:5898', 'ECLI:NL:RBGEL:2021:4870', 'ECLI:NL:RBZWB:2023:6737', 'ECLI:NL:RBMNE:2023:165', 'ECLI:NL:RBMNE:2023:5681', 'ECLI:NL:RBNHO:2023:7408', 'ECLI:NL:PHR:2023:437', 'ECLI:NL:HR:2023:983', 'ECLI:NL:RBOVE:2023:4204', 'ECLI:NL:RBOVE:2023:4210', 'ECLI:NL:RBROT:2023:3273', 'ECLI:NL:RBZWB:2023:5382', 'ECLI:NL:OGEAA:2023:214', 'ECLI:NL:RBAMS:2023:1075', 'ECLI:NL:RBDHA:2023:956', 'ECLI:NL:RBDHA:2023:1861', 'ECLI:NL:RBZWB:2023:5225', 'ECLI:NL:RBAMS:2023:299', 'ECLI:NL:RBNNE:2023:1792', 'ECLI:NL:RBOBR:2023:164', 'ECLI:NL:GHAMS:2023:1510', 'ECLI:NL:RBROT:2023:9332', 'ECLI:NL:RBAMS:2023:4512', 'ECLI:NL:RBMNE:2023:884', 'ECLI:NL:RBGEL:2023:4056', 'ECLI:NL:GHSHE:2023:3270', 'ECLI:NL:GHSHE:2023:3277', 'ECLI:NL:RBOVE:2023:4203', 'ECLI:NL:GHAMS:2023:2182', 'ECLI:NL:RBDHA:2023:14981', 'ECLI:NL:RBNHO:2023:4374', 'ECLI:NL:RBNHO:2023:4434', 'ECLI:NL:RBAMS:2023:269', 'ECLI:NL:RBLIM:2023:6813', 'ECLI:NL:PHR:2023:84', 'ECLI:NL:HR:2023:400', 'ECLI:NL:RBMNE:2023:6176', 'ECLI:NL:RBOVE:2023:3035', 'ECLI:NL:RBDHA:2023:8850', 'ECLI:NL:RBROT:2023:8461', 'ECLI:NL:GHSHE:2023:1157', 'ECLI:NL:RBOBR:2020:5134', 'ECLI:NL:GHSHE:2023:738', 'ECLI:NL:GHSHE:2023:392', 'ECLI:NL:RBLIM:2020:4534', 'ECLI:NL:GHARL:2023:2644', 'ECLI:NL:RBNNE:2021:1688', 'ECLI:NL:GHAMS:2023:2184', 'ECLI:NL:RBMNE:2023:3797', 'ECLI:NL:GHARL:2023:2690', 'ECLI:NL:RBDHA:2023:1291', 'ECLI:NL:RBGEL:2023:375', 'ECLI:NL:GHARL:2023:3611', 'ECLI:NL:RBMNE:2023:6283', 'ECLI:NL:HR:2023:415', 'ECLI:NL:GHAMS:2021:2123', 'ECLI:NL:PHR:2023:44', 'ECLI:NL:RBAMS:2023:440', 'ECLI:NL:GHSHE:2023:447', 'ECLI:NL:RBAMS:2023:1524', 'ECLI:NL:RBAMS:2023:1525', 'ECLI:NL:RBNNE:2023:597', 'ECLI:NL:RBAMS:2023:362', 'ECLI:NL:OGEAA:2023:290', 'ECLI:NL:RBZWB:2023:2581', 'ECLI:NL:RBAMS:2023:2621', 'ECLI:NL:RBAMS:2023:1523', 'ECLI:NL:RBZWB:2023:8013', 'ECLI:NL:OGEAA:2023:2', 'ECLI:NL:RBAMS:2023:5588', 'ECLI:NL:RBZWB:2023:2952', 'ECLI:NL:OGEAC:2023:213', 'ECLI:NL:PHR:2023:1088', 'ECLI:NL:RBOVE:2023:2460', 'ECLI:NL:PHR:2023:44', 'ECLI:NL:HR:2023:415', 'ECLI:NL:RBROT:2023:9340', 'ECLI:NL:RBAMS:2023:3868', 'ECLI:NL:RBAMS:2023:7010', 'ECLI:NL:PHR:2023:83', 'ECLI:NL:HR:2023:398', 'ECLI:NL:PHR:2023:43', 'ECLI:NL:HR:2023:414', 'ECLI:NL:RBOVE:2023:4745', 'ECLI:NL:RBNNE:2023:81', 'ECLI:NL:RBAMS:2023:3292', 'ECLI:NL:GHAMS:2023:455', 'ECLI:NL:GHARL:2023:3648', 'ECLI:NL:RBNNE:2023:1715', 'ECLI:NL:GHDHA:2023:1679', 'ECLI:NL:RBNNE:2023:998', 'ECLI:NL:RBOVE:2023:732', 'ECLI:NL:RBDHA:2023:31', 'ECLI:NL:GHAMS:2023:456', 'ECLI:NL:OGEAC:2023:71', 'ECLI:NL:GHSHE:2023:1181', 'ECLI:NL:RBLIM:2022:2975', 'ECLI:NL:GHSHE:2023:333', 'ECLI:NL:RBOBR:2017:6555', 'ECLI:NL:GHARL:2023:7372', 'ECLI:NL:PHR:2023:141', 'ECLI:NL:HR:2023:485', 'ECLI:NL:RBAMS:2023:4098', 'ECLI:NL:RBZWB:2023:3096', 'ECLI:NL:PHR:2023:50', 'ECLI:NL:HR:2023:321', 'ECLI:NL:PHR:2023:54', 'ECLI:NL:HR:2023:317', 'ECLI:NL:PHR:2023:55', 'ECLI:NL:HR:2023:322', 'ECLI:NL:PHR:2023:53', 'ECLI:NL:HR:2023:320']

unique_list = list(set(raw_ECLI))


