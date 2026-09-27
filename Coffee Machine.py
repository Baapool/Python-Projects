# This ascii art belongs to https://emojicombos.com/coffee-ascii-art.
logo = """
⢰⠢⡑⣎⡱⢣⡑⡎⢥⣃⠳⣌⠳⣘⡜⢢⡝⢢⢣⡙⠦⣙⢆⡳⢌⢣⣃⠳⣌⢱⢊⡼⡑⢎⡜⣡⢎⡱⢊⡕⢪⠜⣢⠙⡦⡙⡜⢢⢇⠣⢎⡱⢊⡜⣌⠞⡰⢩⠲⣡⢓⡬⢓⢬⡑⢣⢎⡱⣌⠳⣌⠳⣌⠥⣋⠴⣉⠦⡙⡴⣉⠶⡑⣎⢱⡊⣕⢪⡑⢎⠥⡓⡜⢬⢒⣍⠲⣉⠖⣡⢋⡬⣑⠎⡜⢆⢣⡓⣌⢣⠚⣌⢣⡙⢆⡣⢳⡘⡜
⢢⢣⡙⢤⡃⢧⡘⡍⠦⢥⡓⢬⠓⢦⠸⡡⢎⠥⢣⢩⡑⢇⠎⡴⢩⡒⣌⠳⣈⠦⣍⠲⡩⢌⡲⢅⡚⢴⠩⡜⣡⠞⡰⢩⠒⡥⢛⠴⣊⡍⢎⠱⡩⠜⡤⢓⡍⢖⡙⠆⠣⢜⡊⢦⡉⢇⡎⠖⣌⠳⢌⡲⡡⢎⡱⢊⡴⡙⠴⡱⢌⡖⡩⢆⢣⠜⡤⢣⢍⠮⣘⠥⣩⠒⡥⢊⠵⡘⢎⡡⢃⡖⣉⢎⡹⢌⠣⡜⡌⣎⡱⢊⠵⣈⠧⣑⠣⣜⠸
⡘⢦⡙⢦⡙⢢⠓⡜⢣⠎⣜⢡⡋⡖⢭⡑⢎⡱⣉⢦⡙⡌⡞⡌⢧⡘⠴⣉⠖⡱⣌⢣⡙⢆⠳⢬⡘⢆⡛⡔⢣⢣⠹⡡⢏⣨⡥⠗⣒⠺⣌⠣⡕⢭⠲⡑⠊⠈⢀⣀⣀⣀⠀⠁⠚⡥⣊⡝⢢⠝⣪⠱⡜⢬⢪⢱⢢⡹⣌⠱⡎⡴⢣⡙⣌⠳⣌⠣⢎⡜⡜⡸⡰⡙⢴⠋⡖⡙⢦⡙⢥⠚⡔⢪⢔⣊⠳⡑⢎⡴⣉⠮⣑⢎⡱⣡⢋⡖⢭
⢜⢢⡙⠦⣩⢣⡙⢬⢃⡞⢔⡣⠜⡜⢆⡙⢦⡱⢊⢦⠱⡑⢎⡜⢦⡙⢎⡱⣊⠵⢌⠦⡙⢎⡱⢦⠹⣌⠲⣩⢃⠏⡕⣱⣯⠋⡴⣉⢎⡳⢌⢳⣘⢣⠳⠁⢠⣾⣿⢿⣿⣻⣿⣶⡀⠀⠧⡜⢣⢎⡥⠣⢝⣊⣒⠣⡓⠴⣊⠵⢣⡜⢥⠓⣬⠓⣬⠙⡆⠞⡴⢃⢳⣉⠖⣩⢒⡙⡢⢍⢆⡛⡌⢇⡎⡔⢣⡙⢆⡲⢜⢢⠕⡪⠴⣡⠳⡘⢦
⡘⢦⢩⢒⠥⢆⡙⢆⠧⣘⠦⡱⡙⡜⢪⢜⡡⢎⡱⢪⠱⡙⢖⡸⢆⡱⢎⠖⣉⢎⢎⠖⡙⢦⡙⢆⡳⢌⡕⣢⢏⠞⢸⣯⡏⡰⢣⠜⠊⠘⠎⡵⢊⡼⠁⠀⣿⠋⢁⢀⠈⠹⣞⣿⣿⡄⠈⣜⠣⢎⡜⡱⢋⢭⡙⢷⡌⢳⢩⡜⢣⠎⢧⠹⣄⡛⣤⠛⣜⡹⢰⢋⡖⣌⠚⡥⢢⠱⣑⠎⢦⡑⡺⡐⢮⡘⣥⠙⡜⣰⢃⢎⡹⢔⠫⡔⢣⡝⡲
⡘⢆⠧⢎⢣⠞⡸⣌⠲⡅⣎⢱⡑⣊⢇⡎⢴⠣⡜⣡⠫⢜⠪⡔⢣⡱⢪⡜⠴⢪⠜⣪⠙⣦⢉⠶⣡⠳⣜⡡⢎⡝⠘⣷⣷⠈⡇⠰⣍⠖⡄⠈⡳⣌⣓⡀⠻⠀⢭⡚⡴⠀⢸⢿⡼⣧⠀⢨⠝⣎⠤⡃⢚⡆⡣⣼⡇⡙⢦⡍⢧⡚⡥⢏⢦⡱⣊⡝⣢⡱⣋⠶⡱⢌⢣⡜⢣⢓⠬⡱⢆⡱⢥⡙⣢⠱⣌⠣⡝⢤⢋⠴⡘⣌⠳⣌⢣⠎⡵
⢸⠡⠞⣡⢎⡱⠱⣌⢣⡑⢎⠦⡙⡴⢊⡜⢆⢏⡲⢡⢋⡜⢥⡙⢦⠱⢣⠜⣙⠦⣋⠴⣉⠦⣩⠖⣡⢏⡴⡙⣎⠼⡀⠙⢾⡷⣍⠔⢮⡹⢜⡀⢱⡒⣜⢢⠦⣄⢧⡙⣖⠀⢸⣽⣟⡇⠀⡸⣘⢦⢫⡜⠣⣪⣴⠟⡠⡝⣢⡙⢦⢣⢝⣊⠖⡱⢥⡚⢥⠳⣌⢣⡙⣬⠣⢎⡓⣌⠧⣑⠎⣔⠣⡜⡰⢍⢆⡣⢝⠢⡍⢎⡱⢌⠳⡌⠶⡩⢖
⢌⠧⣙⠔⣊⢜⡱⣌⢲⡉⠖⡥⢓⣌⠣⢜⣊⠦⡱⢩⠆⣝⢢⡹⣌⠳⡍⡞⡜⢮⡱⢚⣌⠳⢥⣚⡱⢎⡴⡙⣆⢯⠱⣄⠈⠻⣟⣮⢢⡙⢮⠀⢮⡱⢌⣓⠮⡜⢦⡹⠀⢀⣾⣟⣾⠃⢀⡕⡎⡖⡱⣠⠾⡋⢴⡸⢡⢓⠦⡙⢎⡚⢦⠥⢫⡕⢎⡝⢪⡕⠮⢥⡛⢤⣋⠶⡩⢆⡳⢌⡓⣌⠳⢬⡱⢊⢖⡱⢊⠵⣘⠣⡜⣌⠧⡙⢖⡩⢎
⡘⡲⣑⠎⣕⠪⡴⣘⢆⡹⠸⡐⠧⣌⡙⡆⢎⠖⣍⠶⡙⢆⢧⠱⢎⡱⡹⢴⡙⢦⡱⣋⠴⣋⠶⣡⠝⠎⠒⠙⢦⢋⡕⢦⣃⠀⢹⣽⡆⡹⡌⢌⡲⢍⡞⢴⢫⠜⠃⢁⣰⣿⣻⣽⠏⠀⡔⢮⡱⣙⠖⡇⠮⡜⣣⠕⣫⢍⡞⡹⢬⡙⢮⡑⣇⠞⡱⢪⡕⢮⡑⣎⠼⣡⠎⡼⡑⢮⠜⡣⡜⡤⢋⠖⣘⠎⢦⡑⣋⠖⣡⢣⠱⡌⢖⡩⢎⡕⣎
⣘⠱⣌⠚⣤⢓⠲⣌⠲⡱⣩⣑⢣⢆⡕⢪⡱⣚⠴⢣⠝⣎⢮⡙⢦⡱⣓⢮⠱⢎⡴⢣⠳⣌⠳⠁⣠⠲⡔⡤⡀⠈⠸⢥⡚⡄⢀⣿⡅⢣⢜⠣⡝⢪⡜⠃⠁⣠⣴⡿⣟⣷⣿⠉⢀⡜⢬⢣⠓⠎⠳⣤⢳⠱⣎⡹⣒⠎⡖⢭⠲⡍⠶⣑⠮⡙⢮⡱⢎⢧⠱⢎⡓⢦⠹⢴⡙⢦⡙⢆⡳⢌⡣⣙⠦⡙⢦⡑⢎⡬⢱⢊⡵⣉⠦⢳⡘⢲⢌
⢌⠳⢌⠳⣄⢋⠶⣌⡱⡱⢢⡜⢦⢊⡜⢥⡒⣍⢎⡳⢚⠴⢣⡹⢆⡳⢎⢮⡙⣎⠖⣣⠳⣜⠃⠐⢦⠛⠨⣕⢣⠀⠈⡳⡜⠁⣸⣯⠱⣉⢎⡳⡜⠁⢀⣴⣿⡿⣽⣟⣯⡷⠁⠠⠒⢈⣀⣀⣤⣀⣀⡀⠈⠳⣬⢱⠃⠨⣝⢪⡝⣜⢣⢣⠏⣝⠲⡙⣎⢎⡝⢦⡹⢌⢏⡲⢩⢆⡹⢎⢖⡩⢖⡑⢎⡱⢢⡙⠴⣈⢇⠣⢆⠵⣊⠧⣘⠣⢎
⢌⡓⣎⡱⢜⣌⠲⣄⢣⡱⡱⣘⠦⡩⡜⢦⡙⣬⢚⡜⡭⣚⡱⢍⠶⣙⢎⠶⣑⠮⣙⠴⣋⡼⢩⢆⡀⣁⠼⣨⢓⠀⢠⠳⠁⣰⣿⠂⢞⡱⢪⠅⠀⣴⡿⣯⡿⢟⣹⣾⠉⠀⣀⣴⣾⣿⡻⠟⢾⣟⣯⡿⣷⡀⠀⢧⢣⠈⢒⢧⡚⣬⠣⢇⡻⢔⡫⣕⠎⡞⡜⢦⡙⣎⠮⡱⣋⠮⡱⢎⡚⣌⠳⣌⢇⢎⡱⢌⠳⣈⢎⡱⢊⠞⡤⣓⢬⡙⣬
⡜⡔⢢⠕⡪⢔⠣⢎⠆⣇⠱⡥⢎⠵⣉⢖⡹⢔⢣⠞⡴⢃⡳⡜⢮⡱⣊⠷⣡⠹⣌⢳⡱⢎⡓⢮⡱⢍⢶⡡⠏⠀⣨⠃⣰⡿⢂⡝⣢⢝⡃⠀⣼⣻⢿⡟⢁⣾⡿⠀⣠⣾⣿⠟⠉⢁⡀⣀⣀⠀⠑⢿⣽⣧⠀⢨⡓⣆⠀⢮⠱⣜⢣⢏⡜⣣⠕⡮⣜⡱⣙⠦⡝⡬⢳⢥⡙⢲⡱⢪⡕⡪⢕⢎⡜⣪⠑⣎⢑⢣⡊⠼⣉⢖⡱⣌⢲⣉⠖
⡘⣌⢇⠞⣡⢋⠼⣨⠓⣌⡓⡜⡰⣍⡚⡬⢜⠮⡑⢮⠱⣋⠶⣙⢦⢳⢡⠏⡶⣙⢬⣃⢗⣣⠹⢦⡙⣎⠶⡱⢃⠀⠧⠀⣿⠇⡜⡜⡆⢯⠄⠀⣟⡿⡟⠀⣾⣿⠁⣼⣿⠛⠁⡠⢜⠦⣣⠳⣌⠳⠀⢸⣷⡟⠀⡰⡚⡼⡀⠰⣋⠼⣘⠶⣘⢥⡚⡵⣂⠷⡱⢎⡵⡙⢦⠳⣜⢣⡚⡵⣌⠵⣩⢎⠼⣰⢩⠆⡭⢢⢍⠳⡌⢦⠱⣌⠖⣌⠞
⡑⢎⢬⢊⡕⢪⠜⣤⠋⡴⣘⠴⣃⠖⣱⡙⣎⠺⣑⢎⡣⢇⠻⣌⢎⢦⢫⢜⡱⢎⠶⣉⢦⢣⡝⣱⡚⣬⠓⣍⠳⡄⠘⡄⢿⣳⡘⣌⠳⡭⡄⠀⢫⣿⣇⠀⣿⣶⠰⣯⡏⠀⡜⣜⢣⡛⠀⣶⡈⢁⣠⣿⡷⠁⢠⡱⢹⡔⢁⢲⣉⢞⡱⢪⢍⡖⢭⠲⣍⡚⣥⢫⡔⡻⢬⠳⣌⠧⡹⣔⢪⡱⢣⢎⢳⡘⢦⡙⡰⢃⣎⠳⡌⢇⡳⢌⡚⣤⢛
⠱⢎⡜⡜⡱⢊⠴⡩⡒⣅⠫⢆⡝⡲⣍⠳⣙⢦⡹⢜⣣⢚⢦⡙⡞⣜⠪⣜⢣⢞⡰⢋⡜⢮⡱⢋⡵⣩⠶⣙⢦⠓⡤⢁⠜⢿⣧⠙⣦⠣⢧⠀⠘⣿⣟⡀⢻⣿⣶⢿⠁⢰⡱⣙⢎⡳⠀⠻⢷⣾⠿⠏⠁⡠⣌⠳⢎⡡⡜⣬⢛⠬⣓⠮⡜⡱⢎⠶⡩⢧⡙⣎⠵⢣⡜⡢⠝⣔⢣⡝⣊⠗⢮⡘⡎⡵⢊⡕⢣⢎⡙⢦⠱⡜⡡⢎⠳⣉⠞
⢩⠖⡸⢬⢱⢩⢒⠵⡱⢌⡹⡌⢖⡱⣌⠳⡍⢦⠓⡭⠲⣍⠶⣩⠜⣲⠹⣌⠧⣎⠱⣋⡼⣒⢭⠳⡜⡥⢞⡱⢪⠝⣜⢣⠞⣤⠙⢷⡔⣋⢎⢧⡀⠈⢿⣷⡈⢷⣻⣿⡀⠐⢧⡙⢮⡑⢧⠤⣀⡀⣠⢄⡞⣰⢃⡻⣜⠲⣙⢆⡏⡞⣌⠖⣭⢣⢏⡼⢱⡪⣕⠪⣍⠳⡜⣥⢛⡬⢲⢱⢪⡙⢦⡹⡘⡴⢃⠮⣑⢎⡱⢊⠶⡱⢱⢪⠱⢎⡚
⠸⡌⣕⢊⠦⣍⢲⡘⠴⣉⠖⣍⠞⡴⢊⡵⢪⡱⢫⡜⣳⠘⣎⢥⠫⣕⠫⣜⡚⣤⢳⠱⣚⡜⡪⢧⠹⣌⡳⢜⡣⢛⡴⢋⡞⡴⣋⡆⢻⡌⠞⢦⢓⡄⠀⠙⣿⣎⣿⡽⣇⠀⢸⡙⡦⡝⣎⠮⢱⡙⢦⢫⡜⢥⣋⠶⣉⠎⡵⢪⡜⡱⢎⡝⢦⡓⢮⠜⣥⠳⣌⠳⣍⡣⣝⢢⢇⡞⣡⢣⠳⣜⢣⢲⡱⣡⢋⡜⢥⢊⠶⣩⠲⣡⠳⢬⡙⢦⡙
⢱⡉⢦⠩⡖⡌⢦⡙⢲⣉⠞⡴⡙⢴⡋⡴⢣⡍⢧⡜⢦⠛⡜⢦⢛⣌⠳⡜⡜⣤⣋⢧⡓⡼⡱⣃⢟⣰⠹⢎⡵⣋⠶⣍⠞⠴⠃⠞⠉⣷⠘⠃⠋⠘⠓⠀⠈⠻⣾⣻⣟⡆⠀⠙⠒⢡⡶⠡⠧⠙⢎⠧⡜⢧⢎⡳⢍⠾⡱⢣⡍⢧⢫⡜⣣⠹⣌⠳⣌⠣⣜⠳⡬⡱⢎⡕⢮⡸⣅⢧⠳⡌⢧⠣⡵⢡⠎⣜⢢⡙⠦⣅⠣⡥⡓⢦⡙⢦⡙
⣡⠚⡥⢳⡘⢥⠣⢍⡣⢌⡳⠜⣍⠦⣓⡱⢣⢚⢦⠹⣌⢳⡙⢦⠣⡜⣣⠝⡜⢦⡱⢦⡙⢶⡱⡍⡞⠌⠛⠈⠀⠁⠀⠀⣀⣀⣀⣀⣠⣿⣤⣤⣤⣤⣤⣤⣄⠀⠹⣧⢿⣧⠀⢠⣤⣼⣥⣀⣀⣀⣀⠀⠀⠁⠈⠁⠋⠚⠵⡫⡜⢦⠳⣜⣡⢛⣬⢋⠶⡹⣌⠧⣱⡑⢯⣘⢣⢳⡘⡬⢣⠝⣪⠱⣍⠧⡙⣔⠪⢜⡱⢌⠳⣰⠙⢦⡙⢦⡙
⢤⢋⠖⣡⠞⡰⢋⡜⡔⢫⢔⡫⡜⢎⡴⣩⢇⠫⣆⢛⡬⠲⣍⠶⣙⠼⣡⢛⡜⣣⠝⣦⠹⠂⠁⠀⢀⣀⣤⣤⣶⣾⠿⠿⢛⠛⡛⢍⡉⢿⡍⢉⠍⣉⠖⡰⣈⠄⠀⢻⣿⡍⠀⢨⢉⡙⣏⠉⣉⠛⠛⡛⠿⠷⣶⣦⣤⣀⡀⠀⠈⠁⠛⠦⣙⢎⠦⣍⠶⣱⢊⢮⡱⣙⢦⡙⢦⠳⣜⡱⣍⠮⣑⢣⢎⢣⠝⣌⢣⠣⡜⢪⡑⢦⡙⢦⡙⠴⣩
⢢⢋⡜⢢⡙⡬⢃⠖⣩⠎⣲⢱⡙⠮⠴⣑⢎⡳⢌⡳⢜⡳⢜⡚⡴⢫⡔⣫⠜⡥⠋⠀⠀⣠⣴⣾⡿⠟⠙⡉⠥⣐⠢⡑⢎⡰⢉⠆⡔⢢⠙⠒⠌⠤⠣⠑⠤⠉⠀⢸⣟⠃⠀⢦⠘⢤⢂⠵⣁⢎⡱⢌⡒⡜⢠⢌⠩⢋⠻⢿⣶⣤⡀⠀⠉⢮⠹⣌⡳⣌⢫⡲⡱⣍⢦⡹⣉⠗⣬⠲⣜⡲⣩⠎⣎⢎⡚⣤⢣⢓⡌⢧⠙⢦⡙⣤⢙⡚⡴
⢌⡣⢚⢥⡱⢌⠧⡙⢤⠫⣔⢣⡙⣎⢧⡙⣜⠢⣏⡜⢣⢎⠧⣙⢖⡣⢞⢥⠫⠀⠀⣰⣾⡿⠉⢀⡠⠜⡱⣈⠕⠢⠱⠉⠂⠑⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⠀⠀⠀⠀⠀⠀⠁⠐⠁⠂⠱⠈⢖⡨⢃⠎⡔⣀⠉⠺⣿⣦⡀⠀⠱⣊⡵⣌⠳⣌⠳⣌⠶⣡⠏⡞⣔⢫⡔⠣⢧⡙⢦⢣⡙⢤⢃⢎⡜⢢⠝⣢⡑⢦⣉⠖⣱
⢸⡐⣋⠦⣑⢎⡱⡙⢆⠻⡔⣣⢝⣢⢣⡝⣌⠳⢴⣩⠓⣎⠵⣩⢚⡜⣎⢞⠀⠀⢸⣿⢿⠀⠀⣎⠔⠋⠀⠁⠀⠀⠀⠀⠀⠀⡀⢀⠀⡄⠠⠀⠄⠠⠀⢀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠄⢀⠀⡀⠀⠀⠀⠀⠀⠈⠈⠘⠔⠣⡄⠀⢹⣷⡇⠀⠀⣱⢒⢭⠳⣌⠳⣎⠵⢣⡛⡼⣌⠳⣌⢳⠪⣕⣋⢦⡙⢆⢏⠲⣘⠣⢎⠥⡜⢦⣘⢣⢣
⢢⢃⢇⡚⣱⢊⠴⡙⢬⠓⣍⡒⢮⢔⡣⡜⣬⢛⡴⢢⠟⡜⢮⡱⢫⡜⡜⢮⠀⠀⠈⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠠⢀⠐⡈⠐⠀⠁⠀⠀⠀⠄⠀⠐⠀⠔⠊⠁⠀⢀⠀⠂⠈⠁⢂⠐⠠⠀⢀⠀⠂⠄⠀⠂⠀⡀⠀⠀⠀⠈⠀⣠⣿⡿⠀⠀⠀⢶⡩⠖⠋⠜⠓⠊⠓⠣⠝⢦⣍⠳⣌⢧⡓⡜⡴⢣⠜⡣⢎⠳⡌⠳⡜⢪⡜⢆⡜⡆⢧
⠸⡌⢦⡑⢆⡋⠶⣉⢆⠻⠴⡙⡖⢮⢱⡙⣤⢫⠲⣍⠾⣸⠱⣎⠳⣜⡹⢲⠀⠀⢀⠀⠙⠿⣷⣄⡀⠀⠀⠐⠀⠠⠀⠡⠂⠤⠐⢀⠁⢡⠂⢄⢈⠀⡀⡀⡀⠐⣀⠀⡀⠂⡁⠄⠂⠌⠁⠀⠀⠠⠀⠉⠀⠀⠀⠀⠀⠀⠀⣤⣾⡿⠋⠀⡀⠀⠀⠂⠀⠀⣀⣠⣤⣤⣄⣀⠀⠀⠈⠳⣜⢢⠳⡍⢶⠩⢎⡕⢪⡑⢮⠱⡜⡡⢎⢲⡸⡘⡥
⠱⢎⠥⡙⢦⡙⠼⡰⣊⠵⣋⠼⣩⢎⢧⡙⢦⣍⠳⣌⠳⣆⢟⡰⢯⡜⣜⣣⠀⠀⠐⠮⣄⢤⣈⡙⠿⢷⣶⣤⣀⡀⠀⠀⠀⠀⠁⠀⠈⠀⠈⠂⠈⠐⠐⠀⠐⠁⠂⠈⠀⠁⠀⠀⠀⠀⠂⠀⠁⠀⠀⠀⠀⣀⣠⣤⣶⡆⠀⠈⣅⣀⢤⢓⡄⠀⠀⣠⢸⣿⡿⠿⠿⠽⢯⣿⢿⣶⣄⠀⠈⢪⠵⣙⢎⢳⢣⡜⡱⡘⣆⠳⣌⢱⡩⢆⡱⡱⢣
⡙⡌⣎⡱⢣⠜⣣⠱⡜⢆⢣⠛⡴⣊⠶⣩⠲⣌⠳⣜⢣⡚⣌⢗⡪⣜⢢⡳⠀⠀⢸⠱⢬⢸⢿⣿⣷⣷⣻⣯⣟⣿⣿⣷⣶⣦⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣴⣶⣶⣿⢿⢿⣿⣽⣯⣿⢀⠀⢸⣻⡆⡍⠆⠀⠀⠥⣜⠡⠔⠒⠀⠚⠰⢂⠝⢿⣿⣧⠀⠀⢣⢝⡪⡜⣲⠘⡥⢓⣌⠣⡜⢢⡑⢎⢲⡑⢧
⢸⠰⢆⠵⣉⠞⡤⢓⡍⢮⣡⢛⡴⣉⢖⡣⡝⠼⣉⠞⣦⠹⡜⢦⠳⡜⣣⢝⠀⠀⠠⢏⡲⢸⣯⣟⣾⣽⣻⣾⣽⢿⣾⣽⣞⡿⣟⣿⣯⣿⢻⣟⣿⢿⡿⣟⡿⣿⣻⣿⣟⡿⣿⣻⡷⣿⣻⣽⢾⣻⣷⡿⠟⠉⠀⠀⠈⣯⡇⡄⠀⣿⡇⡸⡁⠀⠀⡓⠀⢀⣠⢐⡲⢤⠄⠀⠘⡄⢳⣿⣇⠀⠈⣆⠧⡙⣆⢫⢒⠣⢌⡣⢍⡣⢎⡍⡖⡩⢖
⢌⡓⢮⡘⠼⡘⣌⠣⡜⢢⠥⣓⢬⢓⡎⡵⣩⠳⣍⠾⡰⣋⠞⣭⢓⡝⢦⣋⠆⠀⢈⡳⢜⣼⢷⣿⣾⡷⠛⠉⠀⠀⠀⠀⠉⠛⢿⠉⣷⣿⢿⣽⢯⢿⣟⣿⣽⣿⣻⣞⣿⣻⣯⠁⠀⠀⠀⠉⣿⣯⡟⠁⣠⣶⡆⠀⢀⣏⣯⠀⠀⢽⡇⣡⠃⠀⠀⠀⢀⡳⢆⠯⣜⢣⢏⠆⠀⢘⡂⣿⣿⠀⠀⡜⠼⣱⢊⡇⢎⡹⡘⡔⡣⡜⢆⠞⡬⡱⢩
⡘⡜⢢⡙⢲⡉⢦⡹⡘⣎⠵⡩⠖⡭⡚⣥⢣⠳⡜⢎⡵⡩⢞⡔⣊⢞⡱⢎⡆⠀⠨⢖⡩⢼⣿⣿⠊⠀⠀⠀⣠⣶⣿⣿⣶⠄⠀⠀⢻⡯⠟⠉⠀⡀⠀⠀⠉⠑⠻⢿⣽⣳⣿⣤⣨⣿⠇⠀⡯⠋⣠⣾⡟⠋⠀⣠⣿⣯⣿⠐⠀⢸⢡⢖⡁⠀⠀⣀⠫⡜⣭⢚⡬⣓⢎⡳⠀⢀⠆⣟⣿⠀⠀⣍⢳⣡⢚⢬⢃⡖⢥⡙⠴⣉⠮⡜⣡⠓⡭
⢸⢡⡓⣌⠧⣘⠥⣒⠭⣘⢖⡩⣝⣡⢛⡤⢣⢛⡬⢳⠸⣥⢋⡼⣘⢮⡱⢏⠄⠀⠘⢦⣙⢸⣿⠀⠀⠀⢀⣾⣻⢷⡿⠚⢹⣿⠀⠀⣾⣏⠀⠰⢎⠻⣿⡿⣶⣦⣤⣀⡀⠉⠉⠉⠉⣁⣠⣾⣴⣿⣉⠁⠀⠀⠀⣿⢯⣿⣻⠠⠀⠘⢘⠮⡀⠀⠠⡝⢮⡱⢎⡳⣜⡱⢎⠅⠀⡰⢰⣿⡏⠀⠠⡜⢦⡱⢎⡆⢫⡰⣡⢎⢣⡑⢎⡴⢡⢛⠴
⡘⠦⡱⢌⡚⡔⢣⡜⢲⡉⢮⡔⡎⢦⢣⢚⡥⢣⡚⣥⢛⡴⢋⠶⣩⢖⡹⢎⡇⠀⢘⠦⡜⢸⠇⠀⠀⠀⣾⡽⣽⡯⠀⢰⣿⡛⠀⢠⣽⣿⢶⣤⣴⣾⢷⣿⣽⣷⠟⢿⣟⡏⠙⠙⠉⢁⣾⣯⣷⢿⡟⠀⠀⠀⠀⢹⣿⣯⡿⠇⠂⠀⠀⠑⠀⠀⢏⡜⣣⠝⣮⠱⣎⠵⠋⠀⠠⢄⣿⡯⠁⠀⠴⣙⢦⡱⢪⢜⢣⠒⡥⢎⢆⡹⢢⠜⣡⢋⡜
⢌⡇⢇⢣⠕⡪⠕⡬⢣⠜⣣⠜⣩⠖⡭⣚⠬⢇⡹⣔⢫⡔⣏⢞⡱⢎⡳⣍⠖⠀⠈⡜⢼⠸⠀⠀⠀⢰⣿⣟⣿⣗⡀⠀⠁⠀⣠⣾⠛⠚⠛⠋⢁⣿⣄⠀⠀⠀⣰⣟⣿⣯⠀⡀⠀⠈⣷⣯⣿⣿⠃⠀⣧⠀⠀⠈⣿⠞⠁⠀⠀⢀⠄⢄⠀⠀⢩⢜⡣⡝⢦⣛⢬⠋⠀⣀⢣⣾⣿⠁⠀⣈⢞⡱⢪⡕⡫⠜⣆⠛⡴⣉⠦⡱⢅⡚⢥⡚⡜
⠲⡌⢭⢂⢏⡱⡙⠴⡑⢮⣡⡛⡴⡋⠶⣱⢊⣍⠶⣌⢳⡸⡜⡎⡖⣭⢓⡬⢇⠀⠀⡜⣣⠃⠀⠀⠀⣴⡿⣾⣟⣾⣿⣶⣶⣾⣯⣿⣇⠀⠀⠀⣿⣿⣿⠀⠀⠀⢿⣻⣽⡃⢀⡃⠀⠀⢿⣷⣻⡽⠀⢸⣿⠀⠀⠀⢻⡄⠀⠠⡁⢌⡈⢢⢁⠀⠀⣎⢧⡙⠮⠜⠀⢀⠰⣠⣿⠷⠁⠀⢰⣉⠮⣑⢧⠚⣥⢋⡔⢫⠔⣡⠎⣕⠪⡜⡢⠕⡭
⠱⣌⠣⢎⡜⠴⣉⠞⡡⠧⣆⠳⣥⡙⡳⣌⠳⣌⠳⣌⢧⠳⢥⡙⡼⢢⠏⡼⢭⠀⠀⠸⣐⠇⠀⠀⠀⣯⣿⢷⣯⣷⣿⡳⠛⠙⠻⣷⡿⠀⠀⢸⣯⣷⣿⠀⠀⢠⣾⡿⣿⠀⣸⣷⠀⠀⢸⣷⡿⠇⠀⠚⠉⠁⠀⠀⢸⣄⠀⠐⠨⢄⠒⡠⢈⠂⠀⠸⠂⠉⠀⡠⠐⣨⣾⡿⠋⠀⢀⢎⡳⢌⢧⡙⢎⡕⣢⠓⡬⢣⡙⢆⡛⢤⢋⡴⣉⠳⡜
⢃⢎⡱⣊⡜⡱⡘⢎⠕⡳⢌⠗⣦⢙⡵⣊⠷⣡⢛⡬⢲⡙⢮⡱⣩⢇⡛⡜⢧⡂⠀⠐⢭⠂⠀⠀⠀⣿⣯⢿⣻⣾⠍⠀⣠⣴⠀⢘⣇⠀⠀⠸⠟⠋⠀⠀⠀⢸⠟⠁⡀⢀⠀⠙⠀⠀⠘⣯⣟⠀⢠⣴⣾⣷⠀⠀⠀⣧⠀⠀⡁⢂⠰⡐⡈⠄⠀⢀⠄⠔⣪⣴⣿⠿⠋⠀⠀⡔⣎⢧⡙⢎⡖⣩⢚⡬⢅⡋⠶⣡⠙⢦⢩⢒⢣⠒⣥⢋⡜
⢊⢆⠳⡌⠖⡥⣙⢪⡩⡑⡏⡜⢦⡹⣔⢣⡝⢦⢳⡘⢧⣹⢲⡱⣃⢮⠵⣙⢮⡱⡀⠀⢣⢃⠀⠀⠀⢹⣞⣿⣻⡕⠀⠀⣿⣗⣶⣿⡏⠀⠀⢀⣤⣴⡞⠀⠀⢸⣄⢸⠀⣸⣿⣶⡄⠀⠀⣿⡇⠀⢸⣟⣾⡿⡆⠀⠀⢡⠃⠀⠀⠆⢊⠄⠁⠁⠀⠀⣾⣿⠿⠛⠁⠀⡠⡰⡝⣜⠲⣎⡙⣎⠜⣥⢋⡴⢋⡜⡱⢂⢏⠆⣇⠍⡆⡏⠴⢣⡜
⡸⢌⡳⡘⡵⢢⣑⠣⡴⢩⢜⣩⠲⡱⣌⡳⣘⢧⢪⡕⣣⠖⣣⠞⣜⢪⠳⣍⢖⣣⠅⠀⠐⡭⠀⠀⠀⠘⣿⡽⣿⣝⡀⠀⠘⠿⠟⠉⡀⠀⠀⢸⣻⣿⣿⠀⠀⢸⣿⡏⠀⣿⣻⣽⡇⠀⠀⠸⠁⠀⠘⢽⣾⣟⠇⠀⠀⠈⢓⠀⠀⠈⠀⠀⢀⡀⠤⠐⠋⠀⢀⣀⢤⢳⡱⢣⡝⣬⠓⡦⢳⢌⡓⣆⢫⡔⢫⢌⡓⡍⣎⠼⣈⠞⡱⢌⢇⡳⣘
⡰⢋⠴⣱⢡⠣⣌⠳⣈⠧⢪⡔⢫⡕⡎⢶⡩⢖⡣⡜⢦⢛⡴⡹⣌⢳⡹⡜⠮⠜⠙⠀⠀⠸⡡⠀⠀⠀⢹⡿⣻⣟⣷⣦⣤⣤⢰⣾⡇⠀⠀⢸⣿⣾⠇⠀⠀⠸⠟⠀⠀⢹⣿⣿⣠⣤⣴⢶⠶⠿⠿⣿⣟⣿⡷⣶⣄⡀⣈⠠⣄⠀⠀⢨⠎⠈⠀⣀⠴⣘⠶⣘⡎⢧⣍⠳⡜⢢⡛⢴⠣⡎⣕⠪⢖⡩⢎⠖⡱⠜⡤⢓⡜⡬⡑⢎⠮⡔⢣
⢸⠡⢏⡔⢣⡓⣌⢣⡑⢮⠱⣌⢳⠸⡜⣣⢜⡣⢵⡙⣎⠳⣜⠱⠉⠁⠀⠀⣀⣀⣤⣤⡀⠀⠱⣃⠀⠀⠀⠹⣿⡿⣞⣿⣻⠏⢀⣿⠇⠀⠀⠘⢻⣝⣁⣠⣤⣴⣶⣾⣿⡿⠛⠚⠉⠁⣀⣀⣠⣄⣀⠀⠈⠙⣽⡷⣿⡿⢏⡰⠂⠀⠰⠉⠀⣀⣀⡀⠀⠉⠘⠑⠎⡳⣌⠳⣍⢧⡹⣌⠳⣜⢢⡛⣬⠚⡜⣌⢣⡙⣔⢋⡴⢡⡙⢬⠲⣉⢎
⢢⠛⢦⡙⠦⡑⡎⢥⠓⣌⠳⣌⢣⢫⠜⣥⠺⡜⢣⠞⠈⠉⠀⣀⣤⣴⣾⣿⡿⠿⣛⢛⡳⡀⠀⠩⡓⡤⡀⠀⠈⠙⠛⠛⠉⢀⣼⣃⣠⡤⢶⣶⡿⣟⣯⣿⢿⣽⠿⠉⠁⠀⣠⣴⣾⢿⣻⡿⠻⣿⣿⣷⠀⠀⢸⣿⣳⢋⡴⠁⠀⢀⡀⣠⢚⡛⠿⢿⣟⣶⣦⣤⣀⠀⠈⠑⠎⠶⣱⢌⡳⡌⢧⠹⡰⡩⠖⣌⠣⡜⢢⢍⡒⣣⠙⣌⢳⡘⡬
⢬⡙⢦⡙⣜⠱⡜⣢⠹⣄⢛⡌⠮⣅⢻⡰⢫⠜⠁⢀⣠⣶⣟⡿⠛⣋⠬⣐⠦⡱⣃⠞⣔⢣⢄⠀⠁⠳⣜⡑⢦⣤⣤⣴⡾⣟⣿⡟⠋⠁⣀⢉⣿⣟⣿⠿⠋⠁⠀⣀⣴⣿⣽⣻⣯⣯⠁⠀⣴⣾⣷⠟⠀⢀⣾⡟⢡⡚⠀⠀⢤⠓⡼⢤⠫⣜⡱⢆⡰⡩⢝⠺⢿⣟⣶⣄⡀⠈⠑⡮⣱⢊⢧⢋⠵⡱⢍⢆⠳⣌⠣⢎⠴⣡⢋⢆⠳⡜⡱
⡰⢩⢆⡱⢌⠞⡰⣡⢚⠤⣋⠼⡑⢮⡱⠎⠁⢀⣴⣿⣻⠝⣋⢰⠹⡤⢋⡖⡱⡱⢡⢫⢜⢪⡜⡤⠀⠈⠒⡍⡖⡙⢿⣽⣻⣿⢯⣇⠀⠀⠑⠛⠛⠉⠀⠀⣀⣴⣾⣟⣿⣳⢿⣳⣿⣳⣄⠀⠈⠉⠀⣀⣴⠿⢋⡰⠃⠀⢀⡺⢌⢫⡒⢭⢚⡴⠱⢎⡱⠹⣌⡓⢦⢙⢻⣽⣿⢦⠀⠀⢣⡝⣢⢏⡲⣉⢮⠸⡱⢌⡱⣉⠖⣡⠎⣎⢓⡬⡱
⢸⢡⠚⣔⠫⡜⡑⢦⡩⢖⡩⣒⡝⢢⠇⠀⠀⣾⣿⣾⢋⡜⢤⣋⠳⡜⢣⡜⣱⠱⣍⠖⡪⠵⣘⠖⣩⢆⡀⠈⠒⢙⠦⣌⠛⢯⣿⣟⣷⣤⣤⣤⣤⣴⣾⡿⣿⡷⣟⣿⢾⣟⣿⢯⣷⣟⣿⢿⣟⣿⡿⠛⣡⠚⠂⠀⢠⢸⡘⢦⡋⢶⡙⣬⠓⡜⢭⡒⣍⠳⢤⡙⢆⠏⡴⢹⡾⣿⣧⠀⠀⢎⡔⢮⠰⣉⠦⢣⡑⢣⡜⢢⡋⡴⣉⠦⢣⡒⠵
⡜⡘⢦⢙⢢⠱⡓⣌⢣⠜⡥⢋⡕⠮⡔⠀⠀⣿⣯⣿⡨⢕⡪⠝⡦⡱⢪⡱⢋⢦⡙⡴⢃⠶⡩⠖⣍⠪⣁⠀⠀⠈⠐⠍⢶⢨⡙⠻⠟⣿⣟⡿⣿⣻⣯⣷⢯⣷⣿⣻⡾⣿⡽⣾⣽⣿⡽⠾⢛⡋⣡⠦⠉⠀⠀⢠⢌⢊⠳⢌⡳⢌⠧⣍⢖⡱⢪⠱⣍⠖⡬⠳⣜⠲⡥⢸⡷⣯⣿⠀⠀⢬⡑⢎⢆⡛⡔⢪⢕⡊⢕⢎⡱⢣⡙⡔⢪⡑⢦
⢬⡑⢮⡘⠦⢣⠵⡌⣆⠫⠴⡩⡜⢥⠳⡀⠀⠹⣷⡿⣧⡨⢑⠏⡖⣭⠣⡕⣫⠆⣝⡰⢋⠶⣉⠲⡀⠇⣌⠊⠀⢐⣀⡀⠀⠁⠙⠪⠕⣢⠔⡭⣍⡛⡻⣙⢛⣛⢚⡳⢛⡛⡭⢭⡑⢦⡔⠣⠃⠉⠀⢀⠠⡀⠀⢡⢊⠤⢃⢆⠡⣋⠶⡌⠶⣩⠖⡭⢆⡛⣜⡱⢪⠱⣡⣟⣿⡟⠃⠀⢐⢣⠞⡱⢊⡵⢈⢇⡎⡜⣌⠦⣑⠦⡱⣉⡓⡜⢦
⢢⡙⢦⡙⡬⢣⡜⢔⡪⢍⡲⢱⠚⡌⢧⡑⢆⠀⠈⠻⣿⣿⣦⡌⠑⠢⣛⢬⡱⢚⡤⢳⢩⠖⢠⠃⡜⡘⢄⠂⠀⠐⠦⢓⡆⢆⡄⣀⡀⠀⠀⠁⠈⠁⠑⠉⠒⠉⠒⠙⠃⠉⠈⠀⠀⠀⢀⡀⣠⠰⣌⠶⠉⠀⠀⠰⣈⢒⠌⡌⠆⡱⣊⢭⢓⡥⡚⢥⣋⠶⠬⢁⣡⣾⣿⠻⠛⠀⠀⡄⡏⡼⢨⣑⠣⣜⢩⠲⡜⡰⢌⡲⢌⠲⣑⠦⡙⡜⢦
⢢⡙⢦⡑⢎⡱⢌⡲⡑⡎⢥⢣⠹⣘⠦⡹⡌⠒⡀⠀⠀⠙⠺⢿⣿⣶⣤⣀⡉⠓⠜⢱⢎⡚⣥⢘⡰⠑⣊⡉⢆⠄⡀⠀⠉⠚⠴⢢⠓⣍⢎⡔⢢⡒⡤⢤⡠⡄⢤⠠⣔⢢⡒⣤⢫⡜⡱⠚⠴⠋⠀⠀⠀⡄⠜⡡⢂⢇⢊⡠⢎⡵⡑⢮⠜⠲⠙⢀⣁⣤⣶⣿⡿⠛⠉⠀⠀⢀⠣⡙⡴⢡⢓⡌⡣⢆⢇⡚⢬⡑⢎⠱⢊⡳⠌⡖⣱⡉⠶
⠦⡙⢆⡙⢦⣉⠦⡱⡑⢎⢆⢇⠳⡌⠶⠁⠠⢒⠠⠁⠆⡀⠀⠀⠀⠉⠛⠿⢿⣷⣶⣤⣄⣈⡀⠉⠒⠓⠢⠜⠐⢊⡔⢡⠄⡠⢀⠀⠀⠈⠀⠈⠁⠉⠐⠃⠓⠚⠁⠛⠀⠃⠉⠀⠁⠀⠀⢀⢀⡀⢢⢌⡱⢨⠜⠔⠣⠊⠃⠙⠈⢀⣁⣠⣤⣶⣾⡿⠟⠛⠉⠀⠀⠀⡀⢄⠘⡀⠆⡈⢒⠣⢎⠴⣡⢋⠦⣙⢆⡹⣌⠳⣉⠖⡍⡖⣡⠞⣩
⠴⣉⠞⣌⠧⣘⢬⠱⣉⠎⡜⠪⡕⢬⢓⠈⣁⠂⡌⠡⠌⣀⠣⠐⢠⠀⡀⠀⠀⠀⠉⠙⠛⠻⠿⣿⣿⣖⣶⣤⣤⣤⣀⣀⣀⣀⠁⠈⠀⠁⠁⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠈⠈⠀⠁⠈⣁⣀⣀⣀⣤⣤⣤⣶⣶⣿⡿⠿⠟⠛⠋⠉⠀⠀⠀⠀⡀⢄⠰⢁⠐⡠⢊⠐⡐⠄⢨⡙⢬⡒⢥⡚⠴⣉⢦⠱⢌⠳⡘⢬⡱⢜⡡⢞⡡
⡘⢦⡙⣤⢋⠴⣊⠵⣘⡚⣌⠳⡘⢦⣉⢖⣀⠢⠐⡁⢢⠐⡀⠣⢐⢈⡐⢁⠢⡀⢄⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠻⠿⠿⠿⢿⣿⣿⢿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⣿⡿⢿⣿⡿⠿⠿⠛⠛⠛⠛⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⡀⠄⢂⠤⠑⡐⢂⡐⢂⠡⠐⠂⠔⢐⡰⢣⠜⣡⠚⣤⡙⣆⢣⣌⠓⣎⠱⣉⠖⡱⣊⠼⡡⢝
⢸⢡⡚⠤⣍⠲⣡⠓⡤⢓⡌⢧⡙⢦⡘⢦⢡⠓⡤⡁⠂⠌⡐⢁⠂⣂⠰⠠⠁⠔⡀⠎⠠⡀⠀⠀⠀⠁⠐⠐⢠⠀⠤⢀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⠠⢄⠠⡐⠤⠐⠀⠀⠀⠀⡀⠤⠑⡠⢊⠐⢂⠡⢂⠡⠐⠂⡌⠁⣊⡔⡣⡜⣢⠹⣄⠯⡰⢱⡌⡲⢌⡚⢤⢋⢦⡙⢦⡑⢎⡕⢮
⡘⢦⡙⢦⡉⣖⢡⢋⠴⡉⢆⡳⢌⠦⣙⠬⢆⡝⢤⢃⠗⡢⢌⡐⠂⠄⢂⡑⢈⠢⢐⠨⢁⠰⢁⠢⢐⠀⡀⠀⠀⠀⠁⠈⠂⠑⠊⠜⠢⠱⠌⢦⠱⡰⢘⡒⡔⢲⡐⠆⣆⠣⡜⡘⡤⠣⠜⠰⠣⠘⠑⠈⠁⠈⠀⠀⠀⢀⠀⡄⠤⢁⠢⢀⢃⠐⠤⠉⢂⠒⠤⢘⡨⢅⢲⠩⣔⢣⡱⢱⢂⡳⢌⡲⢍⠲⣌⠱⣊⠵⢊⠎⢦⠱⢢⠝⡬⡘⢦
⡘⢦⢩⢒⡱⢌⠦⣉⠖⣍⠚⡴⣉⠶⣨⠓⣬⢘⠆⡏⡜⣡⠇⣎⡙⡒⢦⠄⣆⣁⠢⠌⠐⠢⠌⡐⢨⠐⢠⠃⠢⢐⠠⠐⡀⢀⠄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⡠⠐⡀⠆⠡⠌⡐⠠⢂⠌⡐⡁⠢⢌⣂⠥⣒⡌⣣⢃⢇⢎⠲⣍⠢⢇⡼⡑⡎⠴⢣⡜⢎⠣⣌⢣⡑⢎⠳⡌⢇⡝⢪⡜⡱⣉⠶
⠸⣌⠦⢍⡜⡜⡢⣍⡚⢬⡙⠴⣡⢒⠥⣋⠴⣉⠞⣸⠘⣤⠫⡔⣩⠜⡌⡞⡰⡘⢬⡙⣱⠒⠦⠥⢤⢌⡐⣀⡑⠂⠡⠘⠄⡡⠈⡔⠡⣀⠃⡰⢀⠢⢐⠂⡰⠀⠆⠢⠐⠄⢢⠐⠄⣁⠃⠌⢡⠈⠌⢂⠅⠢⠡⢘⣐⢂⡡⠥⢤⢖⠲⣉⠳⣌⠦⣋⠴⡱⢢⢍⠮⡜⡱⣌⠓⣎⠔⡱⣊⠵⢣⠜⣌⡓⡜⢢⠝⣌⠳⣌⠣⡜⣃⠲⡱⢌⡞
⠱⣌⡚⠴⣘⠴⡑⢦⣉⠶⣨⠳⣄⡋⠶⣁⠳⣌⠚⣤⢋⠴⢣⡜⡡⢎⡱⢬⠱⣉⠦⡙⣤⠫⡕⢫⡌⢆⠳⡌⠭⣍⠵⡩⢖⡱⢒⠴⠲⢤⢢⢅⠦⢤⠡⡴⠤⡍⢤⡡⠥⡬⠤⣌⠴⡠⡜⡔⢣⢒⡣⢎⡼⣉⠧⡓⣌⢣⠕⣋⡒⢮⠱⣃⠳⣌⠲⣑⢎⠱⡅⢎⢲⢡⠓⣌⠳⣌⠺⡑⢬⠚⡴⢩⠦⡱⢜⢣⠹⣈⢳⡈⢧⠱⣌⢣⠱⡣⡜
⢱⢢⡙⢬⡑⢎⡱⢎⡔⢣⢆⠳⢤⡙⢦⠱⡣⢌⡳⢢⠍⣎⡱⢢⡙⢢⠕⣣⠳⣈⡕⢣⢆⠳⣌⠧⡘⢎⡱⢌⠳⣈⢖⡩⢖⣡⢋⡜⡱⢊⠶⣈⠞⡰⢋⠴⡩⢜⠦⣡⢣⢕⡣⢜⡪⢕⡜⣌⢣⠣⡜⢥⠒⡥⢎⡱⢌⠎⡼⢱⡘⢆⠳⣌⠳⣐⠳⡌⢆⠳⣌⠳⣌⠦⣋⡔⢣⡌⢳⡘⣣⠙⡔⡣⢎⡱⣊⠦⡛⡌⢦⡙⢦⡙⢤⣃⢏⡴⢩
⡘⠦⡙⠦⣙⢌⡲⢡⡚⢥⠪⡱⢆⡙⢆⢏⠴⢣⡜⣡⢚⠤⡃⣗⠸⡡⢞⡰⡩⢆⣙⠢⢎⠳⡨⢖⡙⢆⡝⣌⠳⣁⠎⡴⢃⢆⡫⢔⡡⠫⡔⡥⣋⠵⣉⢖⡩⢎⠲⢥⠚⣤⢓⠪⡔⢣⡜⢤⢋⡞⣘⢆⡛⠴⣡⠚⣬⠩⢖⠣⡜⢥⠳⣌⢣⢍⡖⡩⢎⡱⡊⡕⣢⠓⢦⡘⢣⠜⡥⡚⢤⠛⡔⢣⢣⡑⢎⡱⢱⡸⡡⢎⡕⣊⠧⣘⠲⣌⠳
⡘⡱⣉⠞⡤⢣⡕⢣⡜⢣⡹⡔⢣⡹⢌⢎⡼⢡⢚⠴⣉⢎⠵⣨⠣⡕⣎⠱⡱⢊⣌⢣⡍⢎⡕⢎⡼⢡⢚⢤⣋⠴⣩⢒⡍⢦⢱⢊⠵⣉⠶⡱⡘⠦⣍⠦⣃⢇⣋⠶⣉⢦⢩⠞⣌⠧⣸⠘⡦⢜⡔⣪⠜⡱⢆⠯⡰⣉⠮⣱⠩⢖⠣⡜⡌⠶⣘⢥⢣⠜⣱⡑⢦⡙⢦⢍⠣⡎⡕⣩⠖⡭⣘⠥⣃⢎⢣⡜⢥⢒⡕⢣⠜⡢⢇⡍⠳⣌⠳
"""




MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def check_resources():
    match coffee_type:
        case "Espresso":
            # Not enough water
            if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                e1 = "Sorry, out of water for your espresso. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(e1)
                print("=" * 150)
                return "Not enough resources"


            # Not enough coffee
            elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                e2 = "Sorry, out of coffee for your espresso. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(e2)
                print("=" * 150)
                return "Not enough resources"


            else:
                return "Enough resources"

        case "Latte":
            # Not enough water
            if resources["water"] < MENU["latte"]["ingredients"]["water"]:
                l1 = "Sorry, out of water for your latte. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(l1)
                print("=" * 150)
                return "Not enough resources"


            # Not enough milk
            elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                l2 = "Sorry, out of milk for your latte. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(l2)
                print("=" * 150)
                return "Not enough resources"


            # Not enough coffee
            elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
                l3 = "Sorry, out of coffee for your latte. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(l3)
                print("=" * 150)
                return "Not enough resources"


            else:
                return "Enough resources"

        case "Cappuccino":
            # Not enough water
            if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                c1 = "Sorry, out of water for your cappuccino. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(c1)
                print("=" * 150)
                return "Not enough resources"


            # Not enough milk
            elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                c2 = "Sorry, out of coffee for your cappuccino. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(c2)
                print("=" * 150)
                return "Not enough resources"


            # Not enough coffee
            elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                c3 = "Sorry, out of coffee for your cappuccino. Try again later."
                print("=" * 150)
                print("Out of resources")
                print("-" * 150)
                print(c3)
                print("=" * 150)
                return "Not enough resources"


            else:
                return "Enough resources"




while True:
    print(logo)
    menu = "1. Espresso: $1.5\n2. Latte: $2.5\n3. Cappuccino: $3"
    print("=" * 150)
    print("Menu")
    print("-" * 150)
    print(menu)
    print("=" * 150)
    user_input = str(input("What would you like? Type: ")).lower().strip()
    match user_input:
        case "espresso":
            coffee_type = "Espresso"
            if check_resources() == "Not enough resources":
                break
            else:
                print("Insert Coins")
                input_quarters = int(input("How many quarters? "))
                input_dimes = int(input("How many dimes? "))
                input_nickels = int(input("How many nickels? "))
                input_pennies = int(input("How many pennies? "))

                # Check if ANY of the inputs are negative numbers.
                if input_quarters < 0 or input_dimes < 0 or input_nickels < 0 or input_pennies < 0:
                    print("Invalid input. Please enter a number greater than 0.")

                # Calculate the total cost.
                else:
                    total_cost = ((input_quarters * 0.25) + (input_dimes * 0.10) + (input_nickels * 0.05) + (input_pennies * 0.01))
                    # Cannot afford espresso.
                    if total_cost < MENU["espresso"]["cost"]:
                        print("Not enough coins, Money refunded.")

                    else:
                        change = total_cost - MENU["espresso"]["cost"]
                        money += MENU["espresso"]["cost"]
                        print(f"Here is your ${change:.2f} in change.")
                        print("Here is your Espresso ☕️. Enjoy!")

                        drink_ingredients = MENU["espresso"]["ingredients"]
                        for ingredient in drink_ingredients:
                            resources[ingredient] -= drink_ingredients[ingredient]

        case "latte":
            coffee_type = "Latte"
            if check_resources() == "Not enough resources":
                break
            else:
                print("Insert Coins")
                input_quarters = int(input("How many quarters? "))
                input_dimes = int(input("How many dimes? "))
                input_nickels = int(input("How many nickels? "))
                input_pennies = int(input("How many pennies? "))

                # Check if ANY of the inputs are negative numbers.
                if input_quarters < 0 or input_dimes < 0 or input_nickels < 0 or input_pennies < 0:
                    print("Invalid input. Please enter a number greater than 0.")

                # Calculate the total cost.
                else:
                    total_cost = ((input_quarters * 0.25) + (input_dimes * 0.10) + (input_nickels * 0.05) + (input_pennies * 0.01))
                    # Cannot afford latte.
                    if total_cost < MENU["latte"]["cost"]:
                        print("Not enough coins, Money refunded.")
                    else:
                        change = total_cost - MENU["latte"]["cost"]
                        money += MENU["latte"]["cost"]
                        print(f"Here is your ${change:.2f} in change.")
                        print("Here is your Latte ☕️. Enjoy!")

                        drink_ingredients = MENU["latte"]["ingredients"]
                        for ingredient in drink_ingredients:
                            resources[ingredient] -= drink_ingredients[ingredient]
        case "cappuccino":
            coffee_type = "Cappuccino"
            if check_resources() == "Not enough resources":
                break
            else:
                print("Insert Coins")
                input_quarters = int(input("How many quarters? "))
                input_dimes = int(input("How many dimes? "))
                input_nickels = int(input("How many nickels? "))
                input_pennies = int(input("How many pennies? "))

                # Check if ANY of the inputs are negative numbers.
                if input_quarters < 0 or input_dimes < 0 or input_nickels < 0 or input_pennies < 0:
                    print("Invalid input. Please enter a number greater than 0.")

                # Calculate the total cost.
                else:
                    total_cost = ((input_quarters * 0.25) + (input_dimes * 0.10) + (input_nickels * 0.05) + (input_pennies * 0.01))
                    # Cannot afford cappuccino.
                    if total_cost < MENU["cappuccino"]["cost"]:
                        print("Not enough coins, Money refunded.")
                    else:
                        change = total_cost - MENU["cappuccino"]["cost"]
                        money += MENU["cappuccino"]["cost"]
                        print(f"Here is your ${change:.2f} in change.")
                        print("Here is your Cappuccino ☕️. Enjoy!")

                        drink_ingredients = MENU["cappuccino"]["ingredients"]
                        for ingredient in drink_ingredients:
                            resources[ingredient] -= drink_ingredients[ingredient]

        case "report":
            report_text = (
                f"Water: {resources['water']}ml\n"
                f"Milk: {resources['milk']}ml\n"
                f"Coffee: {resources['coffee']}g\n"
                f"Money: ${money:.2f}"
            )
            print("=" * 150)
            print("Resources")
            print("-" * 150)
            print(report_text)
            print("=" * 150)

        case "refill":
            refilled = "Machine refilled."
            print("=" * 150)
            print("Machine Refilled")
            print("-" * 150)
            print(refilled)
            print("=" * 150)
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100

        case "off":
            shut_down = "Shutting Down"
            print("=" * 150)
            print("Shutting Down")
            print("-" * 150)
            print(shut_down)
            print("=" * 150)
            break
