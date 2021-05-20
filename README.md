# CONVOLUTIONAL NEURAL NETWORK FOR IDENTIFYING GLAUCOMA: USING OCTA VASCULAR SCANS

## The Problem
Optical coherence tomography angiography (OCTA), although a promising image modality to visualize retinal vasculature, is still being investigated for its value in glaucoma diagnosis. Despite the vascular component of glaucoma being relevant to the use of OCTA scans, there is a need for a clinical tool to aid in a more objective diagnosis of glaucoma from OCTA images and database of OCTA images for further application of deep learning. 
Some studies have indicated that glaucoma is more prevalent in women, although the specific OCTA parameters differentiating the two are currently understudied - this is also a potential application of deep learning.

## Our Proposal
We propose to develop a deep-learning approach for the diagnosis of glaucoma and identification of the patient's gender from OCTA images. We plan to use a Convolutional Neural Network (CNN) for this image classification task and will draw from our database of OCTA scans sourced from the UTSW Eye Clinic (Dr. Kooner's patients). With each patient having 8 scans (4 per each eye) and multiple diagnostically relevant features, we envision a great degree of potential for this model to be used as an aid to clinical diagnosis. 

## Workflow
* The data will first be anonymized (to a format P#ID) with a .csv file specifying the Patient Name and corresponding anonymized ID.
* A dataframe containing features of each Patient ID, with columns including a binary Glaucoma diagnosis (Y/N, after expert labeling)  and Gender (M/F) will also be utilized to build the classification model.
* Once the data acquisition process has completed, the choriocapillaries, optic disc, radial circumpapillary capillaries, and superficial scans will be used as inputs into a convolutional neural network in order to predict the Glaucoma diagnosis.
* We also plan on solving another four-class problem, the prediction of the patient's gender and their diagnosis.
* Error rate targets are around 70% considering the limited size of the dataset and will be found after the model validated on test data.

(We will also be adding information about the network's framework).

## Team Members

* Team Leader: Dr. Karanjit Kooner, MD PhD, Ophthalmology, https://utswmed.org/doctors/karanjit-kooner/ 
* SysAdmin: Dr. Dinesh Bhatia, Professor, Electrical Engineering, https://profiles.utdallas.edu/dinesh.bhatia
* Writer: Sruthi Suresh, sps180004@utdallas.edu
* Flex: Binh Vu, voobinh@gmail.com
* Flex: Jacob Akwal, j@utdallas.edu
* Flex: Sumanth Kumar Kotareddy, sxk170004@utdallas.edu
* Flex: Vikas Deo


 
