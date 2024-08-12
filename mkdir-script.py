import os

# 定义书籍信息
bookshelf = {
    '折木奉太郎的书架': [
        '【01】《破狱》吉村昭',
        '【02】《山田风太郎明治小说全集（十一）拉斯普京来了》山田风太郎（筑摩文库）',
        '【03】《产灵山秘录》半村良（角川文库）',
        '【04】《五瓣之椿》山田周五郎（新潮文库）',
        '【05】《八甲田山死之彷徨》新田次郎（新潮文库）',
        '【06】《夏季的灾难》篠田节子（角川文库）',
        '【07】《无赖船》西村寿行（角川文库）',
        '【08】《七胴落》神林长平（早川文库）',
        '【09】现代社会科学丛书《逃避自由》埃里希·弗洛姆（东京创元社）',
        '【10】《天藤真推理小说全集九——大诱拐》天藤真（创元推理文库）',
        '【11】《风云将棋谷》角田喜久雄（春阳文库）',
        '【12】《国语入试问题必胜法》清水义范（讲谈社文库）',
        '【13】《高堡》德蒙·巴格莱（早川文库）',
        '【14】《堕落论》坂口安吾（角川文库）',
        '【15】《秘太刀马骨》藤泽周平（文春文库）',
        '【16】《名叫星期四的男人》G.K.切斯特顿（创元推理文库）',
        '【17】新译版《华氏451度》雷·布拉德伯里（早川文库）',
        '【18】《世界就是这样结束的》内维尔·舒特（创元SF文库）',
        '【19】《西线无战事》雷马克（新潮文库）',
        '【20】《人鱼变生》山田章博（幻冬舍）',
        '【21】《奇想的精神：少年科学俱乐部》鹤田谦二（KC Deluxe Morning）',
        '【22】《别逗了，费曼先生》理查德·费曼（岩波现代文库）',
        '【23】《岂有此理的家伙》杉浦日向子（筑摩文库）',
        '【24】《佛师》下村富美（小池书院）',
        '【25】《夜航》安托万·德·圣-埃克苏佩里（新潮文库）',
        '【26】《无门关漫步》西村惠信/译注（岩波文库）',
        '【27】《皇家战舰“尤利西斯”号》阿利斯泰尔·麦克林（早川文库）',
        '【28】《口袋名言集》寺山修司（角川文库）',
        '【29】《荻原朔太郎诗集》荻原朔太郎（岩波文库）',
        '【30】《交通事故》二木雄策（岩波新书）'
    ],
    '千反田爱瑠的书架': [
        '【01】《对译 狄金森诗集——美国诗人选集（三）》艾米莉·狄金森（岩波文库）',
        '【02】《草叶集》沃尔特·惠特曼（美篶书房）',
        '【03】《海潮声》上田敏（新潮文库）',
        '【04】《春天与阿修罗》宫泽贤治（日本图书中心）',
        '【05】《天使雕像》柯尼斯伯格（岩波少年文库）',
        '【06】《当天使坠落人间》大卫·阿尔蒙德（创元推理文库）',
        '【07】新版《姆米谷的冬天》朵贝·杨笙（讲谈社文库）',
        '【08】《火焰和铁杉》黛安娜·温尼·琼斯（创元推理文库）',
        '【09】《飞翔的教室》埃里希·凯斯特纳（岩波少年文库）',
        '【10】《毛毛》米切尔·恩德（岩波少年文库）',
        '【11】《最后的独角兽》彼得·S·毕格（早川文库）',
        '【12】《弗兰肯斯坦》玛丽·雪莱（新潮文库）',
        '【13】《不存在的骑士》伊塔洛·卡尔维诺（白水社）',
        '【14】《进入盛夏之门》罗伯特·海因莱因（早川文库）',
        '【15】《幸福假面》阿加莎·克里斯蒂（早川文库）',
        '【16】《绿野仙踪》莱曼·弗兰克·鲍姆（岩波少年文库）',
        '【17】《小川未明童话集——红蜡烛和美人鱼》小川未明（新潮文库）',
        '【18】《西方魔女之死》梨木香步（新潮文库）',
        '【19】《清兵卫与葫芦》志贺直哉（新潮文库）',
        '【20】《春昼·春昼后刻》泉镜花（岩波文库）',
        '【21】《兔之眼》灰谷健次郎（角川文库）',
        '【22】《一千零一秒物语》稻垣足穗（新潮文库）',
        '【23】新版《远野物语》附《远野物语拾遗》柳田国男（角川索菲亚文库）',
        '【24】《十二支考》南方熊楠（岩波文库）',
        '【25】《致歌者的书简》正冈子规（岩波文库）',
        '【26】《智识的生产技术》梅棹忠夫（岩波新书）',
        '【27】《柿子的种子》寺田寅彦（岩波文库）',
        '【28】《社会认知的历程》内田义彦（岩波新书）',
        '【29】《论阅读与书籍》亚瑟·叔本华（岩波文库）',
        '【30】现代社会科学丛书《逃避自由》埃里希·弗洛姆（东京创元社）'
    ],
    '福部里志的书架': [
        '【01】《贝克街的福尔摩斯》威廉·S.巴林-古尔德（河出文库）',
        '【02】《Opa！》开高健、高桥曻（集英社文库）',
        '【03】《脑中魅影》V.S.拉马钱德兰、S.布莱克斯利（角川文库）',
        '【04】《奇想的系谱》辻惟雄（筑摩学艺文库）',
        '【05】《无限论教室》野矢茂树（讲谈社现代新书）',
        '【06】新版《杂兵们的战场》（朝日选书）',
        '【07】《你了解希腊神话吗》阿刀田高（新潮文库）',
        '【08】《茶的世界史》角山荣（中公新书）',
        '【09】《疑嫌画像：FBI心理分析官对异常杀人者调查手记》罗伯特·K.雷斯勒、汤姆·夏希特曼（早川文库）',
        '【10】《再来一记慢曲球》山际淳司（角川文库）',
        '【11】《回到正统》G.K.切斯特顿（春秋社）',
        '【12】《孩子的人生学》永井均（讲谈社现代新书）',
        '【13】新版《麦克斯韦妖——从概率走向物理学》都筑卓司（Blue Backs）',
        '【14】《中核vs革马》立花隆（讲谈社文库）',
        '【15】《听尸体怎么说》上野正彦（文春文库）',
        '【16】《日本残酷物语》下川耿史（新潮文库）',
        '【17】《废园》吉村昭（文春文库）',
        '【18】《故事·人间喜剧》中野京子（新潮文库）',
        '【19】《江户的构造》喜多村鸠男（讲谈社学术文库）',
        '【20】《最后的事物的爱》保罗·奥斯特（新潮文库）',
        '【21】《再生障碍者》北村薰（文春文库）',
        '【22】《远野物语拾遗》柳田国男（角川文库）',
        '【23】《新释 古事记传》本居宣长（岩波文库）',
        '【24】《十八史略》三崎良章（岩波新书）',
        '【25】《近代的预谋者》鹤见俊辅（筑摩文库）',
        '【26】《古寺巡礼京都》和辻哲郎（岩波文库）',
        '【27】《日本的思想》丸山真男（岩波新书）',
        '【28】《夜与雾》维克多·弗兰克尔（新版/新潮文库）',
        '【29】《旧约圣经·出埃及记》岩波书店',
        '【30】《单恋》东野圭吾（文艺春秋）'
    ],
    '伊原摩耶花的漫画书架': [
        '【01】《有闲俱乐部》一条由香莉（集英社文库漫画版）',
        '【02】《第十一人（新编版）》萩尾望都（小学馆文库）',
        '【03】《不成问题的餐厅》尾崎衣良（讲谈社文库）',
        '【04】《龙虎门》黄玉郎（中文书局）',
        '【05】《北斗神拳》武论尊、原哲夫（集英社文库漫画版）',
        '【06】《龙珠》鸟山明（集英社文库漫画版）',
        '【07】《死亡笔记》大场鸫、小畑健（集英社文库漫画版）',
        '【08】《铁臂阿童木》手冢治虫（小学馆文库）',
        '【09】《凡尔赛玫瑰》池田理代子（集英社文库漫画版）',
        '【10】《宇宙战舰大和号》松本零士（小学馆文库）',
        '【11】《鬼灭之刃》吾峠呼世晴（集英社文库）',
        '【12】《闪电十一人》LEVEL-5（日刊少年漫画文库）',
        '【13】《名侦探柯南》青山刚昌（小学馆文库）',
        '【14】《游戏王》高桥和希（集英社文库）',
        '【15】《进击的巨人》谏山创（讲谈社文库）',
        '【16】《JOJO的奇妙冒险》荒木飞吕彦（集英社文库）',
        '【17】《灌篮高手》井上雄彦（集英社文库）',
        '【18】《犬夜叉》高桥留美子（小学馆文库）',
        '【19】《棋魂》小畑健、堀田由美（集英社文库）',
        '【20】《东京食尸鬼》石田翠（集英社文库）',
        '【21】《风之谷》宫崎骏（德间书店）',
        '【22】《福星小子》高桥留美子（小学馆文库）',
        '【23】《钢之炼金术师》荒川弘（Square Enix）',
        '【24】《全职猎人》富坚义博（集英社文库）',
        '【25】《浪客剑心》和月伸宏（集英社文库）',
        '【26】《火影忍者》岸本齐史（集英社文库）',
        '【27】《死亡代理人》小林泰三（朝日文库）',
        '【28】《寄生兽》岩明均（讲谈社文库）',
        '【29】《网球王子》许斐刚（集英社文库）',
        '【30】《足球小将》高桥阳一（集英社文库）'
    ]
}

# 创建文件夹结构
def create_bookshelf_folders():
    base_path = os.getcwd()  # 使用当前目录为基准路径

    for person, books in bookshelf.items():
        person_path = os.path.join(base_path, person)

        # 创建一级目录（人名的书架）
        os.makedirs(person_path, exist_ok=True)

        for book in books:
            book_path = os.path.join(person_path, book)

            # 创建二级目录（书籍）
            os.makedirs(book_path, exist_ok=True)

if __name__ == "__main__":
    create_bookshelf_folders()
    print("文件夹创建完毕。")