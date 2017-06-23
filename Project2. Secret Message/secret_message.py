import os
def rename_files():
	file_list=os.listdir(r".\prank\prank")
	print (file_list)
	current_path=os.getcwd()
	print current_path
	os.chdir(r".\prank\prank")

	for file_name in file_list:
		print "Old file name", file_name
		print "new file name",   os.rename(file_name,file_name.translate(None,"0123456789"))
	os.chdir(current_path)	
 
rename_files()

