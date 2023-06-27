# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:49:05 2023

@author: Myriam
"""




liste_a_trier = [[[(4.9298983, 13.1594114), (4.9301449, 13.1613463), (4.9303454, 13.1608429), (4.9306766, 13.1600064), (4.9312761, 13.1605007), (4.9313852, 13.1604875), (4.9314088, 13.1607606), (4.9313909, 13.1609107), (4.9313583, 13.1611829), (4.9313037, 13.1616395), (4.9325441, 13.1619465), (4.9327502, 13.1614873), (4.9334139, 13.1616159), (4.9341783, 13.1616603), (4.9341407, 13.1618014), (4.9339503, 13.1622793), (4.9334471, 13.1622139), (4.9329958, 13.1621361), (4.9331778, 13.1629558), (4.9329958, 13.1621361), (4.9325441, 13.1619465), (4.9323247, 13.1621951), (4.9318943, 13.1631071), (4.9327058, 13.1631203), (4.9318943, 13.1631071), (4.9310366, 13.1633492), (4.9301029, 13.1636175), (4.9299827, 13.1630081), (4.9295434, 13.1630113), (4.9293963, 13.1630211), (4.9295434, 13.1630113), (4.9299591, 13.1619715), (4.9301449, 13.1613463), (4.9303454, 13.1608429), (4.9312761, 13.1605007), (4.9313852, 13.1604875), (4.9316295, 13.1605149), (4.9314088, 13.1607606), (4.9313909, 13.1609107), (4.9328694, 13.1611223), (4.9328694, 13.1609264), (4.9329383, 13.1607898), (4.9327701, 13.1607567), (4.9316295, 13.1605149), (4.9327701, 13.1607567), (4.9328694, 13.1609264), (4.9328694, 13.1611223), (4.9327502, 13.1614873), (4.9313583, 13.1611829), (4.9313037, 13.1616395), (4.9311317, 13.1621525), (4.9310104, 13.1631278), (4.9299827, 13.1630081), (4.9301029, 13.1636175), (4.9302489, 13.1643596), (4.9293999, 13.1643726), (4.9295863, 13.1636218), (4.9293999, 13.1643726), (4.9291679, 13.1644001), (4.9292021, 13.163732), (4.9293395, 13.1634926), (4.9294616, 13.1631804), (4.9293395, 13.1634926), (4.9290703, 13.1634852), (4.9292021, 13.163732), (4.9291679, 13.1644001), (4.9289461, 13.16535), (4.9289429, 13.1655558), (4.9295688, 13.1657524), (4.929465, 13.1659908), (4.9295688, 13.1657524), (4.929916, 13.1658848), (4.9299231, 13.1658625), (4.9306696, 13.1661612), (4.9299231, 13.1658625), (4.9299844, 13.1656389), (4.9299231, 13.1658625), (4.929916, 13.1658848), (4.929935, 13.1659044), (4.9296837, 13.1664319), (4.929935, 13.1659044), (4.929916, 13.1658848), (4.9295688, 13.1657524), (4.9289429, 13.1655558), (4.9287917, 13.1667009), (4.9282372, 13.166654), (4.9287917, 13.1667009), (4.9286341, 13.167331), (4.9287917, 13.1667009), (4.9289429, 13.1655558), (4.9289461, 13.16535), (4.9289471, 13.1646163), (4.9289458, 13.164519), (4.9289412, 13.1644196), (4.9279675, 13.1607012), (4.9289412, 13.1644196), (4.9291679, 13.1644001), (4.9292021, 13.163732), (4.9290703, 13.1634852), (4.9288514, 13.1633541), (4.9290703, 13.1634852)], [(4.9292021, 13.163732), (4.9291679, 13.1644001), (4.9293999, 13.1643726), (4.9302489, 13.1643596)]], [[(4.9302489, 13.1643596), (4.9315772, 13.1644959), (4.9315731, 13.1638667), (4.9319816, 13.1638702), (4.9317687, 13.1644033), (4.9319816, 13.1638702), (4.9323785, 13.1636714), (4.9322256, 13.1643922), (4.9323785, 13.1636714), (4.9328023, 13.1633501), (4.9323785, 13.1636714)], [(4.9319816, 13.1638702), (4.9315731, 13.1638667), (4.9315772, 13.1644959), (4.9325585, 13.1647984), (4.9326917, 13.1648126), (4.9329971, 13.1645086), (4.9332422, 13.1641587)]], [[(4.9332422, 13.1641587), (4.9332368, 13.1640109), (4.9332422, 13.1641587), (4.9333002, 13.1649483), (4.9327323, 13.1648207), (4.932867, 13.1652769), (4.9327323, 13.1648207), (4.9333002, 13.1649483), (4.9343698, 13.1652095), (4.9344976, 13.1645908), (4.9338825, 13.1645283), (4.9344976, 13.1645908)], [(4.9343698, 13.1652095), (4.9342319, 13.1656458), (4.93402, 13.1662596), (4.9336378, 13.1662844)]], [[(4.9336378, 13.1662844), (4.9336821, 13.1661264), (4.9336378, 13.1662844), (4.9335818, 13.1664088), (4.9332523, 13.1662641), (4.9335818, 13.1664088), (4.9334165, 13.1668002), (4.9330907, 13.1677665), (4.9334165, 13.1668002), (4.9328211, 13.1666621), (4.9328329, 13.1661597), (4.9324952, 13.1665652), (4.9311435, 13.1662968), (4.9310852, 13.1662862), (4.930784, 13.1665299), (4.9310852, 13.1662862), (4.9311435, 13.1662968), (4.9308014, 13.1676595), (4.9311435, 13.1662968), (4.9324952, 13.1665652), (4.9327916, 13.1666553), (4.9326964, 13.1671188)], [(4.9327916, 13.1666553), (4.9324952, 13.1665652), (4.9328329, 13.1661597), (4.932851, 13.1661369), (4.9329245, 13.1661226), (4.9325585, 13.1647984), (4.9315772, 13.1644959), (4.9302489, 13.1643596)]], [[(4.9302489, 13.1643596), (4.9315772, 13.1644959), (4.9315731, 13.1638667), (4.9319816, 13.1638702), (4.9317687, 13.1644033), (4.9319816, 13.1638702), (4.9323785, 13.1636714), (4.9322256, 13.1643922), (4.9323785, 13.1636714), (4.9328023, 13.1633501), (4.9323785, 13.1636714)], [(4.9319816, 13.1638702), (4.9315731, 13.1638667), (4.9312224, 13.1636276), (4.9310366, 13.1633492), (4.9310104, 13.1631278), (4.9311317, 13.1621525), (4.9299591, 13.1619715), (4.9301449, 13.1613463), (4.9298983, 13.1594114)]], [[(4.9298983, 13.1594114), (4.9301449, 13.1613463), (4.9303454, 13.1608429), (4.9306766, 13.1600064), (4.9312761, 13.1605007), (4.9313852, 13.1604875), (4.9314088, 13.1607606), (4.9313909, 13.1609107), (4.9313583, 13.1611829), (4.9313037, 13.1616395), (4.9325441, 13.1619465), (4.9327502, 13.1614873), (4.9334139, 13.1616159), (4.9341783, 13.1616603), (4.9341407, 13.1618014), (4.9339503, 13.1622793), (4.9334471, 13.1622139), (4.9329958, 13.1621361), (4.9331778, 13.1629558), (4.9329958, 13.1621361), (4.9325441, 13.1619465), (4.9323247, 13.1621951), (4.9318943, 13.1631071), (4.9327058, 13.1631203), (4.9318943, 13.1631071), (4.9310366, 13.1633492), (4.9301029, 13.1636175), (4.9299827, 13.1630081), (4.9295434, 13.1630113), (4.9293963, 13.1630211), (4.9295434, 13.1630113), (4.9299591, 13.1619715), (4.9301449, 13.1613463), (4.9303454, 13.1608429), (4.9312761, 13.1605007), (4.9313852, 13.1604875), (4.9316295, 13.1605149), (4.9314088, 13.1607606), (4.9313909, 13.1609107), (4.9328694, 13.1611223), (4.9328694, 13.1609264), (4.9329383, 13.1607898), (4.9327701, 13.1607567), (4.9316295, 13.1605149), (4.9327701, 13.1607567), (4.9328694, 13.1609264), (4.9328694, 13.1611223), (4.9327502, 13.1614873), (4.9313583, 13.1611829), (4.9313037, 13.1616395), (4.9311317, 13.1621525), (4.9310104, 13.1631278), (4.9299827, 13.1630081), (4.9301029, 13.1636175), (4.9302489, 13.1643596), (4.9293999, 13.1643726), (4.9295863, 13.1636218), (4.9293999, 13.1643726), (4.9291679, 13.1644001), (4.9292021, 13.163732), (4.9293395, 13.1634926), (4.9294616, 13.1631804), (4.9293395, 13.1634926), (4.9290703, 13.1634852), (4.9292021, 13.163732), (4.9291679, 13.1644001), (4.9289461, 13.16535), (4.9289429, 13.1655558), (4.9295688, 13.1657524), (4.929465, 13.1659908), (4.9295688, 13.1657524), (4.929916, 13.1658848), (4.9299231, 13.1658625), (4.9306696, 13.1661612), (4.9299231, 13.1658625), (4.9299844, 13.1656389), (4.9299231, 13.1658625), (4.929916, 13.1658848), (4.929935, 13.1659044), (4.9296837, 13.1664319), (4.929935, 13.1659044), (4.929916, 13.1658848), (4.9295688, 13.1657524), (4.9289429, 13.1655558), (4.9287917, 13.1667009), (4.9282372, 13.166654), (4.9287917, 13.1667009), (4.9286341, 13.167331), (4.9287917, 13.1667009), (4.9289429, 13.1655558), (4.9289461, 13.16535), (4.9289471, 13.1646163), (4.9289458, 13.164519), (4.9289412, 13.1644196), (4.9279675, 13.1607012), (4.9289412, 13.1644196), (4.9291679, 13.1644001), (4.9292021, 13.163732), (4.9290703, 13.1634852), (4.9288514, 13.1633541), (4.9290703, 13.1634852)], [(4.9292021, 13.163732), (4.9291679, 13.1644001), (4.9289412, 13.1644196), (4.9289458, 13.164519), (4.9282128, 13.1646329), (4.9276257, 13.1645058), (4.9262063, 13.1638986), (4.9250012, 13.1642443)]], [[(4.9250012, 13.1642443), (4.9262063, 13.1638986), (4.9256047, 13.1636746), (4.9262063, 13.1638986), (4.9276257, 13.1645058), (4.9275724, 13.1646684), (4.927454, 13.1650295), (4.9277973, 13.1649955), (4.9275724, 13.1646684), (4.9276257, 13.1645058), (4.9282128, 13.1646329), (4.9282149, 13.1648501), (4.9281827, 13.1650164), (4.9279872, 13.1650844), (4.9281827, 13.1650164), (4.9284598, 13.1648427), (4.9283542, 13.1648094), (4.9284947, 13.1647683), (4.9284598, 13.1648427), (4.9288487, 13.1651091), (4.9284598, 13.1648427), (4.9283542, 13.1648094), (4.9282149, 13.1648501), (4.9277973, 13.1649955), (4.927454, 13.1650295), (4.9274441, 13.1650585), (4.9279801, 13.1652529), (4.9274652, 13.1656228), (4.9272131, 13.1657524), (4.9274441, 13.1650585), (4.927454, 13.1650295), (4.9267177, 13.1651658), (4.9262185, 13.1650227), (4.9260514, 13.1649916), (4.9262185, 13.1650227), (4.9262068, 13.1652828), (4.9267177, 13.1651658), (4.9262185, 13.1650227), (4.9261227, 13.1647253), (4.9262185, 13.1650227), (4.9262068, 13.1652828), (4.925504, 13.1655858), (4.9262068, 13.1652828)], [(4.9267177, 13.1651658), (4.927454, 13.1650295), (4.9274441, 13.1650585), (4.9272131, 13.1657524)]], [[(4.9272131, 13.1657524), (4.9262245, 13.1668464), (4.9272131, 13.1657524), (4.9274652, 13.1656228), (4.9277862, 13.1657109), (4.9282459, 13.1659339), (4.9281036, 13.1665422), (4.9282459, 13.1659339), (4.9279653, 13.1661028), (4.9282459, 13.1659339), (4.9277862, 13.1657109), (4.9281358, 13.1652404), (4.9280154, 13.1652276), (4.9279801, 13.1652529), (4.9280154, 13.1652276), (4.9280834, 13.1651787), (4.9281531, 13.1651072), (4.9281358, 13.1652404), (4.9281903, 13.1652462), (4.9281358, 13.1652404), (4.9281531, 13.1651072), (4.9281827, 13.1650164), (4.9282149, 13.1648501), (4.9282128, 13.1646329), (4.9289458, 13.164519), (4.9289471, 13.1646163), (4.9284947, 13.1647683)], [(4.9289471, 13.1646163), (4.9289461, 13.16535), (4.9291679, 13.1644001), (4.9293999, 13.1643726), (4.9302489, 13.1643596), (4.9315772, 13.1644959), (4.9325585, 13.1647984), (4.9326917, 13.1648126), (4.9327323, 13.1648207), (4.9333002, 13.1649483), (4.9343698, 13.1652095), (4.9342319, 13.1656458), (4.93402, 13.1662596), (4.9336378, 13.1662844)]], [(4.9336378, 13.1662844), (4.9336821, 13.1661264), (4.9336378, 13.1662844), (4.9335818, 13.1664088), (4.9332523, 13.1662641), (4.9335818, 13.1664088), (4.9334165, 13.1668002), (4.9330907, 13.1677665), (4.9334165, 13.1668002), (4.9328211, 13.1666621), (4.9328329, 13.1661597), (4.9324952, 13.1665652), (4.9311435, 13.1662968), (4.9310852, 13.1662862), (4.930784, 13.1665299), (4.9310852, 13.1662862), (4.9311435, 13.1662968), (4.9308014, 13.1676595), (4.9311435, 13.1662968), (4.9324952, 13.1665652), (4.9327916, 13.1666553), (4.9326964, 13.1671188)]]



def extraction_tuple(liste_a_trier):
    u = []
    for element in liste_a_trier:
        
        if len(element) ==2 :
            for liste in element:
                for tuples in liste:
                    u.append(tuples)
        else:
            for tuples in element:
                u.append(tuples)
    print(u)
    return u

A = extraction_tuple(liste_a_trier)
