# Box

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique integer identifying this localization. | [optional] 
**project** | **int** | Unique integer identifying project of this localization. | [optional] 
**meta** | **int** | Unique integer identifying entity type of this localization. | [optional] 
**media** | **int** | Unique integer identifying media of this localization. | [optional] 
**thumbnail_image** | **str** | URL of thumbnail corresponding to this localization. | [optional] 
**modified** | **bool** | Indicates whether this localization has been modified in the web UI. | [optional] 
**version** | **int** | Unique integer identifying a version. | [optional] 
**email** | **str** | Email of last user who modified/created this localization. | [optional] 
**frame** | **int** | Frame number of this localization if it is in a video. | [optional] 
**attributes** | **dict(str, object)** | Object containing attribute values. | [optional] 
**x** | **float** | Normalized horizontal position of left edge of bounding box. | [optional] 
**y** | **float** | Normalized vertical position of top edge of bounding box. | [optional] 
**width** | **float** | Normalized width of bounding box for &#x60;box&#x60; localization types. | [optional] 
**height** | **float** | Normalized height of bounding box for &#x60;box&#x60; localization types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
