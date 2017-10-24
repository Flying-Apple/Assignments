'''
Shiwei_Sun sudoku.py
'''
from copy import *
from itertools import combinations
import re

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message
		
class Sudoku:
	def __init__(self,filename):
	#	self.alldigits={}
		self.filename=filename.strip('.txt')
		self.file=open(filename)
		self.grid=[]
		values=self.file.read()
		re.split(' |\n',values)
		templist=[]
	#	print(values)
		for digit in values:
			if len(self.grid)==9:
				return
			if digit==' ' or digit=='':
				pass
			elif '\n' in digit and len(templist)==9:
				self.grid.append(templist)
				templist=[]
			elif '\n' in digit and len(templist)!=9 and len(digit)>1:
				tempdigit=digit.strip('\n')
				if tempdigit<'0' or tempdigit>'9':
					if tempdigit==' ' or tempdigit== '\n':
						pass
					else:
						raise SudokuError('Incorrect input')
				else:
					int_tempdigit=int(tempdigit)
					templist.append(int_tempdigit)
					if len(templist)==9:
						self.grid.append(templist)
						templist=[]			
			elif '\n' in digit and len(templist)!=9 and len(digit)==1:
				if not templist:
					pass
				else:
					#print(templist)
					raise SudokuError('Incorrect input')

			else:
				#print(digit,int_digit)
				if digit<'0' or digit>'9':

					raise SudokuError('Incorrect input')
				if digit>='0':
					int_digit=int(digit)
					templist.append(int_digit)
		if len(self.grid)!=9:
			raise SudokuError('Incorrect input')
	#	print(self.grid)

		#print (values)
	def preassess(self):
		self.all_cells=[]
		tempgrid=deepcopy(self.grid)
		for i in tempgrid:
			templist=list(filter(lambda a: a != 0, i))				#available digit for each row
			if len(templist)!= len(set(templist)):
				print('There is clearly no solution.')
				return
		#print(len(self.all_cells))
		newgrid=[]
		for col in range (9):					#turn the grid 90 degree row --> col
			newgrid.append([tempgrid[0][col]])
		for row in range (1,9):
			for col in range (9):
				newgrid[col].append(tempgrid[row][col])

		for i in newgrid:
			templist=list(filter(lambda a: a != 0, i))
			if len(templist)!= len(set(templist)):
				print('There is clearly no solution.')
				return
		#print(self.all_cells)
		newgrid=[[],[],[],[],[],[],[],[],[]]
		for col in range(0,3):
			for row in range(0,3):
				newgrid[0].append(tempgrid[row][col])

		for col in range(0,3):
			for row in range(3,6):
				newgrid[1].append(tempgrid[row][col])	

		for col in range(0,3):
			for row in range(6,9):
				newgrid[2].append(tempgrid[row][col])

		for col in range(3,6):
			for row in range(0,3):
				newgrid[3].append(tempgrid[row][col])


		for col in range(3,6):
			for row in range(3,6):
				newgrid[4].append(tempgrid[row][col])

		for col in range(3,6):
			for row in range(6,9):
				newgrid[5].append(tempgrid[row][col])

		for col in range(6,9):
			for row in range(0,3):
				newgrid[6].append(tempgrid[row][col])

		for col in range(6,9):
			for row in range(3,6):
				newgrid[7].append(tempgrid[row][col])

		for col in range(6,9):
			for row in range(6,9):
				newgrid[8].append(tempgrid[row][col])
		for i in newgrid:
			templist=list(filter(lambda a: a != 0, i))
			#print(templist)
			if len(templist)!= len(set(templist)):
				print('There is clearly no solution.')
				return
		#print(self.all_cells)
		print('There might be a solution.')

	def bare_tex_output(self):
		tempfile = open(self.filename+'_bare.tex', 'w')
		tempfile.write('\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}\n\
\\usepackage{cancel}\n\\pagestyle{empty}\n\n\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n\
                               label=above right:{\\tiny #2},\n                               label=below left:{\\tiny #3},\n                               label=below right:{\\tiny #4}]{#5};}}\n\n\
\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}\n\n\\begin{center}\n\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n% Line 1\n')
	
		tempstring='\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 2\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 3\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 4\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 5\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 6\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 7\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 8\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 9\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\
\\end{tabular}\n\\end{center}\n\n\\end{document}\n'    #template tex
		abc=[]
		abc.append([i for i in tempstring])
		inputstring=abc[0]
	
		index_displacement=11							#insert each digit at last {} for each cell
		for digit in self.grid[0]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[1]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[2]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=24
		for digit in self.grid[3]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[4]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[5]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=24
		for digit in self.grid[6]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[7]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[8]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
								#insert grid into imputformat

		newstring=''
		for i in inputstring:
			newstring+=i
		tempfile.write(newstring)

	def getindexforbox(self,boxnumber):
		digits=[]
		if boxnumber==0:
			firstdigit=[0,0]
			seconddigit=[0,1]
			thirddigit=[0,2]
			fourthdigit=[1,0]
			fifthdigit=[1,1]
			sixthdigit=[1,2]
			seventhdigit=[2,0]
			eighthdigit=[2,1]
			ninthdigit=[2,2]
		elif boxnumber==1:
			firstdigit=[0,3]
			seconddigit=[0,4]
			thirddigit=[0,5]
			fourthdigit=[1,3]
			fifthdigit=[1,4]
			sixthdigit=[1,5]
			seventhdigit=[2,3]
			eighthdigit=[2,4]
			ninthdigit=[2,5]
		elif boxnumber==2:
			firstdigit=[0,6]
			seconddigit=[0,7]
			thirddigit=[0,8]
			fourthdigit=[1,6]
			fifthdigit=[1,7]
			sixthdigit=[1,8]
			seventhdigit=[2,6]
			eighthdigit=[2,7]
			ninthdigit=[2,8]
		elif boxnumber==3:
			firstdigit=[3,0]
			seconddigit=[3,1]
			thirddigit=[3,2]
			fourthdigit=[4,0]
			fifthdigit=[4,1]
			sixthdigit=[4,2]
			seventhdigit=[5,0]
			eighthdigit=[5,1]
			ninthdigit=[5,2]
		elif boxnumber==4:
			firstdigit=[3,3]
			seconddigit=[3,4]
			thirddigit=[3,5]
			fourthdigit=[4,3]
			fifthdigit=[4,4]
			sixthdigit=[4,5]
			seventhdigit=[5,3]
			eighthdigit=[5,4]
			ninthdigit=[5,5]
		elif boxnumber==5:
			firstdigit=[3,6]
			seconddigit=[3,7]
			thirddigit=[3,8]
			fourthdigit=[4,6]
			fifthdigit=[4,7]
			sixthdigit=[4,8]
			seventhdigit=[5,6]
			eighthdigit=[5,7]
			ninthdigit=[5,8]
		elif boxnumber==6:
			firstdigit=[6,0]
			seconddigit=[6,1]
			thirddigit=[6,2]
			fourthdigit=[7,0]
			fifthdigit=[7,1]
			sixthdigit=[7,2]
			seventhdigit=[8,0]
			eighthdigit=[8,1]
			ninthdigit=[8,2]
		elif boxnumber==7:
			firstdigit=[6,3]
			seconddigit=[6,4]
			thirddigit=[6,5]
			fourthdigit=[7,3]
			fifthdigit=[7,4]
			sixthdigit=[7,5]
			seventhdigit=[8,3]
			eighthdigit=[8,4]
			ninthdigit=[8,5]
		elif boxnumber==8:
			firstdigit=[6,6]
			seconddigit=[6,7]
			thirddigit=[6,8]
			fourthdigit=[7,6]
			fifthdigit=[7,7]
			sixthdigit=[7,8]
			seventhdigit=[8,6]
			eighthdigit=[8,7]
			ninthdigit=[8,8]
		digits.append(firstdigit)
		digits.append(seconddigit)
		digits.append(thirddigit)
		digits.append(fourthdigit)
		digits.append(fifthdigit)
		digits.append(sixthdigit)
		digits.append(seventhdigit)
		digits.append(eighthdigit)	
		digits.append(ninthdigit)	
		return digits

	def changenumbertobox(self,number):
		if number==0 or number==1 or number==2 or number==9 or number==10 or number==11 or number==18 or number==19 or number==20:
			return 0
		elif number==3 or number==4 or number==5 or number==12 or number==13 or number==14 or number==21 or number==22 or number==23:
			return 1
		elif number==6 or number==7 or number==8 or number==15 or number==16 or number==17 or number==24 or number==25 or number==26:
			return 2
		elif number==27 or number==28 or number==29 or number==36 or number==37 or number==38 or number==45 or number==46 or number==47:
			return 3
		elif number==30 or number==31 or number==32 or number==39 or number==40 or number==41 or number==48 or number==49 or number==50:
			return 4
		elif number==33 or number==34 or number==35 or number==42 or number==43 or number==44 or number==51 or number==52 or number==53:
			return 5
		elif number==54 or number==55 or number==56 or number==63 or number==64 or number==65 or number==72 or number==73 or number==74:
			return 6
		elif number==57 or number==58 or number==59 or number==66 or number==67 or number==68 or number==75 or number==76 or number==77:
			return 7
		elif number==60 or number==61 or number==62 or number==69 or number==70 or number==71 or number==78 or number==79 or number==80:
			return 8
	def forced_tex_output(self):
		self.alldigits={}
		digitset=[1,2,3,4,5,6,7,8,9]
		for i in range(81):
			row=i//9
			col=i%9
			if self.grid[row][col]>0:
				self.alldigits[i]=[self.grid[row][col]]
			else:
				self.alldigits[i]=list(digitset)


		for i in self.alldigits:
			if len(self.alldigits[i])>1:
				for j in self.alldigits:
					#print()
					rowi=i//9
					rowj=j//9
					if len(self.alldigits[j])==1 and rowi==rowj and i!=j:
						#print(self.alldigits)
						if self.alldigits[j][0] in self.alldigits[i]:
							#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
							#print(self.alldigits)
							self.alldigits[i].remove(self.alldigits[j][0])
						else:
							pass

		for i in self.alldigits:
			if len(self.alldigits[i])>1:
				for j in self.alldigits:
					#print()
					coli=i%9
					colj=j%9
					if len(self.alldigits[j])==1 and coli==colj and i!=j:
						#print(self.alldigits)
						if self.alldigits[j][0] in self.alldigits[i]:
							#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
							#print(self.alldigits)
							self.alldigits[i].remove(self.alldigits[j][0])
						else:
							pass
						#print(self.alldigits[i])

		#evaluate for each box
		
		#Boxes
		for boxid in range(9):
			box=self.getindexforbox(boxid)
			givendigit=[]
			#alldigit[box[0]*9+box[1]]
			for i in range(9):
				if len(self.alldigits[box[i][0]*9+box[i][1]])==1:
					givendigit.append(self.alldigits[box[i][0]*9+box[i][1]][0])
			
			badvalue=[]
			for i in range(9):
				if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
					for j in self.alldigits[box[i][0]*9+box[i][1]]:
						#print(j,self.alldigits[box1[i][0]*9+box1[i][1]])
						if j in givendigit:
							badvalue.append(j)
					#print(badvalue)
					for k in badvalue:
						self.alldigits[box[i][0]*9+box[i][1]].remove(k)
					badvalue=[]
			#above removes badvalue with in box
			#below insert value which is forced
			old_allunsurevalue=[]
			while True:
				allunsurevalue=[]
				
				for i in range(9):
					if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
						for j in self.alldigits[box[i][0]*9+box[i][1]]:
							allunsurevalue.append(j)
				
				for i in range(9):
					if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
						for j in self.alldigits[box[i][0]*9+box[i][1]]:
							if allunsurevalue.count(j)==1:
								self.alldigits[box[i][0]*9+box[i][1]]=[j]


				for i in self.alldigits:
					if len(self.alldigits[i])>1:
						for j in self.alldigits:
							#print()
							rowi=i//9
							rowj=j//9
							if len(self.alldigits[j])==1 and rowi==rowj and i!=j:
								#print(self.alldigits)
								if self.alldigits[j][0] in self.alldigits[i]:
									#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
									#print(self.alldigits)
									self.alldigits[i].remove(self.alldigits[j][0])
								else:
									pass

				for i in self.alldigits:
					if len(self.alldigits[i])>1:
						for j in self.alldigits:
							#print()
							coli=i%9
							colj=j%9
							if len(self.alldigits[j])==1 and coli==colj and i!=j:
								#print(self.alldigits)
								if self.alldigits[j][0] in self.alldigits[i]:
									#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
									#print(self.alldigits)
									self.alldigits[i].remove(self.alldigits[j][0])
								else:
									pass

				if len(allunsurevalue)==len(old_allunsurevalue):
					break
				old_allunsurevalue=list(allunsurevalue)
		#print(self.alldigits)
				
		for key in self.alldigits:
			row=key//9
			col=key%9
			if self.grid[row][col]==0 and len(self.alldigits[key])==1:
				self.grid[row][col]=self.alldigits[key][0]

		#print file
#		print(self.alldigits)
		tempfile = open(self.filename+'_forced.tex', 'w')
		tempfile.write('\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}\n\
\\usepackage{cancel}\n\\pagestyle{empty}\n\n\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n\
                               label=above right:{\\tiny #2},\n                               label=below left:{\\tiny #3},\n                               label=below right:{\\tiny #4}]{#5};}}\n\n\
\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}\n\n\\begin{center}\n\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n% Line 1\n')
	
		tempstring='\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 2\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 3\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 4\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 5\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 6\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 7\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 8\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 9\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\
\\end{tabular}\n\\end{center}\n\n\\end{document}\n'    #template tex
		abc=[]
		abc.append([i for i in tempstring])
		inputstring=abc[0]
	
		index_displacement=11							#insert each digit at last {} for each cell
		for digit in self.grid[0]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[1]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[2]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=24
		for digit in self.grid[3]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[4]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[5]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=24
		for digit in self.grid[6]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[7]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[8]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
								#insert grid into imputformat



		newstring=''
		for i in inputstring:
			newstring+=i
		abc=[]
		abc.append([i for i in newstring])
		inputstring=abc[0]
		
		for char in inputstring:
			if char == '\\N' and len(self.alldigits[0])>1:
				for i in self.alldigits[0]:
					if i < 3:
						a=str(i)
						inputstring.insert(input.index(char)+2,a)
			break
		tempfile.write(newstring)

	def marked_tex_output(self):
		self.alldigits={}
		digitset=[1,2,3,4,5,6,7,8,9]
		for i in range(81):
			row=i//9
			col=i%9
			if self.grid[row][col]>0:
				self.alldigits[i]=[self.grid[row][col]]
			else:
				self.alldigits[i]=list(digitset)


		for i in self.alldigits:
			if len(self.alldigits[i])>1:
				for j in self.alldigits:
					#print()
					rowi=i//9
					rowj=j//9
					if len(self.alldigits[j])==1 and rowi==rowj and i!=j:
						#print(self.alldigits)
						if self.alldigits[j][0] in self.alldigits[i]:
							#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
							#print(self.alldigits)
							self.alldigits[i].remove(self.alldigits[j][0])
						else:
							pass

		for i in self.alldigits:
			if len(self.alldigits[i])>1:
				for j in self.alldigits:
					#print()
					coli=i%9
					colj=j%9
					if len(self.alldigits[j])==1 and coli==colj and i!=j:
						#print(self.alldigits)
						if self.alldigits[j][0] in self.alldigits[i]:
							#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
							#print(self.alldigits)
							self.alldigits[i].remove(self.alldigits[j][0])
						else:
							pass
						#print(self.alldigits[i])

		#evaluate for each box
		#Boxes
		for boxid in range(9):
			box=self.getindexforbox(boxid)
			givendigit=[]
			#alldigit[box[0]*9+box[1]]
			for i in range(9):
				if len(self.alldigits[box[i][0]*9+box[i][1]])==1:
					givendigit.append(self.alldigits[box[i][0]*9+box[i][1]][0])
			
			badvalue=[]
			for i in range(9):
				if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
					for j in self.alldigits[box[i][0]*9+box[i][1]]:
						#print(j,self.alldigits[box1[i][0]*9+box1[i][1]])
						if j in givendigit:
							badvalue.append(j)
					#print(badvalue)
					for k in badvalue:
						self.alldigits[box[i][0]*9+box[i][1]].remove(k)
					badvalue=[]
			#above removes badvalue with in box
			#below insert value which is forced
			old_allunsurevalue=[]
			while True:
				allunsurevalue=[]
				
				for i in range(9):
					if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
						for j in self.alldigits[box[i][0]*9+box[i][1]]:
							allunsurevalue.append(j)
				
				for i in range(9):
					if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
						for j in self.alldigits[box[i][0]*9+box[i][1]]:
							if allunsurevalue.count(j)==1:
								self.alldigits[box[i][0]*9+box[i][1]]=[j]


				for i in self.alldigits:
					if len(self.alldigits[i])>1:
						for j in self.alldigits:
							#print()
							rowi=i//9
							rowj=j//9
							if len(self.alldigits[j])==1 and rowi==rowj and i!=j:
								#print(self.alldigits)
								if self.alldigits[j][0] in self.alldigits[i]:
									#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
									#print(self.alldigits)
									self.alldigits[i].remove(self.alldigits[j][0])
								else:
									pass

				for i in self.alldigits:
					if len(self.alldigits[i])>1:
						for j in self.alldigits:
							#print()
							coli=i%9
							colj=j%9
							if len(self.alldigits[j])==1 and coli==colj and i!=j:
								#print(self.alldigits)
								if self.alldigits[j][0] in self.alldigits[i]:
									#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
									#print(self.alldigits)
									self.alldigits[i].remove(self.alldigits[j][0])
								else:
									pass

				if len(allunsurevalue)==len(old_allunsurevalue):
					break
				old_allunsurevalue=list(allunsurevalue)

		for key in self.alldigits:
			row=key//9
			col=key%9
			if self.grid[row][col]==0 and len(self.alldigits[key])==1:
				self.grid[row][col]=self.alldigits[key][0]


		tempfile = open(self.filename+'_marked.tex', 'w')
		tempfile.write('\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}\n\
\\usepackage{cancel}\n\\pagestyle{empty}\n\n\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n\
                               label=above right:{\\tiny #2},\n                               label=below left:{\\tiny #3},\n                               label=below right:{\\tiny #4}]{#5};}}\n\n\
\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}\n\n\\begin{center}\n\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n% Line 1\n')
	
		tempstring='\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 2\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 3\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 4\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 5\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 6\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 7\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 8\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 9\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\
\\end{tabular}\n\\end{center}\n\n\\end{document}\n'    #template tex
		abc=[]
		abc.append([i for i in tempstring])
		inputstring=abc[0]
	
		index_displacement=11							#insert each digit at last {} for each cell
		for digit in self.grid[0]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[1]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[2]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=24
		for digit in self.grid[3]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[4]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[5]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=24
		for digit in self.grid[6]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[7]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[8]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
								#insert grid into imputformat

		newstring=''
		for i in inputstring:
			newstring+=i
		abc=[]
		abc.append([i for i in newstring])
		inputstring=abc[0]

		j=0
		
		for charindex in range(len(inputstring)+1000):
			displacement=0
			space1=0
			space2=0
			space3=0
			space4=0
			#print(char)
			if j ==81:
				break
			if inputstring[charindex] == 'N' and len(self.alldigits[j])>1:
				#print(j)
				for i in self.alldigits[j]:
					if i < 3:
						a=str(i)
						inputstring.insert(charindex+2+displacement,a)
						if space1>0:
							inputstring.insert(charindex+2+displacement,' ')
							displacement+=1
							space1=0
						space1+=1

						displacement+=1
					elif i>=3 and i <5:
						a=str(i)
						inputstring.insert(charindex+4+displacement,a)
						if space2>0:
							inputstring.insert(charindex+4+displacement,' ')
							displacement+=1
							space2=0
						space2+=1
						displacement+=1
					elif i>=5 and i <7:
						a=str(i)
						inputstring.insert(charindex+6+displacement,a)
						if space3>0:
							inputstring.insert(charindex+6+displacement,' ')
							displacement+=1
							space3=0
						space3+=1
						displacement+=1
					else:
						a=str(i)
						inputstring.insert(charindex+8+displacement,a)
						if space4>0:
							inputstring.insert(charindex+8+displacement,' ')
							displacement+=1
							space4=0
						space4+=1
						displacement+=1
				
				j+=1
			elif inputstring[charindex] == 'N' and len(self.alldigits[j])==1:
				j+=1
				#print(j)
		newstring=''
		for i in inputstring:
			newstring+=i
		tempfile.write(newstring)
		#print(self.alldigits[80])

	def worked_tex_output(self):
		self.alldigits={}
		digitset=[1,2,3,4,5,6,7,8,9]
		for i in range(81):
			row=i//9
			col=i%9
			if self.grid[row][col]>0:
				self.alldigits[i]=[self.grid[row][col]]
			else:
				self.alldigits[i]=list(digitset)


		for i in self.alldigits:
			if len(self.alldigits[i])>1:
				for j in self.alldigits:
					#print()
					rowi=i//9
					rowj=j//9
					if len(self.alldigits[j])==1 and rowi==rowj and i!=j:
						#print(self.alldigits)
						if self.alldigits[j][0] in self.alldigits[i]:
							#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
							#print(self.alldigits)
							self.alldigits[i].remove(self.alldigits[j][0])
						else:
							pass

		for i in self.alldigits:
			if len(self.alldigits[i])>1:
				for j in self.alldigits:
					#print()
					coli=i%9
					colj=j%9
					if len(self.alldigits[j])==1 and coli==colj and i!=j:
						#print(self.alldigits)
						if self.alldigits[j][0] in self.alldigits[i]:
							#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
							#print(self.alldigits)
							self.alldigits[i].remove(self.alldigits[j][0])
						else:
							pass
						#print(self.alldigits[i])

		#evaluate for each box
		#Boxes
		for boxid in range(9):
			box=self.getindexforbox(boxid)
			givendigit=[]
			#alldigit[box[0]*9+box[1]]
			for i in range(9):
				if len(self.alldigits[box[i][0]*9+box[i][1]])==1:
					givendigit.append(self.alldigits[box[i][0]*9+box[i][1]][0])
			
			badvalue=[]
			for i in range(9):
				if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
					for j in self.alldigits[box[i][0]*9+box[i][1]]:
						#print(j,self.alldigits[box1[i][0]*9+box1[i][1]])
						if j in givendigit:
							badvalue.append(j)
					#print(badvalue)
					for k in badvalue:
						self.alldigits[box[i][0]*9+box[i][1]].remove(k)
					badvalue=[]
			#above removes badvalue with in box
			#below insert value which is forced
			old_allunsurevalue=[]
			while True:
				allunsurevalue=[]
				
				for i in range(9):
					if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
						for j in self.alldigits[box[i][0]*9+box[i][1]]:
							allunsurevalue.append(j)
				
				for i in range(9):
					if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
						for j in self.alldigits[box[i][0]*9+box[i][1]]:
							if allunsurevalue.count(j)==1:
								self.alldigits[box[i][0]*9+box[i][1]]=[j]


				for i in self.alldigits:
					if len(self.alldigits[i])>1:
						for j in self.alldigits:
							#print()
							rowi=i//9
							rowj=j//9
							if len(self.alldigits[j])==1 and rowi==rowj and i!=j:
								#print(self.alldigits)
								if self.alldigits[j][0] in self.alldigits[i]:
									#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
									#print(self.alldigits)
									self.alldigits[i].remove(self.alldigits[j][0])
								else:
									pass

				for i in self.alldigits:
					if len(self.alldigits[i])>1:
						for j in self.alldigits:
							#print()
							coli=i%9
							colj=j%9
							if len(self.alldigits[j])==1 and coli==colj and i!=j:
								#print(self.alldigits)
								if self.alldigits[j][0] in self.alldigits[i]:
									#print(i//9,j//9,'i j',i,self.alldigits[i],(self.alldigits[j][0]))
									#print(self.alldigits)
									self.alldigits[i].remove(self.alldigits[j][0])
								else:
									pass

				if len(allunsurevalue)==len(old_allunsurevalue):
					break
				old_allunsurevalue=list(allunsurevalue)
		#self.alldigits contains all marked output for each cell from 0 - 80
		self.marked_output=deepcopy(self.alldigits)
		while True:
			old_self_alldigits=deepcopy(self.alldigits)
			set0=set()
			set1=set()
			set2=set()
			set3=set()
			set4=set()
			set5=set()
			set6=set()
			set7=set()
			set8=set()
			sets=[set0,set1,set2,set3,set4,set5,set6,set7,set8]
			for i in self.alldigits:
											#check each row
				if i//9==0 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set0.add(j)
				elif i//9==1 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set1.add(j)
				elif i//9==2 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set2.add(j)
				elif i//9==3 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set3.add(j)
				elif i//9==4 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set4.add(j)
				elif i//9==5 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set5.add(j)
				elif i//9==6 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set6.add(j)
				elif i//9==7 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set7.add(j)
				elif i//9==8 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set8.add(j)
		#	print(set0)
			for row_set_index in range(len(sets)):
				#check preemtive sets for row
				for j in range(2,len(sets[row_set_index])+1):
					row1_combination=list(combinations(sets[row_set_index],j))
					for k in row1_combination:
						counter=0
						for i in self.alldigits:
							if i//9==row_set_index and len(self.alldigits[i])>1:
								tempsetk=set(k)
								temprowset=[]
								for rowdigit in self.alldigits[i]:
									if rowdigit>0:
										temprowset.append(rowdigit)
								tempset=set(temprowset)
								if tempset.issubset(tempsetk):
									counter+=1

						if counter==len(k):	
							#set all other digits in the same row to negative
							for digits in self.alldigits:
								if digits//9==row_set_index and len(self.alldigits[digits])>1:
			
									temprowset=[]
									for rowdigit in self.alldigits[digits]:
										if rowdigit>0:
											temprowset.append(rowdigit)
									tempset=set(temprowset)
									if not tempset.issubset(k):
										for number in k:
											if number in self.alldigits[digits]:
												self.alldigits[digits][self.alldigits[digits].index(number)]*=-1


			set0=set()
			set1=set()
			set2=set()
			set3=set()
			set4=set()
			set5=set()
			set6=set()
			set7=set()
			set8=set()
			sets=[set0,set1,set2,set3,set4,set5,set6,set7,set8]
			for i in self.alldigits:
											#check each col
				if i%9==0 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set0.add(j)
				elif i%9==1 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set1.add(j)
				elif i%9==2 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set2.add(j)
				elif i%9==3 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set3.add(j)
				elif i%9==4 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set4.add(j)
				elif i%9==5 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set5.add(j)
				elif i%9==6 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set6.add(j)
				elif i%9==7 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set7.add(j)
				elif i%9==8 and len(self.alldigits[i])>1:
					for j in self.alldigits[i]:
						if j >0:
							set8.add(j)	
			#print(set0,set1,set2,set3,set4,set5)
	

											#check each col
			for col_set_index in range(len(sets)):
				#check preemtive sets for col
				for j in range(2,len(sets[col_set_index])+1):
					row1_combination=list(combinations(sets[col_set_index],j))
					
					for k in row1_combination:
						counter=0
						for i in self.alldigits:
							if i%9==col_set_index and len(self.alldigits[i])>1:
								tempsetk=set(k)
								tempcolset=[]
								for coldigit in self.alldigits[i]:
									if coldigit>0:
										tempcolset.append(coldigit)
								tempset=set(tempcolset)
								if tempset.issubset(tempsetk):
									counter+=1

						if counter==len(k):	
							
							#set all other digits in the same col to negative
							for digits in self.alldigits:
								if digits%9==col_set_index and len(self.alldigits[digits])>1:
									tempcolset=[]
									for coldigit in self.alldigits[digits]:
										if coldigit>0:
											tempcolset.append(coldigit)
									tempset=set(tempcolset)																		
									if not tempset.issubset(k):
										for number in k:
											if number in self.alldigits[digits]:
												self.alldigits[digits][self.alldigits[digits].index(number)]*=-1
			

	
											#check each box for preemtive sets
			set0=set()
			set1=set()
			set2=set()
			set3=set()
			set4=set()
			set5=set()
			set6=set()
			set7=set()
			set8=set()
			sets=[set0,set1,set2,set3,set4,set5,set6,set7,set8]
			for boxid in range(9):
				box=self.getindexforbox(boxid)
				#givendigit=[]
				#alldigits[box[0]*9+box[1]]
				if boxid==0:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set0.add(j)
				elif boxid==1:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set1.add(j)
				elif boxid==2:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set2.add(j)
				elif boxid==3:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set3.add(j)
				elif boxid==4:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set4.add(j)
				elif boxid==5:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set5.add(j)
				elif boxid==6:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set6.add(j)
				elif boxid==7:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set7.add(j)
				elif boxid==8:
					for i in range(9):
						if len(self.alldigits[box[i][0]*9+box[i][1]])>1:
							for j in self.alldigits[box[i][0]*9+box[i][1]]:
								if j >0:
									set8.add(j)
			
			for box_set_index in range(len(sets)):
				#check preemtive sets for box
				for j in range(2,len(sets[box_set_index])+1):
					row1_combination=list(combinations(sets[box_set_index],j))
					for k in row1_combination:
						counter=0
						for i in self.alldigits:
							if self.changenumbertobox(i)==box_set_index and len(self.alldigits[i])>1:

									tempsetk=set(k)
									tempboxset=[]
									for boxdigit in self.alldigits[i]:
										if boxdigit>0:
											tempboxset.append(boxdigit)
									tempset=set(tempboxset)
									if tempset.issubset(tempsetk):
										counter+=1

						if counter==len(k):	
							#set all other digits in the same box to negative
							for digits in self.alldigits:
								if self.changenumbertobox(digits)==box_set_index and len(self.alldigits[digits])>1:
									tempboxset=[]
									for boxdigit in self.alldigits[digits]:
										if boxdigit>0:
											tempboxset.append(boxdigit)
									tempset=set(tempboxset)
									if not tempset.issubset(k):
										for number in k:
											if number in self.alldigits[digits]:
												self.alldigits[digits][self.alldigits[digits].index(number)]*=-1

			
			for i in self.alldigits:
				row=i//9
				col=i%9
				counter=0
				for j in self.alldigits[i]:
					if j>0:
						counter+=1
						singlevalue=j
				if counter==1:
					self.grid[row][col]=singlevalue
					self.alldigits[i]=[singlevalue]
					#cross out other digits which contain this single value for row col and box
					for other_digits in self.alldigits:
						if other_digits//9==i//9 and len(self.alldigits[other_digits])>1:
							for other_value in self.alldigits[other_digits]:
								if other_value == singlevalue:
									self.alldigits[other_digits][self.alldigits[other_digits].index(singlevalue)]*=-1
						if other_digits%9==i%9 and len(self.alldigits[other_digits])>1:
							for other_value in self.alldigits[other_digits]:
								if other_value == singlevalue:
									self.alldigits[other_digits][self.alldigits[other_digits].index(singlevalue)]*=-1
						if self.changenumbertobox(other_digits)==self.changenumbertobox(i) and len(self.alldigits[other_digits])>1:
							for other_value in self.alldigits[other_digits]:
								if other_value == singlevalue:
									self.alldigits[other_digits][self.alldigits[other_digits].index(singlevalue)]*=-1
									#print('hello')



			

		#	print(self.alldigits,'\n')
		#	print('\n',self.grid)
		#	print(old_self_alldigits)

			if old_self_alldigits==self.alldigits:
				break

		#print the file here with a previously marked self.marked_output and current self.alldigits

		tempfile = open(self.filename+'_worked.tex', 'w')
		tempfile.write('\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}\n\
\\usepackage{cancel}\n\\pagestyle{empty}\n\n\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n\
                               label=above right:{\\tiny #2},\n                               label=below left:{\\tiny #3},\n                               label=below right:{\\tiny #4}]{#5};}}\n\n\
\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}\n\n\\begin{center}\n\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n% Line 1\n')
	
		tempstring='\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 2\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 3\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 4\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 5\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 6\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\n\
% Line 7\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 8\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\n\n\
% Line 9\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\ \\hline\\hline\n\
\\end{tabular}\n\\end{center}\n\n\\end{document}\n'    #template tex
		abc=[]
		abc.append([i for i in tempstring])
		inputstring=abc[0]
		index_displacement=11							#insert each digit at last {} for each cell
		for digit in self.grid[0]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[1]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[2]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=24
		for digit in self.grid[3]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[4]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[5]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=24
		for digit in self.grid[6]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
		index_displacement+=18
		for digit in self.grid[7]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15

		index_displacement+=18
		for digit in self.grid[8]:
			if digit>0:
				a=str(digit)
				inputstring.insert(index_displacement,a)
				index_displacement+=16
			else:
				pass
				index_displacement+=15
								#insert grid into imputformat

		newstring=''
		for i in inputstring:
			newstring+=i
		abc=[]
		abc.append([i for i in newstring])
		inputstring=abc[0]
		#print(self.alldigits)
		j=0

		
		for charindex in range(len(inputstring)+1000):
			displacement=0
			space1=0
			space2=0
			space3=0
			space4=0
			#print(char)
			if j ==81:
				break
			if inputstring[charindex] == 'N' and len(self.marked_output[j])>1:
				#print(j)
				if inputstring[charindex+10]>'0' and inputstring[charindex+10]<='9':
					for i in self.marked_output[j]:
						if i < 3:
							a='\\cancel{'+str(i)+'}'
							inputstring.insert(charindex+2+displacement,a)
							if space1>0:
								inputstring.insert(charindex+2+displacement,' ')
								displacement+=1
								space1=0
							space1+=1

							displacement+=1
						elif i>=3 and i <5:
							a='\\cancel{'+str(i)+'}'
							inputstring.insert(charindex+4+displacement,a)
							if space2>0:
								inputstring.insert(charindex+4+displacement,' ')
								displacement+=1
								space2=0
							space2+=1
							displacement+=1
						elif i>=5 and i <7:
							a='\\cancel{'+str(i)+'}'
							inputstring.insert(charindex+6+displacement,a)
							if space3>0:
								inputstring.insert(charindex+6+displacement,' ')
								displacement+=1
								space3=0
							space3+=1
							displacement+=1
						else:
							a='\\cancel{'+str(i)+'}'
							inputstring.insert(charindex+8+displacement,a)
							if space4>0:
								inputstring.insert(charindex+8+displacement,' ')
								displacement+=1
								space4=0
							space4+=1
							displacement+=1
				else:
					for i in self.alldigits[j]:
						if i < 3 and i >0:
							a=str(i)
							inputstring.insert(charindex+2+displacement,a)
							if space1>0:
								inputstring.insert(charindex+2+displacement,' ')
								displacement+=1
								space1=0
							space1+=1

							displacement+=1
						elif i>=3 and i <5:
							a=str(i)
							inputstring.insert(charindex+4+displacement,a)
							if space2>0:
								inputstring.insert(charindex+4+displacement,' ')
								displacement+=1
								space2=0
							space2+=1
							displacement+=1
						elif i>=5 and i <7:
							a=str(i)
							inputstring.insert(charindex+6+displacement,a)
							if space3>0:
								inputstring.insert(charindex+6+displacement,' ')
								displacement+=1
								space3=0
							space3+=1
							displacement+=1
						elif i>=7:
							a=str(i)
							inputstring.insert(charindex+8+displacement,a)
							if space4>0:
								inputstring.insert(charindex+8+displacement,' ')
								displacement+=1
								space4=0
							space4+=1
							displacement+=1
						elif abs(i) < 3 and i < 0:
							a='\\cancel{'+str(abs(i))+'}'
							inputstring.insert(charindex+2+displacement,a)
							if space1>0:
								inputstring.insert(charindex+2+displacement,' ')
								displacement+=1
								space1=0
							space1+=1

							displacement+=1
						elif abs(i)>=3 and abs(i) <5 and i < 0:
							a='\\cancel{'+str(abs(i))+'}'
							inputstring.insert(charindex+4+displacement,a)
							if space2>0:
								inputstring.insert(charindex+4+displacement,' ')
								displacement+=1
								space2=0
							space2+=1
							displacement+=1
						elif abs(i)>=5 and abs(i) <7 and i < 0:
							a='\\cancel{'+str(abs(i))+'}'
							inputstring.insert(charindex+6+displacement,a)
							if space3>0:
								inputstring.insert(charindex+6+displacement,' ')
								displacement+=1
								space3=0
							space3+=1
							displacement+=1
						elif abs(i)>=7 and i < 0:
							a='\\cancel{'+str(abs(i))+'}'
							inputstring.insert(charindex+8+displacement,a)
							if space4>0:
								inputstring.insert(charindex+8+displacement,' ')
								displacement+=1
								space4=0
							space4+=1
							displacement+=1



					
				j+=1
			elif inputstring[charindex] == 'N' and len(self.alldigits[j])==1:
				j+=1
				#print(j)
		newstring=''
		for i in inputstring:
			newstring+=i
		tempfile.write(newstring)



a=Sudoku("sudoku_5.txt")
a.preassess()
#a.forced_tex_output()
a.marked_tex_output()
a.worked_tex_output()