a = read.csv2("a.csv")
j=0
print("hello")
for (i in 1:386){
	if(a[i][-1]=="Taliban"){
	j+=1
	}
}
print(j)