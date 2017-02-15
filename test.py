sfdasfimport pickle;
dic1 = {"A":10,"B":20,"C":30}
dic2 = {"C":10,"D":20,"E":30}
f = open('dump.txt', 'wb')
str = pickle.dumps(dic1)
print (str)

f = open('dump.txt', 'wb');
# 将内容序列化写入到file文件中
pickle.dump(dic1, f);
pickle.dump(dic2, f);
f.close(); # 最后关闭掉文件资源

# print 'Done';

f = open('dump.txt', 'rb'); # 设定文件选项模式为rb
dic1 = pickle.load(f)
dic2 = pickle.load(f)
print(dic1)
print(dic2)
