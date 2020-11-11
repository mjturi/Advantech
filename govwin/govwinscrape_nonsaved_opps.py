from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import schedule

# Function definition for entire bot process
def bot():
    #'181388','171087','198553','196584','170684','184113','175254','190787','184741','177134','120409','189410','197564','198346','172885','193903','122043','193886','176100','192192','117846','193491','168729','196987','165904','161899','184739','195364','164478','154341','195310','191328','188213','190207','192405','190765','110397','147277','190248','102564','159654','177161','186436','184050','164956','191492','173132','151149','161968','182936','135522','174629',
    # These need to be set to potentially a list of ids or search criteria we are looking for BEFORE ran
    IDS = ['171347','181195','156036','161356','192780','141800','184204','178769','175366','190777','185329','172265','188878','157944','191732','189120','188566','186416','169255','175417','183454','142425','109459','187078','175740','173264','164213','179382','179551','183779','184220','175295','170100','177839','143276','148198','179793','176041','161109','171523','181816','173658','181394','154018','168929','129134','162604','173123','173410','179805','151444','146009','177347','171921','145779','175138','146477','154933','173406','115203','172769','176013','166316','175579','171723','175537','121244','175335','168816','154774','149941','171218','166061','168401','147556','108465','146286','162085','156059','162299','162442','164870','157873','80242','164680','129445','153205','159411','152290','167822','156123','163921','146837','145780','140174','165605','166211','164137','168497','128786','145629','164134','93535','168110','159703','109610','164132','159231','120264','164189','165588','158143','164929','154484','161745','164419','107691','163890','164091','148630','159004','159581','161927','156659','114536','120309','114178','125559','159287','122083','142081','162573','142925','138981','148632','160865','148880','93943','105459','109442','152322','150239','119367','159680','122051','105010','121348','66054','113588','113857','152299','127744','148317','150131','124385','154051','158836','148635','151543','148626','143018','108469','130184','119064','152813','147622','96386','140899','94247','151786','144474','101216','147916','110469','123718','140660','122524','139616','139448','133696','133506','118495','114114','148655','125724','148234','122478','122103','139838','142675','136706','83569','145049','106531','95569','139656','127299','97244','131592','110449','128957','79710','142497','124296','105919','88894','106639','133541','108239','101092','136345','139297','138948','130423','135460','133997','132969','136990','101549','135557','106399','121691','103360','124055','114760','110485','98309','110479','83745','64990','134575','131626','91144','127392','115768','127941','96813','102610','121087','129898','118567','130359','130769','123023','97243','104161','130598','124239','129604','100244','125618','125463','121350','128434','125720','65991','63605','89028','95908','72209','126919','118709','115149','120613','125045','66383','85438','103164','125329','82085','87386','125686','51665','93464','125858','121196','102144','115085','121854','123333','107622','122740','119911','81721','120930','124488','54023','109872','123482','113093','102255','121668','99494','113464','118205','120438','104683','114944','117310','119961','68056','116727','118931','108902','88057','80250','115454','116467','104294','114484','114993','90330','95805','108928','99150','116232','110108','97733','115139','112956','115316','102037','114167','91932','86868','84660','113797','84334','104159','86874','103823','113584','101345','68330','111013','105832','106430','103469','111884','82449','95727','92212','76954','101910','109950','93868','98120','104686','103601','105546','105733','107233','110434','92817','104441','86536','98445','103501','101897','100485','103814','102393','77452','58820','96151','97439','97805','101027','101568','73498','87498','98523','112672','102005','69356','90228','108702','94891','87869','97777','65123','85049','81737','99883','95349','98090','100208','86086','66026','99619','60889','94792','85465','83500','76956','96719','66743','97267','97236','92981','95859','91995','92179','86013','94085','58098','47179','89183','94542','84801','59381','48776','83868','93288','80156','91048','83207','71693','76739','79358','63828','89680','91373','91455','88633','59961','91186','82573','80594','85913','81686','63485','64838','90185','49050','90097','82856','87937','89524','72442','88586','86580','81196','79130','53607','68978','71848','85050','88528','112776','33737','70551','75972','81283','52424','49307','76234','86883','72572','74068','61378','84664','79138','61303','71100','68947','79611','86136','33743','65433','84108','71214','85035','67599','84882','82451','83329','69225','53631','71902','80609','79410','53256','79838','79384','71239','80367','83321','45779','67258','67365','45085','69897','70198','67500','70738','68360','82468','71042','77239','45404','45256','71410','75675','81061','70064','81162','77124','76098','49037','61704','68253','48316','68303','72918','49315','17569','59710','69578','55236','77922','69354','78552','50780','44696','42633','70827','68110','50801','66605','70336','70929','68080','70338','75891','75687','69530','67223','37408','57831','68434','59296','75713','74018','44848','49287','35131','59650','66525','73687','75632','71247','47293','71659','52487','63703','66715','68255','74996','46700','56412','70057','69992','54939','50044','70256','48159','70158','45427','74721','66995','37276','69499','69504','61809','63266','66095','60055','70112','51788','49741','36796','64031','68176','60320','51790','64044','46549','48995','63911','14291','67150','64657','66028','66191','63516','61281','66189','62426','61370','64127','66213','60561','42946','66494','61539','33539','58404','57394','51159','52127','48705','66009','63008','62544','65799','65517','42093','45567','54616','64141','65383','65272','59632','64781','50373','47416','65022','39670','60667','37338','59874','36224','62097','63023','64108','46690','62363','63686','44358','58571','63546','73855','46072','48251','43656','60874','60444','1464','58872','62368','60810','51852','36970','56869','34264','60305','55934','61167','59619','49292','59383','56260','58618','39873','86867','61355','59008','60987','60740','49145','62081','60474','59736','47470','49818','57391','48738','60190','40611','59855','54046','59804','59798','6645','59584','40354','56974','32155','57407','57868','59258','50863','54217','49951','38008','55667','58694','50741','58546','51539','56791','54428','52382','57323','57270','34895','50853','41934','53402','56901','57791','50910','57435','50420','54956','54563','55662','56602','41082','52313','56501','48027','50685','37104','56210','51101','44556','47629','52625','51359','40123','44239','31800','52829','52731','48774','38099','48675','55106','54326','43502','58602','52709','55038','51063','51004','50760','50838','54277','51137','34874','47617','50305','47298','53373','42745','52275','52986','52195','52097','51606','48467','52365','51066','47414','47778','49109','40175','51648','51560','33147','37311','49372','50723','33938','50635','49026','50543','48989','43732','48544','49360','46905','33913','48669','48671','34341','48486','49258','36521','38245','48024','48348','33941','48918','15493','46100','48424','42065','46021','47780','46945','47239','41234','43911','47845','45396','44182','47049','41052','47548','46699','45980','46966','47319','42775','46120','16236','31970','45088','36527','44066','47266','15761','32835','46223','46412','44516','41600','45179','39019','45282','44579','44710','59158','15435','45754','45630','38578','33496','33338','42187','44418','44968','39313','40556','16649','44062','40359','17032','41307','42478','43906','43121','44623','43440','43522','36656','44203','44204','44206','35875','44627','38360','43662','42714','43333','41077','42296','38556','39809','38604','42514','39079','16871','40194','40831','41067','39920','41176','16535','39220','40973','41199','39135','16354','39775','37321','41693','30959','37840','15907','6609','40282','39319','40048','37457','38211','38562','39035','39168','34210','39457','38364','39370','6910','39226','39181','17613','4895','5105','14155','38724','14637','15568','37766','38470','16820','33619','36601','38041','38396','34114','38376','36990','38285','36290','37990','33463','31952','37795','37538','16373','33734','36615','16822','37060','35735','35429','15569','37048','36650','36068','37009','36863','35191','36048','35948','36985','36987','37011','15290','30950','36117','35144','31853','35367','35724','31668','4933','32164','34560','34829','31157','32794','16185','32676','34132','30941','33873','33554','15486','4989','3865','32973','5111','33730','14422','32866','7300','32635','14525','32701','31086','13016','16034','16291','17023','31380','32059','6807','15289','13194','31947','31056','7070','17607','38130','16778','31113','17352','17254','14121','14270','16987','14180','15918','17200','15009','14169','13741','16148','13147','16589','16323','11877','16334','15335','14583','16285','3482','13769','16116','14575','16487','15177','14420','15769','14104','15530','15560','15951','6132','11780','15151','13446','11087','11596','15102','3395','15225','15294','14537','14655','14573','13436','12325','13267','14719','8959','13707','10813','14150','14316','14037','9718','12017','8082','13580','14240','12224','13778','13663','12908','9768','13229','13337','9931','12764','9745','7373','12772','12685','12972','8425','12490','11652','11085','12586','12733','11856','5136','11847','12210','11366','12144','11452','12066','11922','9712','5884','11410','10404','12131','11014','8712','8930','10597','9012','9355','10755','6044','10788','10868','9500','10581','10445','10459','3959','3703','6594','8929','9885','9395','8095','10146','9103','2318','7490','9354','6535','7475','9466','5358','7727','8806','8926','9289','8568','8261','6954','3216','8291','8367','7879','6454','6533','7107','7149','6186','7439','6467','5364','6982','6463','8486','4214','7011','6611','6999','3175','6049','6979','4966','6855','5321','5384','6636','5120','5868','6277','6758','6326','5973','6226','3403','3808','6400','4086','3631','5778','5901','5361','5699','4170','5916','4582','2362','4378','2830','4288','3952','5939','2967','4099','3722','3321','4059','3732','4515','4388','4926','3513','3114','3830','4169','3954','3821','2462','4324','2959','5758','2963','2172','3129','3532','3601','2678','7710','3877','3290','3772','3547','3817','2520','4025','3335','3084','3466','2739','3412','2857','3474','311','2324','2535','481','2869','2991','3045','3041','657','2898','2235','2952','2953','2954','2957','3004','3002','2912','8077','1656','2883','2650','2757','2583','2165','2682','1873','2240','2323','3617','1861','2776','2594','2545','2612','911','2420','2335','2479','2300','550','2572','2186','2382','1736','2319','2219','2277','2260','1685','1860','2264','929','2016','1807','1421','2108','2102','1848','1778','2406','835','1749','2139','1930','1894','930','1783','1793','3169','1854','234','1071','1474','1857','822','1471','1496','1648','1719','1634','1677','1591','1536','1637','1578','1427','1520','1521','1525','1223','879','641','1497','381','44','1401','1228','15','1255','724','464','1430','336','307','221','72','821','525','646','526','1096','408','1087','183','1159','480','910','1326','713','514','628','656','1346','1086','803','551','366','764','633','120','21','850','834','759','1083','1050','1004245','1005058','1009749','1010153','1011709','1014591','1020630','1024848','1025558','1026244','1026653','1032570','1033318','1037787','103884','1043006','1047585','1049944','1051001','1052845','1053470','1057615','105819','1058249','105841','1058462','1060760','1064415','1064426','1066519','1066988','1068107','106811','1068206','1068551','1069516','1073875','1075806','1076628','1076809','1077683','1077926','1078318','1078331','1078334','1079930','1079997','1080840','1082283','1083487','1085457','1086238','1086303','1088711','109039','1093247','1093830','1094832','1096741','109896','1099303','1099347','110486','1114168','11145','1118989','1119722','1120872','112828','1130893','1132325','113273','1133287','1136410','1137051','1138577','1141766','1143245','1143473','114580','114661','114829','1151084','1151445','1152226','1155802','1156241','1156634','1158667','1161063','1161329','1161658','1161826','1161853','1163078','1164663','1164744','1166638','1167752','1169517','116970','1172303','1174003','1174982','1175107','1176317','11774','1177796','1179383','1180886','1183075','1183142','1184070','1185055','1185292','1187221','1188011','1188841','1190363','1190438','1190978','119230','119330','1194796','1200212','1200214','1200693','1201047','1201165','1201266','1201283','1204087','1204289','1205025','1208231','1209022','1210563','1213272','1214275','1214535','1219062','1219758','1219834','1230630','1233492','123489','1235490','123676','1238435','1241922','1241925','1243017','1243070','1245229','1248439','1248822','125263','1253364','1254769','1255313','1256559','1257436','12583','1258318','1258693','1261580','1262963','1269260','1270936','12724','1273090','1274189','1275935','12776','1278183','1279605','12802','1283495','1290741','1302645','130782','1315532','1316219','1320109','1320603','132481','1325655','1326297','132659','1330317','1330586','1332259','133371','1337099','1337117','1337139','1338884','1341003','134164','1343441','1344128','1345409','1345964','1346276','1346383','1350502','1354702','1355381','1356087','1368','1368225','1368610','1371661','1374471','1382296','1383651','1384105','1385959','1386792','1394149','1394273','1400504','1402317','1404789','14063','140943','1416421','141829','142154','1426393','1430744','1433842','1436964','144293','1443616','1448952','1450678','1451674','1452580','1453490','1454307','1455717','1463224','1467410','1467521','1472195','147267','1473385','1474578','1475183','147947','1480202','1480493','1481646','1483164','1487933','1488527','1488534','1489855','1490628','1491141','1494508','1494520','1495638','1497708','1499011','1501569','1504314','1505868','1505961','1506217','1506941','1509627','1509871','1513806','1514546','1517228','1518228','1518507','1518706','1521129','1522076','1522106','152277','1525796','1525804','1527383','1527450','1527535','1527810','1530610','1531607','1532801','1533207','1535196','1536533','1536830','1537002','1538475','1538789','153899','1539744','1541419','1541522','154252','1549816','1552677','1552790','155480','1558461','1559904','156044','1563777','1565241','1566587','1571948','1571964','1571988','1572735','1573204','1573709','1577229','1577998','1581826','1582793','1583506','1583825','1585385','1585855','1588054','1591228','1593400','1594928','1597283','1597556','1600320','1602869','1604019','1604454','1605377','160786','1608355','1608585','1611006','1614009','1618164','161989','1622847','1623226','1623778','1627933','1635063','1636085','1637467','1638222','1638279','1638841','1638985','1644369','1650387','1650445','165305','1654764','16558','1658973','16613','1665034','1666768','1667109','1667345','1667843','1667859','1670571','1679204','1679408','1684594','1687626','168800','168870','1689499','1691940','1693534','1693672','1695366','1696425','1696448','1696711','169963','1700952','1702855','1703845','1703861','1706344','1706403','1708422','1711041','1719630','172366','1725721','1727211','1728888','1735038','1736940','1738463','1739896','1740193','1746263','1747344','1747629','1749377','1751245','1751781','1752545','175504','1755401','1755555','1756116','1756199','1757330','1757480','1757985','175833','1761158','1761743','1761893','176404','17660','1769819','1769949','17703','177077','1773313','1773814','1774108','1778256','1778875','1781020','1782315','1782940','1783327','1783695','1785014','1788298','1791430','1795115','1795261','1798837','180122','1820814','1824990','1825567','1827718','1828080','18292','183119','1832768','1833455','1836561','1837271','1839414','1841439','1841855','1853474','1854697','1855736','1866581','1874100','1876252','1877957','1879316','1887955','18900','18909','1892687','1895761','1898184','1901194','1908182','1910010','1917645','1922656','1923250','1923794','1925370','1932655','1940260','194117','1946223','1946275','1947307','1950596','1951766','1952034','1954871','1960575','1962657','1968837','1974352','1974948','1977749','1978152','197972','1980698','1981107','199472','1998159','199976','2000166','2000210','2001565','2003147','2004874','2006932','2009174','2014805','2016037','2018384','2018479','2023489','202442','2026648','2026707','2027776','202966','2031908','2035920','2040268','2052824','2057280','20573','2061450','2063399','2063415','20669','2074285','2075062','2082100','208866','2097172','2097910','2099920','2100420','2103534','2112231','2117455','2118244','212020','2123838','2130917','2134034','2134397','2136823','2143009','2147679','2147703','2150687','2155552','2155710','216292','216403','2171318','2173100','2175761','2177826','2190775','2196758','2198436','2199007','2206249','2209657','2209725','2213925','221615','2218408','2219610','2222863','2224261','222509','2225608','2227210','2227269','2227392','2227433','222773','2228152','2231605','2235080','22390','2239879','2240265','2240405','2240841','224816','224853','2251595','2252678','2253038','2254537','2255809','2256217','2259454','2261474','2263391','2272413','2272495','2278794','2278853','2282591','2284348','2286066','2290017','229280','229295','2300064','230117','2301187','2301749','230305','2305551','2305575','2307552','2309513','2310262','23121','2317868','2319488','2320194','2324058','2326935','2330463','2331202','2331634','2335929','2342625','23473','2349539','2352758','236223','2372768','2377827','237847','238136','2381536','2389549','2390549','2391419','2392513','2396459','2397352','2398233','2404829','2406767','2407973','2409083','2411361','2411888','2417964','2427333','243130','2436326','243868','2448598','2448603','2448920','2449580','2451432','2452397','2454600','2458119','2463114','2467510','2474761','2474890','2475551','2476897','2483937','2485767','2488833','2490633','2491038','2491639','2500300','2509219','2513568','25141','2516824','2519987','2524514','2526728','2528098','2529347','2531931','2532483','2533106','2535361','2536233','2538756','2543008','2548667','255084','255501','2561718','2562804','2573597','2574612','2576075','2581209','2585102','2592367','2592631','2592698','2609587','2610313','2610656','2620498','2621787','2622132','2624619','2627160','2627596','2629151','2631896','2633906','2635009','2635936','2637748','2642726','2646974','2650861','2660506','2664770','2667348','2667965','2669546','267709','2677873','2692533','269878','2700027','2704541','2712807','2713023','2726461','2730228','2733148','2740702','2744827','2758515','2772293','2774520','2775188','2776610','2777046','2778231','2781311','2783208','278944','2810057','2810075','2814133','2821326','2826043','2828179','2838028','2843438','28436','2849755','2849987','2850152','2853223','2861563','2862882','2864002','2866416','2869132','2869334','2869357','2869461','2872816','2885839','2886784','2886977','288825','2893723','2895024','2895470','2897334','2897999','2898019','2912','2913287','2913816','291850','2928047','2929779','2930215','294','2948038','2958229','2965539','2980871','2982872','2989376','2989997','2990919','3001346','3010222','3013553','3020623','302343','302410','3027545','3030567','3031236','3031252','3034671','3039585','3048886','3049873','3050892','305490','305703','306765','307165','309394','309932','317035','31804','319667','320945','328385','33866','340383','34137','34492','345766','356533','362711','365694','375472','377604','37786','37953','380956','382070','38416','385675','401678','405424','405876','40605','409055','409085','411069','413005','413650','415308','415335','415883','416080','416222','421284','421427','42201','422030','422064','422783','427247','433971','43408','43489','43628','439483','444050','446385','448609','449352','455003','455135','455387','456306','456724','458053','459068','459697','461805','467972','468957','468990','472620','472923','479916','481041','481375','484715','484779','492040','494368','494925','495019','500737','502048','502076','507411','51420','515886','516062','519193','531465','537719','538534','5390','540183','54041','544807','545650','547732','549754','550868','552055','555022','55549','555579','55699','558266','558383','559779','560365','560513','560966','560993','561496','561548','561661','562087','562901','563133','566625','566655','566983','567243','567278','568261','568852','568937','570806','572653','573660','575257','577532','580247','580342','580345','586125','590915','593016','593099','593902','600355','603198','604897','611711','613943','614843','619297','620957','622402','62245','625348','626168','627147','627410','628739','638112','65069','653554','660607','660612','662165','663940','665708','666103','66619','668122','66891','669762','669981','671062','676382','678012','6782','680732','681193','68450','693219','694819','697327','697402','703021','70390','705494','707935','71004','711456','712453','717105','717536','721302','721329','723224','723232','728604','728963','729895','733081','734676','735924','738525','738773','741060','742344','744242','744300','751585','755770','756114','758508','760537','769462','769658','770048','771184','778438','781713','782113','78278','785627','786315','786338','786929','787155','789653','789733','790367','792643','79700','798143','79860','800014','800034','800151','806491','811692','813935','814291','814540','814636','814680','816104','816371','818596','819773','823218','823473','826995','829132','830808','830841','830948','836185','838574','839398','842729','845993','84620','846373','847265','847266','848936','854354','854581','854706','856164','857424','861237','863759','86509','8663','870234','871912','872515','873246','874627','878050','880918','882891','884622','885152','886490','886599','886634','88722','892245','893040','893249','895927','896477','8983','898651','899859','90225','902579','903811','90502','905837','906535','90772','910668','911466','912097','913932','916610','916705','9221','925029','927567','929159','930656','931390','932909','933457','938038','942413','945011','945629','949917','95156','953152','955676','955860','959204','961970','964581','97189','973560','981675','984651','990067','991703','992285','99461','10031','100394','101589','10179','103095','103846','103944','104039','104915','105348','106144','106159','107603','107700','107747','107771','107772','107783','107909','107943','108394','108395','108499','108537','108589','108780','108785','108816','108880','109047','109061','109162','109199','109231','109342','109468','109507','109822','109828','109896','109908','109954','110113','110121','110249','110332','110372','110391','110401','110422','111614','11183','112284','112574','113267','113398','113403','114953','115069','116908','118679','118780','122538','122736','122957','123132','123363','123370','123488','12429','12546','126125','127891','127954','128627','128974','129326','129978','130023','13049','13082','132421','132893','13529','135410','135502','136020','138773','14152','14164','142139','14290','14293','14298','144190','144675','145213','145521','14562','145715','145776','14662','14683','14694','14698','14708','147244','147314','148404','148767','149110','14920','14930','149773','149777','15055','15135','151476','151490','152143','1526','153694','154062','154499','15490','156615','157326','15747','158432','159183','160348','16147','16165','16220','1626','163039','16360','16377','165603','166646','166649','16710','16774','168455','169901','170001','170172','171041','171057','171093','173158','174013','174045','174053','174186','177166','177874','177909','178879','179401','182618','182619','182629','182671','183175','183178','183179','183185','183900','1859','186570','189016','189742','190131','193611','1952','199','2236','2237','3037','305','31114','31919','31983','3212','32453','32637','32746','32844','32890','32945','32963','32982','3302','33185','3343','33660','33728','33751','33814','33915','33976','3400','3401','3424','34383','34462','3473','34868','34885','34917','34921','35188','35480','35522','3585','3650','36522','36932','37047','37134','3773','37815','38102','38258','38300','38318','39308','39650','39820','4008','40127','40141','4040','4064','40787','41111','41509','41863','41957','42175','42424','4262','4365','43650','43860','43882','43883','44190','4501','45062','45258','45319','45375','45468','45472','46158','46207','46636','47392','48786','48787','48952','4928','49283','49338','49785','50028','50165','50167','50169','50504','50869','50918','51067','51068','51163','51574','5167','51779','51820','51974','5270','52814','52852','52889','52894','53064','53163','53424','53455','53460','53917','5420','54226','54230','54236','55841','55875','56001','56071','56124','56152','56482','57551','57674','57735','58121','58208','58362','58797','59165','59555','60066','60133','60187','60348','60570','60890','60999','61017','61518','61998','6207','62200','6253','62552','627','63785','63908','63916','63919','63921','64058','6416','64476','65198','6534','65846','6605','661','66787','66868','66941','6704','6719','6722','67368','67473','67613','6797','68392','68404','68495','68575','68633','68729','68780','68781','68920','69245','69784','70330','70642','70999','71054','71133','7135','71439','71634','72156','72560','7318','7414','7428','7474','75737','75959','78260','78913','78935','79333','80135','80360','80397','81082','81462','81895','81897','81902','81911','82061','83240','83616','83660','83664','84111','86339','86393','87866','88219','88634','88910','89108','89226','89709','90409','91029','91971','92165','92318','927','93114','93507','94198','9503','9507','95074','97153','98901','99300','99783']
    print(len(IDS))
    criteria = ['Industry Day Attendees list', 'Vendors List', 'Event', 'Contractors List',
                'Interested Parties List', 'Registration List', 'Participants Lists', 'Attendees Lists', 'Attendee',
                'Interested Companies', 'Bidders List', 'Industry Day Procurement List', 'Roster', 'Awardees List']

    for op in IDS:
        directory = op
        parent_dir = 'C:/Users/Matt Turi/Desktop/'


        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        path = path.replace('/', '\\')
        print(path)


        # DRIVER WITH SET DOWNLOAD LOCATION
        options = Options()
        # options.add_argument('--incognito')
        options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        driver_path = "C:/Users/Matt Turi/Downloads/chromedriver_win32/chromedriver.exe"
        prefs = {'download.default_directory': str(path)}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(options=options, executable_path=driver_path)

        driver.maximize_window()

        # initialize into govwin
        try:
            driver.get('https://iq.govwin.com/cas/login?service=https://iq.govwin.com/neo/myGovwin')
            time.sleep(1)

            # login
            email = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/div/input')
            email.send_keys('EMAIL')

            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/span/input[1]').click()
            time.sleep(1)

            pswd = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/div[2]/input')
            pswd.send_keys('PASSWORD')

            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/span/input[1]').click()
            time.sleep(2)

            try:
                driver.find_element_by_xpath('/html/body/div[12]/div/button').click()
            except Exception:
                print('No welcome message')

            search = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[2]/div[2]/form/div/input')
            search.send_keys(op)
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[2]/div[2]/form/a[1]').click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/div/div[5]/div[5]/div/div/h3/a').click()
                time.sleep(2)
            except:
                time.sleep(10)
                driver.close()
                break

            driver.find_element_by_xpath('/html/body/div[4]/div[4]/div/div[1]/ul/li[6]/a').click()
            time.sleep(10)

            table_count = 1
        except Exception:
            driver.close()
            continue

        while True:
            try:
                row = driver.find_element_by_xpath(
                    '/html/body/div[4]/div[4]/div/div[8]/div/div/div[3]/div/div/div[2]/div[1]/div[3]/table/tbody/tr[' + str(
                        table_count) + ']/td[2]/a')
                row_text = str(row.text)
                row_text = row_text.split(' ')
                print(row_text)
                table_count += 1
                for row_piece in row_text:
                    if any(row_piece in c for c in criteria):
                        row.click()
                        print('found something')
                        time.sleep(5)
                        break
            except Exception:
                print('out of opp resources links')
                break
        driver.close()
        time.sleep(5)


bot()
# schedule.every().day.at("16:00").do(bot, 'It is 4:00PM')
#
# while True:
#     schedule.run_pending()
#     print('Not time yet...')
#     time.sleep(60) # wait one minute
