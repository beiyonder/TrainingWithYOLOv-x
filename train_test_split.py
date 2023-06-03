import glob
import os

current_dir = '/home/siddharth/yolo/darknet/data/images'
percentage_test = 10  # Percentage of images to be used for the valid set
# print('1')
# Create train.txt and valid.txt
with open('train.txt', 'w') as file_train, open('valid.txt', 'w') as file_test:
    # Populate train.txt and valid.txt
    # print('2')
    counter = 1
    index_test = round(100 / percentage_test)

    for file in glob.iglob(os.path.join(current_dir, '*.jpg')):
        # print('3')
        title, ext = os.path.splitext(os.path.basename(file))
        if counter == index_test:
            counter = 1
            # print("Valid: ", current_dir + "/" + title + '.jpg')
            file_test.write(current_dir + "/" + title + '.jpg' + "\n")
        else:
            # print("Train: ", current_dir + "/" + title + '.jpg')
            file_train.write(current_dir + "/" + title + '.jpg' + "\n")
            counter = counter + 1




# import glob
# import os
# current_dir = '/home/yolo/darknet/images/'
# # Percentage of images to be used for the valid set
# percentage_test = 10
# # Create train.txt and valid.txt
# file_train = open('train.txt', 'w')  
# file_test = open('valid.txt', 'w')
# # Populate train.txt and valid.txt
# counter = 1  
# index_test = round(100 / percentage_test)  
# for file in glob.iglob(os.path.join(current_dir, '*.jpg')):  
#     title, ext = os.path.splitext(os.path.basename(file))
#     if counter == index_test:
#         counter = 1
#         file_test.write(current_dir + "/" + title + '.jpg' + "\n")
#     else:
#         file_train.write(current_dir + "/" + title + '.jpg' + "\n")
#         counter = counter + 1

# file_train.close()
# file_test.close()