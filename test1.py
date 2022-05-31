import re

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sem odio, varius nec aliquam nec, tempor commodo ante. Pellentesque sit amet augue vel ante dictum placerat ut ut sapien. Proin maximus eu diam in posuere. Suspendisse in lectus in lectus finibus auctor. Nam sed porttitor arcu. Vestibulum augue odio, posuere quis libero sed, pharetra sollicitudin est. Donec sit amet nunc eu nisi malesuada elementum id ut purus.Nunc sit amet % massa rhoncus, venenatis eros sit amet, ornare augue. Nunc a mi sed est tincidunt facilisis at nec diam. Donec nec ex lorem. Morbi vitae diam tincidunt, dignissim arcu ut, facilisis nisi. Maecenas non felis #ullamcorper, viverra augue id, consequat_nunc. Suspendisse potenti. Proin tempor, sapien ut ornare placerat, sapien mauris luctus sapi"

split_word1 = re.findall(r'\w+', txt)
wword = []
word_count = {}
for word in split_word1:
    wcount = split_word1.count(word)
    if ( wcount < 3 ):
        word_count[word] = wcount
        wword.append(word)
        


print(word_count)
print(wword[-20:])
