import html_creator as hc
import xml_generator as xg
import data_provider as dp

print(hc.create())
print(xg.create())

hc.new_create(xg.new_create(dp.data_collection()))
# если написать xg.new_create(dp.data_collection()) - то создаст только файл xml
# а если написать hc.new_create(xg.new_create(dp.data_collection())) - создасть оба файла html И xml
