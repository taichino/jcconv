# -*- coding: utf-8 -*-

# define character sets used in japanese
class jcconv:
  (HIRA, KATA, HALF, WNUM, HNUM, WALP, HALP) = (i for i in range(7))
  hira = [u'が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ',
          u'あ い う え お か き く け こ さ し す せ そ た ち つ て と ' + \
          u'な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ ' + \
          u'わ を ん ぁ ぃ ぅ ぇ ぉ ゃ ゅ ょ っ']
  kata = [u'ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド バ ビ ブ ベ ボ パ ピ プ ペ ポ',
          u'ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ' + \
          u'ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ' + \
          u'ワ ヲ ン ァ ィ ゥ ェ ォ ャ ュ ョ ッ']
  half = [u'ｶﾞ ｷﾞ ｸﾞ ｹﾞ ｺﾞ ｻﾞ ｼﾞ ｽﾞ ｾﾞ ｿﾞ ﾀﾞ ﾁﾞ ﾂﾞ ﾃﾞ ﾄﾞ ﾊﾞ ﾋﾞ ﾌﾞ ﾍﾞ ﾎﾞ ﾊﾟ ﾋﾟ ﾌﾟ ﾍﾟ ﾎﾟ',
          u'ｱ ｲ ｳ ｴ ｵ ｶ ｷ ｸ ｹ ｺ ｻ ｼ ｽ ｾ ｿ ﾀ ﾁ ﾂ ﾃ ﾄ ﾅ ﾆ ﾇ ﾈ ﾉ ﾊ ﾋ ﾌ ﾍ ﾎ ﾏ ﾐ ﾑ ﾒ ﾓ ﾔ ﾕ ﾖ ﾗ ﾘ ﾙ ﾚ ﾛ ' + \
          u'ﾜ ｦ ﾝ ｧ ｨ ｩ ｪ ｫ ｬ ｭ ｮ ｯ']
  wnum = [u'０ １ ２ ３ ４ ５ ６ ７ ８ ９']
  hnum = [u'0 1 2 3 4 5 6 7 8 9']
  walp = [u'ａ ｂ ｃ ｄ ｅ ｆ ｇ ｈ ｉ ｊ ｋ ｌ ｍ ｎ ｏ ｐ ｑ ｒ ｓ ｔ ｕ ｖ ｗ ｘ ｙ ｚ ' + \
          u'Ａ Ｂ Ｃ Ｄ Ｅ Ｆ Ｇ Ｈ Ｉ Ｊ Ｋ Ｌ Ｍ Ｎ Ｏ Ｐ Ｑ Ｒ Ｓ Ｔ Ｕ Ｖ Ｗ Ｘ Ｙ Ｚ']
  halp = [u'a b c d e f g h i j k l m n o p q r s t u v w x y z ' + \
          u'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z']
  char_sets = [hira, kata, half, wnum, hnum, walp, halp]

