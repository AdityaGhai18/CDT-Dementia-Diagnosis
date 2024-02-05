# Apple iOS Development on Clock Drawing Test Dementia Diagnosis Application

Orientations of submitted photos using the Vision framework and classification of the corresponding stage of 
dementia and cognitive decline with a Core ML model.

## Overview
The minimal viable product application utilises a MobileNet Model (Condensed Convolutional Neural Network) 
that identifies the stage of dementia by associating the Clock Drawing Test with a score from 0 to 5, 
where 5 represents a healthy brain and a 0 represents a major need of medical attention.

Each time a user selects a photo from the library or takes a photo of their clock drawing test with a camera,
the app passes it to a Vision image classification request.
Vision resizes and crops the photo to meet the MobileNet model's constraints of image input,
and then passes the photo to the trained model using the Core ML framework that is locally stored in the application.
Once the model generates a prediction, Vision relays it back to the app, which presents the results to the user.
These results are presented in a string format including the two most likely predictions made by the trained model, 
along with a confidence score for each percentage.

Links for all specific actions below:

[Vision documentation]: https://developer.apple.com/documentation/vision
[Core ML documentation]: https://developer.apple.com/documentation/coreml
[Classifying Images for Categorization and Search]:
https://developer.apple.com/documentation/vision/classifying_images_for_categorization_and_search
[VNClassifyImageRequest]: https://developer.apple.com/documentation/vision/vnclassifyimagerequest
[Create ML]: https://developer.apple.com/documentation/createml
[Creating an Image Classifier Model]: 
https://developer.apple.com/documentation/createml/creating-an-image-classifier-model
[MLModel]: https://developer.apple.com/documentation/coreml/mlmodel
[VNCoreMLModel]: https://developer.apple.com/documentation/vision/vncoremlmodel
[VNCoreMLRequest]: https://developer.apple.com/documentation/vision/vncoremlrequest
[imageCropAndScaleOption]: 
https://developer.apple.com/documentation/vision/vncoremlrequest/2890144-imagecropandscaleoption
[centerCrop]: https://developer.apple.com/documentation/vision/vnimagecropandscaleoption/centercrop
[makePredictions]: x-source-tag://makePredictions
[VNImageRequestHandler]: https://developer.apple.com/documentation/vision/vnimagerequesthandler
[CGImagePropertyOrientation]: https://developer.apple.com/documentation/imageio/cgimagepropertyorientation
[VNRequest]: https://developer.apple.com/documentation/vision/vnrequest
[VNImageRequestHandler.perform]: https://developer.apple.com/documentation/vision/vnimagerequesthandler/2880297-perform
[visionRequestHandler]: x-source-tag://visionRequestHandler
[VNRequest.results]: https://developer.apple.com/documentation/vision/vnrequest/2867238-results
[VNClassificationObservation]: https://developer.apple.com/documentation/vision/vnclassificationobservation
[Prediction]: x-source-tag://Prediction
[imagePredictionHandler]: x-source-tag://imagePredictionHandler
[updatePredictionLabel]: x-source-tag://updatePredictionLabel
[project tutorial]: https://developer.apple.com/documentation/vision/classifying_images_with_vision_and_core_ml
