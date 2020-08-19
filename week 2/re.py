import re
if __name__ == '__main__':
 	file =open('regex_sum_909816.txt')
 	sum=0
 	word=0
 	for line in file:
 		temp =line.rstrip()
 		temp= re.findall('[0-9]+', temp)
 		if len(temp) >0:
 			for w in temp:
 				word+=1
 				sum+=int(w)
 	print('the sum for the sample text above is%d\n'%sum)			
