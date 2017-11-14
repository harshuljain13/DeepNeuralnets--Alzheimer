"""
After moving all the files using the 1_ file, we run this one to extract
the images from the videos and also create a data file we can use
for training and testing later.
"""
import csv
import glob
import os
import os.path
from subprocess import call
import nibabel as nib
import shutil
from PIL import Image, ImageFilter

def extract_files():
    """After we have all of our videos split between train and test, and
    all nested within folders representing their classes, we need to
    make a data file that we can reference when training our RNN(s).
    This will let us keep track of image sequences and other parts
    of the training process.

    We'll first need to extract images from each of the videos. We'll
    need to record the following data in the file:

    [train|test], class, filename, nb frames

    Extracting can be done with ffmpeg:
    `ffmpeg -i video.mpg image-%04d.jpg`
    """
    data_file = []
    folders = ['/home/ubuntu/Select_original_fmri/data/train/', '/home/ubuntu/Select_original_fmri/data/test/']

    for folder in folders: # test train loop
        class_folders = glob.glob(folder + '*') # get all class folders in test and train
        print ("class_folders",class_folders) # printing all class folders
        for vid_class in class_folders: # for each classfolder
            class_files = glob.glob(vid_class + '/*.nii') # get all nii files
            print ("nii_class:",vid_class) 
            for nii_path in class_files:
                # Get the parts of the file.
                print ("nii path",nii_path)
                nii_parts = get_nii_parts(nii_path)
		#print(nii_parts)
                train_or_test, classname, filename_no_ext, filename = nii_parts
                store_path = '/home/ubuntu/Select_original_fmri/data/'+train_or_test+'/'+classname+'/'+filename_no_ext
                try:
                    count = 1
                    # extracting data from nii files
                    x = nib.load(nii_path).get_data()
                    print('trying...', store_path)
                    # Including only 3 dimentions(length ,width,color) and excluding time dimention
                    for i in xrange(x.shape[3]):
                        for j in xrange(x.shape[2]):
                            y = x[:, :, j, i]
                            img = Image.fromarray(y)
                            img = img.convert("RGB")
                            img = img.resize([224, 224])
                            str_count = '%04d' % count
                            #Saving image in '/home/ubuntu/Select_original_fmri/image/class_/file'
                            img.save(store_path + '-' + str_count + ".jpg")
                            count+=1
            	except:
                    print(filename)
                

                # Only extract if we haven't done it yet. Otherwise, just get
                # the info.
#                if not check_already_extracted(video_parts):
                    # Now extract it.
#                    src = train_or_test + '/' + classname + '/' + \
#                        filename
#                    dest = train_or_test + '/' + classname + '/' + \
#                        filename_no_ext + '-%04d.jpg'
#                    call(["ffmpeg", "-i", src, dest])

                # Now get how many frames it is.
                nb_frames = get_nb_frames_for_nii(nii_parts)

                data_file.append([train_or_test, classname, filename_no_ext, nb_frames])

                print("Generated %d frames for %s" % (nb_frames, filename_no_ext))

    with open('data_file.csv', 'w') as fout:
        writer = csv.writer(fout)
        writer.writerows(data_file)

    print("Extracted and wrote %d video files." % (len(data_file)))
    
#functions............
def get_nb_frames_for_nii(nii_parts):
    """Given video parts of an (assumed) already extracted video, return
    the number of frames that were extracted."""
    train_or_test, classname, filename_no_ext, _ = nii_parts
    generated_files = glob.glob('/home/ubuntu/Select_original_fmri/data/'+train_or_test + '/' + classname + '/' +
                                filename_no_ext + '*.jpg')
   # print("generated files:",generated_files)
    return len(generated_files)

def get_nii_parts(nii_path):
    """Given a full path to a nii file, return its parts."""
    parts = nii_path.split('/')
    filename = parts[-1]
    filename_no_ext = filename.split('.')[0]
    classname = parts[-2]
    train_or_test = parts[-3]
    print ("train_or_test:",train_or_test)
    print("classname:",classname)
    print("filename_no_ext:",filename_no_ext)
    print("filename:",filename)

    return train_or_test, classname, filename_no_ext, filename

def check_already_extracted(video_parts):
    """Check to see if we created the -0001 frame of this file."""
    train_or_test, classname, filename_no_ext, _ = video_parts
    return bool(os.path.exists(train_or_test + '/' + classname +
                               '/' + filename_no_ext + '-0001.jpg'))

def main():
    """
    Extract images from videos and build a new file that we
    can use as our data input file. It can have format:

    [train|test], class, filename, nb frames
    """
    
    extract_files()

if __name__ == '__main__':
    main()
