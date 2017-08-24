# FlowFileSummaryDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI that can be used to access this FlowFile. | [optional] 
**uuid** | **str** | The FlowFile UUID. | [optional] 
**filename** | **str** | The FlowFile filename. | [optional] 
**position** | **int** | The FlowFile&#39;s position in the queue. | [optional] 
**size** | **int** | The FlowFile file size. | [optional] 
**queued_duration** | **int** | How long this FlowFile has been enqueued. | [optional] 
**lineage_duration** | **int** | Duration since the FlowFile&#39;s greatest ancestor entered the flow. | [optional] 
**cluster_node_id** | **str** | The id of the node where this FlowFile resides. | [optional] 
**cluster_node_address** | **str** | The label for the node where this FlowFile resides. | [optional] 
**penalized** | **bool** | If the FlowFile is penalized. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


