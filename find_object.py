from DeepImageSearch import Load_Data,Search_Setup
import re
import os
from PIL import Image
import time


os.environ['KMP_DUPLICATE_LIB_OK']='True'
count=0

dir=os.chdir('C:\\digi')
direction_list=[]

for filename in os.listdir(dir):
    direction_list.append("C:\\digi\\%s"%filename)
    count+=1
print(count)
print(direction_list)
image_list=Load_Data().from_folder(direction_list)
st = Search_Setup(image_list=image_list, model_name='vgg19', pretrained=False, image_count=None)
st.run_index()

# print(direction_list)
metadata = st.get_image_metadata_file()
similar_img=st.plot_similar_images('C:\\digi\\dkp-13968309\\19803d271ead915815b861428c5ec21213c6fef2_1704176139.jpg', number_of_images=count)




# for i in similar_img.values():
#     print (i)
#     img = Image.open("%s"%i)
#     img.show()
#     time.sleep(0.8)
#     img.close()

    # PhotoImage=tk.PhotoImage(file='%s'%i)
    # label=tk.Label(root,image=PhotoImage)
    
    # root.mainloop()

# print('3')

# for i in image_list :
#     print(i)
#     count_1+=1
#     print(count_1)

# for i in os.listdir(filename):
#     print(i)
#     count+=1
#     print(count)

