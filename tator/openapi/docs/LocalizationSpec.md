# LocalizationSpec

Localization creation spec. Attribute key/values must be included in the base object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frame** | **int** | Frame number of this localization if it is in a video. | [default to 0]
**height** | **float** | Normalized height of bounding box for &#x60;box&#x60; localization types. | [optional] 
**media_id** | **int** | Unique integer identifying a media. | 
**modified** | **bool** | Whether this localization was created in the web UI. | [optional] 
**parent** | **float** | If a clone, the pk of the parent. | [optional] 
**type** | **int** | Unique integer identifying a localization type. | 
**u** | **float** | Horizontal vector component for &#x60;line&#x60; localization types. | [optional] 
**v** | **float** | Vertical vector component for &#x60;line&#x60; localization types. | [optional] 
**version** | **int** | Unique integer identifying the version. | [optional] 
**width** | **float** | Normalized width of bounding box for &#x60;box&#x60; localization types. | [optional] 
**x** | **float** | Normalized horizontal position of left edge of bounding box for &#x60;box&#x60; localization types, start of line for &#x60;line&#x60; localization types, or position of dot for &#x60;dot&#x60; localization types. | [optional] 
**y** | **float** | Normalized vertical position of top edge of bounding box for &#x60;box&#x60; localization types, start of line for &#x60;line&#x60; localization types, or position of dot for &#x60;dot&#x60; localization types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

