# CONVOLUTIONAL NEURAL NETWORK FOR IDENTIFYING OCTA VASCULAR SCANS

## The Problem
Optical coherence tomography angiography (OCTA), although a promising image modality to visualize retinal vasculature, is still being investigated for its value in glaucoma diagnosis. Despite the vascular component of glaucoma being relevant to the use of OCTA scans, there is a need for a clinical tool to aid in a more objective diagnosis of glaucoma from OCTA images and database of OCTA images for further application of deep learning. 
Some studies have indicated that glaucoma is more prevalent in women, although the specific OCTA parameters differentiating the two are currently understudied - this is also a potential application of deep learning.

## Our Proposal
We propose to develop a deep-learning approach for the diagnosis of glaucoma and identification of the patient's gender from OCTA images. We plan to use a Convolutional Neural Network (CNN) for this image classification task and will draw from our database of OCTA scans sourced from the UTSW Eye Clinic (Dr. Kooner's patients). With each patient having 8 scans (4 per each eye) and multiple diagnostically relevant features, we envision a great degree of potential for this model to be used as an aid to clinical diagnosis. 

## Workflow
* The data will first be anonymized (to a format P#ID) with a .csv file specifying the Patient Name and corresponding anonymized ID.
* A dataframe containing features of each Patient ID, with columns including a binary Glaucoma diagnosis (Y/N, after expert labeling)  and Gender (M/F) will also be utilized to build the classification model.
* Once the data acquisition process has completed, two CNNs will be built in order to predict either Glaucoma diagnosis or the patient's gender in a binary classification system. After assessing the error rates, an integrated multi-output model will be developed.

(We will also be adding information about the network's framework).

## Team Members

* Team Leader: Dr. Karanjit Kooner, MD, Ophthalmology, https://utswmed.org/doctors/karanjit-kooner/ 
* SysAdmin: Dr. Dinesh Bhatia, Professor, Electrical Engineering, https://profiles.utdallas.edu/dinesh.bhatia
* Writer: Sruthi Suresh, sps180004@utdallas.edu
* Flex: Binh Vu, voobinh@gmail.com
* Flex: Jacob Akwal, j@utdallas.edu
