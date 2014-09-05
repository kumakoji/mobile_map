#!/bin/py
import sys
argvs = sys.argv

def main():
	f = init()
	log = input_log()
	output_geo(log,f)

def init():
	f = open('map.json','w');
	f.write('var geodata = {"Marker":[\n{')
	return f

def input_log():
	log = []
	content = ""
	id = 0
	for line in open(argvs[1],'r'):
		if 'AlarmManager' in line:
			content = '"content":"'+content+'"'
			log.append(lat+','+lng+','+content)
			id += 1;
			content = str(id)+"<br>"
		elif 'Location ' in line:
			lat = line[:-1].split('\t')[1].split(': ')[1].split(', ')[0].replace("(","")
			lng = line[:-1].split('\t')[1].split(': ')[1].split(', ')[1].replace(")","")
			lat = '"lat":"'+lat+'"'
			lng = '"lng":"'+lng+'"'
		content += line[:-1]+"<br>"
	return log

def output_geo(log,f):
	f.write(('\n},\n{\n').join(log))
	f.write('}\n]}\n')
	f.close()


main()	
