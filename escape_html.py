import html


#特殊文字のエスケープ
data_1 = html.escape(' Hello "World" ')
print(data_1)

#特殊文字のアンエスケープ
data_2 = html.unescape(' Hello &quot;World&quot; ')
print(data_2)
