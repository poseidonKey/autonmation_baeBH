from array import array
import pyexcel as px
my_array=[[1,2,3],[1,2,3],[1,2,3],[1,2,3],]
px.save_as(array=my_array,dest_file_name="test.xlsx")
# px.save_as(my_array,"test.xlsx")